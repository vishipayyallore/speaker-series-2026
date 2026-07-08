# Role: Speaker Series assistant

**Scope:** Supplements `.cursor/rules/*.mdc`, especially `project-scope.mdc` and `09_core-agent-role.mdc`.

## Context

Speaker portfolio repository:

```text
talks/     — session index and in-repo demos
assets/    — slides, recordings, diagrams
templates/ — new in-repo talk scaffolding
docs/      — FAQ, roadmap, speaker profile
```

Python curriculum: [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice) (link only, no duplication).

## Coding rules

1. Per-talk demo code under `talks/{id}/src/`
2. Portable paths; no secrets in repo
3. Update root README when adding or delivering talks
4. After governance edits: `tools/psscripts/sync-assistant-mirrors.ps1`

## Quality gate

`.github/skills/ci-checks/SKILL.md` and `.github/workflows/ci-*.yml`
