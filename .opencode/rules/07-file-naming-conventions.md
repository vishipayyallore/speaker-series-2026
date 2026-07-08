# File Naming Conventions

## Talk folders

Format: `YYYY-MM-short-kebab-description`

Examples:

- `2026-01-python-l1-s5-mini-calculator`
- `2026-07-amazon-bedrock-cline-agentic`

Chronological prefix keeps folders sorted; suffix identifies the session.

## Talk files

| Talk type | Required files |
| --------- | -------------- |
| External index | `README.md` |
| In-repo demo | `README.md`, `agenda.md`, `demo-script.md`, `references.md`, `links.md` (+ optional `src/`, `prompts/`) |

## Shared assets

Name media to match talk id:

- `assets/slides/2026-07-amazon-bedrock-cline-agentic.pdf`
- `assets/recordings/2026-07-amazon-bedrock-cline-agentic.mp4`

## Prohibited

- Never use `00-` prefixes
- Do not add learning-pipeline stage folders (`01-knowledge/`, etc.)

## Templates

Copy from `templates/` when creating a new **in-repo** talk. Rename `talk-readme.md` → `README.md`.
