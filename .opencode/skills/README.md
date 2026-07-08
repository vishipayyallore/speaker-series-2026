# Agent skills (OpenCode mirror)

Canonical source: `.github/skills/`. Edit there first, then resync this folder.

| Skill | Purpose |
| --- | --- |
| `applied-engineering/` | Domain context — mirror of `.github/skills/applied-engineering/` |
| `ci-checks/` | Local CI — mirror of `.github/skills/ci-checks/` |
| `workspace-review/` | Full workspace audit checklist |

**CI:** Pushes that touch skills run `.github/workflows/ci-skills-parity.yml` (`.github` ↔ `.cursor` only).

When updating OpenCode skills, keep all three folders identical to `.github/skills/`.
