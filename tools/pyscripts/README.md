# Python Tools

**Location**: `tools/pyscripts/`  
**Repo**: Speaker Series 2026

Small Python utilities for repository maintenance and optional speaker assets (recordings,
slide conversion). Run from repo root with your virtual environment active.

---

## Repository maintenance

| Script | Purpose |
| ------ | ------- |
| `task_check.py` | Duplicate markdown, notebook JSON sanity, reference scan |
| `sync_clinerules_from_canonical.py` | Regenerate `.clinerules/` from canonical sources |
| `sync_opencode_from_canonical.py` | Regenerate `.opencode/` from canonical sources |
| `verify_clinerules_parity.py` | Compare Cline mirror to canonical |
| `verify_opencode_parity.py` | Compare OpenCode mirror to canonical |
| `sync_clinerules_skills.py` | Cline skill stub sync helper |

```powershell
python tools/pyscripts/task_check.py --json
python tools/pyscripts/verify_clinerules_parity.py
python tools/pyscripts/verify_opencode_parity.py
```

Prefer **`tools/psscripts/sync-assistant-mirrors.ps1`** for day-to-day mirror sync on Windows.

`sync_clinerules_from_canonical.py` and `sync_opencode_from_canonical.py` are **legacy**
imports from another repository — do not use them here. Use the PowerShell script above.

---

## Optional — speaker assets

Use when processing recordings or imported decks (output typically under `assets/`).

| Script | Purpose |
| ------ | ------- |
| `video_to_transcript.py` | Video → transcript markdown |
| `pptx_to_md.py` | PowerPoint → markdown |
| `pdf_to_md.py` | PDF → markdown |
| `md_to_pdf_reportlab.py` | Markdown → PDF handout |

Example:

```powershell
python tools/pyscripts/video_to_transcript.py --input "assets/recordings/session.mp4"
```

---

## Legacy / optional staging

These target an optional gitignored `source-material/` folder (not part of the default
speaker-series workflow):

- `html_to_md.py`, `docx_to_md.py`, `Convert-SourceMaterialToMarkdown.ps1` (PowerShell wrapper)
- `generate_hierarchical_notebook.py`, `fix_quiz_code_fences.py`, `generate_source_material_coverage.py`

Keep them for reuse if you add a staging folder; they are not required for talk indexing.

---

## Shared module

`_common.py` — path helpers used by sibling scripts.
