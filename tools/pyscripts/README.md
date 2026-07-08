# Python Tools

**Location**: `tools/pyscripts/`

These are small Python utilities for extracting/staging content and supporting my learning workflow.
They are designed to be run inside the repo's virtual environment.

## Shared module

### `_common.py`

Small helpers (for example `is_within` for path checks). Import from sibling scripts when useful.

### `task_check.py`

Portable repository-health summary for duplicate Markdown, notebook JSON parsing, `source-material/`
extension counts, and public references to `source-material/`.

```powershell
uv run python tools/pyscripts/task_check.py --json
```

## Tools

### `pdf_to_md.py`

Raw PDF → Markdown extraction (staging artifact). Uses **pypdf** by default; for image-only PDFs use `--ocr` or `--ocr-when-empty` (requires [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) on PATH).

```powershell
uv run python tools/pyscripts/pdf_to_md.py --input "source-material\livesessions" --recursive --output-same-folder

# Scanned / image-only PDFs (PyMuPDF + Tesseract @ 300 DPI):
uv run python tools/pyscripts/pdf_to_md.py --input "source-material\universitynotes\machine learning week 8-13.pdf" --output-same-folder --ocr

# Batch: OCR only when pypdf finds no text (used by Convert-SourceMaterialToMarkdown.ps1):
uv run python tools/pyscripts/pdf_to_md.py --input source-material --recursive --output-same-folder --ocr-when-empty
```

### `html_to_md.py`

Raw HTML slide deck → Markdown extraction (staging artifact). Targets self-contained decks
with `<!-- Slide N: title -->` markers (for example Session 1 reading notes saved from a browser).

```powershell
uv run python tools/pyscripts/html_to_md.py --input "source-material/week1/04-reading-notes/Session1-Introduction-to-Machine-Learning.html" --output-same-folder

# All HTML under source-material (recursive)
uv run python tools/pyscripts/html_to_md.py --input source-material --recursive --output-same-folder
```

### `pptx_to_md.py`

Raw PPTX → Markdown extraction (staging artifact). Optionally extracts embedded images.
Supports single files or batch conversion with `--recursive` and `--output-same-folder`.

```powershell
uv run python tools/pyscripts/pptx_to_md.py --input "C:\path\deck.pptx" --extract-images --include-notes

# All PPTX under source-material (recursive, colocated .md)
uv run python tools/pyscripts/pptx_to_md.py --input source-material --recursive --output-same-folder --allow-source-material-output
```

### `docx_to_md.py`

Raw DOCX/DOC → Markdown extraction (staging artifact).

- **`.docx`** — `python-docx`
- **`.doc`** — pandoc first; on Windows falls back to **Microsoft Word COM** when pandoc cannot read legacy DOC (Word must be installed)

```powershell
uv run python tools/pyscripts/docx_to_md.py --input "source-material\universitynotes\Machine Learning.docx" --output-same-folder

# All Word files under source-material (recursive)
uv run python tools/pyscripts/docx_to_md.py --input source-material --recursive --output-same-folder --allow-source-material-output
```

### Batch: all PDF, HTML, PPTX, and Word under `source-material/` (colocated `.md`)

From repo root (runs `pdf_to_md.py`, `html_to_md.py`, `pptx_to_md.py`, and `docx_to_md.py` via the PowerShell wrapper):

```powershell
.\tools\psscripts\Convert-SourceMaterialToMarkdown.ps1
```

Equivalent manual invocations:

```powershell
uv run python tools/pyscripts/pdf_to_md.py --input source-material --recursive --output-same-folder --allow-source-material-output --ocr-when-empty
uv run python tools/pyscripts/html_to_md.py --input source-material --recursive --output-same-folder --allow-source-material-output
uv run python tools/pyscripts/pptx_to_md.py --input source-material --recursive --output-same-folder --allow-source-material-output
uv run python tools/pyscripts/docx_to_md.py --input source-material --recursive --output-same-folder --allow-source-material-output
```

### `video_to_transcript.py`

Video/audio → Markdown transcript (OpenAI Whisper, local). Output by default in the same folder as the media file.

```powershell
# Single file
uv run python tools/pyscripts/video_to_transcript.py --input "path\to\video.mp4"

# All media under a folder (for example source-material)
uv run python tools/pyscripts/video_to_transcript.py --input "source-material" --recursive
```

Requires: `uv sync --extra transcript` (or `pip install openai-whisper`) and ffmpeg on PATH for video.

### `md_to_pdf_reportlab.py`

Generic Markdown (subset) → PDF via **ReportLab**. Use for notes or report exports that stay within the supported constructs (see the script docstring).

```powershell
uv run python tools/pyscripts/md_to_pdf_reportlab.py --input path/to/report.md --output path/to/out.pdf --title "Title" --author "Swamy PKV"
```

### `generate_hierarchical_notebook.py`

One-off generator for a from-scratch hierarchical clustering Jupyter notebook (writes JSON to stdout or a target path). Use when scaffolding a future week notebook; edit the emitted notebook before publishing under `src/weekN/03-notebooks/`.

```powershell
uv run python tools/pyscripts/generate_hierarchical_notebook.py > src/weekN/03-notebooks/NN-hierarchical-clustering-implementation.ipynb
```

Review and adapt cell content to match the active week topic index before committing.

### `fix_quiz_code_fences.py`

One-off maintenance: fixes quiz/discussion Markdown where closing code fences were written as ` ```text ` instead of ` ``` `.

```powershell
uv run python tools/pyscripts/fix_quiz_code_fences.py
```

Scans active `src/week1`–`week13` quiz and discussion folders.
