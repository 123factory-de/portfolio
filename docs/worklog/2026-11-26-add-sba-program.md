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
- Used the slug `sba-poc-2026` to match the other program slugs (year suffix). The five company pages previously referenced `sba-poc`; their `programs` tags were updated to `sba-poc-2026`.
- Framed the page around 123factory's role as the program operator (SBA global partner), not as a participant. Roles follow the SBA–123 Factory partnership agreement (March 2026): SBA leads overall planning and recruitment, while 123factory designs and runs the program, selects the participating companies, and works closely with each one.
- Program description uses only facts from the announcement and agreement: the PoC focus (validation with overseas demand partners). A list of support items was dropped after review to keep the page short.
- Budget, KPI targets, and signatory details from the agreement were intentionally left out (the agreement restricts sharing exchanged information with third parties).
- Recruitment details from the announcement (budgets, KPIs, evaluation criteria, contacts) were intentionally left out. Target country/region is not stated in the source, so it was not added.

## Verification

- `hugo --gc --minify` build passed.
- `/programs/sba-poc-2026/` and `/ko/programs/sba-poc-2026/` render and list all five companies.
- Recruitment/filler-language check from the skill returned no matches.
