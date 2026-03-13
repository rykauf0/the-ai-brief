# The AI Brief — Weekly Publishing Workflow

**Publication:** The AI Brief
**Cadence:** Every Sunday
**Audience:** Informed, skeptical readers — people who follow serious news, want to understand AI's real consequences, and have seen enough hype cycles to be deeply wary of them.
**Format:** 3–4 distinct headline developments (one primary source each) + a substantial analytical synthesis

---

## The Format

Each issue has two parts, weighted deliberately:

**Part 1 — This Week's Developments** (3–4 items)
Each development is anchored by a *distinct* primary source. If the same paper, report, or event is the source for more than one item, those items belong together as one development. The goal is genuine breadth — not artificial fragmentation of a single story into multiple entries.

Each development: 2–3 paragraphs of tight analysis + source links. No pull quotes, no "shareable" boxes, no individual "why it matters" callouts — that's what the synthesis is for.

**Part 2 — What It All Means** (~600–800 words)
This is the centrepiece of the publication, not the postscript. The synthesis reads the week's developments together, identifies what they mean in combination, and gives readers something they could not get from reading the individual stories alone. It earns its length.

**Why this structure?**
The old five-story format created a sourcing problem: when one big study dominates a week, it gets cited three times across three "stories" that are really three angles on one source. The new format treats one source as one development, and moves the multi-angle analysis into the synthesis where it belongs.

---

## The Four Topic Pillars

1. **Governance & Policy** (`badge-gov`) — AI regulation, government adoption, institutional accountability
2. **Work & Organizations** (`badge-work`) — how AI reshapes how organizations function, what gets automated
3. **Economy & Society** (`badge-econ`) — productivity, labour markets, inequality, who bears the cost of the transition
4. **Environment & Planet** (`badge-env`) — energy and water footprint, data centre growth, climate trade-offs

---

## Step 1: Load the Skill

```
Load skill: research-assistant
```

This governs source credibility tiers, search strategy, and the skeptic-first evidence standard.

---

## Step 2: Research the Week (research-assistant)

**Goal:** Find 3–5 genuinely distinct AI developments from the past 7 days — each anchored by a different primary source.

### Search Strategy

```
AI news [current week] major developments
AI governance policy [current month] [year]
AI workforce jobs [current week]
AI energy data centres [current month]
AI regulation [current week]
```

**The one-source-per-development rule:** Before selecting a development, ask: *what is the single primary source for this item?* If two candidate stories both trace back to the same paper, report, or announcement, they are one development. Merge them.

**Distinct = different domain, different publication, different event.** A government announcement, a peer-reviewed study, an independent poll, and an industry earnings report are four distinct sources. Four angles on the same earnings report are not.

### Source Credibility Tiers

| Tier | Examples | How to Use |
|------|----------|------------|
| **Tier 1** | Peer-reviewed research, major analyst firms, major journalism (WSJ, FT, HBR, NYT, Reuters, Guardian) | Use freely. Cite specifically. |
| **Tier 2** | MIT Tech Review, think tanks (CFR, Brookings, Chatham House), company research labs, reputable trade press | Use with clear attribution. |
| **Tier 3** | Vendor surveys, smaller blogs, opinion pieces | Flag clearly. Use only when corroborated. |

### Triple-Verification Requirement

Every cited source must pass three checks:
1. **Existence** — the URL resolves and the article is real
2. **Content** — the article says what is attributed to it
3. **Currency** — the publication date is within ±7 days of the issue date

### Citation Date Rule

**Core citations** must be published within ±7 days of the issue's Sunday date. This is the fundamental constraint for a weekly lookback — every source should be from that week.

**Background citations** are the sole exception: foundational research papers, landmark policy documents, or reference material that provides essential context for a development but was not published that week. These must be tagged with `data-type="background"` on the `<li>` element:

```html
<li data-type="background"><a href="[URL]">[Publication], "[Title]"</a></li>
```

Background citations should be rare (0–2 per issue). If you're tagging more than 2 sources as background, the development may not belong in this week's issue.

### Automated Validation

Run the citation date validator before publishing:

```bash
python3 workflow/validate-citations.py                    # all issues
python3 workflow/validate-citations.py issues/YYYY-MM-DD.html  # one issue
```

The validator checks all URL-embedded dates against the ±7 day window and flags violations. Background-tagged citations are reported but not counted as failures.

---

## Step 3: Draft the Issue

### File naming
- File: `issues/YYYY-MM-DD.html` (Sunday's date)
- Issue number: Sequential from Issue #1
- Title: A frame for the week, not a news headline

### HTML template

The canonical template is **Issue #10** (`issues/2026-03-08.html`). Read that file before drafting. Key structural elements:

```html
<div class="article-body">

  <!-- Framing paragraph: 2-3 sentences connecting the week's developments -->
  <p>[Framing intro]</p>

  <div class="section-break"><span>this week</span></div>

  <!-- Repeat for each development (3-4 total) -->
  <article class="story">
    <div class="story-header">
      <span class="story-num">[1-4]</span>
      <h2>[Development headline]</h2>
    </div>
    <span class="badge badge-[pillar]">[Pillar name]</span>

    <p>[Paragraph 1: What happened — the news, stated precisely]</p>
    <p>[Paragraph 2: Why it matters — mechanism, evidence, context]</p>
    <p>[Optional Paragraph 3: Second-order implication or complicating factor]</p>

    <div class="story-sources">
      <p class="src-label">Sources</p>
      <ul>
        <li><a href="[URL]">[Publication], "[Title]"</a></li>
      </ul>
    </div>
  </article>

  <div class="section-break"><span>• • •</span></div>

  <div class="section-break"><span>what it means</span></div>

  <section class="synthesis">
    <h2>What It All Means</h2>
    <p class="syn-byline">The AI Brief · Issue #[N], [Date]</p>
    <!-- 4-6 substantive paragraphs connecting the week's developments -->
    <div class="bottom-line">
      <strong>Bottom line</strong>
      <p>[The single most important takeaway — 2-3 sentences]</p>
    </div>
  </section>

  <nav class="issue-nav">
    <a href="[PREV].html" class="nav-prev">Issue #[N-1] — [Month Day]</a>
    <a href="../index.html" class="nav-home">Home</a>
    <!-- Latest issue: <span class="nav-disabled">No newer issue →</span> -->
    <!-- Otherwise: <a href="[NEXT].html" class="nav-next">Issue #[N+1] — [Month Day]</a> -->
  </nav>

  <div class="author-bio">
    <span class="bio-label">About this publication</span>
    <p>The AI Brief publishes every Sunday. The week's signal developments, then what they mean together. No advertising. <a href="../about.html">About our editorial standards →</a></p>
  </div>

</div>
```

### Writing standards

**Voice:** Calm urgency. Collaborative "we" in synthesis. No hype words without direct evidentiary support.

**Audience test:** Would a thoughtful, skeptical professional who has seen many hype cycles roll their eyes? If yes, remove the hype and add evidence.

**Development length:** 2–3 tight paragraphs + sources. No padding.

**Synthesis length:** 4–6 paragraphs (~600–800 words) + bottom line.

**Synthesis quality test:** Does the synthesis say something that none of the individual developments say? Does it identify a pattern or tension only visible when the developments are read together? If not, it's a summary, not a synthesis. Revise.

---

## Step 4: Pre-Publish Review

**Sourcing**
- [ ] Each development traces to a distinct primary source
- [ ] No single source cited as the basis for more than one development
- [ ] All URLs resolve and content matches attribution
- [ ] All sources are Tier 1 or Tier 2
- [ ] `python3 workflow/validate-citations.py issues/YYYY-MM-DD.html` passes with 0 failures
- [ ] All citations published within ±7 days of the issue date (background sources tagged)

**Content**
- [ ] Framing paragraph connects all developments without over-explaining
- [ ] Synthesis addresses developments in combination, not in sequence
- [ ] Bottom line is specific, not generic
- [ ] No hype language without evidence

**Technical**
- [ ] HTML structure matches the Issue #10 template
- [ ] Both stylesheets linked (`../site.css`, `../article.css`)
- [ ] `<script src="../js/main.js"></script>` before `</body>`
- [ ] Meta description tag present
- [ ] Issue nav links correct (prev, home, next or nav-disabled)

---

## Step 5: Update the Homepage

1. **Update the featured issue** (`<section class="hero">`) — point to new issue, update title and excerpt
2. **Add a new issue card** to `.issue-grid` — at the top, before existing cards
3. **Update the previous issue's nav** — add `nav-next` link pointing to the new issue

Issue card template:
```html
<a class="issue-card" href="issues/YYYY-MM-DD.html" data-topics="[topics]">
  <div class="card-meta">
    <span class="card-date">[Month Day, Year]</span>
    <span class="card-num">No. [N]</span>
  </div>
  <p class="card-title">[ISSUE TITLE]</p>
  <p class="card-excerpt">[One specific sentence — what the reader will learn]</p>
  <div class="card-tags">
    <span class="tag [pillar]">[PILLAR]</span>
  </div>
</a>
```

---

## Archive Management

Issues are stored permanently in `issues/` — never deleted, only corrected with a visible correction notice. Filename = publication date: `YYYY-MM-DD.html`.

---

*The AI Brief exists to reduce noise to signal. The readers are experienced and skeptical. One source = one development. The analytical work belongs in the synthesis.*
