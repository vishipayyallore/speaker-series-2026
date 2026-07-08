# Source Material Rules

**Folder**: `source-material/` when present
**Status**: Optional staging / read-only / reference input

## Critical Restrictions

### Read-Only Policy

- **NEVER modify** any file inside `source-material/`
- **NEVER overwrite** any file inside `source-material/`
- **NEVER edit** content even if it contains errors
- Files are treated as reference inputs

### No Deletion Policy

- **NEVER delete** anything from `source-material/`
- Content remains available for traceability

### Export Location Policy (.pdf / .pptx conversions)

- **NEVER export converted outputs to unrelated canonical docs folders** when converting files that live in `source-material/`.
- For `.pdf` / `.pptx` conversion jobs, create output files **inside the same
   `source-material/` path tree** as the input source file.
- Keep source and extraction artifacts colocated within `source-material/`
   for traceability.

## 🔄 Migration Workflow

When migrating content from `source-material/`:

1. **Read** from `source-material/` to understand concepts
2. **Synthesize** - Rewrite in your own words (NO copy-paste)
3. **Publish** to the appropriate path under `docs/`, `src/`, or another repo-owned destination
4. **Cite** when using specific source claims or close references

## ✅ Zero-Copy Policy

### Good Synthesis (Accepted)

- Demonstrates understanding
- Uses different vocabulary
- Explains concepts, not restates them
- Shows original thinking and interpretation

### Bad Synthesis (Rejected)

- Word-for-word copying
- Minor rephrasing
- Close paraphrasing without understanding
- Direct copy-paste with minimal changes

**Reference**: See `01_educational-content-rules.mdc` for detailed zero-copy
policy.

## 📁 Purpose

The `source-material/` folder is a staging area for:

- imported notes
- exported documents
- raw reference materials
- sample code from outside this repo

These materials remain **untouched** and serve as **permanent references**
while you create **repository-specific derived content** in the proper folders.

## Migration status (local `source-material/`)

When present locally, each import file has a canonical synthesized destination.
Do not copy-paste from source; rewrite into the pipeline location.

| Source file (read-only) | Canonical destination | Status |
| --- | --- | --- |
| `01-pkl_keras_objstate.md` | `01-knowledge/ai-ml/mlops/04-model-artifacts-vs-runtime-state.md` | Migrated |
| `02-model_under_fitting.md` | `01-knowledge/ai-ml/mlops/02-underfitting-high-bias-signals.md` | Migrated |
| `03-metrics.md` | `01-knowledge/ai-ml/mlops/01-classification-metrics-and-confusion-matrix.md` | Migrated |
| `04-model-over-fitting.md` | `01-knowledge/ai-ml/mlops/03-overfitting-high-variance-signals.md` | Migrated |
| `05-scatter-gather.md` | `02-patterns/integration-patterns/01-scatter-gather.md` | Migrated |
| `06-interview-topics.md` | `07-interview-prep/company-specific/genai-engineering-leader-life-sciences/` | Migrated |
| `07-AgentFrameworks.md` | `06-research/comparisons/agent-frameworks.md` | Migrated |
| `08-confussion-matrix.md` | `01-knowledge/ai-ml/mlops/01-classification-metrics-and-confusion-matrix.md` (subscription campaign worked example) | Migrated |
| `09-Hyperparameters.md` | `01-knowledge/ai-ml/mlops/05-hyperparameters-and-tuning.md` | Migrated |

If a new file appears under `source-material/`, add a row here after migration.

## ⚠️ Enforcement

- Reviewers must reject any PRs that modify or delete files in
   `source-material/`
- AI assistants must refuse requests to edit, overwrite, or delete content in
   `source-material/`
- Any migration must result in repo-specific derived content, not copied content
