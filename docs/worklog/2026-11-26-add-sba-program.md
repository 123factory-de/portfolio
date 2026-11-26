---
title: "feat(content): add SBA global expansion PoC program"
date: 2026-11-26
branch: feat/add-sba-program
request-source: chat, 2026-11-26
---

## Request

Add a program page using the `add-program-content` skill for the 2026 Seoul Startup Hub (SBA) Global Expansion Program, based on the SBA partner-selection announcement PDF. The participating companies are MobilWithUs, Closer Labs, Day1Lab, SSenStone, and Opticmix.

## Changes

- Added `content/programs/sba-poc/index.md` and `index.ko.md` (English and Korean).
- Used the slug `sba-poc` because all five company pages already reference `programs: ["sba-poc"]`; no company files needed changes.
- Program description is limited to facts in the announcement: operated by Seoul Startup Hub / SBA, April–December 2026, PoC track (demand-partner-based technology validation and localization), and the common support items (pre-consulting, decision-maker business matching, PoC proposals, post-program follow-up).
- Recruitment details from the announcement (budgets, KPIs, evaluation criteria, contacts) were intentionally left out. Target country/region is not stated in the source, so it was not added.

## Verification

- `hugo --gc --minify` build passed.
- `/programs/sba-poc/` and `/ko/programs/sba-poc/` render and list all five companies.
- Recruitment/filler-language check from the skill returned no matches.
