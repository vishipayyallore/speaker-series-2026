# Cline rules — Speaker Series 2026

Mirrors Cursor/GitHub governance for Cline.

**Canonical sources:** `.cursor/rules/`, `.github/copilot-instructions.md`, `.github/skills/`, `.github/agents/`

## Sync

```powershell
./tools/psscripts/sync-assistant-mirrors.ps1
```

| Cline path | Canonical |
| --- | --- |
| `rules/` | `.cursor/rules/*.mdc` |
| `skills/` | `.github/skills/*/SKILL.md` (stubs with `canonical:`) |
| `agents/` | `.github/agents/*.md` |
| `AGENTS.md` | root [`AGENTS.md`](../AGENTS.md) |

## Bundled skills

- `speaker-series` — portfolio and talk context
- `ci-checks` — local CI aligned with workflows
- `workspace-review` — structure and parity audit

## Subagents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After code, docs, or governance edits |
| `talk-content-review` | Reviewing talk folders and portfolio docs |
| `docs-originality-review` | Spot-checking imports for repo fit |

## CI

`ci-python.yml`, `ci-documentation.yml`, `ci-skills-parity.yml`

Local runner: `.github/skills/ci-checks/SKILL.md`
