---
name: workspace-review
description: Review Speaker Series 2026 for portfolio alignment, assistant mirror parity, and cross-repo contamination.
canonical: ".github/skills/workspace-review/SKILL.md"
---

# Workspace Review — Speaker Series 2026

Use when auditing the repository or after importing assistant configuration.

## Portfolio alignment

- [ ] Root `README.md` talk index matches folders under `talks/`
- [ ] Python talks are thin indexes linking to [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice)
- [ ] In-repo demos are self-contained under `talks/{id}/`
- [ ] `docs/01-folder-structure.md` matches actual layout

## Assistant parity

- [ ] `.github/skills/` ↔ `.cursor/skills/` ↔ `.opencode/skills/` byte-identical
- [ ] `.cursor/rules/*.mdc` synced to `.clinerules/rules/*.md` and `.opencode/rules/*.md`
- [ ] `.github/agents/` synced to `.clinerules/agents/` and `.opencode/agents/`
- [ ] No references to `applied-engineering`, `01-knowledge/`, or unrelated repos
- [ ] `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` describe speaker-series scope

## CI alignment

- [ ] `ci-documentation.yml` globs cover `talks/`, `templates/`, `docs/`
- [ ] Workflow names in assistant files match `.github/workflows/`

## Content spot-check

- [ ] Talk `links.md` and external URLs resolve
- [ ] Bedrock talk `.env.example` documented; no secrets committed

## Deliverables

1. Summary table: high / medium / low issues
2. Files to fix
3. Up to five next steps