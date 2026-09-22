---
title: "feat: add Mercedes-Benz Korea delegation program"
date: 2026-09-21
branch: feat/add-program-mercedes-benz-korea-startup-delegation
request-source: "chat, 2026-09-21"
---

## Request

Add a program hub page for the Global Substantiation Challenge (Korean startups visiting Stuttgart with Mercedes-Benz Korea) and profiles for the 8 participating startups, in English and Korean. The request came with three source files: a participant list, a program description, and company descriptions that the program coordinator collected from the startups.

Three instructions shaped the content:

- Add `-2026` to the program slug only, not to the page title.
- For the 5 companies that sent their own descriptions, use their sentences as written and drop source links. Leave the other 3 companies as researched.
- Use the program coordinator's program description as written.

## Changes

- Added the program hub `content/programs/mercedes-benz-korea-startup-delegation-2026/` (`index.md`, `index.ko.md`). The English body is the program coordinator's text, used verbatim with its three sections (Program Overview, Networking Event, Participating Startups). This departs from the two-section default in `docs/skills/add-program-content/SKILL.md` on request. The source's top heading is used as the page title; heading bold markers, `&nbsp;` spacer lines, and the `\&` escape in "Y&Archer" were dropped or normalized. The Korean body is a translation of the same text. The Korean title keeps the English program name ("Global Substantiation Challenge") and translates only the subtitle, because no official Korean name was provided.
- Added 8 company bundles under `content/companies/`, each with `index.md`, `index.ko.md`, and an official logo, all tagged `programs: ["mercedes-benz-korea-startup-delegation-2026"]`:
  - `perseus`: multi-domain hypervisor for software-defined vehicles, ASIL-D certified.
  - `meta-mobility` (title MetaMobility): early detection of electrical anomalies in EV batteries with the ELI Solution.
  - `vsion` (title Viewzen): black PDLC switchable film for automotive roof glass.
  - `quantum-hitech` (title Quantum Hi-Tech): TRIZ-AI platform for EV battery health from real driving data.
  - `linetron`: AutoTest, AI-based test automation for vehicle and ECU software.
  - `vision-innovation`: retrofit nozzle that removes moisture and gas from resin in injection molding.
  - `smartride`: operations platform for taxi and commercial passenger fleets, extending to autonomous-vehicle operations.
  - `zephyros-electronic`: EMI filters, sensor and wireless modules, and edge computing boards for robotics.
- Content sources differ by company:
  - For the first 5 companies above, the English body is the company-supplied text, used verbatim in the five standard sections. The Korean body is a translation of that text. These pages carry no source links. Titles follow the company-supplied names. The `description` shown on company cards is the supplied Company Overview text (Korean: its translation), with bold markers removed because cards print the field as plain text.
  - For `vision-innovation`, `smartride`, and `zephyros-electronic`, no company text was supplied. Their pages are written from public sources (official sites and press), with source links in the Traction section, following `docs/skills/add-company-content/SKILL.md`. Their `description` is a one-sentence summary written for cards, not a copy of the Company Overview. Where public sources mention it, these pages also note the company's track in the Mercedes-Benz Korea startup program run with KISED (Konnectz or ASK).
  - Front matter facts for all 8 (website, founding year, CEO, headquarters, industries, verticals) come from public sources.
- The "item" column of the participant list is shifted between rows for several companies, so it was not used as a basis for any product description.
- Logos are official assets from each company's own site. Two companies only publish a white wordmark, so their official favicon or app icon is used instead.
- Website notes: Linetron uses `http://` because its HTTPS endpoint serves an invalid certificate. Quantum Hi-Tech uses its `.co.kr` site because the `.com` domain does not open.
- The slug was first created without the year and then renamed to `...-2026` on request. All 16 company files were updated to match.
- Added `temp/` to `.gitignore`. The source files contain attendee contact details and must not be committed.

## Verification

- `hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio` passed with Hugo extended v0.153.3 (80 EN pages, 78 KO pages, no errors or warnings).
- The built program page lists all 8 companies in both `/programs/mercedes-benz-korea-startup-delegation-2026/` and `/ko/programs/mercedes-benz-korea-startup-delegation-2026/`. Each company has EN and KO output, and its logo is published in the page bundle.
- A script check confirmed that every body paragraph of the company-supplied text appears unchanged in the 5 English pages, and that these 10 files contain no links. The same check passed for the program coordinator's text in the English program page.
- The built HTML of those 10 pages and both program pages contains no unrendered `**` markers. Two Korean bold spans that failed to render next to a particle were fixed.
- `gitleaks dir` with `.gitleaks.toml` reported no leaks for the 8 company directories, the program directory, and this worklog file (each path scanned separately). A grep for phone numbers, email addresses, and old section names in the new content returned nothing.
- For the 3 researched companies, all cited links returned HTTP 200 with a browser user agent. Some publishers return 403 or 410 to plain scripted requests, which is bot blocking and not a removed article.
- Re-checked on 2026-09-22 before commit: the production build, the gitleaks scan, the verbatim-text check against the source files, the 8-company link count on both program pages, and the `**` leftover check all passed again with the same results.
- Not done: the pages were not opened in the Hugo development server or a browser. Checks were made on the production build output.
