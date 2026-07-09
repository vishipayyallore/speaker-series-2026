---
name: ci-checks
description: Run CI-aligned quality checks locally for Speaker Series 2026. Use when asked to run CI, lint, test, or verify docs, tracked Python, and mirrored skills.
canonical: ".github/skills/ci-checks/SKILL.md"
---

# CI Checks — Local Runner (Speaker Series 2026)

Use `.github/workflows/` as the source of truth.

## Required checks

| # | Check | Workflow |
| - | ----- | -------- |
| 1 | Python byte-compile | `ci-python.yml` |
| 2 | Markdown lint | `ci-documentation.yml` |
| 3 | Skills parity | `ci-skills-parity.yml` (when skills changed) |

## Prerequisites

- **Python 3.12** (or version in `.python-version`)
- **Node.js 20.x** for `markdownlint-cli2`

## Commands (PowerShell, repo root)

Local wrappers in `tools/psscripts/` mirror CI where possible:

```powershell
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1 -MarkdownOnly
.\tools\psscripts\sync-assistant-mirrors.ps1 -VerifyOnly
```

### 1. Python byte-compile

```powershell
$py = @(git ls-files '*.py')
if ($py.Count -gt 0) { python -m py_compile @py } else { Write-Host 'No tracked .py files; skipping.' }
```

### 2. markdownlint-cli2

Same globs as `ci-documentation.yml`:

```bash
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml `
  "README.md" "CONTRIBUTING.md" "AGENTS.md" "CLAUDE.md" `
  "docs/**/*.md" "talks/**/*.md" "templates/**/*.md" "src/**/*.md" "tools/**/*.md"
```

### 3. Skills parity

Run `tools/psscripts/sync-assistant-mirrors.ps1 -VerifyOnly` or see `.github/skills/README.md`.

## Optional: Lychee

```powershell
lychee --config lychee.toml --cache --max-cache-age 1d `
  README.md CONTRIBUTING.md docs/**/*.md talks/**/*.md templates/**/*.md src/**/*.md
```

## Summary format

| # | Check | Status | Notes |
| - | ----- | ------ | ----- |
| 1 | py_compile | | |
| 2 | markdownlint | | |
| 3 | skills parity | | optional unless skills changed |