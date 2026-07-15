---
title: "feat: add two Gangnam testbed profiles"
date: 2026-07-15
branch: feat/add-companies-gangnam-global-testbed-2026
request-source: "chat, 2026-07-15"
---

## Request

Add DaWinKS and KL Cube as participating companies in the 2026 Gangnam Global Testbed program, using the supplied investment decks, extracted deck text, and prepared company profiles as source material.

## Changes

- Added synchronized English and Korean company pages for DaWinKS and KL Cube.
- Classified both companies with PitchBook-aligned primary industries and verticals.
- Connected both profiles to the `gangnam-global-testbed-2026` program.
- Added official company logos extracted from the supplied investment decks.
- Focused the DaWinKS profile on the DPEC Platform, MTM/DTM terminals, e-KYC and AML technology, deployments, certifications, and practical collaboration paths.
- Linked the DaWinKS English profile to the company's English-language homepage while retaining the Korean homepage on the Korean profile.
- Focused the KL Cube profile on HandSignVerse, its NOVA sign-language generation engine, accessibility deployments, certifications, awards, and integration options.
- Used a direct portfolio voice for established company facts instead of source-review phrasing.
- Qualified company-provided claims and omitted forward-looking investment projections from both portfolio profiles.

## Verification

- `hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio` completed successfully with Hugo 0.153.3 extended.
- Confirmed the English and Korean DaWinKS company cards render and use the shared page-bundle asset at `/companies/dawinks/logo.png`.
- Confirmed the English and Korean KL Cube company cards render and use the shared page-bundle asset at `/companies/kl-cube/logo.svg`.
- Confirmed the required English and Korean section names render on all four generated profile pages.
- Searched the new content for prohibited section names, contact details, email addresses, personal phone-number patterns, and trailing whitespace; no matches were found.
- `xmllint --noout content/companies/kl-cube/logo.svg` completed successfully.
- `gitleaks dir --no-banner --redact content/companies/dawinks content/companies/kl-cube docs/worklog/2026-07-15-add-companies-gangnam-global-testbed-2026.md` completed with no leaks found.
