# Repository Structure

**Project:** Speaker Series 2026

## Primary layout

```text
talks/        â€” per-session metadata and talk-specific demo code
assets/       â€” slides, diagrams, images, recordings
templates/    â€” copy before each new in-repo talk
docs/         â€” speaker profile, FAQ, roadmap, folder layout
src/          â€” optional repo-wide utilities only
.github/ â€¦    â€” assistant and CI configuration
```

## Working rule

Follow the convention of the surface you edit:

- **External Python talks:** thin `README.md` linking out
- **In-repo demos:** self-contained under `talks/{id}/`
- **Shared media:** `assets/`, not scattered in talk folders

## Imported material

1. Identify whether content belongs in this repo or the external Python repo
2. Rewrite imported assistant config to match speaker-series scope
3. Remove stale repo names, URLs, and folder models
4. Run `tools/psscripts/sync-assistant-mirrors.ps1` after governance edits

## Guidance

- Keep `README.md`, `docs/01-folder-structure.md`, and assistant files aligned
- Do not add `01-knowledge/` â€¦ `07-interview-prep/` pipeline folders
