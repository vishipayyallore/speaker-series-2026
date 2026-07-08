---
name: applied-engineering
description: Work on the applied-engineering repository — practical notes,
license: MIT
compatibility: opencode
---

# Applied Engineering

**Scope:** Applied Engineering workspace. See `README.md` and
`.cursor/rules/project-scope.mdc`.

**Core role:** Same single stance repo-wide — Senior Software Engineer and
Systems Architect with a pragmatic engineering focus. Full wording:
`.cursor/rules/09_core-agent-role.mdc` and `.github/copilot-instructions.md`.

## Layout

Use the current repository layout and local conventions as the source of truth.

- **Shared docs:** `docs/`
- **Code and examples:** `src/`
- **Assistant and workflow config:** `.github/`, `.cursor/`, `.claude/`, `.copilot/`, `.vscode/`
- **Read-only staging:** `source-material/` (imports) and `.archive/` (drafts and
  migration sources — excluded from documentation CI). See
  `.cursor/rules/06_source_material_rules.mdc` for migration status.

Do not invent a rigid folder model unless the repository actually adopts one.

## Numbered topic bundles

When a folder holds multiple sequenced learning notes:

- Prefix content files with `01-`, `02-`, … in **incremental learning order**.
- Keep `README.md` unnumbered; list ordered notes there (`Read in order:`).
- Update README links and sibling cross-links when adding or renumbering files.
- Full rules: `.cursor/rules/07_file-naming-conventions.mdc`.

## When editing

- **Repo fit:** Rewrite imported material so it matches this project.
- **Accuracy:** Keep README, prompts, templates, and workflows aligned.
- **Simplicity:** Prefer small, coherent updates over broad speculative scaffolding.

## Related

- **Local CI commands:** `.github/skills/ci-checks/SKILL.md`
- **Canonical assistant rules:** `.github/copilot-instructions.md`
