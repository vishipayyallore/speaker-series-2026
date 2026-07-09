# File Naming Conventions

## Talk folders

Format: `NN-short-kebab-description` (zero-padded sequence in delivery order)

Examples:

- `01-l1-s5-mini-calculator-in-python`
- `02-l1-s6-python-loops`
- `03-amazon-bedrock-cline-agentic`

Use the **two-digit prefix** so folders sort in event order. Include session codes
(`l1-s5`, `l1-s6`) for Python curriculum talks. Record the delivery date in each talk
`README.md` and the root portfolio table — not in the folder name.

## Talk files

| Talk type | Required files |
| --------- | -------------- |
| External index | `README.md` |
| In-repo demo | `README.md`, `agenda.md`, `demo-script.md`, `references.md`, `links.md` (+ optional `src/`, `prompts/`) |

## Shared assets

Name media to match talk folder id:

- `assets/slides/03-amazon-bedrock-cline-agentic.pdf`
- `assets/recordings/03-amazon-bedrock-cline-agentic.mp4`

## Prohibited

- Never use `00-` prefixes
- Do not add learning-pipeline stage folders (`01-knowledge/`, etc.)

## Templates

Copy from `templates/` when creating a new **in-repo** talk. Rename `talk-readme.md` → `README.md`.