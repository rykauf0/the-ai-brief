# Weekly Brief — Guided Setup Template

> **What this is:** Paste this entire document into a new Claude chat. It will run a guided setup — asking you all the right questions — then build the complete site automatically. No bracket-filling required.

---

## How to Use

1. Copy this entire document.
2. Paste it into a fresh Claude Code chat.
3. Answer the questions Claude asks you.
4. Claude builds the entire site from your answers.

---

# WEEKLY BRIEFING SITE — GUIDED SETUP

You are a site builder. Your job is to scaffold a complete weekly editorial briefing website. Before building anything, you must run the guided setup below to collect all configuration from the user.

---

## PHASE 1: GUIDED SETUP (ask before building)

Run these steps IN ORDER. Do not skip ahead. Do not start building until all answers are collected.

### Step 1 — Identity

Ask the user these questions (present as a numbered list they can respond to naturally):

```
I'll set up your weekly briefing site. First, a few questions about your publication:

1. What is the name of your publication?
   (e.g. "The AI Brief", "The Climate Dispatch", "The Trade Report")

2. What topic does it cover?
   (e.g. "artificial intelligence", "climate policy", "global trade", "cybersecurity")

3. What day of the week will you publish?
   (e.g. Sunday, Friday, Monday)

4. Who is your target reader? Describe them in one sentence.
   (e.g. "Informed professionals who follow AI closely and are skeptical of hype.")

5. What is the publication's editorial identity — one line?
   (e.g. "The full picture." / "Good, bad, and ugly." / "What's actually happening." / "No cheerleading. No doom. Just evidence.")
```

Wait for answers. Then proceed to Step 2.

### Step 2 — Topic Pillars

Ask the user to define their four content pillars. Present it like this:

```
Every issue is tagged with topic pillars — exactly four categories that cover your subject's landscape.
These are topic areas for filtering and tagging — the editorial lens (what's working, what's not,
what nobody's saying) operates across ALL pillars in the synthesis.

For each pillar, I need:
- A short code (3-4 letters, lowercase — used in CSS and HTML)
- A display name (what readers see)
- A one-sentence scope (what falls under this pillar)

Here's an example for an AI publication:
  1. sci  — Science & Research — Breakthroughs, papers, benchmarks, technical advances
  2. gov  — Governance & Policy — Regulation, institutional adoption, accountability frameworks
  3. work — Work & Industry — How organizations change, what gets automated, business models
  4. soc  — Society & Ethics — Human impact, inequality, philosophical questions, cultural shifts

Now define your four pillars:
  1. [code] — [Display Name] — [Scope]
  2. [code] — [Display Name] — [Scope]
  3. [code] — [Display Name] — [Scope]
  4. [code] — [Display Name] — [Scope]
```

Wait for answers. Then proceed to Step 3.

### Step 3 — Colour Preference

Ask the user:

```
Last question. Each pillar gets its own accent colour. You have two options:

A) I'll pick harmonious colours for you based on your topic (recommended)
B) You specify four hex colours, one per pillar

Which do you prefer?
```

If they choose A, select four professional, muted colours that complement the base palette and suit the topic. Slate blues, forest greens, warm golds, and earthy tones work well. Avoid bright/saturated primaries.

If they choose B, collect four hex values.

### Step 4 — Confirm and Build

Present a summary of all collected values:

```
Here's your publication setup:

  Name:      [collected name]
  Topic:     [collected topic]
  Cadence:   Every [collected day]
  Audience:  [collected audience]
  Motto:     [collected motto]

  Pillars:
    1. [code] — [Name] — [colour] — [scope]
    2. [code] — [Name] — [colour] — [scope]
    3. [code] — [Name] — [colour] — [scope]
    4. [code] — [Name] — [colour] — [scope]

Ready to build? (yes / or tell me what to change)
```

Wait for confirmation. Then proceed to Phase 2.

---

## PHASE 2: BUILD THE SITE

Once all values are confirmed, build everything below using the collected answers. Replace every instance of the placeholder tokens with the user's actual values:

- `{{NAME}}` → publication name
- `{{TOPIC}}` → topic
- `{{DAY}}` → publication day
- `{{AUDIENCE}}` → audience description
- `{{MOTTO}}` → motto
- `{{TAGLINE}}` → generate from name + topic (e.g. "Weekly intelligence on [topic]")
- `{{P1_CODE}}`, `{{P1_NAME}}`, `{{P1_COLOR}}`, `{{P1_SCOPE}}` → pillar 1 values
- `{{P2_CODE}}`, `{{P2_NAME}}`, `{{P2_COLOR}}`, `{{P2_SCOPE}}` → pillar 2 values
- `{{P3_CODE}}`, `{{P3_NAME}}`, `{{P3_COLOR}}`, `{{P3_SCOPE}}` → pillar 3 values
- `{{P4_CODE}}`, `{{P4_NAME}}`, `{{P4_COLOR}}`, `{{P4_SCOPE}}` → pillar 4 values
- `{{YEAR}}` → current year

---

### 2.1 File Structure

Create this exact structure:

```
[project-root]/
├── index.html                  Homepage (hero, about strip, pillars, archive grid)
├── about.html                  Editorial standards and mission
├── site.css                    Global design system
├── article.css                 Article components
├── vercel.json                 Deployment config
├── js/
│   └── main.js                 Topic filter + reading progress bar
├── templates/
│   ├── issue-template.html     Canonical template for new issues
│   └── homepage-card.html      Homepage card markup pattern
├── issues/
│   └── [first-issue-date].html Issue #1
└── workflow/
    └── WORKFLOW.md             Publishing workflow and editorial standards
```

---

### 2.2 Design System

Build a static site with **zero dependencies** — pure HTML, CSS, and vanilla JavaScript. No frameworks, no build step, no package manager.

#### Colour Palette

```
Backgrounds:
  --bg:         #FAFAF8     (warm off-white)
  --surface:    #F4F3F0     (slightly darker surface)
  --surface-2:  #ECEAE5     (card hover / inset)
  --border:     #E0DED8
  --border-2:   #CCCAC4

Text:
  --text:       #1A1917     (near-black)
  --text-2:     #3D3C39     (dark gray — body secondary)
  --text-3:     #7A7872     (medium gray — metadata)

Primary accent:
  --navy:       #1B3A6B
  --navy-light: #EEF3FB
  --navy-mid:   rgba(27,58,107,0.12)

Warm accent:
  --gold:       #8B5E00
  --gold-light: #FDF6E3

Pillar colours (from user input):
  --{{P1_CODE}}-color: {{P1_COLOR}}
  --{{P2_CODE}}-color: {{P2_COLOR}}
  --{{P3_CODE}}-color: {{P3_COLOR}}
  --{{P4_CODE}}-color: {{P4_COLOR}}
```

#### Typography

- **Serif:** Georgia, 'Times New Roman', serif — headlines, titles, publication name
- **Sans-serif:** -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif — body, metadata, UI
- **Type scale:** Minimum 16px base. Body text 18px (1.125rem). Scale: 0.8125rem / 0.875rem / 1.125rem / 1.25rem / 1.5rem / 1.875rem / 2.25rem
- **Line height:** 1.6 base, 1.8 for body paragraphs

#### Layout

- `--max-w: 1080px` (homepage)
- `--content-w: 720px` (article body)
- `--r: 4px` (border-radius)
- `--r-lg: 8px` (large border-radius)
- Mobile-first: 1 col → 2 col (600px) → 3 col (900px)

#### Design Patterns

- **Sticky masthead** — backdrop blur, serif italic logo, nav links, "Latest Issue" CTA button
- **Mobile hamburger menu** — toggles nav visibility
- **Hero section** — latest issue with excerpt, meta info, read CTA
- **About strip** — 3-column value proposition (What's Working / What's Not / What Nobody's Saying)
- **Pillars key** — coloured dots with pillar names as visual legend
- **Archive grid** — responsive card grid with topic filter buttons (All + one per pillar)
- **Reading progress bar** — 3px fixed bar at viewport top, scroll-driven
- **Section breaks** — centered text labels with horizontal rules on each side
- **Synthesis section** — navy-tinted background, 3px navy top border, rounded bottom
- **Bottom line box** — white background, navy border inside synthesis
- **Issue navigation** — prev / home / next links between issues
- **Footer** — 3-column grid: brand + motto, nav links, standards statement

---

### 2.3 Component Specifications

#### Global Stylesheet (`site.css`)

All CSS variables, reset, base styles, and these components:
- **Reading progress bar** — `#reading-progress`: fixed, top:0, 3px height, navy bg, width transitions
- **Masthead** — sticky, backdrop-blur, 64px height, flex layout, mobile toggle
- **Hero** — border-bottom, large serif title with underline hover, meta badges, excerpt, CTA
- **About strip** — 3-column grid (1-col mobile), uppercase labels, descriptive text
- **Pillars key** — flex wrap, 8px coloured dots, pillar names
- **Archive** — filter bar (pill buttons), responsive issue grid
- **Issue cards** — white bg, border, rounded corners, hover (navy border + shadow), meta/title/excerpt/tags
- **Tags** — pill-shaped, coloured per pillar with light backgrounds and tinted borders
- **Footer** — surface bg, 3-column grid, logo, motto, nav links, standards
- **About page** — hero section, body content, pillar list cards, standards list with em-dash bullets
- **Scrollbar** — thin, subtle, themed

#### Article Stylesheet (`article.css`)

- **Article header** — surface bg, issue kicker, badges, h1, deck (serif italic), byline
- **Story blocks** — numbered circle badge (navy-light bg), serif h2, border-bottom header
- **Badges** — inline-flex pills, uppercase, coloured per pillar (`.badge.{{CODE}}` and `.badge-{{CODE}}`)
- **Section breaks** — flex with before/after pseudo-element lines, centered uppercase label
- **Synthesis** — navy-light bg, navy top border (3px), rounded bottom, generous padding
- **Bottom line** — white box inside synthesis, navy uppercase label, summary text
- **Editorial note** — `.editorial-note`: italic, text-3 colour, 0.9375rem, border-left 2px border colour, padding-left 1rem, margin-top 0.5rem
- **Synthesis sub-sections** — `.syn-section` h3 headers within `.synthesis`: uppercase, 0.8125rem, letter-spacing 0.08em, margin-top 2rem; `.syn-good` colour: `#2E6E3F`; `.syn-bad` colour: `#8B3A3A`; `.syn-ugly` colour: `#6B4E00`
- **Story sources** — border-top separator, uppercase "Sources" label, links with arrow prefix
- **Issue navigation** — flex space-between, bordered pill buttons, disabled state at 60% opacity
- **Author bio** — bordered card, surface bg, uppercase label, description text

#### JavaScript (`js/main.js`)

Two progressive-enhancement features (site fully functional without JS):

**Topic filter:**
- Reads `data-topic` from `.filter-btn` clicks
- Shows/hides `.issue-card` elements by matching `data-topics` attribute
- "all" shows everything; specific topic checks `.includes()`

**Reading progress:**
- Passive scroll listener
- Calculates: `scrollY / (scrollHeight - innerHeight) * 100`
- Sets width on `#reading-progress`

---

### 2.4 Issue Template (`templates/issue-template.html`)

Each issue page follows this exact structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[ONE-SENTENCE DESCRIPTION]">
  <title>[ISSUE TITLE] — {{NAME}}</title>
  <link rel="stylesheet" href="../site.css">
  <link rel="stylesheet" href="../article.css">
</head>
<body>
  <div id="reading-progress"></div>

  <header class="masthead">
    <div class="masthead-inner">
      <a href="../index.html" class="masthead-brand">
        <span class="masthead-name">{{NAME}}</span>
        <span class="masthead-tagline">{{TAGLINE}}</span>
      </a>
      <button class="nav-toggle" onclick="document.querySelector('.masthead-nav').classList.toggle('open')" aria-label="Toggle navigation">
        ☰ Menu
      </button>
      <nav class="masthead-nav">
        <a href="../index.html">Home</a>
        <a href="../about.html">About</a>
        <a href="../index.html#archive">Archive</a>
        <a href="../issues/[LATEST-DATE].html" class="masthead-cta">Latest Issue →</a>
      </nav>
    </div>
  </header>

  <div class="article-header">
    <div class="article-header-inner">
      <p class="issue-kicker">Issue #[N] · [Day], [Full Date]</p>
      <div class="article-header-badges">
        <span class="badge badge-[pillar]">[Pillar Name]</span>
        <span class="badge badge-[pillar]">[Pillar Name]</span>
      </div>
      <h1>[ISSUE TITLE]</h1>
      <p class="article-deck">[ONE-LINE FRAME — what connects the developments]</p>
      <p class="article-byline">{{NAME}} · [Day], [Full Date]</p>
    </div>
  </div>

  <div class="article-body">
    <p>[FRAMING PARAGRAPH — 2-3 sentences connecting the week's developments]</p>

    <div class="section-break"><span>this week</span></div>

    <!-- DEVELOPMENT 1 (repeat pattern for 5 developments) -->
    <article class="story">
      <div class="story-header">
        <span class="story-num">1</span>
        <h2>[DEVELOPMENT HEADLINE]</h2>
      </div>
      <span class="badge badge-[pillar]">[Pillar Name]</span>
      <p>[What happened — stated precisely]</p>
      <p>[Why it matters — mechanism, evidence, context]</p>
      <p class="editorial-note">Why this matters: [one sentence — is this progress, a setback, or an uncomfortable truth nobody wants to name?]</p>
      <div class="story-sources">
        <p class="src-label">Sources</p>
        <ul>
          <li><a href="[URL]">[Publication], "[Title]"</a></li>
        </ul>
      </div>
    </article>

    <div class="section-break"><span>• • •</span></div>
    <!-- ... more developments ... -->

    <div class="section-break"><span>what it means</span></div>

    <section class="synthesis">
      <h2>What It All Means</h2>
      <p class="syn-byline">{{NAME}} · Issue #[N], [Full Date]</p>

      <h3 class="syn-section syn-good">What's Working</h3>
      <p>[3-5 sentences. Genuine progress backed by evidence. Be specific — name the advance, cite the data.]</p>

      <h3 class="syn-section syn-bad">What's Not</h3>
      <p>[3-5 sentences. Failures, overpromises, gaps. Name what broke, what underdelivered. Specific, not generic.]</p>

      <h3 class="syn-section syn-ugly">What Nobody's Saying</h3>
      <p>[3-5 sentences. Uncomfortable truths, perverse incentives, structural problems. The stuff both boosters and critics avoid.]</p>

      <div class="bottom-line">
        <strong>Bottom line</strong>
        <p>[2-3 sentences — the single most important takeaway that holds the good, bad, and ugly together. Specific to this week.]</p>
      </div>
    </section>

    <nav class="issue-nav">
      <a href="[PREV-DATE].html" class="nav-prev">Issue #[N-1] — [Mon Day]</a>
      <a href="../index.html" class="nav-home">Home</a>
      <a href="[NEXT-DATE].html" class="nav-next">Issue #[N+1] — [Mon Day]</a>
      <!-- Use <span class="nav-disabled"> for first/latest issue boundaries -->
    </nav>

    <div class="author-bio">
      <span class="bio-label">About this publication</span>
      <p>{{NAME}} publishes every {{DAY}}. The week's signal developments, then what they mean together. No advertising. <a href="../about.html">About our editorial standards →</a></p>
    </div>
  </div>

  <footer>
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="footer-logo">{{NAME}}</div>
        <p class="footer-motto">{{TAGLINE}}. Published every {{DAY}}.</p>
      </div>
      <div class="footer-links">
        <h4>Navigate</h4>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../about.html">About</a></li>
          <li><a href="../index.html#archive">All Editions</a></li>
        </ul>
      </div>
      <div class="footer-standards">
        <h4>Our Standards</h4>
        <p>Every claim sourced. Every source linked. No advertising. Sources verified before publication.</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {{YEAR}} {{NAME}}</span>
      <span><a href="../about.html">About</a></span>
    </div>
  </footer>
  <script src="../js/main.js"></script>
</body>
</html>
```

### Homepage Card Template (`templates/homepage-card.html`)

```html
<a class="issue-card" href="issues/[YYYY-MM-DD].html" data-topics="[pillar1] [pillar2]">
  <div class="card-meta">
    <span class="card-date">[Month Day, Year]</span>
    <span class="card-num">No. [N]</span>
  </div>
  <p class="card-title">[Issue Title]</p>
  <p class="card-excerpt">[One specific sentence — what the reader will learn]</p>
  <div class="card-tags">
    <span class="tag [pillar1-code]">[Pillar1]</span>
    <span class="tag [pillar2-code]">[Pillar2]</span>
  </div>
</a>
```

---

### 2.5 Publishing Workflow (`workflow/WORKFLOW.md`)

Create this file adapted to the user's topic. Include all of the following:

#### Issue Format

Two parts, weighted deliberately:

**Part 1 — This Week's Developments** (5 items)
- Each anchored by a *distinct* primary source (preferably Tier 1 research)
- Same source = same development — merge them
- 2-3 paragraphs of tight analysis + one-line editorial note + source links per development
- The editorial note signals where this development sits: genuine progress, a setback, or an uncomfortable truth
- Developments are reported with evidence-weighted honesty — no reflexive optimism or pessimism

**Part 2 — What It All Means** (~300-450 words total, three concise sections)
- The centrepiece, not the postscript — but concise, not exhaustive
- **What's Working** — 3-5 sentences. Genuine progress backed by evidence
- **What's Not** — 3-5 sentences. Failures, overpromises, gaps between claims and reality
- **What Nobody's Saying** — 3-5 sentences. Structural problems, perverse incentives, uncomfortable truths
- **Bottom Line** — 2-3 sentences that hold all three dimensions together
- Each section earns its space through specificity, not length. Say it once, say it well, move on

#### Research Process

- **Goal:** 5 genuinely distinct developments from the past 7 days, grounded in primary research
- **Research-first:** Start with academic journals, research labs, think tanks, and government reports. Use journalism to find *leads*, then trace back to the primary source.
- **Development scope is broad:** Developments can come from scientific breakthroughs, academic papers, philosophical/ethical scholarship, social science research, policy analysis, environmental science, clinical trials — any domain where the topic intersects with real-world consequences. This is not a tech news roundup.
- **One-source-per-development rule:** If two stories trace to the same paper/report/event, they are one development — merge them
- **Distinct = different domain, different publication, different event**
- **Balance in selection:** Actively seek developments that represent genuine progress *and* genuine problems. If all candidates are good news or all bad news, the research isn't done.
- Include topic-specific search strategy templates adapted to the user's subject area

#### Source Credibility Tiers

Sources are divided into three tiers. **Only Tier 1 and Tier 2 sources may be cited in a published issue.** Tier 3 sources are rejected outright — they cannot appear even as corroboration.

**Tier 1 — Research & Primary Authority** (the foundation — prioritise above all else)

The publication leads with research, not news. These sources are the evidence base.

| Category | Examples |
|----------|----------|
| **Peer-reviewed journals & academic research** | Nature, Science, PNAS, The Lancet, JAMA, IEEE, ACM, arXiv (with peer-review status noted), NBER working papers, SSRN, university press releases tied to published papers |
| **Research institutions & labs** | Google DeepMind, OpenAI research papers, Microsoft Research, Meta FAIR, Allen Institute for AI, Santa Fe Institute, Mozilla Foundation research |
| **Think tanks with research arms** | Brookings, RAND, CFR, Chatham House, Carnegie Endowment, Peterson Institute, Aspen Institute, Atlantic Council, Center for a New American Security, AI Now Institute |
| **Government & regulatory research** | NIST, GAO, CBO, EU Commission research, UK Parliament reports, OECD, IMF/World Bank research, NIH, NSF, DARPA, FDA, EPA |
| **Major consulting & analyst research** | McKinsey Global Institute, BCG Henderson Institute, Deloitte Insights, Gartner, Forrester, IDC, CB Insights |
| **Ethical & philosophical scholarship** | University centres for ethics/AI/technology, philosophy journals, policy ethics publications |

**Tier 2 — Contextual & Specialist Reporting** (adds depth and accessibility — secondary to research)

Journalism is used to contextualise research findings, not as the primary evidence base. Quality journalism *reporting on* Tier 1 research is valuable. Journalism offering its own analysis without primary sources is weaker.

| Category | Examples |
|----------|----------|
| **Prestige journalism (when reporting on primary research)** | Reuters, Associated Press, Financial Times, Wall Street Journal, New York Times, Washington Post, The Guardian, The Economist, Bloomberg, HBR |
| **Specialist press covering research** | MIT Technology Review, Wired (features), Ars Technica, The Information, Semafor, Rest of World, STAT News, E&E News, Inside Climate News |
| **Credentialed thought leaders** | Stratechery, One Useful Thing (Ethan Mollick), Dario Amodei's writing, substantive Substack authors with demonstrated domain expertise |
| **Industry bodies & standards orgs** | IEEE Spectrum, Partnership on AI, Electronic Frontier Foundation, W3C, IETF, World Economic Forum reports |

**Tier 3 — REJECTED (never cite)**

These sources are explicitly banned from the publication. Do not use them in any capacity — not as primary sources, not as corroboration, not as "one perspective."

| Rejected category | Examples & why |
|-------------------|----------------|
| **Aggregation & clickbait news** | Yahoo News, Yahoo Finance, MSN, AOL, Huffington Post — repackage others' work, add no original reporting |
| **Cable news & partisan outlets** | Fox News, CNBC, CNN opinion, MSNBC, Daily Mail, New York Post — editorial slant contaminates factual reporting |
| **Content farms & SEO mills** | Business Insider (most articles), Forbes contributor network, Inc.com, Entrepreneur.com — pay-per-click incentives over accuracy |
| **Vendor marketing disguised as research** | Company blogs announcing their own products, vendor-sponsored "surveys" with leading questions, press releases without independent verification |
| **Social media as source** | Tweets, LinkedIn posts, Reddit threads — use only to locate the *actual* primary source, never cite the social post itself |
| **Crypto/hype ecosystem** | CoinDesk, TechCrunch (puff pieces), VentureBeat (most), product launch coverage with no critical analysis |

**When in doubt:** Ask — "Is this outlet paid to report accurately, or paid to generate clicks?" If the latter, reject it.

---

#### PHASE 2.5: CITATIONS VERIFICATION GATE

**This is a mandatory step.** After deep research and before writing begins, run this verification protocol on every candidate source. No source enters the draft without passing all checks.

##### Step 1 — Source Sufficiency Check

Before writing, confirm:

```
Research quality gate:
- [ ] At least 10-15 candidate sources identified (to select the best 10-15 for 5 developments)
- [ ] At least 2 distinct sources per development (primary + corroboration)
- [ ] Sources span at least 3 of the 4 topic pillars
- [ ] At least 50% of sources are Tier 1 (primary authority)
- [ ] Remaining sources are Tier 2 (specialist journalism)
- [ ] Zero Tier 3 sources in the candidate list

If any check fails → return to research. Do not proceed to writing with thin sourcing.
```

##### Step 2 — Source-by-Source Verification

For every source that will appear in the issue, run these checks sequentially:

```
For each source URL:

1. TIER CHECK
   → Identify the publication. Is it on the Tier 1 or Tier 2 list?
   → If Tier 3 or unlisted: REJECT. Find an alternative.
   → If borderline: flag for user review before proceeding.

2. LINK VERIFICATION
   → Fetch the URL. Does it resolve to a live page (not 404, not paywall-only, not redirect to homepage)?
   → If the link is dead or broken: search for the correct URL.
   → If the article cannot be located at all: DROP the source entirely.

3. CONTENT MATCH
   → Read/scan the fetched page. Does the article actually say what you're attributing to it?
   → Check: author, date, key claims, key data points.
   → If the content doesn't match your attribution: correct the attribution or drop the source.

4. CURRENCY CHECK
   → Is the publication date within the last 7 days (for news) or last 12 months (for research/reports)?
   → If older: flag explicitly in the development ("published in [month/year]") or find something more current.

5. INDEPENDENCE CHECK
   → Is this source independent from the subject it covers?
   → A company's press release about its own product is not an independent source.
   → A vendor-commissioned survey is not independent research.
   → If not independent: use only with explicit caveat, or find independent corroboration.
```

##### Step 3 — Cross-Source Integrity

After individual verification, check the full source set:

```
Cross-source checks:
- [ ] No two developments rely on the same primary source
- [ ] No single publication appears more than twice across the entire issue
- [ ] Sources represent at least 3 different types (e.g. research paper + policy report + journalism + analyst firm)
- [ ] No source is cited for a claim it doesn't actually make
- [ ] All URLs are HTTPS and resolve to the specific article (not a homepage or section page)
```

##### Step 4 — Verification Report

Present the verification results to the user before writing:

```
Source verification complete. Here's what I found:

  Development 1: [headline]
    ✓ [Source 1] — Tier [X], verified, [publication date]
    ✓ [Source 2] — Tier [X], verified, [publication date]

  Development 2: [headline]
    ✓ [Source 1] — Tier [X], verified, [publication date]
    ⚠ [Source 2] — [issue found, e.g. "paywall — using cached excerpt"]

  [etc.]

  Summary: [N] sources verified, [N] flagged, [N] rejected
  Tier breakdown: [N] Tier 1, [N] Tier 2

Proceed to writing? (yes / or flag concerns)
```

Wait for user confirmation before writing the issue.

---

#### Writing Standards

- **Voice:** Calm clarity. Collaborative "we" in synthesis. Match your tone to the evidence — celebrate what works, name what doesn't, surface what's hidden. No default stance.
- **Balance test:** Does this issue acknowledge genuine progress *and* genuine problems? If it reads as uniformly optimistic or uniformly pessimistic, the lens isn't doing its job.
- **Audience test:** Would a thoughtful professional who's seen hype cycles *and* premature dismissals trust this? If it reads like cheerleading or doom, revise.
- **Development length:** 2-3 tight paragraphs + editorial note + sources
- **Synthesis length:** 3 sections (What's Working / What's Not / What Nobody's Saying) totalling ~300-450 words + bottom line. Each section: 3-5 sentences. Concise and specific, not exhaustive
- **Synthesis quality test:** Does each section earn its space? Does the bottom line hold all three dimensions together without picking a side? If the synthesis skips any dimension, it's incomplete.

#### Pre-Publish Checklist

**Sourcing (must have passed Phase 2.5 Citations Verification Gate):**
- [ ] Each development traces to a distinct primary source
- [ ] No single source for multiple developments
- [ ] All URLs verified live and resolving to correct article
- [ ] All sources Tier 1 or Tier 2 — zero Tier 3 sources present
- [ ] No rejected-list publications (Yahoo, Fox, CNBC, Forbes contributors, etc.)
- [ ] At least 50% of sources are Tier 1 (primary authority)
- [ ] Verification report presented to user and approved

**Content:**
- [ ] Framing connects without over-explaining
- [ ] Each development has a one-line editorial note (progress / setback / uncomfortable truth)
- [ ] Synthesis has all three sections: What's Working, What's Not, What Nobody's Saying
- [ ] Each synthesis section earns its space with specific evidence, not filler
- [ ] Bottom line holds all three dimensions together without picking a side
- [ ] Issue doesn't read as uniformly optimistic or uniformly pessimistic
- [ ] No hype language without evidence; no doom without evidence

**Technical:**
- [ ] HTML matches issue template
- [ ] Both stylesheets linked
- [ ] Script tag before `</body>`
- [ ] Meta description present
- [ ] Issue nav links correct

#### Homepage Update Process

1. Update hero section → point to new issue
2. Add new card to top of `.issue-grid`
3. Update previous issue's nav → add `nav-next` link
4. Update masthead "Latest Issue" link across all pages

---

### 2.6 Analytical Framework

Embed these principles in the workflow and about page:

#### The Full Picture Lens

The publication's core commitment: **tell readers what's actually happening — what's working, what's not, and what nobody wants to say out loud.** This is not "both sides" centrism. It's evidence-weighted honesty. The evidence decides the tone, not a predetermined editorial stance.

- **Balance as discipline:** If the evidence says something is working, celebrate it without reflexive caveats. If it says something is broken, name the failure without softening it. If it's complicated, say that. Reflexive skepticism is as dishonest as reflexive hype.
- **Three questions for every development:**
  1. What's genuinely new or significant here?
  2. What's being overstated, understated, or left out?
  3. What would change if this trend continues — and who benefits or loses?
- **Good news earns its place:** Real progress doesn't need qualifiers if the evidence supports it. A breakthrough is a breakthrough. Report it as one.
- **Bad news earns specificity:** Don't just say "it's failing" — name the mechanism, the gap between promise and reality, the evidence.
- **Ugly truths earn their name:** "What nobody's saying" isn't cynicism — it's the structural dynamics, incentive problems, and second-order effects that don't fit neat narratives. The stuff that makes both boosters and critics uncomfortable.
- **Research-grounded, not news-driven:** Lead with academic research, scientific findings, policy analysis, and expert scholarship. Journalism provides context and accessibility, not the primary evidence base.
- **Combination over sequence:** The synthesis finds patterns visible only when developments are read together — and sorts them into what's working, what's not, and what nobody wants to name.

#### What Makes Good Synthesis

The synthesis has three visible sections — **What's Working**, **What's Not**, and **What Nobody's Saying** — plus a unifying **Bottom Line**.

Quality tests:
- Does the synthesis say something none of the individual developments say?
- Does "What's Working" identify genuine progress supported by evidence (not just announcements)?
- Does "What's Not" name specific failures, gaps, or overpromises (not generic caution)?
- Does "What Nobody's Saying" surface a structural truth that both cheerleaders and doomsayers would rather ignore?
- Does the bottom line hold all three together — not picking a side, but naming the reality?

Good synthesis:
- Names the coherent signal across developments
- Identifies tension or contradiction between them
- Surfaces second-order implications
- Connects to institutional or structural dynamics
- Gives readers an analytical frame they cannot get elsewhere
- **Earns every section:** If there's nothing genuinely good this week, say so — don't manufacture optimism. If there's nothing ugly, don't force it. But usually, all three are present.

---

### 2.7 Deployment (`vercel.json`)

```json
{
  "version": 2,
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" }
      ]
    },
    {
      "source": "/(.*)\\.(css|js)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
```

---

### 2.8 Build Order

1. Create all directories and files per the structure in 2.1
2. Write complete `site.css` — all variables, all components from 2.3
3. Write complete `article.css` — all article components from 2.3
4. Write `main.js` — both progressive-enhancement features
5. Build `index.html` — masthead, hero, about strip, pillars key, archive grid
6. Build `about.html` — editorial mission, pillar descriptions, standards, analytical lens (adapted to topic)
7. Create both templates in `templates/`
8. Write `workflow/WORKFLOW.md` — full editorial workflow with topic-specific search strategies
9. Create `vercel.json`
10. Draft Issue #1 — run deep research, then run the **Citations Verification Gate (Phase 2.5)** on all candidate sources, present the verification report for user approval, and only then write the issue as a scene-setting edition that establishes the publication's analytical identity

The site must work with zero build steps. Progressive enhancement: fully functional without JavaScript.

---

### 2.9 The Pattern

```
┌────────────────────────────────────────┐
│  5 distinct developments               │
│  (research-grounded, one source each)  │
│  (2-3 paragraphs + editorial note      │
│   + citations each)                    │
├────────────────────────────────────────┤
│  "What It All Means" synthesis         │
│  (300-450 words, three sections)       │
│                                        │
│  ┌── What's Working ──────────────┐    │
│  │ Genuine progress, earned       │    │
│  │ optimism backed by evidence    │    │
│  ├── What's Not ──────────────────┤    │
│  │ Failures, overpromises, gaps   │    │
│  │ between claims and reality     │    │
│  ├── What Nobody's Saying ────────┤    │
│  │ Uncomfortable truths, perverse │    │
│  │ incentives, structural problems│    │
│  └────────────────────────────────┘    │
├────────────────────────────────────────┤
│  Bottom line                           │
│  (2-3 sentences — holds all three      │
│   dimensions together)                 │
└────────────────────────────────────────┘
```

**The value proposition:** The full picture — good, bad, and ugly. Not cheerleading. Not doom. Evidence-weighted honesty about what's actually happening, grounded in research and primary sources. The synthesis is where the genuine analytical work happens: identifying what's working, naming what's not, and surfacing what nobody wants to say out loud.
