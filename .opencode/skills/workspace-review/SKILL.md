---
name: workspace-review
description: Review Applied Engineering for structure alignment, assistant parity, source-material migration, and cross-repo contamination.
license: MIT
compatibility: opencode
---

# Workspace Review — Applied Engineering

Use when auditing the full repository or onboarding new assistant mirrors.

## Structure alignment

- [ ] `README.md` and `docs/01-folder-structure.md` match actual top-level layout
- [ ] Pipeline folders `01-knowledge/` … `07-interview-prep/` follow stage intent
- [ ] Infrastructure folders (`templates/`, `scripts/`, `tools/`, `sandbox/`, `src/`) have no numeric prefix
- [ ] Numbered topic bundles use `01-`, `02-`, … with unnumbered `README.md` indexes

## Assistant parity

- [ ] `.github/skills/` ↔ `.cursor/skills/` byte-identical
- [ ] `.clinerules/` and `.opencode/` aligned with `.cursor/rules/` and `.github/copilot-instructions.md`
- [ ] No references to unrelated repos (`agentic-engineering-in-practice`, `presentation/demo-0N/`, etc.)
- [ ] CI workflow names in assistant files match `.github/workflows/` (only `ci-python`, `ci-documentation`, `ci-skills-parity`)

## Source material

- [ ] `source-material/` not edited (read-only)
- [ ] All known imports have pipeline destinations (see `.cursor/rules/06_source_material_rules.mdc`)

## Content quality spot-check

- [ ] Active pipeline notes have plain-English explanations or worked examples
- [ ] Mermaid blocks include ASCII fallbacks where present
- [ ] Cross-links in touched bundles resolve

## Deliverables

1. Summary table: high / medium / low issues
2. Files to fix with suggested edits
3. Up to five next steps
