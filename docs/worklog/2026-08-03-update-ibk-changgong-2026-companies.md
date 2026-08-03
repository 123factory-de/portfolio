---
title: "feat(content): update AIT Studio profile for IBK Changgong 2026 cohort"
date: 2026-08-03
branch: feat/update-ibk-changgong-2026-companies
request-source: "chat, 2026-08-03"
---

## Request

Update the AIT Studio portfolio company entry (`content/companies/ait-studio/`) with revised product lineup information, explicit accuracy metrics, CE-MDR Class I & ISO 13485 certifications, specific Swiss hospital reference (Felix Platter Hospital), and clinical-grade terminology adjustments.

## Changes

- **`content/companies/ait-studio/index.md` & `index.ko.md`**:
  1. **Company Overview**: Adjusted phrasing to "clinical-grade tool for gait analysis" (임상 등급 보행분석 도구) to align with CE-MDR Class I intended use.
  2. **Technology & Product**: Replaced general product line description with MEDISTEP M Pro (Class I medical device) and MEDISTEP M (non-medical version for fitness/senior care/wellness), excluding kiosks from the export lineup.
  3. **Accuracy Metrics**: Detailed accuracy as ~95% compared to gold-standard motion-capture systems (Vicon, Qualisys, GAITRite) based on third-party test reports.
  4. **Certifications**: Added CE-MDR Class I certification, ISO 13485 certification, and EU Authorized Representative in Germany to Traction & References.
  5. **Reference Hospital**: Specified Felix Platter Hospital in Basel, Switzerland.

## Verification

- **Hugo Build**: Executed `hugo --gc --minify` successfully without errors (71 EN / 69 KO pages rendered).
