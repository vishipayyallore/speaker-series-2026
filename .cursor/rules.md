# Role: Applied engineering implementation assistant

**Scope:** This file supplements always-applied Cursor rules under
`.cursor/rules/*.mdc`, especially `project-scope.mdc`,
`09_core-agent-role.mdc`, `01_educational-content-rules.mdc`, and
`05_primary-directives.mdc`.

## Context

This repository organizes content in a **three-category folder model**:

**Learning pipeline** (01–07) — place new knowledge, patterns, labs, projects,
playbooks, research, and interview prep in the matching numbered stage folder.

| Folder               | Stage    |
|----------------------|----------|
| `01-knowledge/`      | Learn    |
| `02-patterns/`       | Pattern  |
| `03-labs/`           | Practice |
| `04-projects/`       | Apply    |
| `05-playbooks/`      | Operate  |
| `06-research/`       | Explore  |
| `07-interview-prep/` | Defend   |

**Shared reference:** `docs/`, `assets/`

**Repository infrastructure** (no numeric prefix): `templates/`, `scripts/`,
`tools/`, `sandbox/`, `src/`, and the hidden config folders (`.github/`,
`.cursor/`, `.claude/`, `.copilot/`, `.vscode/`)

**Intra-folder numbering:** Inside topic bundles with sequenced notes, prefix
content files with `01-`, `02-`, … in incremental learning order. Leave folder
`README.md` unnumbered. See `.cursor/rules/07_file-naming-conventions.mdc`.

## Coding rules

1. Prefer the local convention of the area you are editing.
2. Keep utilities and examples readable before making them abstract.
3. Handle invalid inputs when writing reusable code.
4. Use relative or portable paths instead of hardcoded machine-specific paths.

## Anti-patterns

- Imported structure assumptions that do not match this repository
- Hardcoded absolute paths
- Boilerplate abstractions without a real caller or use case

## Quality gate

Before finishing a change that touches docs, code, or automation, align with
`.cursor/skills/ci-checks/SKILL.md` and the workflow files under
`.github/workflows/`.
