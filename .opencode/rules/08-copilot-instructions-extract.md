# Copilot Instructions Extract

Source: `.github/copilot-instructions.md`  
Repository: `speaker-series-2026`

## Core role

Senior Software Engineer and Systems Architect â€” speaker portfolio and talk assets.

## Structure

- `talks/` â€” session metadata and optional in-repo demos
- `assets/` â€” shared media
- `templates/` â€” in-repo talk scaffolding
- `docs/` â€” cross-talk reference
- External Python: [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice)

## Rules

- Thin README for external curriculum talks; full template set for in-repo demos
- No Applied Engineering / learning-pipeline assumptions
- Sync mirrors via `tools/psscripts/sync-assistant-mirrors.ps1`
- Skills canonical path: `.github/skills/`

## Quality

- CI: `ci-python.yml`, `ci-documentation.yml`, `ci-skills-parity.yml`
- Local: `.github/skills/ci-checks/SKILL.md`
