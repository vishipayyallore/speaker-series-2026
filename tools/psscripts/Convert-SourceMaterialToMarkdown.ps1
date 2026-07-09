# Convert PDF, HTML, PPTX, and Word files under source-material/ to Markdown
# in the same folder as each source file.
# Requires: uv sync (pypdf, python-pptx, python-docx), run from repo root.
# Legacy .doc files also require pandoc on PATH (Word COM fallback on Windows).
# Usage (from repo root): .\tools\psscripts\Convert-SourceMaterialToMarkdown.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Push-Location $repoRoot

try {
    uv run python tools/pyscripts/pdf_to_md.py --input "source-material" --recursive --output-same-folder --allow-source-material-output --ocr-when-empty
    uv run python tools/pyscripts/html_to_md.py --input "source-material" --recursive --output-same-folder --allow-source-material-output
    uv run python tools/pyscripts/pptx_to_md.py --input "source-material" --recursive --output-same-folder --allow-source-material-output
    uv run python tools/pyscripts/docx_to_md.py --input "source-material" --recursive --output-same-folder --allow-source-material-output
} finally {
    Pop-Location
}
