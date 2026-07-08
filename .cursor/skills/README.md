# Agent skills (mirrored)

The `.github/skills/` tree is the **source of truth** for bundled agent skills
used with Cursor and GitHub Copilot (see `.github/copilot-instructions.md`).
`.cursor/skills/` is a byte-identical mirror.

This README is therefore identical in both locations. Read it as guidance for
whichever copy you happen to be in; edits should always be made first under
`.github/skills/` and then mirrored to `.cursor/skills/`.

## Mirror

`.cursor/skills/` must stay **identical** to `.github/skills/` (same paths,
same `SKILL.md` and `README.md` bytes). After editing under `.github/skills/`,
copy the updated tree to `.cursor/skills/`.

### Verify parity (PowerShell, repo root)

```powershell
$gRoot = Join-Path (Get-Location) ".github\skills"
$cRoot = Join-Path (Get-Location) ".cursor\skills"
Get-ChildItem $gRoot -Recurse -Filter SKILL.md | ForEach-Object {
 $rel = $_.FullName.Substring($gRoot.Length + 1)
 $c = Join-Path $cRoot $rel
 if (-not (Test-Path $c)) { Write-Host "Missing in .cursor/skills: $rel"; return }
 if ((Get-FileHash $_.FullName -Algorithm SHA256).Hash -ne (Get-FileHash $c -Algorithm SHA256).Hash) {
 Write-Host "MISMATCH: $rel"
 }
}
Get-ChildItem $cRoot -Recurse -Filter SKILL.md | ForEach-Object {
 $rel = $_.FullName.Substring($cRoot.Length + 1)
 $g = Join-Path $gRoot $rel
 if (-not (Test-Path $g)) { Write-Host "Extra in .cursor/skills (not in .github): $rel" }
}
```

## Bundled skills

- `applied-engineering` — domain context for this repository
- `ci-checks` — local commands aligned with `.github/workflows/ci-*.yml`
- `workspace-review` — full-repository audit checklist (structure, parity, migration)

**CI:** Pushes that touch skills also run `.github/workflows/ci-skills-parity.yml` on GitHub Actions.
