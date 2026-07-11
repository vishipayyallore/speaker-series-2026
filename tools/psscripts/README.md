# PowerShell Scripts

**Location**: `tools/psscripts/`  
**Repo**: Speaker Series 2026

Automation for validation, CI-aligned checks, and assistant mirror sync (Windows + PowerShell).

---

## Essential scripts

| Script | Purpose |
| ------ | ------- |
| `RepoConfig.psd1` | Expected folders and scan roots for this repo |
| `Quick-HealthCheck.ps1` | Folder structure + markdown counts |
| `Run-MarkdownLintAndLychee.ps1` | Same surfaces as CI (`markdownlint-cli2` + Lychee) |
| `sync-assistant-mirrors.ps1` | Sync `.github/skills/` → mirrors; rules → `.clinerules/`, `.opencode/` |
| `Validate-FileReferences.ps1` | Broken relative links in markdown |

---

## Quick start

```powershell
.\tools\psscripts\Quick-HealthCheck.ps1
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1
.\tools\psscripts\sync-assistant-mirrors.ps1 -VerifyOnly
```

After governance edits:

```powershell
.\tools\psscripts\sync-assistant-mirrors.ps1
```

Markdown lint only / Lychee only:

```powershell
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1 -MarkdownOnly
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1 -LycheeOnly
```

---

## Optional utilities

| Script | Purpose |
| ------ | ------- |
| `Get-RepoStats.ps1` / `Get-FileStats.ps1` | Repo and file metrics |
| `Get-MarkdownSummary.ps1` | Markdown inventory |
| `Export-Diagrams.ps1` | Export `.mmd` → PNG under `assets/diagrams/` |
| `Test-ContentCompliance.ps1` | Policy checks via `RepoConfig.psd1` |
| `Run-AllPSScripts.ps1` | Batch runner (review before use) |

---

## Related docs

- [Folder layout](../../docs/01-folder-structure.md)
- [CI checks skill](../../.github/skills/ci-checks/SKILL.md)
- [CONTRIBUTING.md](../../CONTRIBUTING.md)
