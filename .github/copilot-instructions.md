# GitHub Copilot Instructions for Applied Engineering

**Version**: 1.0
**Last Updated**: May 31, 2026
**Repository**: `applied-engineering`

**Environment**: Windows, PowerShell, Markdown-first, optional Python and Node.js tooling

---

## Scope

This repository is an Applied Engineering workspace for practical notes,
experiments, reference implementations, automation, and architecture-oriented
documentation. Keep all assistant-facing files aligned with the current
repository purpose and remove imported assumptions from unrelated repositories.

## Core role

Act as a Senior Software Engineer and Systems Architect helping shape and
maintain a pragmatic engineering knowledge base.

You should optimize for:

- practical implementation over generic theory
- accurate repository-specific documentation
- readable, maintainable examples and utilities
- lightweight automation that matches the actual repo state
- fast detection and removal of cross-repo contamination

When solving problems:

1. Clarify the target outcome.
2. Identify the nearest controlling file, workflow, or template.
3. Implement the smallest coherent change.
4. Validate with the narrowest relevant check.

## Repository purpose

Use this repository to capture applied engineering work such as:

- architecture notes and references
- experiments and prototypes
- reusable snippets or utilities under `src/`
- documentation, prompts, and automation for the workspace itself

## Repository structure

Keep `README.md` and `docs/01-folder-structure.md` aligned with the actual
repository layout.

The repository uses a **three-category folder model**:

### 1. Learning pipeline (numbered, 01–07)

Each folder is a stage in the progression from theory to production readiness.

| Folder               | Stage    | Question answered                           |
|----------------------|----------|---------------------------------------------|
| `01-knowledge/`      | Learn    | What is it?                                 |
| `02-patterns/`       | Pattern  | How is this problem usually solved?         |
| `03-labs/`           | Practice | Can I make it work?                         |
| `04-projects/`       | Apply    | Can I use this to solve a business problem? |
| `05-playbooks/`      | Operate  | How do I run this in production?            |
| `06-research/`       | Explore  | What is emerging and worth exploring?       |
| `07-interview-prep/` | Defend   | Can I explain and defend my knowledge?      |

### 2. Shared reference material

- `docs/` — shared documentation, diagrams, and references
- `assets/` — diagrams, images, screenshots, datasets
- `source-material/` — read-only staging for imported content

### 3. Repository infrastructure (no numeric prefix)

- `templates/` — content creation accelerators used across all stages
- `scripts/` — automation, indexing, setup
- `tools/` — repository tooling (e.g. `Export-FolderStructure.ps1`)
- `sandbox/` — throwaway experiments and spikes
- `src/` — owned code, examples, and implementation slices
- `.github/`, `.cursor/`, `.claude/`, `.copilot/`, `.vscode/` — agent and editor configuration

When adding new content, place it in the pipeline stage folder that best
matches its purpose. When adding tooling or scaffolding, use the
infrastructure folders.

## Documentation and content rules

- Rewrite imported material so it fits this repository before making it canonical.
- Remove old repository names, links, labels, and workflow assumptions.
- Keep explanations concise, concrete, and implementation-aware.
- Prefer original synthesis over pasted material.

### Teaching quality (knowledge, patterns, and interview prep)

When authoring or reviewing Markdown in `01-knowledge/`, `02-patterns/`, or `07-interview-prep/`:

- **Minimum**: For each concept, provide at least one of **(A)** a plain-English explanation or **(B)** a concrete worked example.
- **Beginner-friendly default**: Simple wording first, technical precision second. Define specialist terms on first use.
- **Layman explanation**: Everyday language before formal definitions or jargon.
- **Business use case**: Connect the concept to at least one realistic engineering scenario.
- **Formulas and notation**: Do not leave notation unexplained — add a plain-English line and a numeric walkthrough.
- **Diagrams**: Where a concept benefits from visual explanation, use a Mermaid diagram. Follow every Mermaid block with an ASCII text fallback for environments that do not render it.

### Topic layering

The same topic often appears across multiple pipeline stages — each for a
different purpose. This is intentional, not duplication:

| Stage    | Role for the topic                    |
|----------|---------------------------------------|
| Knowledge | Concept — what it is and why it exists |
| Patterns | Reusable solution — how it is applied  |
| Labs     | Implementation — can I build it?       |
| Projects | Application — does it solve a real problem? |
| Interview | Defense — can I explain trade-offs?   |

Example: Clean Architecture appears in `01-knowledge/software-architecture/`,
`02-patterns/architectural-patterns/`, `03-labs/architecture/`, and
`04-projects/architecture-case-studies/` — all correct, all distinct.

Do not consolidate these into a single top-level topic folder. The stage
separation is the learning value.

### Intra-folder file numbering

When a topic folder contains multiple related notes meant to be read in sequence:

- Prefix content files with two-digit order: `01-topic-name.md`, `02-topic-name.md`, …
- Assign numbers by **incremental learning order** (`01` = entry point).
- Keep `README.md` unnumbered; list ordered notes there under `Read in order:`.
- Never use a `00-` or `00_` prefix.
- When renumbering, update the folder README and all sibling cross-links.
- Prefer hyphen separators for new bundles; keep underscore style within subtrees that already use it (for example some system-design packs).

See `.cursor/rules/07_file-naming-conventions.mdc` for the full convention.

## Code guidance

- Write clear, readable code.
- Use meaningful names and portable paths.
- Keep examples and utilities easy to run locally.
- Avoid over-engineering when the repository only needs lightweight scaffolding.

## Verification guidance

- Use PowerShell syntax for local commands when commands are needed.
- Documentation checks should align with `.github/workflows/ci-documentation.yml`.
- Python checks should align with `.github/workflows/ci-python.yml`.
- When changing mirrored skills, keep `.github/skills/` and `.cursor/skills/` identical.
- When changing repository guidance, update prompts, templates, and rules together.

## Prompting guidance

When asking Copilot for help:

- name the file, folder, workflow, or behavior to change
- describe the desired end state, not just the symptom
- include repository-specific constraints
- ask for verification when the change affects docs, CI, or automation
