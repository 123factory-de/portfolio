# AGENTS.md

Operating instructions for AI coding agents (Hermes, Claude Code, and any other
AGENTS.md-compatible agent) working in this repository. This is the canonical,
tool-agnostic source of truth. Tool-specific files (`CLAUDE.md`, `.agent/rules/general.md`)
defer to this document.

**Read this file fully before making any change.**

---

## 🚦 Guardrails — non-negotiable

These rules are hard limits. If a task appears to require breaking one, **stop and ask a
human** instead of proceeding.

1. **Never commit to `main`.** Always work on a branch and open a Pull Request. `main` is
   protected and deploys to production on merge.
2. **Never commit secrets or personal data.** No API keys, tokens, credentials, Korean
   resident registration numbers (주민등록번호), personal phone numbers, or private email
   addresses. Commits are scanned by gitleaks locally (`.githooks/pre-commit`) and in CI
   (`.github/workflows/pr-checks.yml`). Do not disable, bypass, or edit these scans.
3. **Never modify protected paths.** The following may only be changed by a trusted human
   maintainer via a reviewed PR — an agent must not touch them:
   - `.github/` (CI workflows)
   - `.gitleaks.toml` (secret/PII scan rules)
   - `.githooks/` (git hooks)
   - `.agent/` (agent rules)
   - `AGENTS.md`, `CLAUDE.md` (agent instructions — you may not rewrite your own guardrails)
   - `.gitmodules` (submodule config)

   CI enforces this (`protected-paths` job); a PR from a non-maintainer that touches these
   paths will fail.
4. **Never edit generated or vendored files.** Do not hand-edit `public/`, `resources/`, or
   the `themes/blowfish/` submodule.
5. **Keep changes atomic and in scope.** One task per branch/PR. If you discover unrelated
   work, note it — do not bundle it in.
6. **When uncertain about a destructive or irreversible action, ask.** Deleting content,
   force operations, history rewrites, and dependency changes warrant a human check.

---

## Project

- **Name**: `portfolio`
- **Owner**: 123 Factory
- **Objective**: Build and maintain the portfolio website for 123 Factory.
- **Live site**: https://portfolio.123factory.de/
- **Stack**: [Hugo](https://gohugo.io/) (extended) static site generator with the
  [Blowfish](https://github.com/nunocoracao/blowfish) theme (git submodule at `themes/blowfish`).
- **Languages**: Bilingual site — English (default) and Korean (`ko`).

## Repository layout

| Path | Purpose |
| :--- | :--- |
| `config/_default/` | Hugo configuration (`hugo.toml`, `params.toml`, `menus.*.toml`, `languages.*.toml`, `markup.toml`) |
| `content/companies/` | Portfolio company pages (`_index.md` / `_index.ko.md` per entry) |
| `content/programs/` | Program pages |
| `layouts/` | Custom Hugo templates overriding the theme |
| `assets/`, `static/` | Site assets and static files |
| `i18n/` | Translation strings |
| `themes/blowfish/` | Theme (git submodule — do not edit) |
| `docs/` | Workflow docs, references, and agent skills |
| `.githooks/`, `.gitleaks.toml`, `.github/` | Safety guardrails (protected — see above) |
| `public/`, `resources/` | Generated output — do not edit |

## Setup & common commands

Requires Hugo **extended** (developed against `v0.153.x`) and `gitleaks` (for the commit hook).

```bash
git submodule update --init --recursive   # fetch the Blowfish theme
git config core.hooksPath .githooks       # enable the local secret-scan hook (once per clone)
brew install gitleaks                     # macOS; other platforms: gitleaks.io

hugo server -D                            # local dev server with drafts at http://localhost:1313
hugo --gc --minify                        # production build into ./public
```

Deployment is automated via GitHub Actions (`.github/workflows/deploy-pages.yml`) on merge to
`main`. Do not commit changes to the generated `public/` directory as part of feature work.

## Git workflow — source of truth

Follow these documents exactly. They are authoritative:

- [docs/git-workflow/branching-strategy.md](docs/git-workflow/branching-strategy.md)
- [docs/git-workflow/commit-convention.md](docs/git-workflow/commit-convention.md)
- [docs/git-workflow/pr-convention.md](docs/git-workflow/pr-convention.md)

Key rules:

- **GitHub Flow.** Branch from `main` using prefixes: `feat/`, `fix/`, `docs/`, `refactor/`,
  `test/`, `chore/`.
- **Merge to `main` with `--no-ff`** (create a merge commit; never fast-forward, squash, or
  rebase-merge) to preserve branch history.
- **Conventional Commits.** Format `<type>[scope]: <description>`; imperative mood; subject
  ≤ 50 chars; no trailing period.
- **Pull Requests** follow the template and process in the PR convention doc; keep PRs atomic.
  All PR checks (secret scan, protected paths) must pass before merge.
- Delete feature branches after merge.

## Content authoring

- Company and program entries are Markdown with front matter. Each entry has an English file
  and a Korean counterpart (`*.ko.md`). Keep both language versions in sync when adding or
  editing content.
- Do not publish personal data. Only use approved public contact addresses (see the allowlist
  in `.gitleaks.toml`); adding a new one requires a human-reviewed change to that protected file.
- Reusable content tasks are captured as skills in `docs/skills/`:
  - [`add-company-content`](docs/skills/add-company-content/SKILL.md) — add a new portfolio company.
  - [`add-program-content`](docs/skills/add-program-content/SKILL.md) — add a new program.
  Prefer these skills over ad-hoc edits when they apply.
- Industry taxonomy references live in `docs/references/` (PitchBook taxonomy/verticals).

## Conventions

- **Language**: All documentation, code comments, commit messages, and PR text in **English**.
- **Style**: Be concise and technical.
- Proactively suggest best practices, but keep changes focused and atomic.
