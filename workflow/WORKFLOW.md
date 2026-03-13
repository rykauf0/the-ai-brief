# The Climate Brief — Weekly Publishing Workflow

**Publication:** The Climate Brief
**Cadence:** Every Sunday
**Audience:** Informed, skeptical readers — people who follow climate and energy seriously, want to understand real-world consequences, and have seen enough greenwashing and alarmism to be deeply wary of both.
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
The old five-story format created a sourcing problem: when one big report dominates a week, it gets cited three times across three "stories" that are really three angles on one source. The new format treats one source as one development, and moves the multi-angle analysis into the synthesis where it belongs.

---

## The Five Topic Pillars

1. **Policy & Governance** (`badge-pol`) — Climate legislation, international agreements (UNFCCC/COP), carbon pricing, regulatory shifts, just transition frameworks
2. **Energy & Grid** (`badge-nrg`) — Renewables deployment, grid modernization, fossil fuel transitions, nuclear, battery storage, energy markets
3. **Science & Systems** (`badge-sci`) — Climate research, IPCC findings, tipping points, extreme weather attribution, carbon cycle dynamics, modeling
4. **Industry & Finance** (`badge-ind`) — Corporate emissions, green finance, carbon markets, supply chain decarbonization, adaptation tech, ESG
5. **Land & Agriculture** (`badge-land`) — Deforestation, soil carbon, food systems, land use change, agricultural emissions, biodiversity

---

## Deep Research Workflow

### Step 1: Systematic Source Monitoring

Monitor these source categories weekly. Each category contains Tier 1 and Tier 2 sources that form the backbone of credible climate reporting.

#### Tier 1 Sources — Use Freely, Cite Specifically

| Category | Sources |
|----------|---------|
| **Intergovernmental bodies** | IPCC, UNFCCC, IEA, IRENA, World Bank Climate, UNEP |
| **Peer-reviewed journals** | Nature, Nature Climate Change, Nature Energy, Science, Environmental Research Letters, The Lancet Planetary Health, Joule, Energy Policy |
| **Major journalism** | Financial Times (Climate Capital), Reuters (Sustainability), The Guardian (Environment), New York Times (Climate), Washington Post (Climate & Environment), The Economist |
| **Data & tracking** | Global Carbon Project, Climate Action Tracker, Our World in Data, Ember (electricity data), BloombergNEF |

#### Tier 2 Sources — Use with Clear Attribution

| Category | Sources |
|----------|---------|
| **Specialist climate media** | Carbon Brief, Climate Home News, E&E News, Canary Media, The Energy Mix, Grist |
| **Think tanks & research** | World Resources Institute, RMI (Rocky Mountain Institute), Climate Analytics, Carbon Tracker, Chatham House (Environment), Bruegel (Energy), IISD |
| **Industry research** | Wood Mackenzie, S&P Global Commodity Insights, Lazard LCOE reports, BNEF, McKinsey Sustainability |
| **Government agencies** | US EIA, US EPA, European Environment Agency, UK Climate Change Committee, China's NDRC |

#### Tier 3 Sources — Flag Clearly, Require Corroboration

| Category | Sources |
|----------|---------|
| **Industry-funded** | Trade association reports, corporate sustainability reports, industry-commissioned surveys |
| **Advocacy** | NGO campaign materials, activist research, opinion columns |
| **Emerging/unverified** | Preprints, conference presentations, social media claims |

### Step 2: Weekly Research Protocol

**Goal:** Find 3–5 genuinely distinct climate and energy developments from the past 7 days — each anchored by a different primary source.

#### Search Strategy

```
climate energy news [current week] major developments
climate policy legislation [current month] [year]
renewable energy deployment grid [current week]
carbon emissions research [current month]
climate finance ESG [current week]
deforestation land use agriculture emissions [current month]
IPCC climate science findings [current month]
energy transition [current week] [year]
```

#### Deep Research Checklist

For each candidate development, complete this verification process:

1. **Identify the primary source**
   - What is the original report, study, dataset, or official announcement?
   - Is it peer-reviewed? Government-issued? From a credible research institution?
   - Can you access the primary document, not just media coverage of it?

2. **Cross-reference with multiple outlets**
   - Is the development covered by at least 2 independent, credible outlets?
   - Do different outlets report consistent facts, or are there discrepancies?
   - If only one outlet covers it, is the source strong enough to stand alone (e.g., a Nature paper)?

3. **Check for context and counter-evidence**
   - What is the historical baseline? Is this genuinely new, or a continuation?
   - Are there credible dissenting views or methodological concerns?
   - Does the primary source acknowledge limitations?

4. **Verify data claims**
   - Can you trace specific numbers back to their origin dataset?
   - Are units, timeframes, and comparison periods clearly stated?
   - Has the data been adjusted, normalized, or cherry-picked?

5. **Assess significance**
   - Does this development change how institutions function or make decisions?
   - Does it reveal a pattern not visible from individual data points?
   - Would a skeptical professional find this worth knowing?

#### The One-Source-Per-Development Rule

Before selecting a development, ask: *what is the single primary source for this item?* If two candidate stories both trace back to the same paper, report, or announcement, they are one development. Merge them.

**Distinct = different domain, different publication, different event.** An IEA report, a Nature study, a government policy announcement, and a corporate filing are four distinct sources. Four angles on the same IPCC report are not.

### Step 3: Source Validation Protocol

#### Triple-Verification Requirement

Every cited source must pass three checks:

1. **Existence** — the URL resolves and the article/report is real
2. **Content** — the article says what is attributed to it (specific claims, numbers, quotes verified against original)
3. **Currency** — the publication date is within the claimed period

#### Climate-Specific Verification

Climate and energy reporting requires additional scrutiny:

| Check | What to verify |
|-------|---------------|
| **Units & baselines** | CO₂ vs CO₂-equivalent, GW vs GWh, absolute vs per-capita, what year is the baseline? |
| **Timeframes** | Is the claim about annual, cumulative, or peak values? 20-year vs 100-year GWP for methane? |
| **Attribution** | Does the study attribute outcomes to specific causes, or just correlate? |
| **Modeling vs observation** | Is this a projection, a model result, or observed data? Make the distinction explicit. |
| **Funding & conflicts** | Who funded the research? Does the source have commercial interests in the outcome? |
| **Geographic scope** | Global, national, or regional? Don't generalize regional findings to global conclusions. |

---

## Step 4: Draft the Issue

### File naming
- File: `issues/YYYY-MM-DD.html` (Sunday's date)
- Issue number: Sequential from Issue #1
- Title: A frame for the week, not a news headline

### HTML template

The canonical template is at `templates/issue-template.html`. Read that file before drafting. Key structural elements:

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
    <p class="syn-byline">The Climate Brief · Issue #[N], [Date]</p>
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
    <p>The Climate Brief publishes every Sunday. The week's signal developments in climate and energy, then what they mean together. No advertising. <a href="../about.html">About our editorial standards →</a></p>
  </div>

</div>
```

### Writing standards

**Voice:** Calm urgency. Collaborative "we" in synthesis. No hype words without direct evidentiary support. No doom without evidence. No optimism without caveats.

**Audience test:** Would a thoughtful, skeptical professional who has seen many greenwashing campaigns and climate doom cycles roll their eyes? If yes, remove the rhetoric and add evidence.

**Development length:** 2–3 tight paragraphs + sources. No padding.

**Synthesis length:** 4–6 paragraphs (~600–800 words) + bottom line.

**Synthesis quality test:** Does the synthesis say something that none of the individual developments say? Does it identify a pattern or tension only visible when the developments are read together? If not, it's a summary, not a synthesis. Revise.

---

## Step 5: Pre-Publish Review

**Sourcing**
- [ ] Each development traces to a distinct primary source
- [ ] No single source cited as the basis for more than one development
- [ ] All URLs resolve and content matches attribution
- [ ] All sources are Tier 1 or Tier 2
- [ ] Climate-specific verification checklist completed (units, baselines, timeframes)

**Content**
- [ ] Framing paragraph connects all developments without over-explaining
- [ ] Synthesis addresses developments in combination, not in sequence
- [ ] Bottom line is specific, not generic
- [ ] No hype language without evidence
- [ ] No doom language without evidence
- [ ] Modeling vs observation distinction clear where relevant

**Technical**
- [ ] HTML structure matches the issue template
- [ ] Both stylesheets linked (`../site.css`, `../article.css`)
- [ ] `<script src="../js/main.js"></script>` before `</body>`
- [ ] Meta description tag present
- [ ] Issue nav links correct (prev, home, next or nav-disabled)

---

## Step 6: Update the Homepage

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

*The Climate Brief exists to reduce noise to signal. The readers are experienced and skeptical. One source = one development. The analytical work belongs in the synthesis.*
