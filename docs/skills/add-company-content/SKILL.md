---
name: add-company-content
description: Add a new company profile to this Hugo portfolio from source company information, including English and Korean content, page-bundle assets, industry metadata, and validation.
---

# Add Company Content

Use this skill when adding a company to the portfolio from source material such as a PDF, website, notes, deck, or pasted company information.

## Target Audience

Write for:
- Investors evaluating startup quality, traction, technology defensibility, and investment relevance.
- Enterprise PoC and Open Innovation teams evaluating strategic fit, pilot potential, integration relevance, and partnership timing.
- Startup executives and founders evaluating whether the company could become a partner for joint PoCs, technology collaboration, market entry, or Korea-Europe expansion.

Write concise profiles that help these readers quickly understand the company, technology, market relevance, and collaboration or investment review points.

These readers are likely to ask:
- What does the company actually do, and what problem does it solve?
- What is the core technology or product, and how mature is it?
- Which industry, customer segment, or use case is most relevant?
- What proof points exist: customers, pilots, partners, certifications, awards, revenue, production, or IP?
- What makes the company differentiated from alternatives?
- What kind of collaboration could make sense: PoC, distribution, manufacturing, data partnership, R&D, licensing, investment, or market entry?
- What would another startup or founder need to know before approaching them?
- Are there geographic links, especially Korea-Europe relevance?

## Target Structure

Create one page bundle per company:

```text
content/companies/{slug}/
  index.md
  index.ko.md
  logo.{ext}
```

Use lowercase kebab-case for `{slug}`. Keep existing company URLs stable by matching the slug to the intended permalink.

## Required Front Matter

Both language files must use the same structural fields:

```yaml
---
title: "Company Name"
date: 2026-06-10
draft: false
description: "One-sentence summary for cards and metadata."
industries: ["Information Technology", "Healthcare"]
verticals: ["Cybersecurity", "Digital Health"]
programs: ["gangnam-global-testbed-2026"]
website: "https://example.com"
founded: "2021"
ceo: "Jane Doe"
headquarters: "Seoul, Korea"
logo: "logo.svg"
---
```

For Korean pages, localize `description` and use the same `logo` filename unless there is a real Korean-specific logo asset.

Rules:
- Keep `website` if available.
- Add `founded`, `ceo`, and `headquarters` when they are available from public source material. Do not guess these values.
- Keep `founded` concise and consistent for the portfolio facts block. Prefer the year only, such as `"2024"`. Use year and month only when the month is important for context. Do not include the exact day unless the user explicitly asks for legal-level detail.
- Do not include personal phone numbers, emails, or private contact details.
- Set `industries` using **PitchBook Primary Industry Sectors** only. See [`../../references/pitchbook-industry-taxonomy.md`](../../references/pitchbook-industry-taxonomy.md). Choose one or more of the 7 sectors, written exactly as listed:
  - `Business Products and Services`
  - `Consumer Products and Services`
  - `Energy`
  - `Financial Services`
  - `Healthcare`
  - `Information Technology`
  - `Materials and Resources`
- Assign the sector(s) that best match the company's primary customers and core business. Most companies have one primary sector; add a second only when the business genuinely spans two. Do not invent sector names or use vertical/technology labels (e.g. `AI`, `Bio`, `Battery`) in `industries` — put those in `verticals` instead.
- Set `verticals` using **PitchBook Industry Verticals** only. See [`../../references/pitchbook-industry-verticals.md`](../../references/pitchbook-industry-verticals.md). Pick from the A–Z vertical list, written exactly as listed (e.g. `Cleantech`, `Cybersecurity`, `Artificial Intelligence & Machine Learning (AI/ML)`, `Agtech`, `Digital Health`).
  - Verticals are thematic and cross-sector, so they are independent of `industries` — a company can sit in one sector but carry several verticals.
  - Assign **1–4** verticals, most central theme first. Add a vertical only when the company's core business clearly fits it; do not over-tag.
  - Use the exact vertical names from the reference. Do not invent new verticals. If no listed vertical fits, leave `verticals: []`.
- Use `programs` for accelerator, testbed, PoC, challenge, or portfolio-track membership when that affiliation matters for discovery or grouping.
  - Examples: `climate-launchpad`, `climaccelerator`, `gangnam-global-testbed-2026`, `kosme-poc`, `sba-poc`, `biocap`.
  - Use lowercase kebab-case slugs in `programs` so they map cleanly to `content/programs/{slug}/`.
  - Only add a `programs` entry when the company has a real affiliation, selection, participation, or explicit connection to that track.

## Page Sections

English pages should use:

```markdown
## Company Overview

## Technology & Product

## Market & Use Cases

## Traction & References

## Collaboration Relevance
```

Korean pages should use:

```markdown
## 회사 개요

## 기술 및 제품

## 시장 및 활용 분야

## 성과 및 레퍼런스

## 협업 가능성
```

Tone:
- Avoid hype, marketing filler, and unsupported claims.
- Avoid internal memo language such as "Key Signals".
- Write English at a clear B1-B2 business level. Prefer short, direct sentences that a non-native executive can read quickly.
- Avoid long noun chains and dense phrases. Split complex ideas into two sentences when needed.
- Avoid research-note phrasing in English such as "according to", "reported by", "references", "is positioned as", "indicates", and "is described as" when the fact can be stated directly.
- When adding a source link in English, state the fact first and attach the source inline.
- Bad: "The VC references more than KRW 4 billion in cumulative investment."
- Good: "Cumulative investment is more than KRW 4 billion([The VC](https://example.com))."
- Bad: "The company raised a Series A round, reported by [Media]."
- Good: "The company raised a Series A round([Media](https://example.com))."
- Prefer concrete evidence: product scope, technology, customers or partners, certifications, awards, traction, PoC fit, regulatory or commercialization status.
- In `Technology & Product` / `기술 및 제품`, link product names or core technology phrases to the company's official product, solution, or homepage explanation page when one is available.
- Before adding a product, technology, homepage, or source link, verify that the URL opens. If a product-specific page does not open, leave the product name unlinked or use a working broader official page only when it clearly explains the same product.
- Remove or replace homepage URLs that do not open. Do not keep broken homepage links in front matter.
- In `Traction & References` / `성과 및 레퍼런스`, include concrete proof points such as investment, customers, pilots, partners, certifications, awards, revenue, production status, exports, public programs, and IP.
- Do not repeat basic company facts such as founding year, CEO, headquarters, or website in `Traction & References` / `성과 및 레퍼런스` when they are already shown in the facts block.
- Do not frame portfolio company content as if the page is externally "validating" the company. Use neutral business language such as "성과", "레퍼런스", "수상 및 선정 이력", "사업화 레퍼런스", or "투자 유치".
- Link concrete proof points to relevant sources when available: official history pages, company pages, investor profiles, award pages, press articles, certification pages, or trusted startup databases.
- Prefer official company pages for product and technology explanations. Use third-party links for funding, awards, selections, and press-reported traction when official pages do not cover the specific proof point.
- Add links inline where they help the reader verify the claim. Do not create a long source dump at the end of the page.
- **Link placement by section** — concentrate links in `Traction & References` / `성과 및 레퍼런스`, with one exception:
  - `Company Overview`, `Market & Use Cases`, `Collaboration Relevance` (and `회사 개요`, `시장 및 활용 분야`, `협업 가능성`): no inline links. These sections are the author's synthesis, not claims that need external validation, and the homepage is already in the facts block `website`.
  - `Technology & Product` / `기술 및 제품`: only a navigational product/technology deep-link on the product name (per the rule above). Do not add parenthetical source citations here.
  - `Traction & References` / `성과 및 레퍼런스`: this is where source links live — funding, awards, certifications, customers, programs, IP.
  - Never cite the company's own root homepage (e.g. `([Company](https://company.com))`) as a source anywhere; it is redundant with the `website` field. Deep product/solution pages are fine in `Technology & Product`.
- In `Collaboration Relevance` / `협업 가능성`, include collaboration-relevant details when supported by source material: likely partner types, PoC use cases, market-entry angles, integration points, supply chain relevance, or Korea-Europe fit.
- If information is uncertain, avoid turning it into a firm claim. Either omit it or state the uncertainty briefly in plain language.
- Do not include a "Fit With 123factory" section.

Korean localization:
- Do not write translationese. Rewrite Korean copy so it reads like natural Korean business writing, not a literal translation of the English page.
- Prefer clear Korean sentence flow over preserving English sentence order.
- Use Korean business terms where they are common, but keep widely used industry terms such as PoC, Open Innovation, SaaS, OEM, IP, EV, and fleet when they are clearer.
- Avoid awkward direct translations such as "신호", "정렬", "사이클" unless the term is technically correct in context.
- Avoid indirect research-note phrasing such as "기준", "소개됩니다", "언급됩니다", "확인됩니다", "제시하고 있습니다", "보도됐습니다", and "검토할 수 있습니다" when a direct statement is supported. Prefer direct copy such as "주요 레퍼런스입니다", "인증을 보유하고 있습니다", "PoC에 적합합니다", or "협업할 수 있습니다".
- When adding a source link in Korean, do not make the source the grammatical subject unless it matters. State the fact directly and attach the source inline.
- Bad: "[The VC] 기준 누적 투자금은 40억 원 이상으로 소개됩니다."
- Good: "누적 투자금은 40억 원 이상입니다([The VC](https://example.com))."
- Bad: "관련 내용은 [매체명]에 보도됐습니다."
- Good: "2022년 45억 원 규모의 Series A 투자를 유치했습니다([매체명](https://example.com))."
- Write Korean like a concise company report prepared by a person. Vary sentence structure, avoid repeating "기업입니다", "개발합니다", "가능합니다", and do not mirror English paragraph rhythm.
- Make each section answer the reader's practical question first. For example, start market sections with the actual customer or use case, and start validation sections with concrete proof points.
- Keep Korean sentences concise. Split long English-style sentences into shorter Korean sentences when needed.

## Asset Handling

Store company logos inside the company bundle, not under `static/logos`.

Do not create fake, placeholder, or AI-made logo files. Only add a logo asset when it is the company's official logo or a faithful copy from an official/public source. Prefer a full official wordmark or logo from the company website. If no full logo is available, an official favicon, app icon, or apple-touch-icon from the company's own domain can be used as the card logo. If no official logo or official favicon asset is available, leave `logo: ""` in front matter. The company card will show the company name as a text fallback.

Preferred filenames:
- English/default logo: `logo.svg`, `logo.png`, or `logo.jpg`

Use one shared logo file across languages when the logo image is identical. Only add a Korean logo variant such as `logo.ko.svg`, `logo.ko.png`, or `logo.ko.jpg` when the company has a real Korean-specific official logo.

## Workflow

0. Create a branch from the latest `main` before touching any file (e.g.
   `feat/add-company-{slug}`). Do not ask for permission to branch, and never work
   directly on `main`.
1. Read the source company information and extract only public, company-level facts.
2. Assign `industries` by matching the company to a PitchBook Primary Industry Sector using [`../../references/pitchbook-industry-taxonomy.md`](../../references/pitchbook-industry-taxonomy.md).
3. Assign `verticals` by matching the company's themes to PitchBook Industry Verticals using [`../../references/pitchbook-industry-verticals.md`](../../references/pitchbook-industry-verticals.md).
4. Assign `programs` when the company belongs to an accelerator, PoC, testbed, or portfolio track.
5. Pick a stable slug and create `content/companies/{slug}/`.
6. Add or copy logo assets into that folder.
7. Write `index.md` in English using the required sections.
8. Write `index.ko.md` as a Korean translation localized for Korean readers.
9. Verify no contact/private data was added.
10. Verify no old section names remain:

```sh
rg -n "Key Signals|핵심 신호|Strategic Highlights|검토 포인트|Fit With 123factory|Contact|Phone|Email" content/companies/{slug}
```

11. Build the site:

```sh
hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio
```

12. Confirm generated card assets point to page-bundle URLs such as `/companies/{slug}/logo.svg` and `/ko/companies/{slug}/logo.svg` when the same logo is shared across languages.

13. Write the branch's worklog file `docs/worklog/YYYY-MM-DD-<branch-slug>.md` from
    [docs/worklog/_template.md](../../worklog/_template.md) and commit it on the same
    branch (see "Worklog — mandatory for every PR" in AGENTS.md).

14. Commit on the branch, then summarize the change and ask the user whether to create
    a Pull Request. Ask in plain, non-developer language as described in AGENTS.md
    ("Agent workflow for all tasks"): explain that the change is not on the live
    site yet and that a Pull Request is GitHub's review-and-approve page. Do not push
    or open a PR without the user's confirmation.
