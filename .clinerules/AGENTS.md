# AGENTS.md — Applied Engineering (Cline)

**Canonical index:** root [`AGENTS.md`](../AGENTS.md) (precedence, skills, recovery).

**Repository:** `applied-engineering`

Applied Engineering workspace for practical notes, experiments, reference
implementations, automation, and assistant configuration — organized as a
numbered learning pipeline (`01-knowledge/` … `07-interview-prep/`).

## Read first

1. `README.md` — repo purpose and structure
2. `docs/01-folder-structure.md` — folder layout
3. `.github/copilot-instructions.md` — canonical assistant rules
4. `CLAUDE.md` — repo-level entry point
5. `.cursor/rules/project-scope.mdc` — scope and anti-contamination

## Structure

```text
01-knowledge/ … 07-interview-prep/   # learning pipeline
docs/  assets/  src/  templates/  scripts/  tools/  sandbox/
.github/  .cursor/  .claude/  .copilot/  .vscode/
source-material/                     # optional read-only imports (gitignored)
```

## Subagents

Canonical definitions live in `.github/agents/`; `.clinerules/agents/` is a
Cline-facing mirror.

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After code or governance edits |
| `content-quality-review` | Auditing pipeline teaching content |
| `docs-originality-review` | Doc rewrites under pipeline folders |

## CI workflows

| Workflow | Scope |
| --- | --- |
| `ci-python.yml` | Tracked Python byte-compile |
| `ci-documentation.yml` | Markdown lint |
| `ci-skills-parity.yml` | Skills mirror parity |

Local runner: `.github/skills/ci-checks/SKILL.md` (mirror: `skills/ci-checks.md`).

## Rules

`.clinerules/rules/` mirrors `.cursor/rules/*.mdc` (project-scope + numbered
`01`–`09`).

## Do not

- Edit files in `source-material/` (read-only staging)
- Import folder models from unrelated repositories
- Treat `.archive/` as canonical pipeline content
