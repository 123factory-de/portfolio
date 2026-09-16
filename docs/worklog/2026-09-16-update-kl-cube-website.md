---
title: "fix: update KL Cube website URL"
date: 2026-09-16
branch: fix/update-kl-cube-website
request-source: "Slack, 2026-09-16"
---

## Request

Update the website address on the English KL Cube company page to https://www.klcube.co.kr/.

## Changes

Changed the English page's `website` front matter from the former `/eng/` URL to the requested canonical KL Cube URL. The Korean page already used the requested URL, so it was left unchanged.

## Verification

- Confirmed the English and Korean KL Cube page front matter.
- Ran `hugo --gc --minify --cacheDir /private/tmp/hugo_cache_portfolio` successfully.
- Reviewed the focused Git diff and checked for whitespace errors.
