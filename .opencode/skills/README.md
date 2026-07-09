# Agent skills (mirrored)

**Source of truth:** `.github/skills/`

| Mirror | Must match |
| --- | --- |
| `.cursor/skills/` | byte-identical to `.github/skills/` |
| `.opencode/skills/` | byte-identical to `.github/skills/` |
| `.clinerules/skills/*.md` | stubs pointing to canonical SKILL.md |

Edit `.github/skills/` first, then run:

```powershell
./tools/psscripts/sync-assistant-mirrors.ps1
```

## Verify parity (PowerShell)

```powershell
./tools/psscripts/sync-assistant-mirrors.ps1 -VerifyOnly
```

Or rely on CI: `.github/workflows/ci-skills-parity.yml`

## Bundled skills

- `speaker-series` — domain context for this repository
- `ci-checks` — local commands aligned with `.github/workflows/ci-*.yml`
- `workspace-review` — portfolio and mirror audit checklist

**CI:** Pushes touching skills run `ci-skills-parity.yml`.
