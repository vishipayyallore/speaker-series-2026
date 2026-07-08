# Repository Structure

This document describes the current folder layout for Speaker Series 2026 and how each area is intended to be used.

## Current Layout

```text
speaker-series-2026/
|-- .claude/
|-- .clinerules/
|-- .copilot/
|-- .cursor/
|-- .github/
|-- .opencode/
|-- docs/
|   |-- 01-repository-structure.md
|   `-- images/
|-- src/
|-- talks/
|-- templates/
|-- AGENTS.md
|-- CLAUDE.md
|-- LICENSE
|-- README.md
`-- lychee.toml
```

## Folder Purpose

- `.github/`: CI workflows, repository automation, and GitHub-related configuration.
- `.copilot/`, `.cursor/`, `.claude/`, `.clinerules/`, `.opencode/`: AI assistant and editor guidance files.
- `docs/`: supporting documentation for repository operations and planning.
- `docs/images/`: reusable image assets for documentation.
- `src/`: shared repo-wide utilities only; talk-specific demo code belongs under `talks/{id}/src/`.
- `talks/`: speaker-session content and talk-specific working files.
- `templates/`: reusable templates for planning and content creation.

## Maintenance Notes

- Keep this file updated when top-level folders are added, removed, or renamed.
- Prefer concise, purpose-driven folder names.
- Place new files where they are easiest to discover by purpose, not by author.
