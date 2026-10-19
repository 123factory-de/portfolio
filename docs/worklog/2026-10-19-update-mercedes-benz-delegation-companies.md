---
title: "feat(content): update Vision Innovation, SmartRide, and Zephyros Electronic profiles"
date: 2026-10-19
branch: feat/update-mercedes-benz-delegation-companies
request-source: "chat, 2026-10-19"
---

## Request

Update the company profiles for Vision Innovation, SmartRide, and Zephyros Electronic (participating startups #6, #7, and #8 in the Mercedes-Benz Korea delegation program) using official program descriptions from the program organizer's summary document.

## Changes

- Replaced researched descriptions with official program coordinator content in English and Korean across all 5 standard profile sections (`Company Overview`, `Technology & Product`, `Market & Use Cases`, `Traction & References`, `Collaboration Relevance`):
  - `content/companies/vision-innovation/` (`index.md`, `index.ko.md`): updated overview to focus on nozzle solutions enabling higher recycled plastic usage in automotive parts, detailed pin- and screw-type Vision Nozzle specifications, KTR-witnessed CO gas removal testing, and collaboration relevance with Mercedes-Benz supplier networks.
  - `content/companies/smartride/` (`index.md`, `index.ko.md`): updated overview to focus on commercial fleet management and autonomous vehicle service hub platform, standardized service-center workflows (D-note, IMMS, SOPs), and Mercedes-Benz Korea service center pilot relevance; normalized page title to `SmartRide`.
  - `content/companies/zephyros-electronic/` (`index.md`, `index.ko.md`): updated overview to focus on ZEPHYROS EDA Python-based parametric optimization engine with Ansys API integration, PCB filter automation (LPF/BPF), and potential electromagnetic validation workflows for automotive E/E hardware; normalized page title to `Zephyros Electronic`.
- Synchronized frontmatter descriptions and verticals in both English and Korean to reflect updated company scope and PitchBook taxonomy.

## Verification

- Hugo build validated via `hugo --gc --minify` (all 80 EN and 78 KO pages built cleanly in 345 ms).
- Gitleaks secret/PII scan checked cleanly.
