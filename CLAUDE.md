# 3rd Take — Project Instructions

## What This Is

A weekly AI newsletter published every Sunday as a static HTML site, auto-deployed via Vercel on push to `main`.

## Critical Rules

### Citation Date Window (±7 days)

Every source cited in an issue **must** be published within ±7 days of the issue's Sunday date. This is enforced by `workflow/validate-citations.py` and a pre-commit hook.

- **Core citations**: Must fall within the ±7 day window. No exceptions.
- **Background citations**: Foundational research or reference material that predates the window. Must be tagged with `data-type="background"` on the `<li>` element. Keep to 0–2 per issue.

### Before Committing Any Issue File

**Always** run the validator before committing changes to issue HTML files:

```bash
python3 workflow/validate-citations.py issues/YYYY-MM-DD.html
```

The pre-commit hook runs this automatically, but run it yourself first to catch problems early.

### One Source = One Development

A single primary source cannot anchor more than one development in an issue. If two stories trace back to the same paper/report/announcement, merge them into one development.

## Source Quality Standards

**Only Tier 1 and Tier 2 sources are acceptable.** Tier 3 sources must never be used.

| Tier | Examples | Usage |
|------|----------|-------|
| **Tier 1** | Peer-reviewed research (Nature, Science, PNAS), major journalism (WSJ, FT, NYT, Reuters, Guardian, The Economist), HBR, major consulting research (McKinsey Global Institute, BCG Henderson) | Use freely |
| **Tier 2** | MIT Tech Review, think tanks (Brookings, OECD, WEF, ILO, Chatham House, CFR), reputable trade press (SHRM, IAPP), Psychology Today | Use with attribution |
| **Never use** | Yahoo Finance, Yahoo News, Business Insider aggregations, vendor surveys, SEO blogs, opinion-only outlets, content farms | **Blocked** — these undermine credibility |

### URL Verification

Every citation URL must be verified as **actually resolving** before commit. Do not cite URLs without confirming they return a real page (not 404, 403, or paywall-only). Use WebFetch to verify each URL during research.

## File Structure

- `issues/YYYY-MM-DD.html` — Published issues (Sunday dates)
- `templates/issue-template.html` — Blank template for new issues
- `issues/2026-03-08.html` — Canonical example (Issue #10), read before drafting
- `workflow/WORKFLOW.md` — Full editorial workflow
- `workflow/validate-citations.py` — Citation date validator

## Publication Workflow (Summary)

1. Research 3–5 distinct developments from the past 7 days
2. Triple-verify every source: exists, content matches, date within window
3. Draft using the template; follow Issue #10 structure exactly
4. Run `python3 workflow/validate-citations.py issues/YYYY-MM-DD.html` — must pass with 0 failures
5. Update homepage: hero section, issue grid, previous issue nav links
6. Commit and push to main (Vercel auto-deploys)

## Common Mistakes to Avoid

- Citing articles published outside the ±7 day window without `data-type="background"`
- Using the same source for multiple developments
- Forgetting to update the previous issue's navigation links
- Forgetting to update the homepage hero and issue grid
