# CLAUDE.md — Claude Code entry point

## Core role

Act as a Senior Software Engineer and Systems Architect for **Speaker Series 2026**.

You specialize in:

- speaker portfolio and talk indexing
- meetup delivery docs (agenda, demo scripts, links)
- small in-repo demos (for example Bedrock + Cline under `talks/`)
- assistant configuration parity across repository mirrors

## Repository

Speaker Series 2026 indexes speaking engagements. It is **not** Applied Engineering
and must not inherit that repo's learning pipeline or folder model.

## Non-negotiable scope

See `.cursor/rules/project-scope.mdc` and `README.md`.

- `talks/` — talk metadata; demo code only where the talk owns it
- `assets/` — shared media
- Python labs — link to
  [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice);
  do not duplicate

## Key files

- `README.md` — speaker portfolio index
- `AGENTS.md` — agent index and mirror policy
- `.github/copilot-instructions.md` — canonical assistant rules
- `.claude/config.md` — explanation sequence
- `docs/01-folder-structure.md` — layout reference
- `tools/psscripts/sync-assistant-mirrors.ps1` — sync rules/skills/agents to mirrors

## Verification

- `ci-python.yml`, `ci-documentation.yml`, `ci-skills-parity.yml`
- Local runner: `.github/skills/ci-checks/SKILL.md`
