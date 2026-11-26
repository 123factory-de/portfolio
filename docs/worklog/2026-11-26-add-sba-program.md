---
title: "feat(content): add SBA global expansion PoC program"
date: 2026-11-26
branch: feat/add-sba-program
request-source: chat, 2026-11-26
---

## Request

Add a program page using the `add-program-content` skill for the 2026 Seoul Startup Hub (SBA) Global Expansion Program, based on the SBA partner-selection announcement and the SBA–123 Factory partnership agreement. 123factory is the program operator (SBA global partner), not a participating company. The participating companies are MobilWithUs, Closer Labs, Day1Lab, SSenStone, and Opticmix.

## Changes

- Added `content/programs/sba-poc-2026/index.md` and `index.ko.md` (English and Korean).
- Used the slug `sba-poc-2026` to match the other program slugs (year suffix). The five company pages (`closer-labs`, `day1lab`, `mobilwithus`, `opticmix`, `ssenstone`) previously referenced `sba-poc`; their `programs` tags were updated to `sba-poc-2026`.
- Framed the page around 123factory's role as the program operator (global partner), not as a participant, covering program planning, company selection, and operation.
- Kept the program overview concise and focused on the PoC objective (technology and service validation with overseas demand partners such as large corporations to check market fit and localize technology before full market entry), dropping redundant track attribution and support-item lists during review and aligning EN/KO tense and phrasing.
- Budget, KPI targets, and signatory details from the agreement were intentionally left out (the agreement restricts sharing exchanged information with third parties).
- Recruitment details from the announcement (budgets, KPIs, evaluation criteria, contacts) were intentionally left out. Target country/region is not stated in the source, so it was not added.

## Verification

- `hugo --gc --minify` build passed cleanly.
- `/programs/sba-poc-2026/` and `/ko/programs/sba-poc-2026/` render and list all five participating companies.
- Recruitment/filler-language check from the skill returned no matches.
- Gitleaks secret/PII scan passed with 0 leaks detected.
