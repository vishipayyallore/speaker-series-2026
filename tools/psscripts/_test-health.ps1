Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$config = Import-PowerShellDataFile -Path (Join-Path $PSScriptRoot 'RepoConfig.psd1')
Write-Host "Config keys: $($config.Keys -join ', ')"
$expectedFolders = @()
if ($config.ContainsKey('ExpectedFolders') -and $null -ne $config['ExpectedFolders']) {
    $expectedFolders = @($config['ExpectedFolders'])
}
Write-Host "Count: $($expectedFolders.Count)"
foreach ($folder in $expectedFolders) {
    Write-Host "  $folder"
}
