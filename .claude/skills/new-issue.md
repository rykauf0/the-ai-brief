# Skill: New Issue

Research, draft, and validate a new weekly issue of 3rd Take.

## When to Use

Invoke with `/new-issue` on publication day (Sunday) or when preparing the next issue.

## Instructions

You are the editorial engine for 3rd Take, a weekly AI newsletter. Your job is to research the week's most significant AI developments, verify every source, draft a complete issue, and validate it — then stop for the editor's review before publishing.

### Step 1 — Determine Issue Metadata

1. Read `index.html` to find the latest issue number and date.
2. Calculate the next issue:
   - **Issue number:** latest + 1
   - **Issue date:** the upcoming Sunday (or today if it's Sunday). Format: `YYYY-MM-DD`
   - **Citation window:** issue date minus 7 days through issue date plus 7 days
3. Confirm these details with the user before proceeding.

### Step 2 — Research the Week

Search for 3-5 genuinely distinct AI developments from the past 7 days. Use these search patterns:

```
AI news [current week] major developments
AI governance policy [current month] [year]
AI workforce jobs [current week]
AI energy data centres [current month]
AI regulation [current week]
AI research breakthrough [current week]
AI safety [current week]
```

**Rules:**
- Each development must be anchored by a **different** primary source
- If two stories trace to the same paper/report/announcement, they are ONE development — merge them
- Only use **Tier 1** and **Tier 2** sources (see CLAUDE.md for tiers)
- Never use Tier 3 sources (Yahoo, Business Insider aggregations, vendor surveys, SEO blogs, etc.)
- Aim for coverage across at least 3 of the 4 pillars: Governance, Work, Economy, Environment
- Seek balance: genuine progress AND genuine problems. If all candidates are good news or all bad, keep researching.

### Step 3 — Verify Every Source (Citations Verification Gate)

For each candidate source, run these checks:

1. **Tier check** — Is the publication Tier 1 or Tier 2? Reject Tier 3.
2. **Link verification** — Use WebFetch to confirm the URL resolves to a real page (not 404/403/paywall-only).
3. **Content match** — Confirm the article says what you're attributing to it.
4. **Currency check** — Confirm the publication date falls within the +/-7 day citation window.
5. **Independence check** — Is the source independent from its subject?

**Cross-source checks:**
- No two developments share the same primary source
- No single publication appears more than twice in the entire issue
- At least 50% of sources are Tier 1

Present a verification report to the user:

```
Source verification complete:

  Development 1: [headline]
    [ok] [Source 1] — Tier [X], verified, [date]
    [ok] [Source 2] — Tier [X], verified, [date]

  Development 2: [headline]
    [ok] [Source 1] — Tier [X], verified, [date]
    [!!] [Source 2] — [issue found]

  Summary: [N] sources verified, [N] flagged, [N] rejected
  Tier breakdown: [N] Tier 1, [N] Tier 2

Proceed to drafting? (yes / flag concerns)
```

**Wait for user approval before proceeding to Step 4.**

### Step 4 — Draft the Issue

1. Read `issues/2026-03-08.html` (the canonical Issue #10) to match structure exactly.
2. Read `templates/issue-template.html` for the blank template.
3. Create `issues/[YYYY-MM-DD].html` following the exact HTML structure from Issue #10.

**Writing standards:**
- **Voice:** Calm urgency. Collaborative "we" in synthesis. No hype without evidence.
- **Developments:** 2-3 tight paragraphs each + editorial note + sources
- **Synthesis:** 4-6 paragraphs (~600-800 words) with three sections:
  - **What's Working** — genuine progress backed by evidence
  - **What's Not** — failures, overpromises, gaps
  - **What Nobody's Saying** — uncomfortable truths, perverse incentives
- **Bottom line:** 2-3 sentences, specific to this week
- **Audience test:** Would a thoughtful, skeptical professional roll their eyes? If yes, cut the hype.

**HTML requirements:**
- Both stylesheets linked (`../site.css?v=2`, `../article.css?v=2`)
- `<script src="../js/main.js"></script>` before `</body>`
- Meta description tag present
- Masthead "Latest Issue" link points to this new issue's date
- Issue nav: `nav-prev` links to previous issue, `nav-disabled` for "No newer issue"
- Background citations (if any, max 0-2) tagged with `data-type="background"` on the `<li>`

### Step 5 — Validate Citations

Run the citation date validator:

```bash
python3 workflow/validate-citations.py issues/[YYYY-MM-DD].html
```

The validator **must pass with 0 failures**. If it fails:
1. Identify which citations are outside the window
2. Either find replacement sources within the window, or tag as `data-type="background"` if they are genuinely foundational (max 0-2)
3. Re-run the validator until it passes

### Step 6 — Present for Review

Tell the user:

```
Issue #[N] draft is ready for your review.

File: issues/[YYYY-MM-DD].html
Title: [title]
Developments: [count]
Sources: [count] verified ([N] Tier 1, [N] Tier 2)
Citation validator: PASSED

Please review the draft. When you're happy with it, run /publish to update
the homepage, commit, and push.
```

**STOP HERE.** Do not update the homepage, commit, or push. The user reviews first.
