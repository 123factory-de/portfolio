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
  logo.ko.{ext}
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
industries: ["AI", "Bio"]
tags: ["specific technology", "secondary keyword"]
website: "https://example.com"
founded: "2021"
ceo: "Jane Doe"
headquarters: "Seoul, Korea"
logo: "logo.svg"
---
```

For Korean pages, localize `description` and set `logo` to the Korean asset filename, for example `logo.ko.svg`.

Rules:
- Keep `website` if available.
- Add `founded`, `ceo`, and `headquarters` when they are available from public source material. Do not guess these values.
- Do not include personal phone numbers, emails, or private contact details.
- Do not add `company` as a tag.
- Keep `industries` broad and filter-friendly, such as `AI`, `Bio`, `Battery`, `Materials`, `Manufacturing`, `Mobility`, `Energy`, `Healthcare`, `Robotics`, `Semiconductor`, `Sustainability`.
- Keep `tags` technical and specific, but remember they are metadata and should not be emphasized in the page UI.

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

Preferred filenames:
- English/default logo: `logo.svg`, `logo.png`, or `logo.jpg`
- Korean logo variant: `logo.ko.svg`, `logo.ko.png`, or `logo.ko.jpg`

If no Korean-specific logo exists, copy the same logo into the `logo.ko.*` file so the Korean page can later be updated independently.

## Workflow

1. Read the source company information and extract only public, company-level facts.
2. Pick a stable slug and create `content/companies/{slug}/`.
3. Add or copy logo assets into that folder.
4. Write `index.md` in English using the required sections.
5. Write `index.ko.md` as a Korean translation localized for Korean readers.
6. Verify no contact/private data was added.
7. Verify no old section names remain:

```sh
rg -n "Key Signals|핵심 신호|Strategic Highlights|검토 포인트|Fit With 123factory|Contact|Phone|Email" content/companies/{slug}
```

8. Build the site:

```sh
hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio
```

9. Confirm generated card assets point to page-bundle URLs such as `/companies/{slug}/logo.svg` and `/ko/companies/{slug}/logo.ko.svg`.
