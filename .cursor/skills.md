# Repository skills (Applied Engineering)

This file is local to `applied-engineering`. It complements `.cursor/rules/*.mdc` and `.github/copilot-instructions.md` with concise guidance for assistants editing this repo.

**Project scope:** This repo is an Applied Engineering workspace. See `README.md` and `.cursor/rules/project-scope.mdc`.

**Core role:** `.cursor/rules/09_core-agent-role.mdc` and `.github/copilot-instructions.md` define the single professional stance used in this repo.

**Bundled agent skills:** `.github/skills/` is canonical and `.cursor/skills/` is the mirror. Bundles: `applied-engineering` and `ci-checks`.

## CI expectations

- Docs: Markdown lint and Lychee per `ci-documentation.yml`
- Python: tracked-file compilation per `ci-python.yml`
- Skills: mirror parity per `ci-skills-parity.yml`
