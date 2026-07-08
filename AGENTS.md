# Agent instructions (index)

This repository is an Applied Engineering workspace for practical notes,
experiments, documentation, automation, and reference implementations.

## Read first

1. `README.md` — repo purpose and current structure.
2. `CLAUDE.md` — repo-level assistant entry point and key policies.
3. `.github/copilot-instructions.md` — canonical assistant rules for this repository.
4. `.cursor/rules/project-scope.mdc` — repository scope and anti-contamination rules.
5. `.cursor/rules/09_core-agent-role.mdc` — primary engineering stance for agent work.

If these documents conflict, follow this order of precedence: 1) `.github/copilot-instructions.md`, 2) `CLAUDE.md`, 3) `.cursor/rules/*`, 4) `README.md`.

If any referenced file cannot be read, proceed using the remaining available documents and explicitly note which guidance files were unavailable.

## Claude-specific emphasis

- `.claude/CLAUDE.md` — style and output habits for explanations and documentation.
- `.claude/config.md` — preferred sequencing for technical explanations.

## Repository structure

This repository uses a **numbered learning pipeline** (01–07) for all content
artifacts, alongside unnumbered infrastructure folders:

```text
01-knowledge → 02-patterns → 03-labs → 04-projects →
05-playbooks → 06-research → 07-interview-prep
```

Supporting folders (`docs/`, `assets/`, `templates/`, `scripts/`, `tools/`,
`sandbox/`, `src/`) are outside the pipeline. See `docs/01-folder-structure.md`
for the full layout and intent.

If new content does not clearly fit a pipeline stage or supporting folder, place it in `sandbox/` and ask the user to confirm the final destination.

## Source material

`source-material/` is optional read-only staging for imported raw content (gitignored
locally). Read from it; synthesize into pipeline folders; never edit source files.
See `.cursor/rules/06_source_material_rules.mdc` for the migration workflow and
status table.

## Numbered files inside topic folders

When a folder contains multiple sequenced learning notes, prefix content files
with two-digit order in incremental learning sequence (`01-topic.md`,
`02-topic.md`, …). Keep each folder `README.md` unnumbered and use it as the
ordered index. See `.cursor/rules/07_file-naming-conventions.mdc`.

- Always make edits in `.github/skills/`; `.cursor/skills/` is an auto-generated mirror and must not be edited directly. If they diverge, treat `.github/skills/` as the source of truth. If asked to edit `.cursor/skills/`, redirect the change to `.github/skills/` and explain that `.cursor/skills/` is a mirror.
- Bundled skills: `applied-engineering`, `ci-checks`, `workspace-review` (see `.github/skills/README.md`).

## Prompts

- `.github/prompts/` contains repo-specific task and audit prompts.

## Subagents

Canonical subagent definitions live in `.github/agents/`:

| Agent | Use when |
| --- | --- |
| `content-quality-review` | Auditing pipeline teaching content |
| `agent-ci-verify` | After code, docs, or governance edits |
| `docs-originality-review` | Spot-checking doc rewrites for fit and synthesis |

`.clinerules/agents/` and `.opencode/agents/` mirror these definitions for
non-Cursor assistants.

## Assistant mirrors (optional)

- `.clinerules/` — Cline-facing mirror of `.cursor/rules/`, `.github/skills/`, and `.github/agents/`
- `.opencode/` — OpenCode plugin mirror of the same canonical sources

Edit canonical paths (`.github/`, `.cursor/`) first, then resync mirrors.
