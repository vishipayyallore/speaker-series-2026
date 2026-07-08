# Quality Assurance

## Code Quality Checklist

### Python scripts

- [ ] Follows PEP 8 style guide.
- [ ] Type hints used where they improve clarity.
- [ ] Comments explain non-obvious logic.
- [ ] No hardcoded paths (use `pathlib` or relative paths).

### Documentation and config

- [ ] README and templates match the current repository.
- [ ] Links and repo references point to the correct destination.
- [ ] Imported names and labels from other repos are removed.

## Automation checks

- [ ] Workflow names and summaries match the project purpose.
- [ ] Local tasks and CI commands work with tracked files only when appropriate.
- [ ] Mirror rules are preserved when `.github/skills/` and `.cursor/skills/` are both used.

## Content review checklist

- [ ] Imported text has been rewritten to fit this repo.
- [ ] Examples and commands are relevant to the touched files.
- [ ] Added guidance does not imply unsupported structure or tooling.

## Documentation Quality

- README.md must match actual implementation.
- Usage guides must be accurate.
- Code comments explain complex logic where needed.
- File references and labels must remain internally consistent.
