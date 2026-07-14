---
title: "fix: simplify Gangnam testbed emphasis"
date: 2026-07-14
branch: fix/remove-gangnam-testbed-emphasis
request-source: "chat, 2026-07-14"
---

## Request

Simplify the Korean and English descriptions for the 2026 Gangnam Global Testbed Program. Retain bold emphasis only on the program name in the introductory sentence and remove other emphasis and purple styling.

## Changes

- Removed bold formatting from `1:1` in the Korean and English program descriptions.
- Retained bold formatting only for the program name in each introductory sentence.
- Confirmed the two Markdown source files contain no purple color markup or color classes.

## Verification

- Reviewed the bilingual Markdown files to confirm the intended program names remain the only bolded text.
- Ran `hugo --gc --minify` successfully.
