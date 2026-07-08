# Project scope

This repository is **Speaker Series 2026** â€” a speaker portfolio and canonical index for meetup sessions (Dot Net Learners House and related events).

1. Keep repository guidance, links, labels, and folder references specific to `speaker-series-2026`.
2. Remove imported assumptions from unrelated repos (for example Applied Engineering learning pipeline `01-knowledge/` â€¦ `07-interview-prep/`) before treating files as canonical here.
3. Do not describe this repository as a general-purpose engineering notebook unless it actually evolves in that direction.

## Do

- Keep `README.md` as the speaker portfolio index (talk table, upcoming/completed, links).
- Separate **talk metadata** (`talks/`) from **shared media** (`assets/`).
- Link to external repos for Python labs; do not duplicate that code here.
- Keep Bedrock and other original demos self-contained under the relevant `talks/{id}/` folder.

## Folder model

```text
talks/       â€” per-session metadata, scripts, and talk-specific demo code
assets/      â€” slides, diagrams, images, recordings
templates/   â€” copy before each new talk
docs/        â€” cross-talk reference (profile, FAQ, roadmap)
src/         â€” optional repo-wide utilities only (not per-talk demos)
```

Talk folders use chronological prefixes: `2026-07-04-python-l1-s5-mini-calculator`, `2026-07-11-amazon-bedrock-cline-agentic`, etc.

Do not add numeric learning-pipeline stage folders (`01-knowledge/`, etc.) unless the repository purpose explicitly changes.
