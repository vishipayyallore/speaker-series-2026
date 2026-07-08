---
name: ci-checks
description: Run CI-aligned quality checks locally for Applied Engineering. Use when asked to run CI, lint, test, or verify docs, tracked Python, and mirrored skills.
---

# CI Checks — Local Runner (Applied Engineering)

Use the workflow files under `.github/workflows/` as the source of truth.

## CI-aligned checks (required)

- Python byte-compilation for tracked `.py` files (`ci-python.yml`)
- Markdown lint for documentation (`ci-documentation.yml`)
- Skills parity between `.github/skills/` and `.cursor/skills/` (`ci-skills-parity.yml`)

The repository may temporarily contain no Python files. Checks should skip
cleanly in that case.

## Prerequisites

- **Python 3.12** (or the version in `.python-version`)
- **Node.js 20.x** for `markdownlint-cli2`

## Required checks

Report each as PASS or FAIL with output.

### 1. Python byte-compile

```powershell
$py = @(git ls-files '*.py')
if ($py.Count -gt 0) { python -m py_compile @py } else { Write-Host 'No tracked .py files; skipping.' }
```

### 2. markdownlint-cli2

Same globs as `ci-documentation.yml` (`.archive/**` is excluded via
`.markdownlint-cli2.yaml` ignores):

```powershell
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" "src/**/*.md" "tools/**/*.md" "01-knowledge/**/*.md" "02-patterns/**/*.md" "03-labs/**/*.md" "04-projects/**/*.md" "05-playbooks/**/*.md" "06-research/**/*.md" "07-interview-prep/**/*.md"
```

### 3. Skills parity (when skills changed)

See the PowerShell snippet in `.github/skills/README.md`, or push and rely on
`ci-skills-parity.yml`.

## Optional local checks

### Lychee (link checker)

If the `lychee` CLI is installed and `lychee.toml` exists:

```powershell
lychee --config lychee.toml --cache --max-cache-age 1d README.md docs/**/*.md src/**/*.md tools/**/*.md 01-knowledge/**/*.md 02-patterns/**/*.md 03-labs/**/*.md 04-projects/**/*.md 05-playbooks/**/*.md 06-research/**/*.md 07-interview-prep/**/*.md
```

### Python style (only when `src/` has tracked `.py` files)

Run only if you have project dev tools installed locally:

```powershell
$py = @(git ls-files 'src/**/*.py')
if ($py.Count -eq 0) { Write-Host 'No tracked src Python; skipping style checks.'; return }
python -m isort --check-only --diff @py
python -m black --check --line-length 127 --target-version py312 @py
python -m flake8 @py --count --select=E9,F63,F7,F82 --show-source --statistics
```

### Tests (only when `tests/` exists)

```powershell
if (Test-Path tests) { python -m pytest tests/ -q --tb=short }
```

## On failure

- **py_compile / markdownlint:** report file and line when available.
- **Skills parity:** sync `.github/skills/` to `.cursor/skills/` per `.github/skills/README.md`.

## Summary format

| # | Check | Status | Notes |
|---|--------|--------|-------|
| 1 | py_compile | | |
| 2 | markdownlint | | |
| 3 | skills parity | | optional unless skills changed |
