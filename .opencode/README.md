# OpenCode — Speaker Series 2026

OpenCode plugin config. **Canonical:** `.github/copilot-instructions.md`, `.cursor/rules/`, `.github/skills/`, `.github/agents/`

## Sync

```powershell
./tools/psscripts/sync-assistant-mirrors.ps1
```

## Layout

```text
talks/  assets/  templates/  docs/  tools/
```

## Skills

Same bundles as `.github/skills/`: `speaker-series`, `ci-checks`, `workspace-review`

## Agents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After governance edits |
| `talk-content-review` | Talk folders and portfolio docs |
| `docs-originality-review` | Import / repo fit review |

## CI

`ci-python.yml`, `ci-documentation.yml`, `ci-skills-parity.yml`

## Package

`package.json` pins `@opencode-ai/plugin` for local OpenCode integration.
