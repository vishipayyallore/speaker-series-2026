# Primary Directives

**Professional stance:** Use the single core role in
`09_core-agent-role.mdc` (senior software engineer and architect) for work in
this repository.

## Project Focus

This is an applied engineering workspace that:

- documents practical implementation ideas clearly
- keeps repository guidance accurate and project-specific
- supports lightweight code, automation, and reference material across
  repo-owned content areas such as `docs/`, `01-knowledge/`, `03-labs/`,
  `04-projects/`, and `src/`
- removes imported assumptions that do not belong here

### Working philosophy

- **Pragmatic first**: Prefer useful, maintainable structure over theoretical completeness.
- **Keep it local**: Follow the convention of the touched area instead of forcing a repo-wide pattern.
- **Document intent**: Update docs when structure, behavior, or workflow meaning changes.
- **Beginner friendly**: Default to beginner-friendly explanations for knowledge and interview prep content before adding technical depth.
- **Business grounded**: Connect concepts to realistic engineering problems, not just abstract theory.
- **Layman explanation**: Everyday language before formal definitions in knowledge-oriented content.
- **Equations**: Pair every display-math block with a plain-English line and a numeric walkthrough.

## Current State

- ✅ Documentation-first repository with assistant and CI configuration
- ✅ Optional Python and Node.js tooling where useful
- ✅ `docs/`, `07-interview-prep/`, `01-knowledge/`, `03-labs/`,
  `04-projects/`, and `src/` are active content surfaces today
- ❌ NOT a clone of the imported source repository

## Documentation Accuracy

- README and templates must accurately describe this repository.
- Prompts, issue templates, and rules must point to the correct repo and paths.
- Comments should explain the *why* of a design or implementation decision when it is not obvious.

## Code Maintenance

- Keep reusable logic in `src/` when code belongs in the repository.
- Keep CI and local tasks aligned with tracked files and existing tooling.
- Prefer small, coherent changes over sweeping imported scaffolding.

