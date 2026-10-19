---
title: "feat(content): update delegation company profiles and logos"
date: 2026-10-19
branch: feat/update-mercedes-benz-delegation-companies
request-source: "chat, 2026-10-19"
---

## Request

Update the company profiles and official logos for participating startups in the Mercedes-Benz Korea delegation program using official program descriptions from the program organizer's summary document and logo image files in `temp/참여기업_로고_png/`.

## Changes

- Replaced researched descriptions with official program coordinator content in English and Korean across all 5 standard profile sections (`Company Overview`, `Technology & Product`, `Market & Use Cases`, `Traction & References`, `Collaboration Relevance`):
  - `content/companies/vision-innovation/` (`index.md`, `index.ko.md`): updated overview to focus on nozzle solutions enabling higher recycled plastic usage in automotive parts, detailed pin- and screw-type Vision Nozzle specifications, KTR-witnessed CO gas removal testing, and collaboration relevance with Mercedes-Benz supplier networks.
  - `content/companies/smartride/` (`index.md`, `index.ko.md`): updated overview to focus on commercial fleet management and autonomous vehicle service hub platform, standardized service-center workflows (D-note, IMMS, SOPs), and Mercedes-Benz Korea service center pilot relevance; normalized page title to `SmartRide`.
  - `content/companies/zephyros-electronic/` (`index.md`, `index.ko.md`): updated overview to focus on ZEPHYROS EDA Python-based parametric optimization engine with Ansys API integration, PCB filter automation (LPF/BPF), and potential electromagnetic validation workflows for automotive E/E hardware; normalized page title to `Zephyros Electronic`.
- Synchronized frontmatter descriptions and verticals in both English and Korean to reflect updated company scope and PitchBook taxonomy.
- Escaped tilde ranges (`\~`) in the Korean Vision Innovation profile to prevent Goldmark from interpreting pairs of `~` as strikethrough markup.
- Moved English parentheticals outside bold markup (`**한글**(English)조사`) in Korean profiles to prevent CommonMark delimiter ambiguity when followed directly by Korean particles.
- Updated company names based on organizer annotations in summary document: `Viewzen` to `VSION` (English title and body references in `content/companies/vsion/`) and `MetaMobility` to `Meta Physical Intelligence` / `메타피지컬인텔리전스` (English/Korean titles and body references in `content/companies/meta-mobility/`).
- Updated official logos across 7 delegation companies using provided PNG assets, optimized and downscaled oversized assets to max width 1200px (e.g. SmartRide from 10,985px down to 38KB, MetaMobility from 4,857px down to 39KB) for responsive web performance:
  - `linetron`: replaced `logo.jpg` with `logo.png`
  - `meta-mobility`: replaced `logo.svg` with official `logo.png` (Meta Physical Intelligence)
  - `vision-innovation`: replaced `logo.svg` with official `logo.png`
  - `smartride`: replaced `logo.svg` with official `logo.png`
  - `zephyros-electronic`: updated `logo.png`
  - `quantum-hitech`: updated `logo.png` with official horizontal wordmark
  - `perseus`: updated `logo.png` with official emblem asset

## Verification

- Hugo build validated via `hugo --gc --minify` (all 80 EN and 78 KO pages built cleanly in 345 ms).
- Gitleaks secret/PII scan checked cleanly.
