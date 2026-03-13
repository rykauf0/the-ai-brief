# Weekly Brief — Reusable Template

> **What this is:** A complete set of instructions to give Claude in a new chat so it can build you a weekly editorial briefing site on **any topic you choose**. Copy everything below the line, paste it into a new conversation, fill in the `[BRACKETED]` placeholders with your topic, and let Claude build it.

---

## How to Use

1. Copy everything from **"START OF PROMPT"** to **"END OF PROMPT"** below.
2. Replace every `[BRACKETED PLACEHOLDER]` with your own topic, pillar names, colours, and publication name.
3. Paste it into a fresh Claude Code chat (or any Claude chat with tool access).
4. Claude will scaffold the entire project — site, styles, templates, workflow — ready for you to start publishing.

---

<!-- ═══════════════════════════════════════════════════════════════ -->
# START OF PROMPT
<!-- ═══════════════════════════════════════════════════════════════ -->

---

# Build Me a Weekly Editorial Briefing Site

## 1. The Publication

**Name:** `[YOUR PUBLICATION NAME]`
**Tagline:** `[SHORT TAGLINE, e.g. "Weekly intelligence on [TOPIC]"]`
**Cadence:** Every `[DAY OF WEEK, e.g. Sunday]`
**Topic:** `[YOUR TOPIC — e.g. "climate policy", "education technology", "global trade", "cybersecurity"]`
**Audience:** `[DESCRIBE YOUR READER — e.g. "Informed, skeptical professionals who follow [TOPIC] closely and have seen enough hype cycles to be deeply wary of them."]`
**Motto:** `[ONE-LINE EDITORIAL IDENTITY — e.g. "Consequences, not announcements." or "Signal over noise." or "Evidence over enthusiasm."]`

---

## 2. The Four Topic Pillars

Define exactly four content pillars that cover the landscape of your topic. Each gets a short code, a display name, and a colour.

| Code | Display Name | Colour (hex) | Scope |
|------|-------------|---------------|-------|
| `[pillar1-code]` | `[Pillar 1 Name]` | `[#hex]` | `[What it covers]` |
| `[pillar2-code]` | `[Pillar 2 Name]` | `[#hex]` | `[What it covers]` |
| `[pillar3-code]` | `[Pillar 3 Name]` | `[#hex]` | `[What it covers]` |
| `[pillar4-code]` | `[Pillar 4 Name]` | `[#hex]` | `[What it covers]` |

**Example for AI:**
| Code | Display Name | Colour | Scope |
|------|-------------|--------|-------|
| `gov` | Governance & Policy | `#1B5E7B` | Regulation, government adoption, institutional accountability |
| `work` | Work & Organizations | `#2E6E3F` | How it reshapes organizations, what gets automated |
| `econ` | Economy & Society | `#8B5E00` | Productivity, labour markets, inequality, transition costs |
| `env` | Environment & Planet | `#3A6E3A` | Energy/water footprint, data centre growth, climate trade-offs |

---

## 3. Design System

Build a static site with **zero dependencies** — pure HTML, CSS, and vanilla JavaScript. No frameworks, no build step, no package manager.

### Colour Palette

```
Backgrounds:
  --bg:         #FAFAF8     (warm off-white)
  --surface:    #F4F3F0     (slightly darker surface)
  --surface-2:  #ECEAE5     (card hover / inset)
  --border:     #E0DED8
  --border-2:   #CCCAC4

Text (warm near-black stack):
  --text:       #1A1917     (near-black)
  --text-2:     #3D3C39     (dark gray — body secondary)
  --text-3:     #7A7872     (medium gray — metadata)

Primary accent (authority):
  --navy:       #1B3A6B
  --navy-light: #EEF3FB
  --navy-mid:   rgba(27,58,107,0.12)

Warm accent (dates, highlights):
  --gold:       #8B5E00
  --gold-light: #FDF6E3

Pillar colours:
  --[pillar1]-color: [hex]
  --[pillar2]-color: [hex]
  --[pillar3]-color: [hex]
  --[pillar4]-color: [hex]
```

### Typography

- **Serif:** Georgia, 'Times New Roman', serif — for headlines, titles, publication name
- **Sans-serif:** -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif — for body, metadata, UI
- **Type scale:** Minimum 16px base. Body text at 18px (`1.125rem`). Scale: `0.8125rem / 0.875rem / 1.125rem / 1.25rem / 1.5rem / 1.875rem / 2.25rem`
- **Line height:** 1.6 base, 1.8 for body paragraphs

### Layout

- `--max-w: 1080px` (homepage max width)
- `--content-w: 720px` (article body max width)
- `--r: 4px` (standard border-radius)
- `--r-lg: 8px` (large border-radius)
- Mobile-first responsive: 1 column → 2 columns (600px) → 3 columns (900px) for archive grid

### Key Design Patterns

- **Sticky masthead** with backdrop blur, logo (serif italic), nav links, and "Latest Issue" CTA button
- **Mobile hamburger menu** that toggles nav visibility
- **Hero section** featuring the latest issue with excerpt, meta info, and read CTA
- **About strip** — 3-column value proposition (Format / Standards / Perspective)
- **Pillars key** — coloured dots with pillar names as a visual legend
- **Archive grid** — responsive card grid with topic filter buttons (All + one per pillar)
- **Reading progress bar** — 3px fixed bar at top of viewport tracking scroll depth
- **Section breaks** — centered text labels with horizontal rules on each side
- **Synthesis section** — navy-tinted background, 3px navy top border, rounded bottom corners
- **Bottom line box** — white background with navy border inside the synthesis
- **Issue navigation** — prev / home / next links between issues
- **Footer** — 3-column grid: brand + motto, nav links, standards statement

---

## 4. Site Architecture

### File Structure

```
[project-root]/
├── index.html                  Homepage (hero, about strip, pillars, archive grid)
├── about.html                  Editorial standards and mission
├── site.css                    Global design system (all variables, masthead, hero, grid, footer, about page styles)
├── article.css                 Article components (header, stories, badges, section breaks, synthesis, sources, issue nav, author bio)
├── vercel.json                 Deployment config (clean URLs, security headers, asset caching)
├── js/
│   └── main.js                 Topic filter + reading progress bar (progressive enhancement)
├── templates/
│   ├── issue-template.html     Canonical template for new issues
│   └── homepage-card.html      Homepage card markup pattern
├── issues/
│   └── YYYY-MM-DD.html         Individual issues (filename = publication date)
└── workflow/
    └── WORKFLOW.md             Complete publishing workflow and editorial standards
```

### Pages

1. **Homepage (`/`)** — Featured latest issue hero, about strip, pillars key, filterable archive grid
2. **About (`/about.html`)** — Editorial mission, format explanation, pillar descriptions, editorial standards, analytical lens
3. **Issues (`/issues/YYYY-MM-DD.html`)** — Individual weekly issues following the canonical template

---

## 5. Component Specifications

### 5a. Global Stylesheet (`site.css`)

Contains all CSS variables, reset, base styles, and these component blocks:
- **Reading progress bar** — `#reading-progress`: fixed, top:0, 3px height, navy background, width transitions
- **Masthead** — sticky, backdrop-blur, 64px height, flex layout, mobile toggle
- **Hero** — border-bottom, large serif title with underline hover, meta badges, excerpt, CTA button
- **About strip** — 3-column grid (1-col on mobile), uppercase labels, descriptive text
- **Pillars key** — flex wrap, 8px coloured dots, pillar names
- **Archive** — filter bar (pill buttons), responsive issue grid
- **Issue cards** — white bg, border, rounded corners, hover effect (navy border + shadow), card-meta/title/excerpt/tags
- **Tags** — pill-shaped, coloured per pillar with light backgrounds and tinted borders
- **Footer** — surface background, 3-column grid, logo, motto, nav links, standards
- **About page styles** — hero section, body content, pillar list cards, standards list with em-dash bullets
- **Scrollbar styling** — thin, subtle, themed

### 5b. Article Stylesheet (`article.css`)

Contains:
- **Article header** — surface background, issue kicker, badges, h1, deck (serif italic), byline
- **Story blocks** — numbered circle badge (navy-light bg), serif h2, border-bottom header, paragraphs
- **Badges** — inline-flex pills, uppercase, coloured per pillar (supports both `.badge.gov` and `.badge-gov` class patterns)
- **Section breaks** — flex with before/after pseudo-element lines, centered uppercase label
- **Synthesis** — navy-light background, navy top border (3px), rounded bottom, generous padding
- **Bottom line** — white box inside synthesis, navy uppercase label, summary text
- **Story sources** — border-top separator, uppercase "Sources" label, links with ↗ arrow prefix
- **Issue navigation** — flex space-between, bordered pill buttons, disabled state at 60% opacity
- **Author bio** — bordered card, surface background, uppercase label, description text

### 5c. JavaScript (`js/main.js`)

Two progressive-enhancement features (site works fully without JS):

**Topic filter:**
```javascript
// Reads data-topic from .filter-btn clicks
// Shows/hides .issue-card elements based on data-topics attribute match
// "all" shows everything; specific topic checks .includes()
```

**Reading progress:**
```javascript
// Listens to scroll (passive)
// Calculates percentage: scrollY / (scrollHeight - innerHeight) * 100
// Sets width on #reading-progress element
```

---

## 6. HTML Templates

### 6a. Issue Template (`templates/issue-template.html`)

Each issue page follows this exact structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[ONE-SENTENCE DESCRIPTION]">
  <title>[ISSUE TITLE] — [PUBLICATION NAME]</title>
  <link rel="stylesheet" href="../site.css">
  <link rel="stylesheet" href="../article.css">
</head>
<body>
  <div id="reading-progress"></div>

  <!-- Masthead (sticky nav) -->
  <header class="masthead">
    <div class="masthead-inner">
      <a href="../index.html" class="masthead-brand">
        <span class="masthead-name">[PUBLICATION NAME]</span>
        <span class="masthead-tagline">[TAGLINE]</span>
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

  <!-- Article Header -->
  <div class="article-header">
    <div class="article-header-inner">
      <p class="issue-kicker">Issue #[N] · [Day], [Full Date]</p>
      <div class="article-header-badges">
        <span class="badge badge-[pillar]">[Pillar Name]</span>
        <span class="badge badge-[pillar]">[Pillar Name]</span>
      </div>
      <h1>[ISSUE TITLE]</h1>
      <p class="article-deck">[ONE-LINE FRAME — what connects the developments]</p>
      <p class="article-byline">[PUBLICATION NAME] · [Day], [Full Date]</p>
    </div>
  </div>

  <!-- Article Body -->
  <div class="article-body">

    <!-- Framing paragraph: 2-3 sentences connecting the week's developments -->
    <p>[FRAMING PARAGRAPH]</p>

    <div class="section-break"><span>this week</span></div>

    <!-- Repeat for each development (3-4 total) -->
    <article class="story">
      <div class="story-header">
        <span class="story-num">[1-4]</span>
        <h2>[DEVELOPMENT HEADLINE]</h2>
      </div>
      <span class="badge badge-[pillar]">[Pillar Name]</span>

      <p>[What happened — the news, stated precisely]</p>
      <p>[Why it matters — mechanism, evidence, context]</p>
      <!-- Optional: complicating factor or counter-evidence -->

      <div class="story-sources">
        <p class="src-label">Sources</p>
        <ul>
          <li><a href="[URL]">[Publication], "[Title]"</a></li>
        </ul>
      </div>
    </article>

    <div class="section-break"><span>• • •</span></div>
    <!-- ... more developments with • • • breaks between them ... -->

    <div class="section-break"><span>what it means</span></div>

    <!-- Synthesis — the centrepiece -->
    <section class="synthesis">
      <h2>What It All Means</h2>
      <p class="syn-byline">[PUBLICATION NAME] · Issue #[N], [Full Date]</p>

      <p>[SYNTHESIS PARAGRAPH 1: The coherent signal across developments]</p>
      <p>[SYNTHESIS PARAGRAPH 2: Develop a major thread — connect, don't restate]</p>
      <p>[SYNTHESIS PARAGRAPH 3: Tension or second thread between developments]</p>
      <p>[SYNTHESIS PARAGRAPH 4: Second-order implication — what follows from reading together?]</p>
      <p>[SYNTHESIS PARAGRAPH 5 (optional): Additional depth or complicating factor]</p>

      <div class="bottom-line">
        <strong>Bottom line</strong>
        <p>[2-3 sentences. The single most important takeaway. Specific to this week.]</p>
      </div>
    </section>

    <!-- Issue Navigation -->
    <nav class="issue-nav">
      <!-- First issue: <span class="nav-disabled">← First issue</span> -->
      <a href="[PREV-DATE].html" class="nav-prev">Issue #[N-1] — [Mon Day]</a>
      <a href="../index.html" class="nav-home">Home</a>
      <!-- Latest issue: <span class="nav-disabled">No newer issue →</span> -->
      <a href="[NEXT-DATE].html" class="nav-next">Issue #[N+1] — [Mon Day]</a>
    </nav>

    <!-- Author Bio -->
    <div class="author-bio">
      <span class="bio-label">About this publication</span>
      <p>[PUBLICATION NAME] publishes every [DAY]. The week's signal developments, then what they mean together. No advertising. <a href="../about.html">About our editorial standards →</a></p>
    </div>

  </div>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="footer-logo">[PUBLICATION NAME]</div>
        <p class="footer-motto">[TAGLINE + SCHEDULE]. Published every [DAY].</p>
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
      <span>© [YEAR] [PUBLICATION NAME]</span>
      <span><a href="../about.html">About</a></span>
    </div>
  </footer>
  <script src="../js/main.js"></script>
</body>
</html>
```

### 6b. Homepage Card Template (`templates/homepage-card.html`)

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

## 7. Publishing Workflow (`workflow/WORKFLOW.md`)

Create this file with the complete editorial workflow. Here is the specification:

### Issue Format

Each issue has two parts, weighted deliberately:

**Part 1 — This Week's Developments** (3-4 items)
- Each development is anchored by a *distinct* primary source
- If the same paper, report, or event is the source for more than one item, those items belong together as one development
- Each development: 2-3 paragraphs of tight analysis + source links
- No pull quotes, no "shareable" boxes, no individual "why it matters" callouts — that's what the synthesis is for

**Part 2 — What It All Means** (~600-800 words)
- This is the centrepiece, not the postscript
- Reads the developments together, identifies what they mean in combination
- Gives readers something they could not get from reading the individual stories alone
- Earns its length

### Research Process

**Goal:** Find 3-5 genuinely distinct developments from the past 7 days — each anchored by a different primary source.

**The one-source-per-development rule:** Before selecting a development, ask: what is the single primary source for this item? If two candidate stories trace back to the same paper, report, or announcement, they are one development. Merge them.

**Distinct = different domain, different publication, different event.**

### Source Credibility Tiers

| Tier | Examples | How to Use |
|------|----------|------------|
| **Tier 1** | Peer-reviewed research, major analyst firms, major journalism (WSJ, FT, HBR, NYT, Reuters, Guardian) | Use freely. Cite specifically. |
| **Tier 2** | Specialist trade press, think tanks (CFR, Brookings, Chatham House), company research labs | Use with clear attribution. |
| **Tier 3** | Vendor surveys, smaller blogs, opinion pieces | Flag clearly. Use only when corroborated. |

### Triple-Verification Requirement

Every cited source must pass three checks:
1. **Existence** — the URL resolves and the article is real
2. **Content** — the article says what is attributed to it
3. **Currency** — the publication date is within the claimed period

### Writing Standards

- **Voice:** Calm urgency. Collaborative "we" in synthesis. No hype words without direct evidentiary support.
- **Audience test:** Would a thoughtful, skeptical professional who has seen many hype cycles roll their eyes? If yes, remove the hype and add evidence.
- **Development length:** 2-3 tight paragraphs + sources. No padding.
- **Synthesis length:** 4-6 paragraphs (~600-800 words) + bottom line.
- **Synthesis quality test:** Does the synthesis say something that none of the individual developments say? Does it identify a pattern or tension only visible when the developments are read together? If not, it's a summary, not a synthesis. Revise.

### Pre-Publish Checklist

**Sourcing:**
- [ ] Each development traces to a distinct primary source
- [ ] No single source cited as the basis for more than one development
- [ ] All URLs resolve and content matches attribution
- [ ] All sources are Tier 1 or Tier 2

**Content:**
- [ ] Framing paragraph connects all developments without over-explaining
- [ ] Synthesis addresses developments in combination, not in sequence
- [ ] Bottom line is specific, not generic
- [ ] No hype language without evidence

**Technical:**
- [ ] HTML structure matches the issue template
- [ ] Both stylesheets linked (`../site.css`, `../article.css`)
- [ ] `<script src="../js/main.js"></script>` before `</body>`
- [ ] Meta description tag present
- [ ] Issue nav links correct (prev, home, next or nav-disabled)

### Homepage Update Process

When publishing a new issue:
1. **Update the featured issue** (hero section) — point to new issue, update title and excerpt
2. **Add a new issue card** to `.issue-grid` — at the top, before existing cards
3. **Update the previous issue's nav** — add `nav-next` link pointing to the new issue
4. **Update masthead** "Latest Issue" link across all pages

### Archive Management

Issues are stored permanently in `issues/` — never deleted, only corrected with a visible correction notice. Filename = publication date: `YYYY-MM-DD.html`.

---

## 8. Analytical Framework

This is the intellectual engine of the publication. Embed these principles throughout the workflow and about page:

### The Skeptic-First Lens

- **Institutional & systemic focus:** Not just "what happened" but "what does this mean for how institutions function, how decisions get made, and what the second-order effects are likely to be"
- **Evidence-first standard:** When evidence is thin, contested, or absent, say so explicitly — do not fill gaps with confident-sounding speculation
- **Failure modes before success stories:** Earn trust by naming what doesn't work before celebrating what does
- **Complexity as feature:** Nuance and uncertainty are treated as analytical strengths, not obstacles to be smoothed over
- **Combination over sequence:** The synthesis identifies patterns visible only when developments are read together — if it just restates the developments in order, it's a summary, not a synthesis

### What Makes Good Synthesis

The synthesis quality test: "Does this say something that none of the individual developments say?" If the synthesis could be written having read only one of the developments, it has failed. Good synthesis:

- Names the coherent signal across developments
- Identifies tension or contradiction between them
- Surfaces second-order implications
- Connects to institutional or structural dynamics
- Gives readers an analytical frame they cannot get elsewhere

---

## 9. Deployment Configuration

### Vercel (`vercel.json`)

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

## 10. Initial Build Instructions

When scaffolding the project:

1. **Create all files** in the structure defined in Section 4
2. **Write the complete CSS** for both `site.css` and `article.css` using the design system in Section 3 and component specs in Section 5
3. **Write `main.js`** with the two progressive-enhancement features
4. **Build `index.html`** with all sections (masthead, hero, about strip, pillars key, archive) — use placeholder content for the first issue
5. **Build `about.html`** with editorial standards, pillar descriptions, and analytical lens — adapted to the chosen topic
6. **Create both templates** in `templates/`
7. **Write the complete `workflow/WORKFLOW.md`** with all editorial standards, search strategy templates (adapted to the topic), checklists, and the one-source-per-development rule
8. **Create `vercel.json`** for deployment
9. **Draft Issue #1** as a scene-setting edition that establishes the publication's analytical identity

The site must work with zero build steps — just HTML, CSS, and JS served statically. Progressive enhancement means the site is fully functional without JavaScript.

---

## 11. Summary of the Pattern

This is a **weekly editorial briefing** that follows a disciplined structure:

```
┌────────────────────────────────────────┐
│  3-4 distinct developments             │
│  (one primary source each)             │
│  (2-3 paragraphs + citations each)     │
├────────────────────────────────────────┤
│  "What It All Means" synthesis         │
│  (600-800 words)                       │
│  (the centrepiece — reads them         │
│   together, finds what none say alone) │
├────────────────────────────────────────┤
│  Bottom line                           │
│  (2-3 sentences, specific to the week) │
└────────────────────────────────────────┘
```

The value proposition is: **developments in isolation are misleading. The synthesis is where the genuine analytical work happens.** Every design, structural, and editorial decision serves this principle.

---

<!-- ═══════════════════════════════════════════════════════════════ -->
# END OF PROMPT
<!-- ═══════════════════════════════════════════════════════════════ -->
