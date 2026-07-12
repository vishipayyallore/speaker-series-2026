# Repository Structure

**Project:** Speaker Series 2026

## Primary layout

```text
talks/        — per-session metadata and talk-specific demo code
assets/       — slides, diagrams, images, recordings
templates/    — copy before each new in-repo talk
docs/         — speaker profile, FAQ, roadmap, folder layout
tools/        — repo maintenance scripts (CI, mirror sync)
.github/ …    — assistant and CI configuration
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

Optional local staging folder `source-material/` (if used during imports) is **not** tracked in
git. Migrate transformed content into `talks/`, `docs/`, or `templates/` and delete the staging
copy. The legacy rule name was `06-source-material-rules`; the current rule is
`06_external_curriculum_rules.mdc`.

## Guidance

- Keep `README.md`, `docs/01-folder-structure.md`, and assistant files aligned
- Do not add `01-knowledge/` … `07-interview-prep/` pipeline folders