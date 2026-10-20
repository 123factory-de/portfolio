---
title: "feat(content): add Daedong Industrial, update profiles, and consolidate company list"
date: 2026-10-20
branch: fix/correct-company-info
request-source: "chat, 2026-10-20"
---

## Request

Add a company profile for Daedong Industrial, update technical and regulatory details for DaWinKS and MK Solar, and consolidate portfolio company browsing onto the homepage.

## Changes

- Added new company profile and logo for Daedong Industrial (`content/companies/daedong-industrial/index.md`, `index.ko.md`, `logo.png`):
  - Covered automotive interior plastic injection parts (core business) and BCS (Bio-based Carbon Storage) eco-friendly permeable sidewalk paving blocks.
  - Documented EPD environmental product declaration, patent KR 10-2996164, and European partner search.
- Updated DaWinKS profile (`content/companies/dawinks/index.md`, `index.ko.md`):
  - Corrected English website URL to `https://dawinks.com/en/index.html`.
  - Added patent portfolio details: 11 domestic patents and 9 overseas/PCT patent filings (US, Japan, Indonesia, Singapore, China, Thailand).
  - Clarified ICT Regulatory Sandbox approvals: crypto ATM/POS fast-track confirmation and AI facial-recognition remote real-name verification temporary permit.
- Updated MK Solar profile (`content/companies/mk-solar/index.md`, `index.ko.md`):
  - Added OLED display ytterbium (Yb) recycling technology and high-purity (3N5 / 99.987%) wet/dry hybrid refining process (patents KR 10-2652842, 10-2651225) verified by a global top-tier display manufacturer.
- Consolidated portfolio company browsing onto the homepage:
  - Updated `layouts/partials/recent-articles/cardview.html` to show all portfolio company entries sorted by title with filter counts enabled.
  - Updated `layouts/companies/list.html` to redirect visitors to the homepage while preserving URL search query parameters and anchor hashes.
  - Removed `/companies` entry from `config/_default/menus.en.toml` and `config/_default/menus.ko.toml`.
  - Disabled `showMoreLink` in `config/_default/params.toml` and pointed `$companiesURL` to `site.Home.RelPermalink` in `layouts/partials/company-facts.html`.

## Verification

- Hugo static site build verified cleanly via `hugo --gc --minify` (86 EN and 84 KO pages built without errors in 330 ms).
- Gitleaks secret/PII scan executed across repository files with 0 leaks detected.
- Verified bilingual frontmatter, taxonomy tags, and section alignments across all updated Markdown files.
