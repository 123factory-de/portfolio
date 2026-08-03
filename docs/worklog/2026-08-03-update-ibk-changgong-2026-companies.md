---
title: "feat(content): update company profiles for IBK Changgong 2026 cohort (AIT Studio, LMNTIC Biotech, AAVATAR Therapeutics, BICHEDAM, BeyondDx)"
date: 2026-08-03
branch: feat/update-ibk-changgong-2026-companies
request-source: "chat, 2026-08-03"
---

## Request

Update company profiles for IBK Changgong 2026 cohort entries:
1. **AIT Studio** (`content/companies/ait-studio/`): revised product lineup, explicit accuracy metrics, CE-MDR Class I & ISO 13485 certifications, specific Swiss hospital reference (Felix Platter Hospital), and clinical-grade terminology.
2. **LMNTIC Biotech** (`content/companies/lmntic/`): updated Company Overview, Technology & Product (L:Biopsy microfluidic platform details, ~87% CTC recovery, >90% purity mode, ~4-hour run, no centrifuge, benchtop system), and Market & Use Cases.
3. **AAVATAR Therapeutics** (`content/companies/aavatar/`): updated Company Overview (AI-driven AAV capsid engineering, in-house manufacturing, licensing/co-development focus), Technology & Product (manufacturability-prioritized ML platform, NGS screening, NHP/rodent validation), Market & Use Cases (CNS, heart, skeletal muscle, kidney targeting; Krabbe disease, hereditary hearing loss, GA programs), and Collaboration Relevance.
4. **BICHEDAM** (`content/companies/bichedam/`): updated Company Overview (aging-related vascular diseases, Gyeongsan/Seoul/Daegu offices), Technology & Product (BCD101 liquid soft-extract formulation, 6-herb extract, puerarin marker, RhoA/ROCK pathway, rapid Tmax profile), Market & Use Cases (Nocturnal Leg Cramps / NLC unmet need, aging vascular conditions), Traction & References (KRW 2.3B raised, Phase 1 IND/completion in healthy adults, US patent 12,329,798 B2), and Collaboration Relevance (European pharma partnership focus).
5. **BeyondDx** (`content/companies/beyonddx/`): updated Company Overview (AI-enabled IVD solutions, LDCT-positive nodule management), Technology & Product (ForeCheck LC 3-protein biomarker assay, 150-min run, iDXGate platform), Market & Use Cases (LDCT-positive pulmonary nodules, Korean approval & CE-IVDR preparation), Traction & References (ISO 13485, Korean GMP, 3,400+ specimen dataset, ASCO 2025/2026 presentations, Shanghai Kehua MOU, with updated The Yakup reference links), and Collaboration Relevance (European hospital/lab validation, Germany strategic gateway).

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
  3. **Market & Use Cases**: Rephrased target users, applications, lower-cost market positioning alongside tissue biopsy and ctDNA tests, and research-use-only status.

- **`content/companies/aavatar/index.md` & `index.ko.md`**:
  1. **Company Overview**: Positioned as AI-driven AAV capsid engineering platform company focused on capsid licensing and co-development with pharma partners.
  2. **Technology & Product**: Emphasized ML-driven AAV capsid engineering platform prioritizing manufacturability, NGS screening, rodent and NHP validation, and integrated in-house AAV manufacturing.
  3. **Market & Use Cases**: Updated strategic focus areas (CNS, heart, skeletal muscle, kidney) and proof-of-platform programs (Krabbe disease, hereditary hearing loss, geographic atrophy), with expansion capacity to PNS and pancreas.
  4. **Collaboration Relevance**: Highlighted joint validation, MTAs, sponsored research, co-development, and platform licensing.

- **`content/companies/bichedam/index.md` & `index.ko.md`**:
  1. **Company Overview**: Updated focus on aging-related vascular diseases, combining traditional Korean medicine with modern drug development, noting offices in Gyeongsan, Seoul, and Daegu.
  2. **Technology & Product**: Specified BCD101 as an oral liquid soft-extract formulation based on standardized 6-herb extract with puerarin marker, modulating RhoA/ROCK contraction pathway, with improved oral bioavailability and rapid Tmax profile confirmed in Phase 1.
  3. **Market & Use Cases**: Focused on Nocturnal Leg Cramps (NLC) unmet need and pipeline expansion to aging-related vascular/neurovascular disorders.
  4. **Traction & References**: Updated funding (KRW 2.3 billion across Seed/Pre-A), Phase 1 trial completion at Chungbuk National University Hospital, Yeungnam University know-how licensing, US patent (12,329,798 B2), and Korean patents.
  5. **Collaboration Relevance**: Detailed European partnership focus targeting phytomedicine, vascular aging, sleep-related symptoms, and elderly-care markets.

- **`content/companies/beyonddx/index.md` & `index.ko.md`**:
  1. **Company Overview**: Reframed as precision diagnostics company developing AI-enabled blood-based IVD solutions, focusing on ForeCheck LC for LDCT-positive pulmonary nodule risk assessment.
  2. **Technology & Product**: Specified ForeCheck LC as an adjunctive IVD measuring 3 serum protein biomarkers with a locked ML algorithm (~150 min assay) integrated into iDXGate platform.
  3. **Market & Use Cases**: Focused on patients with LDCT-detected pulmonary nodules, Korean regulatory approval pursuit, and preparation for CE-IVDR certification through European validation.
  4. **Traction & References**: Added ISO 13485 QMS and Korean GMP manufacturing details, 3,400+ specimen dataset, ASCO 2025/2026 presentations, Shanghai Kehua MOU, and Women's Startup Competition Grand Prize; updated reference links for The Yakup.
  5. **Collaboration Relevance**: Highlighted long-term European hospital/lab collaborations, CE-IVDR validation, companion diagnostics, and Germany as a strategic gateway.

## Verification

- **Hugo Build**: Executed `hugo --gc --minify` successfully without errors (71 EN / 69 KO pages rendered).
