# Repository Structure

**Project**: Applied Engineering

## Primary layout

- `README.md` — repository overview and current structure
- `docs/` — shared documentation and diagrams
- `src/` — code, experiments, utilities, prototypes, or topic-oriented work
- `.github/`, `.cursor/`, `.claude/`, `.copilot/`, `.vscode/` — tooling and assistant configuration

## Working rule

Follow the local convention of the surface you are editing. If a subtree later
adopts a stricter bundle pattern, document it in `README.md` and related
assistant files before assuming it everywhere.

## Topic bundle numbering

Multi-file topic folders in the learning pipeline may use numbered content
files to express read order:

- `01-knowledge/ai-ml/mlops/` — example bundle with ordered notes
- `07-interview-prep/system-design/02-multi-tenant-saas-platform/` — phased design pack

Rules:

- Number only sequenced content files; keep each folder `README.md` unnumbered.
- Use two-digit prefixes in incremental learning order.
- Prefer `NN-kebab-case.md`; match an existing underscore style within the same subtree if already established.

## Imported material

1. Identify the intended destination in this repository
2. Rewrite the imported content to match local naming and scope
3. Remove stale references to the original repo
4. Validate links, file references, and workflow assumptions

## Guidance

- Do not hardcode nonexistent folder models into templates or prompts.
- Keep `README.md`, issue templates, prompts, and rules aligned with the actual repo state.
- Prefer flexible, explicit structure over copied conventions from another repository.

