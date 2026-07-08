# Sync assistant mirrors for Speaker Series 2026
#
# Canonical sources:
#   .github/skills/     -> .cursor/skills/, .opencode/skills/
#   .github/agents/     -> .clinerules/agents/, .opencode/agents/
#   .cursor/rules/*.mdc -> .clinerules/rules/*.md, .opencode/rules/*.md
#
# Usage:
#   ./scripts/sync-assistant-mirrors.ps1
#   ./scripts/sync-assistant-mirrors.ps1 -VerifyOnly

param(
    [switch]$VerifyOnly
)

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

function Sync-Directory {
    param([string]$Source, [string]$Dest)
    if (-not (Test-Path $Source)) { throw "Missing source: $Source" }
    if ($VerifyOnly) { return }
    if (Test-Path $Dest) { Remove-Item $Dest -Recurse -Force }
    New-Item -ItemType Directory -Path $Dest -Force | Out-Null
    Copy-Item -Path (Join-Path $Source '*') -Destination $Dest -Recurse -Force
}

function Convert-MdcToMd {
    param([string]$MdcPath, [string]$MdPath)
    $content = Get-Content $MdcPath -Raw
    if ($content -match '(?s)^---\r?\n.*?\r?\n---\r?\n') {
        $content = $content -replace '(?s)^---\r?\n.*?\r?\n---\r?\n', ''
    }
    $dir = Split-Path $MdPath -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    if (-not $VerifyOnly) {
        Set-Content -Path $MdPath -Value $content.TrimEnd() -Encoding UTF8
    }
}

function Write-ClineSkillStub {
    param([string]$SkillName, [string]$SkillDir)
    $skillMd = Join-Path $SkillDir 'SKILL.md'
    if (-not (Test-Path $skillMd)) { return }
    $body = Get-Content $skillMd -Raw
    if ($body -match '(?s)^---\r?\n(?<front>.*?)\r?\n---\r?\n(?<rest>.*)$') {
        $front = $Matches['front']
        $rest = $Matches['rest']
    } else {
        $front = "name: $SkillName`ndescription: See canonical SKILL.md"
        $rest = $body
    }
    $canonical = ".github/skills/$SkillName/SKILL.md"
    $stub = @"
---
$front
canonical: "$canonical"
---

$($rest.Trim())
"@
    $out = Join-Path $Root ".clinerules/skills/$SkillName.md"
    if (-not $VerifyOnly) {
        Set-Content -Path $out -Value $stub.TrimEnd() -Encoding UTF8
    }
}

$exitCode = 0

# --- Skills: .github -> .cursor, .opencode ---
Sync-Directory '.github/skills' '.cursor/skills'
Sync-Directory '.github/skills' '.opencode/skills'

# Remove legacy applied-engineering skill folders if present
foreach ($legacy in @('.cursor/skills/applied-engineering', '.opencode/skills/applied-engineering', '.github/skills/applied-engineering')) {
    if (Test-Path $legacy) {
        if (-not $VerifyOnly) { Remove-Item $legacy -Recurse -Force }
    }
}

# --- Agents ---
Sync-Directory '.github/agents' '.clinerules/agents'
Sync-Directory '.github/agents' '.opencode/agents'
$legacyAgent = '.clinerules/agents/content-quality-review.md'
if (Test-Path $legacyAgent) {
    if (-not $VerifyOnly) { Remove-Item $legacyAgent -Force }
}
$legacyAgent2 = '.opencode/agents/content-quality-review.md'
if (Test-Path $legacyAgent2) {
    if (-not $VerifyOnly) { Remove-Item $legacyAgent2 -Force }
}

# --- Rules: .cursor/rules/*.mdc -> .clinerules/rules, .opencode/rules ---
$mdcFiles = Get-ChildItem '.cursor/rules' -Filter '*.mdc'
foreach ($mdc in $mdcFiles) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($mdc.Name)
    $mdName = ($base -replace '_', '-') + '.md'
    $clineOut = Join-Path '.clinerules/rules' $mdName
    $opencodeOut = Join-Path '.opencode/rules' $mdName
    Convert-MdcToMd $mdc.FullName $clineOut
    Convert-MdcToMd $mdc.FullName $opencodeOut
}

# --- Cline skill stubs ---
Get-ChildItem '.github/skills' -Directory | ForEach-Object {
    Write-ClineSkillStub $_.Name $_.FullName
}
$legacyStub = '.clinerules/skills/applied-engineering.md'
if (Test-Path $legacyStub) {
    if (-not $VerifyOnly) { Remove-Item $legacyStub -Force }
}

# --- Verify skills parity ---
$gRoot = Join-Path $Root '.github/skills'
$cRoot = Join-Path $Root '.cursor/skills'
Get-ChildItem $gRoot -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring($gRoot.Length + 1)
    $c = Join-Path $cRoot $rel
    if (-not (Test-Path $c)) {
        Write-Host "MISSING in .cursor/skills: $rel"
        $exitCode = 1
    } elseif ((Get-FileHash $_.FullName -Algorithm SHA256).Hash -ne (Get-FileHash $c -Algorithm SHA256).Hash) {
        Write-Host "MISMATCH .github vs .cursor: $rel"
        $exitCode = 1
    }
}

$oRoot = Join-Path $Root '.opencode/skills'
Get-ChildItem $gRoot -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring($gRoot.Length + 1)
    $o = Join-Path $oRoot $rel
    if (-not (Test-Path $o)) {
        Write-Host "MISSING in .opencode/skills: $rel"
        $exitCode = 1
    } elseif ((Get-FileHash $_.FullName -Algorithm SHA256).Hash -ne (Get-FileHash $o -Algorithm SHA256).Hash) {
        Write-Host "MISMATCH .github vs .opencode: $rel"
        $exitCode = 1
    }
}

if ($VerifyOnly -and $exitCode -eq 0) {
    Write-Host 'All assistant mirrors verified.'
} elseif (-not $VerifyOnly) {
    Write-Host 'Assistant mirrors synced.'
}

exit $exitCode
