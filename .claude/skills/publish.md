# Skill: Publish Issue

Update the homepage, previous issue navigation, commit, and push a reviewed issue to main.

## When to Use

Invoke with `/publish` after you have reviewed the draft created by `/new-issue` and are satisfied with it.

## Instructions

You are publishing a reviewed issue of 3rd Take. The issue HTML file has already been drafted and validated. Your job is to update all supporting files, commit, and push.

### Step 1 — Identify the New Issue

1. Find the newest file in `issues/` by date to determine the issue being published.
2. Read that file to extract: issue number, title, date, pillar badges, and synthesis highlights.
3. Confirm with the user: "Publishing Issue #[N]: [title] ([date]). Correct?"

### Step 2 — Update the Previous Issue's Navigation

1. Identify the previous issue file (the second-newest in `issues/`).
2. In that file, replace the `nav-disabled` span for "No newer issue" with a `nav-next` link pointing to the new issue:

```html
<a href="[NEW-YYYY-MM-DD].html" class="nav-next">Issue #[N] — [Mon Day]</a>
```

### Step 3 — Update the Homepage (`index.html`)

Make these changes to `index.html`:

**A. Masthead "Latest Issue" link** — Update the `masthead-cta` href to the new issue date.

**B. Hero section** — Replace the entire hero content:
- `hero-label`: "Latest Edition — [Full Date]"
- `hero-title` link: points to new issue, text is the issue title
- `hero-meta`: date, issue number, pillar names
- `hero-excerpt`: 2-3 sentences summarizing what the reader will learn
- `hero-read` link: points to new issue
- `hero-lens` items: extract the key point from each synthesis section (What's Working / What's Not / What Nobody's Saying)

**C. Issue grid** — Add a new issue card at the TOP of `.issue-grid` (before the first existing card), using the format from `templates/homepage-card.html`:

```html
<a class="issue-card" href="issues/[YYYY-MM-DD].html" data-topics="[pillars]">
  <div class="card-meta">
    <span class="card-date">[Full Date]</span>
    <span class="card-num">No. [N]</span>
  </div>
  <p class="card-title">[Title]</p>
  <p class="card-excerpt">[One specific sentence]</p>
  <div class="card-tags">
    <span class="tag [pillar]">[Pillar]</span>
    ...
  </div>
</a>
```

**D. Footer "Latest Issue" link** — Update the footer nav link to the new issue.

### Step 4 — Update the New Issue's Masthead

In the new issue file, ensure the masthead `masthead-cta` link points to itself (it is now the latest issue).

### Step 5 — Run Final Validation

```bash
python3 workflow/validate-citations.py issues/[YYYY-MM-DD].html
```

Must pass with 0 failures. If it fails, stop and alert the user.

### Step 6 — Commit and Push

Stage and commit with a clear message:

```bash
git add issues/[YYYY-MM-DD].html issues/[PREV-YYYY-MM-DD].html index.html
git commit -m "Publish Issue #[N]: [Title]"
git push
```

### Step 7 — Confirm Publication

Tell the user:

```
Issue #[N] published successfully.

  File: issues/[YYYY-MM-DD].html
  Homepage: updated (hero, grid card, nav links)
  Previous issue: nav-next link added
  Commit: [hash]
  Push: complete — Vercel will auto-deploy

The issue should be live shortly.
```
