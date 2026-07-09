---
name: speaker-series
description: Work on the speaker-series-2026 repository — speaker portfolio, talk indexing, meetup delivery docs, in-repo demos, and assistant configuration.
canonical: ".github/skills/speaker-series/SKILL.md"
---

# Speaker Series 2026

**Scope:** Speaker portfolio for Dot Net Learners House. See `README.md` and
`.cursor/rules/project-scope.mdc`.

**Core role:** Senior Software Engineer and Systems Architect — see
`.cursor/rules/09_core-agent-role.mdc` and `.github/copilot-instructions.md`.

## Layout

- **`talks/`** — one folder per session (`NN-short-description`); in-repo demo code under `talks/{id}/src/`
- **`assets/`** — slides, diagrams, images, recordings
- **`templates/`** — scaffold for new in-repo talks
- **`docs/`** — cross-talk reference
- **`tools/`** — repo maintenance scripts

## Talk types

| Type | Example | Files in `talks/{id}/` |
| ---- | ------- | ------------------------ |
| External curriculum | Python L1 · S5, S6 | `README.md` only (links out) |
| In-repo demo | Bedrock + Cline | Full template set + `src/`, `prompts/`, etc. |

External Python curriculum:
[python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice)

## When editing

- **Portfolio:** keep root README talk table, upcoming, and completed sections current
- **No duplication:** do not copy session docs or lab code from the Python repo
- **Parity:** after governance edits, run `tools/psscripts/sync-assistant-mirrors.ps1`
- **Contamination:** remove Applied Engineering / learning-pipeline references

## Related

- **CI:** `.github/skills/ci-checks/SKILL.md`
- **Audit:** `.github/skills/workspace-review/SKILL.md`
- **Canonical rules:** `.github/copilot-instructions.md`