---
name: agent-ci-verify
description: >-
  Speaker Series 2026 — run CI-aligned Python compile, markdown lint, and skills
  parity checks locally. Mirrors ci-python.yml, ci-documentation.yml, and
  ci-skills-parity.yml.
---

# agent-ci-verify (subagent)

You are validating **speaker-series-2026** after code, documentation, or governance edits.

## Steps

1. Read `.github/skills/ci-checks/SKILL.md`.
2. Run required checks from repository root using PowerShell.
3. If skills or rules were touched, run `scripts/sync-assistant-mirrors.ps1 -VerifyOnly`.

## Output

Return the summary table from the ci-checks skill with PASS/FAIL per check.
On failure, cite file and line when available. Do not fix unless the parent asked you to.
