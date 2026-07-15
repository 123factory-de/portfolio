---
title: "fix: space company meeting button and ToC"
date: 2026-07-15
branch: fix/space-company-toc
request-source: "chat, 2026-07-15"
---

## Request

Add visual separation between the meeting-request button and the table of contents on company profile pages, where the two elements appeared attached on narrow screens.

## Changes

- Added a consistent top margin to the company profile body section.
- Scoped the spacing change to company detail pages so the shared meeting-request component and other page types remain unchanged.

## Verification

- `hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio` completed successfully with Hugo 0.153.3 extended.
- Confirmed generated English and Korean company detail pages include the `mt-6` body spacing class.
- `git diff --check` completed without whitespace errors.
- `gitleaks dir --no-banner --redact layouts/companies/single.html docs/worklog/2026-07-15-space-company-toc.md` completed with no leaks found.
