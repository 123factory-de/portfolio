---
title: "feat(content): update StepHow and NAVOROS profile references"
date: 2026-10-20
branch: feat/update-deeptech-academy-companies
request-source: "chat, 2026-10-20"
---

## Request

Update and refine customer references and media source citations across deep-tech academy cohort company profiles (StepHow, NAVOROS).

## Changes

- `content/companies/stephow/` (`index.md`, `index.ko.md`):
  - Refined customer references in Traction & References to clarify and streamline customer citations (Techcross, KAIST, Pulmuone, Stemco) across both English and Korean profiles.
- `content/companies/navoros/` (`index.md`, `index.ko.md`):
  - Corrected media source outlet name for defense exhibition coverage from KIDD to `산업일보` (Korean) and `Industry Ilbo` (English) in Traction & References.

## Verification

- Hugo static site build verified cleanly via `hugo --gc --minify` (85 EN and 83 KO pages built without errors in 333 ms).
- Gitleaks secret/PII scan executed across repository files with 0 leaks detected.
