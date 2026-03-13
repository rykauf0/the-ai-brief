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

5. What is the publication's motto or editorial identity — one line?
   (e.g. "Consequences, not announcements." / "Signal over noise." / "Evidence over enthusiasm.")
```

Wait for answers. Then proceed to Step 2.

### Step 2 — Topic Pillars

Ask the user to define their four content pillars. Present it like this:

```
Every issue is tagged with topic pillars — exactly four categories that cover the landscape of your subject.

For each pillar, I need:
- A short code (3-4 letters, lowercase — used in CSS and HTML)
- A display name (what readers see)
- A one-sentence scope (what falls under this pillar)

Here's an example for an AI publication:
  1. gov  — Governance & Policy — Regulation, government adoption, institutional accountability
  2. work — Work & Organizations — How AI reshapes organizations, what gets automated
  3. econ — Economy & Society — Productivity, labour markets, inequality, transition costs
  4. env  — Environment & Planet — Energy footprint, data centre growth, climate trade-offs

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
- **About strip** — 3-column value proposition (Format / Standards / Perspective)
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

    <!-- DEVELOPMENT 1 (repeat pattern for 3-4 developments) -->
    <article class="story">
      <div class="story-header">
        <span class="story-num">1</span>
        <h2>[DEVELOPMENT HEADLINE]</h2>
      </div>
      <span class="badge badge-[pillar]">[Pillar Name]</span>
      <p>[What happened — stated precisely]</p>
      <p>[Why it matters — mechanism, evidence, context]</p>
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
      <p>[SYNTHESIS — 4-6 paragraphs, 600-800 words]</p>
      <div class="bottom-line">
        <strong>Bottom line</strong>
        <p>[2-3 sentences — the single most important takeaway, specific to this week]</p>
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

**Part 1 — This Week's Developments** (3-4 items)
- Each anchored by a *distinct* primary source
- Same source = same development — merge them
- 2-3 paragraphs of tight analysis + source links per development
- No pull quotes, no "shareable" boxes, no "why it matters" callouts — that's what synthesis is for

**Part 2 — What It All Means** (~600-800 words)
- The centrepiece, not the postscript
- Reads developments together, identifies what they mean in combination
- Gives readers something they cannot get from individual stories alone

#### Research Process

- Goal: 3-5 genuinely distinct developments from the past 7 days
- One-source-per-development rule: if two stories trace to the same paper/report/event, they are one development
- Distinct = different domain, different publication, different event
- Include topic-specific search strategy templates adapted to the user's subject area

#### Source Credibility Tiers

| Tier | Examples | Usage |
|------|----------|-------|
| **Tier 1** | Peer-reviewed research, major analyst firms, major journalism (WSJ, FT, HBR, NYT, Reuters, Guardian) | Use freely, cite specifically |
| **Tier 2** | Specialist trade press, think tanks, company research labs | Use with clear attribution |
| **Tier 3** | Vendor surveys, smaller blogs, opinion pieces | Flag clearly, use only when corroborated |

#### Triple-Verification Requirement

Every source must pass:
1. **Existence** — URL resolves, article is real
2. **Content** — article says what is attributed
3. **Currency** — publication date within claimed period

#### Writing Standards

- **Voice:** Calm urgency. Collaborative "we" in synthesis. No hype without evidence.
- **Audience test:** Would a thoughtful skeptic roll their eyes? If yes, cut the hype, add evidence.
- **Development length:** 2-3 tight paragraphs + sources
- **Synthesis length:** 4-6 paragraphs (~600-800 words) + bottom line
- **Synthesis quality test:** Does it say something none of the individual developments say? If not, it's a summary — revise.

#### Pre-Publish Checklist

**Sourcing:**
- [ ] Each development traces to a distinct primary source
- [ ] No single source for multiple developments
- [ ] All URLs resolve, content matches attribution
- [ ] All sources Tier 1 or 2

**Content:**
- [ ] Framing connects without over-explaining
- [ ] Synthesis addresses combinations, not sequences
- [ ] Bottom line is specific, not generic
- [ ] No hype language without evidence

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

#### The Skeptic-First Lens

- **Institutional & systemic focus:** Not "what happened" but "what does this mean for how institutions function, decisions get made, and what are the second-order effects"
- **Evidence-first:** When evidence is thin/contested/absent, say so — don't fill gaps with confident speculation
- **Failure modes before success stories:** Earn trust by naming what doesn't work before celebrating what does
- **Complexity as feature:** Nuance and uncertainty are analytical strengths, not obstacles
- **Combination over sequence:** Synthesis finds patterns visible only when developments are read together

#### What Makes Good Synthesis

Quality test: "Does this say something none of the individual developments say?"

Good synthesis:
- Names the coherent signal across developments
- Identifies tension or contradiction between them
- Surfaces second-order implications
- Connects to institutional or structural dynamics
- Gives readers an analytical frame they cannot get elsewhere

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
10. Draft Issue #1 — a scene-setting edition that establishes the publication's analytical identity for the chosen topic

The site must work with zero build steps. Progressive enhancement: fully functional without JavaScript.

---

### 2.9 The Pattern

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

**The value proposition:** Developments in isolation are misleading. The synthesis is where the genuine analytical work happens. Every design, structural, and editorial decision serves this principle.
