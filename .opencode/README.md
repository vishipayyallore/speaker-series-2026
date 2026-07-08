# OpenCode — Applied Engineering

OpenCode plugin config for this repository. **Canonical sources:**
`.github/copilot-instructions.md`, `.cursor/rules/`, `.github/skills/`, and
`.github/agents/`.

## Layout

```text
01-knowledge/ … 07-interview-prep/   # learning pipeline
docs/  src/  templates/  scripts/  tools/  sandbox/
.github/  .cursor/  .claude/  .copilot/  .vscode/
```

## Rules

`rules/` mirrors `.cursor/rules/*.mdc` (project-scope + numbered `01`–`09`).

## Skills

Same bundles as `.github/skills/` plus `workspace-review` — see `skills/README.md`.

## Agents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After code, docs, or governance edits |
| `content-quality-review` | Auditing pipeline teaching content |
| `docs-originality-review` | Spot-checking doc rewrites |

## CI workflows

| Workflow | Scope |
| --- | --- |
| `ci-python.yml` | Tracked `.py` byte-compile |
| `ci-documentation.yml` | Markdown lint |
| `ci-skills-parity.yml` | `.github/skills/` ↔ `.cursor/skills/` mirror |

Local runner: `skills/ci-checks/SKILL.md` (canonical: `.github/skills/ci-checks/SKILL.md`).

## Package

`package.json` pins `@opencode-ai/plugin` for local OpenCode integration.

When editing governance, update canonical paths first, then resync this tree.
