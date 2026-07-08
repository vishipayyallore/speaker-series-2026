# File Naming Conventions

## Talk folders

Format: `YYYY-MM-DD-short-kebab-description`

Examples:

- `2026-07-04-python-l1-s5-mini-calculator`
- `2026-07-08-python-l1-s6-loops`
- `2026-07-11-amazon-bedrock-cline-agentic`

Use the **delivery date** in the prefix so folders sort chronologically; suffix identifies the session.

## Talk files

| Talk type | Required files |
| --------- | -------------- |
| External index | `README.md` |
| In-repo demo | `README.md`, `agenda.md`, `demo-script.md`, `references.md`, `links.md` (+ optional `src/`, `prompts/`) |

## Shared assets

Name media to match talk id:

- `assets/slides/2026-07-11-amazon-bedrock-cline-agentic.pdf`
- `assets/recordings/2026-07-11-amazon-bedrock-cline-agentic.mp4`

## Prohibited

- Never use `00-` prefixes
- Do not add learning-pipeline stage folders (`01-knowledge/`, etc.)

## Templates

Copy from `templates/` when creating a new **in-repo** talk. Rename `talk-readme.md` â†’ `README.md`.
