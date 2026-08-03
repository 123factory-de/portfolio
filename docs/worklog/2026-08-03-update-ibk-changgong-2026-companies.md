---
title: "feat(content): update company profiles for IBK Changgong 2026 cohort (AIT Studio, LMNTIC Biotech)"
date: 2026-08-03
branch: feat/update-ibk-changgong-2026-companies
request-source: "chat, 2026-08-03"
---

## Request

Update company profiles for IBK Changgong 2026 cohort entries:
1. **AIT Studio** (`content/companies/ait-studio/`): revised product lineup, explicit accuracy metrics, CE-MDR Class I & ISO 13485 certifications, specific Swiss hospital reference (Felix Platter Hospital), and clinical-grade terminology.
2. **LMNTIC Biotech** (`content/companies/lmntic/`): updated Company Overview, Technology & Product (L:Biopsy microfluidic platform details, ~87% CTC recovery, >90% purity mode, ~4-hour run, no centrifuge, benchtop system), and Market & Use Cases (research-use-only tool positioning, cell counting/characterization, ctDNA/tissue biopsy complement).

## Changes

- **`content/companies/ait-studio/index.md` & `index.ko.md`**:
  1. **Company Overview**: Adjusted phrasing to "clinical-grade tool for gait analysis" (임상 등급 보행분석 도구).
  2. **Technology & Product**: Replaced general product line description with MEDISTEP M Pro (Class I medical device) and MEDISTEP M (non-medical version for fitness/senior care/wellness).
  3. **Accuracy Metrics**: Detailed accuracy as ~95% compared to gold-standard motion-capture systems (Vicon, Qualisys, GAITRite).
  4. **Certifications**: Added CE-MDR Class I certification, ISO 13485 certification, and EU Authorized Representative in Germany.
  5. **Reference Hospital**: Specified Felix Platter Hospital in Basel, Switzerland.

- **`content/companies/lmntic/index.md` & `index.ko.md`**:
  1. **Company Overview**: Updated founding year (2022), location (DGIST), and technical foundation (Prof. Cheol-Gi Kim's magnetophoretic cell-control technology).
  2. **Technology & Product**: Updated L:Biopsy microfluidic chip details, 10 mL blood sample processing, 87% cell recovery, >90% high-purity mode for sequencing, ~4-hour automated run time without centrifuge, and benchtop device cost-efficiency.
  3. **Market & Use Cases**: Rephrased target users (research labs, hospitals, cancer centers), applications (tumor cell counting/characterization, therapy response tracking, translational research), lower-cost market positioning alongside tissue biopsy and ctDNA tests, and research-use-only status.

## Verification

- **Hugo Build**: Executed `hugo --gc --minify` successfully without errors (71 EN / 69 KO pages rendered).
