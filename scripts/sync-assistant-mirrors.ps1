<#
.SYNOPSIS
  Backward-compatibility wrapper for assistant mirror sync.

.DESCRIPTION
  Canonical implementation: tools/psscripts/sync-assistant-mirrors.ps1
  Prefer the tools path in new docs and automation; this shim keeps older
  references working.

.EXAMPLE
  ./scripts/sync-assistant-mirrors.ps1 -VerifyOnly
#>

[CmdletBinding()]
param(
    [switch]$VerifyOnly
)

$ErrorActionPreference = 'Stop'

$canonical = Join-Path $PSScriptRoot '..\tools\psscripts\sync-assistant-mirrors.ps1'
if (-not (Test-Path -LiteralPath $canonical)) {
    throw "Missing canonical script: $canonical"
}

& $canonical @PSBoundParameters
exit $LASTEXITCODE
