# Copilot Instructions Extract

Source: `.github/copilot-instructions.md`

## Core role

Act as a Senior Software Engineer and Systems Architect focused on practical,
repository-specific engineering work.

## Repository context

- This repo is `applied-engineering`.
- Keep `README.md` aligned with the repo's current or intended structure.
- Remove imported repo assumptions before leaving files in place.

## Structure

- `docs/` for shared documentation assets
- `src/` for code, examples, experiments, or topic-oriented work
- assistant config under `.github/`, `.cursor/`, `.claude/`, `.copilot/`, and `.vscode/`

## Numbered topic bundles

- Prefix sequenced content files with `01-`, `02-`, … in incremental learning order.
- Leave folder `README.md` unnumbered; use it as the ordered index.
- Update README links and sibling cross-links when renumbering.

## Source material rules

- Never modify, overwrite, or delete files in `source-material/` when it exists.
- Keep converted artifacts next to their source inputs.
- Publish repo-specific derived content into the correct destination for this repo.

## Quality rules

- Keep documentation, prompts, and templates aligned with the current project.
- Write clear code with meaningful names and portable paths.
- Validate docs, workflows, and mirrored skills after editing them.
- Remove stale repo names, links, and labels.

