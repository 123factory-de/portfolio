---
title: "feat(content): add KOSME deeptech youth startup academy companies and remove inactive companies"
date: 2026-10-20
branch: feat/add-and-remove-portfolio-companies
request-source: "chat, 2026-10-20"
---

## Request

Add program overview and company profile pages for the eight Korean deep-tech startups participating in the 2026 KOSME Deep-Tech Youth Startup Academy Germany expansion program, and remove four inactive or withdrawn portfolio company entries.

## Changes

- Added program overview page for the 2026 Deep-Tech Youth Startup Academy Germany program (`content/programs/deeptech-youth-startup-academy-germany-2026/index.md`, `index.ko.md`) detailing the overseas expansion program in Düsseldorf (September 9–12, 2026) organized by KOSME (Korea SMEs and Startups Agency) and Openknowl, with 123 Factory as the German local partner.
- Added company profiles and brand assets in both English and Korean (`index.md`, `index.ko.md`) across standard profile sections for eight participating deep-tech companies:
  - `content/companies/bookend/`: BOOKEND (AI publishing tools, SENTENCIFY proofreading and "editorial" book editing; Information Technology / AI/ML / SaaS).
  - `content/companies/nanobridge/`: Nanobridge (Nano-carbon materials, CRYOLINK liquid coolant for data centers, and NVIA flame-retardant films; Materials and Resources / Nanotechnology / Advanced Manufacturing).
  - `content/companies/navoros/`: NAVOROS (Commercial drone safety infrastructure combining risk detection, physical crash mitigation, and incident recording; Robotics & Drones / AI/ML / Insurtech / IoT).
  - `content/companies/sig-corporation/`: SIG Corporation (SENIHUG contactless under-mattress sleep and vital signs monitoring sensor pad for senior care; Healthcare / Digital Health / IoT).
  - `content/companies/stephow/`: StepHow (Wissly enterprise knowledge and on-premises document AI; Information Technology / AI/ML / SaaS / Big Data).
  - `content/companies/syntherixs/`: Syntherixs (AI synthetic data generation for tabular, text, and visual datasets under privacy constraints; Information Technology / AI/ML / Cybersecurity).
  - `content/companies/textway/`: Textway (On-premises enterprise AI for long-form document search and source-backed question answering; Information Technology / AI/ML / Big Data / SaaS).
  - `content/companies/twell/`: TWELL (Standardized functional bioactive ingredients from Aster yomena / YomenaX for pet health, cosmetics, and functional foods; Materials and Resources / Healthcare / Life Sciences / Agtech).
- Removed four inactive portfolio company entries and associated assets:
  - `content/companies/heart-planet-company/`
  - `content/companies/heatai/`
  - `content/companies/lesaut/`
  - `content/companies/spoing/`

## Verification

- Hugo static site build verified cleanly via `hugo --gc --minify` (85 EN and 83 KO pages generated with 0 errors).
- Gitleaks secret/PII scan executed across repository files with 0 leaks detected.
- Verified bilingual frontmatter, taxonomy tags, and section alignments across all new English and Korean Markdown files.
