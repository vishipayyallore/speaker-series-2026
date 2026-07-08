# Applied Engineering core context

**Repository:** `applied-engineering`

## Purpose

Working repository for applied engineering knowledge, hands-on labs, interview
preparation, research notes, and repository automation. Content progresses through
a deliberate learning pipeline:

```text
Learn → Pattern → Practice → Apply → Operate → Explore → Defend
01-knowledge → 02-patterns → 03-labs → 04-projects → 05-playbooks → 06-research → 07-interview-prep
```

## Active content surfaces

| Surface | Role |
| --- | --- |
| `01-knowledge/` | Concepts and domain notes |
| `02-patterns/` | Reusable solutions |
| `03-labs/` | Runnable exercises |
| `07-interview-prep/` | Role-first interview packs |
| `06-research/` | Comparisons, deep dives, PoCs |
| `docs/` | Shared repo documentation |
| `src/` | Owned code and utilities |

## Read-only imports

`source-material/` (when present locally) holds raw imports. Synthesize into
pipeline folders; never edit source files. See `.cursor/rules/06_source_material_rules.mdc`.

## Governance mirrors

| Tooling | Mirror path | Canonical |
| --- | --- | --- |
| Cursor | `.cursor/rules/`, `.cursor/skills/` | `.github/copilot-instructions.md`, `.github/skills/` |
| Cline | `.clinerules/` | Same canonical sources |
| OpenCode | `.opencode/` | Same canonical sources |

Skills and agents in mirrors must stay aligned after canonical edits.
