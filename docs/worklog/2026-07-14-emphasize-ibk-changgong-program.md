---
title: "fix: emphasize IBK Changgong program"
date: 2026-07-14
branch: fix/emphasize-ibk-changgong-program
request-source: "chat, 2026-07-14"
---

## Request

Emphasize only the full 2026 IBK Changgong Global (Germany) Accelerating Program name in the Korean and English introductory descriptions.

## Changes

- Replaced inline-code formatting with bold emphasis for the full Korean program name.
- Replaced inline-code formatting with bold emphasis for the full English program name.
- Left all surrounding introductory text unchanged.

## Verification

- Reviewed the bilingual Markdown diff to confirm that only the requested program names are bolded.
- Ran `hugo --gc --minify` successfully.
