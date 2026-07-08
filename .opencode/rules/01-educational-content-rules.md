# Documentation and Content Rules

**Context**: Repository docs, notes, prompts, and supporting content
**Priority**: HIGH

---

## Core Principles

### Repository Fit

- Rewrite imported material so it matches this repository's scope.
- Remove stale repo names, URLs, labels, and structure assumptions.
- Prefer original wording over pasted or lightly edited content.

### Clarity and Structure

- Explain the purpose of a file or change before deep detail.
- Keep headings, examples, and references easy to scan.
- Use diagrams or examples when they make the change clearer.

### Plain English or worked example (knowledge and interview content)

Apply this standard to content in `01-knowledge/`, `02-patterns/`, and `07-interview-prep/`:

- **Minimum**: For each concept, provide at least one of **(A)** a plain-English explanation or **(B)** a concrete worked example.
- **Beginner-friendly default**: Simple wording first, technical precision second. Define specialist terms on first use.
- **Layman explanation**: Everyday language before formal definitions, notation, or industry jargon.
- **Business use case**: Connect each concept to at least one realistic engineering problem or scenario it solves.
- **Formulas and notation**: Do not leave notation unexplained — add a plain-English line and a numeric walkthrough alongside any formal expression.

### Technical Content

- Comments should explain non-obvious intent, coupling, or tradeoffs.
- Examples should be runnable or clearly marked as illustrative.
- Keep commands and paths portable where practical.

## Voice and Tone

- Keep the tone practical and repository-specific.
- Do not rewrite repository docs as generic marketing copy.
- Prefer direct engineering language over academic or course framing.

## Repository Surfaces

- `README.md` for repository-level scope and navigation
- `docs/` for shared documentation assets
- `src/` for code, examples, experiments, and implementation-oriented material
- assistant config under `.github/`, `.cursor/`, `.claude/`, `.copilot/`, and `.vscode/`

## Numbered topic bundles

When a folder contains multiple sequenced learning notes:

- Prefix content files with two-digit order: `01-topic-name.md`, `02-topic-name.md`, …
- Leave `README.md` unnumbered; use it as the ordered index (`Read in order:`).
- Number by incremental learning order, not alphabetical or creation order.
- Update sibling cross-links and the folder README when renumbering.

See `.cursor/rules/07_file-naming-conventions.mdc` for full rules.

## Markdown Standards

- Use H2 (`##`) for main topics, H3 (`###`) for subtopics.
- Use blockquotes (`>`) for concise callouts when useful.
- Use tables when they genuinely improve scanability.
- **Diagrams**: Prefer Mermaid for visual explanations; follow every Mermaid block with an ASCII text fallback for environments that do not render it.
