---
title: "fix(company): update ABR company profile"
date: 2026-08-03
branch: fix/update-company-abr
request-source: chat, 2026-08-03
---

## Request

Update the company profile for ABR (Korean and English versions) with updated details regarding products, traction, headquarters location, and grammatical improvements.

## Changes

- Updated Korean profile (`content/companies/abr/index.ko.md`):
  - Updated headquarters address to "전남광주통합특별시 광양시".
  - Clarified recycling process description.
  - Updated remanufactured anode material entry.
  - Updated target markets to battery manufacturers and battery recyclers with closed-loop structure.
  - Updated traction & references with ongoing PoCs (PowerCo SE, Exide Energy Solutions), awards, and ISO 9001 certification.
- Updated English profile (`content/companies/abr/index.md`):
  - Standardized CEO name format to "YU TACK, KIM".
  - Updated remanufactured anode entry.
  - Updated target market description and fixed conjunction grammar ("battery manufacturing gigafactories and battery recycling companies").
  - Updated traction section with PoC details, awards, and ISO 9001 certification.

## Verification

- Built static site with `hugo --gc --minify` successfully without errors.
- Verified local development server rendering for both Korean and English company pages.
