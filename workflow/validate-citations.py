#!/usr/bin/env python3
"""
Citation Date Validator for 3rd Take

Checks that all citation URLs in issue HTML files have publication dates
within ±7 days of the issue date. Citations tagged with
data-type="background" are allowed to fall outside that window but are
still reported as informational.

Usage:
    python3 workflow/validate-citations.py                  # validate all issues
    python3 workflow/validate-citations.py issues/2026-03-08.html  # validate one
"""

import re
import sys
import os
from datetime import datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path

WINDOW_DAYS = 7

# ── Date extraction patterns found in URLs ──────────────────────────────

URL_DATE_PATTERNS = [
    # /2026/03/08/ or /2026/03/ or /2026-03-08
    re.compile(r'/(\d{4})[/-](0[1-9]|1[0-2])[/-](0[1-9]|[12]\d|3[01])(?:[/\-.]|$)'),
    # /2026/03/ (month only, no day)
    re.compile(r'/(\d{4})[/-](0[1-9]|1[0-2])(?:/|$)'),
    # Compact dates in slugs: 20260308 or 260308
    re.compile(r'[/-](\d{4})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(?:[/-]|$)'),
    # Two-digit year: /26-01-20 or news250120
    re.compile(r'(\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])'),
    # nature DOI year hint: s41746-025- means 2025
    re.compile(r's\d+-(\d{3})-'),
    # nature DOI: d41586-024- means 2024
    re.compile(r'd\d+-(\d{3})-'),
]


def extract_date_from_url(url: str):
    """Try to extract a publication date from a URL. Returns (datetime, precision) or (None, None).
    precision is 'day', 'month', or 'year'."""

    # Full date patterns (YYYY/MM/DD)
    m = re.search(r'/(\d{4})[/-](0[1-9]|1[0-2])[/-](0[1-9]|[12]\d|3[01])(?:[/\-.]|$)', url)
    if m:
        try:
            return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3))), 'day'
        except ValueError:
            pass

    # Compact 8-digit: 20260308
    m = re.search(r'[/-](\d{4})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(?:[/-]|$)', url)
    if m:
        try:
            return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3))), 'day'
        except ValueError:
            pass

    # Compact 6-digit with 2-digit year: news250120 = 2025-01-20
    # Only match if clearly in a slug-like context
    m = re.search(r'(?:news|article|post|blog|update)(\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])', url)
    if m:
        yr = int(m.group(1))
        year = 2000 + yr if yr < 50 else 1900 + yr
        try:
            return datetime(year, int(m.group(2)), int(m.group(3))), 'day'
        except ValueError:
            pass

    # Date in slug: YYYY-MM-DD separated by hyphens in path segment
    m = re.search(r'/(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])/', url)
    if m:
        try:
            return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3))), 'day'
        except ValueError:
            pass

    # Nature DOI year hints: s41746-025- or d41586-024-
    m = re.search(r'[sd]\d+-0?(\d{2,3})-', url)
    if m:
        digits = m.group(1)
        if len(digits) == 3:
            year = 2000 + int(digits)
        elif len(digits) == 2:
            yr = int(digits)
            year = 2000 + yr if yr < 50 else 1900 + yr
        else:
            return None, None
        if 2020 <= year <= 2030:
            return datetime(year, 6, 15), 'year'  # mid-year estimate

    # Month-only: /2026/january/ or /2026/01/
    m = re.search(r'/(\d{4})/(0[1-9]|1[0-2])(?:/|$)', url)
    if m:
        try:
            return datetime(int(m.group(1)), int(m.group(2)), 15), 'month'
        except ValueError:
            pass

    # Month name: /2026/january/
    month_names = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    m = re.search(r'/(\d{4})/(' + '|'.join(month_names.keys()) + r')(?:/|$)', url, re.IGNORECASE)
    if m:
        year = int(m.group(1))
        month = month_names[m.group(2).lower()]
        return datetime(year, month, 15), 'month'

    # /electricity-2025 or similar year-tagged report names
    # Only match years in path segments (between slashes), not in final slug
    for seg in url.split('?')[0].split('/'):
        m = re.match(r'^.*?(\d{4})$', seg)
        if m:
            year = int(m.group(1))
            if 2020 <= year <= 2027:
                # Skip if the segment looks like a content slug with the year
                # at the end (e.g., "by-2030", "to-2030", "2024-2026")
                if re.search(r'(by|to|through|until)-\d{4}$', seg):
                    continue
                if re.search(r'\d{4}-\d{4}$', seg):
                    continue
                return datetime(year, 6, 15), 'year'

    return None, None


class CitationParser(HTMLParser):
    """Extract citations from story-sources divs, tracking background tags."""

    def __init__(self):
        super().__init__()
        self.citations = []  # list of (url, text, is_background)
        self._in_sources = False
        self._in_li = False
        self._current_href = None
        self._current_text = ''
        self._current_background = False
        self._depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'div' and 'story-sources' in attrs_dict.get('class', ''):
            self._in_sources = True
        if self._in_sources and tag == 'li':
            self._in_li = True
            self._current_background = attrs_dict.get('data-type') == 'background'
        if self._in_li and tag == 'a':
            self._current_href = attrs_dict.get('href', '')
            self._current_text = ''

    def handle_data(self, data):
        if self._in_li and self._current_href is not None:
            self._current_text += data

    def handle_endtag(self, tag):
        if tag == 'a' and self._in_li and self._current_href is not None:
            self.citations.append((
                self._current_href,
                self._current_text.strip(),
                self._current_background
            ))
            self._current_href = None
            self._current_text = ''
        if tag == 'li':
            self._in_li = False
            self._current_background = False
        if tag == 'div' and self._in_sources:
            self._in_sources = False


def validate_issue(filepath: str) -> list:
    """Validate a single issue file. Returns list of (level, message) tuples."""
    results = []

    # Extract issue date from filename
    basename = os.path.basename(filepath)
    m = re.match(r'(\d{4}-\d{2}-\d{2})\.html', basename)
    if not m:
        results.append(('ERROR', f'Cannot parse date from filename: {basename}'))
        return results

    issue_date = datetime.strptime(m.group(1), '%Y-%m-%d')
    window_start = issue_date - timedelta(days=WINDOW_DAYS)
    window_end = issue_date + timedelta(days=WINDOW_DAYS)

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    parser = CitationParser()
    parser.feed(html)

    if not parser.citations:
        results.append(('WARN', 'No citations found in file'))
        return results

    for url, text, is_background in parser.citations:
        pub_date, precision = extract_date_from_url(url)

        if pub_date is None:
            results.append(('INFO', f'No date detected in URL: {url}'))
            continue

        # For month/year precision, use wider tolerance
        if precision == 'year':
            year_start = datetime(issue_date.year, 1, 1)
            year_end = datetime(issue_date.year, 12, 31)
            if not (year_start <= pub_date <= year_end) and not is_background:
                delta = (pub_date - issue_date).days
                results.append(('FAIL', f'[{delta:+d}d] {text[:70]}... | URL date: {pub_date.strftime("%Y")} | {url}'))
            elif not (year_start <= pub_date <= year_end) and is_background:
                delta = (pub_date - issue_date).days
                results.append(('BG-OK', f'[{delta:+d}d] Background source: {text[:70]}... | {url}'))
            continue

        if precision == 'month':
            # Allow if same month or adjacent month
            month_diff = (pub_date.year - issue_date.year) * 12 + (pub_date.month - issue_date.month)
            if abs(month_diff) > 1 and not is_background:
                results.append(('FAIL', f'[~{month_diff:+d}mo] {text[:70]}... | URL date: {pub_date.strftime("%Y-%m")} | {url}'))
            elif abs(month_diff) > 1 and is_background:
                results.append(('BG-OK', f'[~{month_diff:+d}mo] Background source: {text[:70]}... | {url}'))
            continue

        # Day precision — strict ±7 day window
        delta = (pub_date - issue_date).days
        if window_start <= pub_date <= window_end:
            results.append(('PASS', f'[{delta:+d}d] {text[:70]}...'))
        elif is_background:
            results.append(('BG-OK', f'[{delta:+d}d] Background source: {text[:70]}... | {url}'))
        else:
            results.append(('FAIL', f'[{delta:+d}d] {text[:70]}... | URL date: {pub_date.strftime("%Y-%m-%d")} | {url}'))

    return results


def main():
    issues_dir = Path(__file__).parent.parent / 'issues'

    if len(sys.argv) > 1:
        files = [Path(f) for f in sys.argv[1:]]
    else:
        files = sorted(issues_dir.glob('*.html'))

    total_fail = 0
    total_bg = 0
    total_pass = 0
    total_info = 0

    for filepath in files:
        results = validate_issue(str(filepath))
        fails = [r for r in results if r[0] == 'FAIL']
        passes = [r for r in results if r[0] == 'PASS']
        bgs = [r for r in results if r[0] == 'BG-OK']
        infos = [r for r in results if r[0] == 'INFO']

        icon = '✗' if fails else '✓'
        print(f'\n{icon} {filepath.name}  ({len(passes)} pass, {len(fails)} fail, {len(bgs)} background, {len(infos)} undated)')

        for level, msg in results:
            if level == 'FAIL':
                print(f'    ✗ FAIL  {msg}')
            elif level == 'BG-OK':
                print(f'    ◎ BG    {msg}')
            elif level == 'INFO':
                # Only show undated in verbose or if there are failures
                if fails or '--verbose' in sys.argv:
                    print(f'    · INFO  {msg}')

        total_fail += len(fails)
        total_bg += len(bgs)
        total_pass += len(passes)
        total_info += len(infos)

    print(f'\n{"═" * 60}')
    print(f'TOTAL: {total_pass} pass, {total_fail} fail, {total_bg} background, {total_info} undated')
    if total_fail > 0:
        print(f'\n✗ {total_fail} citation(s) outside ±{WINDOW_DAYS} day window')
        sys.exit(1)
    else:
        print(f'\n✓ All dated citations within ±{WINDOW_DAYS} day window')
        sys.exit(0)


if __name__ == '__main__':
    main()
