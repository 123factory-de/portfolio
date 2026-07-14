---
name: add-program-content
description: Add or update a Hugo program page for this portfolio, including English and Korean content, program-page assets, and validation for company-linked program hubs.
---

# Add Program Content

Use this skill when adding or updating a page under `content/programs/{slug}/`.

This skill is for accelerator, PoC, testbed, challenge, and portfolio program pages. It is not for company profiles.

## What A Program Page Is

In this repo, a program page is a short hub page.

It should do two things:
- briefly explain the program
- lead into the linked company list

The company list is rendered automatically from company pages that use:

```yaml
programs: ["{slug}"]
```

Do not manually maintain a long participant list in the markdown body unless the user explicitly asks for it.

Relevant templates:
- `layouts/programs/single.html`
- `layouts/partials/company-filter-list.html`

## File Structure

Each program should use a page bundle:

```text
content/programs/{slug}/
  index.md
  index.ko.md
  optional-source-assets
```

Keep `{slug}` stable. Company pages depend on it.

## Front Matter

Both language files should at minimum use:

```yaml
---
title: "Program Name"
description: "One-sentence summary for cards and metadata."
---
```

Rules:
- Keep the same slug across languages.
- Localize `title` and `description` naturally.
- Keep `description` short and plain. One sentence is enough.
- Write `description` for metadata, cards, and search results. It does not need to repeat the page body.
- Keep `description` even if the template does not show it on the page.
- Only add extra fields when the page needs them, such as `showBreadcrumbs: false`.

## Writing Style

Keep the writing short and direct.

Default structure:

English:

```markdown
## Program Overview

## Participating Companies
```

Korean:

```markdown
## 프로그램 소개

## 참여 기업
```

Rules:
- Two sections are usually enough.
- Keep each section short. One or two paragraphs is usually enough.
- Do not write long explanations about what the page is. Readers already know they are on a program page.
- Avoid phrases like "This page is..." unless they are necessary.
- Do not repeat the `description` in the opening paragraph.
- Do not sound like a public call for applications if the cohort is already selected.
- Use concrete facts only: operator role, support scope, target sectors, period, and what readers can review here.
- Do not invent dates, counts, partner roles, or benefits.

When the page is for an already selected cohort:
- write it like a company directory or hub
- keep recruitment poster details brief
- move quickly to the participating companies section

## Workflow

0. Create a branch from the latest `main` before touching any file (e.g.
   `feat/add-program-{slug}`). Do not ask for permission to branch, and never work
   directly on `main`.
1. Read the source material.
2. Confirm the slug.
3. Check linked companies:

```sh
rg -n 'programs: \["{slug}"\]' content/companies
```

4. Review the existing page, if there is one.
5. Write `index.md`.
6. Write `index.ko.md`.
7. Keep the body short and avoid repeating the title or obvious page context.
8. Build the site:

```sh
hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio
```

9. After validation, commit on the branch, then summarize the change and ask the user
   whether to create a Pull Request. Ask in plain, non-developer language as described
   in AGENTS.md ("Agent workflow for content tasks"): explain that the change is not
   on the live site yet and that a Pull Request is GitHub's review-and-approve page.
   Do not push or open a PR without the user's confirmation.

## Validation

Check for leftover recruitment or filler language:

```sh
rg -n "모집 마감|Apply now|지원하세요|This page is|이 페이지는|Key Signals|검토 포인트|Contact|Phone|Email" content/programs/{slug}
```

Use judgment:
- recruitment wording may stay if the page is intentionally archival
- remove filler when the page is meant to be a clean program hub

Confirm the program page resolves at:

```text
/programs/{slug}/
/ko/programs/{slug}/
```
