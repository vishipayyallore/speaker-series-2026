# Talk and portfolio content rules

**Context:** Talk folders, templates, portfolio docs  
**Priority:** HIGH

## Core principles

### Repository fit

- This is a speaker portfolio — not a general learning pipeline.
- Remove stale references to Applied Engineering, `01-knowledge/`, or unrelated repos.
- Python curriculum stays in [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice).

### Talk doc depth

| Talk type | Minimum files |
| --------- | ------------- |
| External curriculum (Python) | `README.md` with links to session doc + code |
| In-repo demo (Bedrock, etc.) | Full template set from `templates/` |

### Clarity

- Attendees should find agenda, demo, code, and links within one click from root README.
- Use tables for link lists and talk indexes.
- Keep demo scripts actionable (checklists, commands, fallback plans).

### Markdown

- H2 for main sections; tables when they improve scanning.
- Mermaid optional; include ASCII fallback when used.

## Surfaces

- Root `README.md` — portfolio index
- `talks/{id}/` — per-session content
- `templates/` — new talk scaffolding
- `docs/` — cross-talk reference