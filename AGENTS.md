# Agent instructions (index)

This repository is **Speaker Series 2026** — a speaker portfolio and canonical index
for meetup sessions. Python hands-on curriculum lives in
[python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice).

## Read first

1. `README.md` — speaker portfolio index and talk table
2. `CLAUDE.md` — repo-level assistant entry point
3. `.github/copilot-instructions.md` — canonical assistant rules
4. `.cursor/rules/project-scope.mdc` — scope and anti-contamination rules
5. `.cursor/rules/09_core-agent-role.mdc` — professional stance

**Precedence:** `.github/copilot-instructions.md` → `CLAUDE.md` → `.cursor/rules/*` → `README.md`

## Repository structure

```text
talks/       — per-session metadata; in-repo demos under talks/{id}/
assets/      — slides, diagrams, images, recordings
templates/   — new in-repo talk scaffolding
docs/        — speaker profile, FAQ, roadmap, folder layout
tools/       — repo maintenance scripts (CI, mirror sync)
```

See `docs/01-folder-structure.md` for talk types (external index vs in-repo demo).

## Skills (canonical → mirror)

- **Source of truth:** `.github/skills/`
- **Cursor mirror:** `.cursor/skills/` (byte-identical — do not edit directly)
- **OpenCode mirror:** `.opencode/skills/`
- **Cline stubs:** `.clinerules/skills/*.md` (point to canonical SKILL.md)

Bundled skills: `speaker-series`, `ci-checks`, `workspace-review` — see `.github/skills/README.md`.

After editing `.github/skills/`, copy to `.cursor/skills/` and `.opencode/skills/`, or run `tools/psscripts/sync-assistant-mirrors.ps1`.

## Subagents (canonical → mirror)

| Agent | Use when |
| --- | --- |
| `talk-content-review` | Auditing talk folders, templates, portfolio docs |
| `agent-ci-verify` | After code, docs, or governance edits |
| `docs-originality-review` | Spot-checking doc rewrites for repo fit |

Canonical: `.github/agents/`. Mirrors: `.clinerules/agents/`, `.opencode/agents/`.

## Assistant mirrors

| Path | Role |
| --- | --- |
| `.cursor/rules/` | Cursor rules (`.mdc`) — canonical for rules |
| `.clinerules/` | Cline mirror of rules, skills stubs, agents |
| `.opencode/` | OpenCode mirror of rules, skills, agents |
| `.claude/` | Claude Code style and config |
| `.copilot/` | Copilot editor settings |

**Workflow:** edit canonical paths → run `tools/psscripts/sync-assistant-mirrors.ps1` → verify with
`ci-skills-parity` and the workspace-review checklist.

## Prompts

Repo-specific prompts: `.github/prompts/`
