# Python Tools

**Location**: `tools/pyscripts/`  
**Repo**: Speaker Series 2026

Small Python utilities for repository maintenance and optional speaker assets (recordings,
slide conversion). Run from repo root with your virtual environment active.

---

## Repository maintenance

| Script | Purpose |
| ------ | ------- |
| `task_check.py` | Duplicate markdown and notebook JSON sanity checks |
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

### Deprecated (import residue — do not run)

| Script | Reason |
| ------ | ------ |
| `fix_quiz_code_fences.py` | Expects `src/weekN/` quiz paths from Applied Engineering |
| `generate_hierarchical_notebook.py` | ML notebook generator unrelated to speaker portfolio |

---

## Optional — speaker assets

Use when producing portable handouts for talks.

| Script | Purpose |
| ------ | ------- |
| `md_to_pdf_reportlab.py` | Markdown → PDF handout |

Example:

```powershell
python tools/pyscripts/md_to_pdf_reportlab.py --input README.md --output assets/slides/speaker-series-overview.pdf
```

---

## Shared module

`_common.py` — path helpers used by sibling scripts.
