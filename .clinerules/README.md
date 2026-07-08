# Cline rules — Applied Engineering

Mirrors Cursor/GitHub governance for Cline. **Canonical sources:** `.cursor/rules/`,
`.github/copilot-instructions.md`, `.github/skills/`, and `.github/agents/`.

## Sync sources

| Cline path | Canonical |
| --- | --- |
| `rules/` | `.cursor/rules/*.mdc` (same topics, `.md` extension) |
| `skills/` | `.github/skills/*/SKILL.md` (+ `workspace-review.md`) |
| `agents/` | `.github/agents/*.md` |
| `AGENTS.md` | Cline entry — defers to root [`AGENTS.md`](../AGENTS.md) |

## Bundled skills

- `applied-engineering` — domain context for this repository
- `ci-checks` — local commands aligned with `.github/workflows/ci-*.yml`
- `workspace-review` — structure, parity, and contamination audits

## Subagents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After code, docs, or governance edits |
| `content-quality-review` | Reviewing pipeline learning content |
| `docs-originality-review` | Spot-checking doc rewrites for fit and synthesis |

## CI workflows

| Workflow | Scope |
| --- | --- |
| `ci-python.yml` | Tracked `.py` byte-compile |
| `ci-documentation.yml` | Markdown lint |
| `ci-skills-parity.yml` | `.github/skills/` ↔ `.cursor/skills/` mirror |

Local runner: `.github/skills/ci-checks/SKILL.md` (Cline mirror: `skills/ci-checks.md`).

When editing governance, update canonical paths first, then resync this tree.
