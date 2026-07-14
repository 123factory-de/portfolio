---
title: "docs: define agent content workflow and worklog convention"
date: 2026-07-14
branch: docs/agent-content-workflow
request-source: "chat, 2026-07-14"
---

## Request

Three related improvements to the agent operating instructions:

1. When a user asks an agent to add, edit, or delete content, the agent
   should create a branch and do the work automatically (without asking
   step by step), and only ask the user for confirmation before opening
   a Pull Request.
2. That confirmation question must be phrased in plain language that a
   non-developer can understand — explaining that the change is not on
   the live site yet, what a GitHub Pull Request is, and what happens
   after approval.
3. Adopt the worklog convention from the `openinnovation` repository:
   every PR carries one worklog file that is the source of truth for the
   PR title and description.

## Changes

- Added an "Agent workflow for content tasks" section to `AGENTS.md`:
  branch from `main` automatically, do the work, validate and commit,
  write the worklog, then ask before pushing or opening a PR.
- The PR confirmation question must avoid bare jargon and make three
  things clear: the change is saved on a separate branch and not live
  yet; a Pull Request is GitHub's review-and-approve page; merging
  publishes to the live site. Included an example phrasing to translate
  into the user's language.
- Added a "Worklog — mandatory for every PR" section to `AGENTS.md` and
  `docs/worklog/_template.md`, mirroring the openinnovation convention:
  one `docs/worklog/YYYY-MM-DD-<branch-slug>.md` per PR, committed before
  the PR is opened; PR title/description are generated from it.
- Updated the `docs/` row of the repository layout table to mention
  worklogs.
- Reflected the branch-first and ask-before-PR steps in the
  `add-company-content` and `add-program-content` skill workflows.
- This file is the first worklog, serving as a filled-in example of the
  convention it introduces.

## Verification

- gitleaks pre-commit hook passed on this branch.
- `docs/` is outside Hugo's `content/`, so nothing from this change is
  rendered to the public site.
- Note: this PR touches `AGENTS.md`, a protected path, so the
  `protected-paths` CI job requires the PR to come from a trusted
  maintainer; the change was made at the maintainer's explicit request.
