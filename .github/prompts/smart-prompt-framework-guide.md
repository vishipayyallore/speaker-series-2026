# S.M.A.R.T. Prompt Framework (Applied Engineering Edition)

This guide helps me write effective requests for GitHub Copilot in this repository.

---

## The S.M.A.R.T. framework

```text
S - Specific role definition (who the agent should act as)
M - Mission with measurable outcomes (what “done” means)
A - Audience-aware communication (my level + preferred tone)
R - Response format control (files to create/modify + structure)
T - Task constraints (non-negotiables and forbidden actions)
```

---

## Repo-specific constraints (non-negotiable)

- Never modify or delete anything in `source-material/` (top-level, not under `docs/`).
- Rewrite imported content so it matches this repository; avoid copy-paste artifacts.
- Follow the repository structure described in `README.md`.
- Prefer Windows + PowerShell commands when commands are needed.
- Remove stale repo names, URLs, and folder assumptions.

---

## A good task prompt template

```markdown
## ROLE

You are a [role] specializing in [engineering surface] and clear technical writing.

## MISSION

[What to create/change] with [measurable outcomes].

## CONTEXT

- Current topic number: XX
- Related files: [list]
- Known issues: [if any]

## REQUIREMENTS

- Repository fit (paths, labels, and scope match this repo)
- Original synthesis (no copied cross-repo wording)
- Validation expectations (docs, code, or workflow checks)
- Naming conventions (no 00_ prefix)

## OUTPUT FORMAT

- Update these files: ...
- Create these files: ...
- Provide a short recap and next steps

## DO NOT

- Do not edit `source-material/`
- Do not add unrelated refactors
```

---

## Role examples that fit this repo

### 1) Repository guidance cleanup

```markdown
ROLE: You are a repository documentation engineer.

MISSION: Update assistant-facing files under `.github/`, `.cursor/`, and `.claude/` so they:
- match the current project scope
- remove imported repo references
- stay internally consistent with `README.md`

SUCCESS CRITERIA:
- All repo names, links, and paths are correct
- Templates and prompts match the real repo layout
- Validation steps are included where needed
```

### 2) Implementation slice builder

```markdown
ROLE: You are a pragmatic software engineer.

MISSION: Add or update a small implementation slice under `src/` to:
- solve a concrete repository problem
- keep code readable and locally coherent
- include the narrowest validation needed for the touched surface

SUCCESS CRITERIA:
- The change matches the local folder convention
- Commands and paths are portable
- Validation is documented or run
```

### 3) Automation maintainer

```markdown
ROLE: You are a CI and tooling maintainer.

MISSION: Update workflows, tasks, or templates so they:
- reflect the current repo structure
- skip cleanly when optional file types are absent
- avoid references to the imported source repository

SUCCESS CRITERIA:
- Commands are runnable on the current repo
- Names and summaries are repository-specific
- No stale repo identity remains
```
