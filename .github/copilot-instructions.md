# GitHub Copilot Instructions — Speaker Series 2026

**Version**: 1.0  
**Last Updated**: July 8, 2026  
**Repository**: `speaker-series-2026`

**Environment**: Windows, PowerShell, Markdown-first, optional Python (Bedrock demos)

---

## Scope

This repository is a **speaker portfolio and talk index** for Dot Net Learners House
and related meetups. It centralizes talk metadata, delivery notes, in-repo demo code
(for example AWS Bedrock + Cline), and links to external curriculum
([python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice)).

Remove imported assumptions from unrelated repositories (for example Applied
Engineering, learning pipeline `01-knowledge/` … `07-interview-prep/`).

## Core role

Act as a Senior Software Engineer and Systems Architect helping maintain a clear
speaker portfolio and reproducible talk assets.

Optimize for:

- accurate talk indexing and portfolio README
- minimal duplication of external curriculum
- self-contained in-repo demos under `talks/{id}/`
- assistant mirror parity across `.github/`, `.cursor/`, `.claude/`, `.clinerules/`, `.opencode/`, `.copilot/`
- fast detection of cross-repo contamination

When solving problems:

1. Clarify the target outcome and owning surface (`talks/`, `assets/`, `docs/`, assistant config).
2. Identify the nearest controlling file or template.
3. Implement the smallest coherent change.
4. Validate with the narrowest relevant check.

## Repository structure

Keep `README.md` and `docs/01-folder-structure.md` aligned with the actual layout.

```text
speaker-series-2026/
├── talks/        # One folder per session (metadata + optional in-repo demo code)
├── assets/       # Slides, diagrams, images, recordings (shared media)
├── templates/    # Copy before each new in-repo talk
├── docs/         # Cross-talk reference (profile, FAQ, roadmap)
├── src/          # Optional repo-wide utilities only — not per-talk demos
└── .github/ …    # Assistant and CI configuration
```

### Talk folder conventions

- Prefix: `YYYY-MM-DD-short-description` (example: `2026-07-11-amazon-bedrock-cline-agentic`)
- **External curriculum talks** (Python): thin `README.md` only — link to session doc and code in the external repo
- **In-repo demo talks** (Bedrock): full template set — `README.md`, `agenda.md`, `demo-script.md`, `references.md`, `links.md`, plus `src/`, `prompts/`, etc. as needed

### External Python curriculum

Do **not** copy lab code or session markdown from
[python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice).
Index only via links (for example `docs/sessions/L1/S5.md`).

## Documentation rules

- Rewrite imported material before treating it as canonical.
- Keep root README as the speaker portfolio table (index, upcoming, completed).
- Use consistent talk README sections for in-repo talks: Title → Abstract → Audience → Prerequisites → Agenda → Demo → Hands-on Code → Slides → Recording → References → Questions
- Prefer tables and links over duplicating long-form curriculum.

## Code guidance

- Per-talk demo code lives under `talks/{id}/src/`, not repo root `src/`.
- Use portable paths (`pathlib`, relative paths).
- Bedrock demos: never commit secrets; use `.env` from `.env.example`.
- Keep Python samples minimal and runnable.

## Verification

- **Python:** `ci-python.yml` — byte-compile all tracked `.py` files
- **Docs:** `ci-documentation.yml` — markdownlint on portfolio surfaces
- **Skills:** `ci-skills-parity.yml` — `.github/skills/` ↔ `.cursor/skills/` identical
- **Mirrors:** After editing canonical files, sync `.clinerules/` and `.opencode/` per `tools/psscripts/sync-assistant-mirrors.ps1`

## Assistant parity (canonical → mirrors)

| Canonical | Mirrors |
| --- | --- |
| `.github/copilot-instructions.md` | extract in `.cursor/rules/08_copilot-instructions-extract.mdc`; `.clinerules/rules/08-copilot-instructions-extract.md` |
| `.github/skills/` | `.cursor/skills/`, `.opencode/skills/` (byte-identical SKILL.md) |
| `.github/agents/` | `.clinerules/agents/`, `.opencode/agents/` |
| `.cursor/rules/*.mdc` | `.clinerules/rules/*.md`, `.opencode/rules/*.md` |
| `AGENTS.md`, `CLAUDE.md` | `.clinerules/AGENTS.md`, `.claude/CLAUDE.md` |

**Edit order:** `.github/` and `.cursor/rules/` first → run sync script → verify parity.

## Bundled skills

- `speaker-series` — domain context for this repository
- `ci-checks` — local commands aligned with CI workflows
- `workspace-review` — structure, mirror parity, contamination audit

## Subagents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After code, docs, or governance edits |
| `talk-content-review` | Reviewing talk folders, templates, portfolio docs |
| `docs-originality-review` | Spot-checking imports for repo fit |
