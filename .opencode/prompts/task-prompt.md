# Applied Engineering Repository Verification (Content Audit Prompt)

## Context

You are working in **applied-engineering**, a repository for practical notes,
experiments, reference implementations, automation, and assistant-facing
configuration. Adopt the repo's assistant stance from
`.github/copilot-instructions.md` and `.cursor/rules/09_core-agent-role.mdc`.

**Repository structure (high level):**

- `docs/` — shared documentation assets and diagrams
- `src/` — code, examples, experiments, or topic-oriented work
- `.github/`, `.cursor/`, `.claude/`, `.copilot/`, `.vscode/` — repo tooling and assistant configuration
- `source-material/` — optional read-only staging for imported raw content when present

## Primary objective

Perform a comprehensive audit of the repository for:

- **Cross-repo contamination** (old repo names, links, labels, or assumptions)
- **Structure and metadata alignment** with the current repository layout
- **Documentation and workflow accuracy**
- **Code and automation hygiene**

---

## Verification checks

### A. Content integrity (mandatory)

- Ensure `source-material/` files are not modified when present (read-only
    rule)
- Ensure imported content is rewritten to fit this repository
- Ensure examples, commands, and references match the current project

### B. Repository accuracy

- Verify README, prompts, skills, and templates use the correct repo identity
- Verify paths, links, and workflow names match the current structure
- Check that assumptions are stated where they matter

### C. Automation and config quality

- Workflow and task commands should match the actual repo surfaces
- Mirrored skills in `.github/skills/` and `.cursor/skills/` should stay aligned
- Editor and lint settings should fit the repository's current tooling

### D. Structure and naming

- README matches the current or explicitly planned repository structure
- No file or folder names start with `00-` or `00_`
- Templates and prompts point to the correct repository and folder model
- Imported filenames or labels that expose another project are removed or renamed when appropriate

### E. Documentation hygiene

- README matches actual folder structure
- Links are valid
- Templates and project metadata match this repository (no unrelated system references)

---

## Deliverables

1. A concise summary of issues found (high/medium/low)
2. A list of files to fix, with suggested edits
3. A short set of next steps (max 5)
