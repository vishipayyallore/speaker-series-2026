# tools

Repository-local helper scripts (**not** application code under `src/` or talk demos under
`talks/{id}/`).

| Folder | Purpose |
| ------ | ------- |
| [`psscripts/`](psscripts/README.md) | PowerShell — CI checks, health, assistant mirror sync |
| [`pyscripts/`](pyscripts/README.md) | Python — parity verification, optional media utilities |

## Quick start (PowerShell, repo root)

```powershell
.\tools\psscripts\Quick-HealthCheck.ps1
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1
.\tools\psscripts\sync-assistant-mirrors.ps1 -VerifyOnly
```

After editing `.github/skills/`, `.github/agents/`, or `.cursor/rules/`:

```powershell
.\tools\psscripts\sync-assistant-mirrors.ps1
```

See also [CONTRIBUTING.md](../CONTRIBUTING.md) and [.github/skills/ci-checks/SKILL.md](../.github/skills/ci-checks/SKILL.md).
