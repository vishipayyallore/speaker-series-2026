# Contributing

Thank you for helping grow the Speaker Series portfolio.

This repository separates **talk metadata** (under `talks/`) from **shared assets** (under `assets/`).

---

## Adding a new talk

1. **Pick a folder name** using `YYYY-MM-short-description` (example: `2026-04-mcp-from-scratch`).
2. **Copy templates** from `templates/` into the new talk folder:
   - `talk-readme.md` → `README.md`
   - `agenda.md`
   - `demo-script.md`
   - `references.md`
   - `links.md`
3. **Fill in every section** in the talk `README.md` using the standard outline:
   - Title, Abstract, Audience, Prerequisites, Agenda, Demo, Hands-on Code,
     Slides, Recording, References, Questions
4. **Decide where code lives:**
   - **External curriculum** (Python track): add `talks/YYYY-MM-name/README.md` with
     links to the session doc (e.g. `S5.md`) and `src/` in
     [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice).
     Do not copy lab code or duplicate agenda/demo markdown here.
   - **In-repo demo** (Bedrock pattern): add `src/`, `prompts/`, `notebooks/`, or
     `infra/` inside the talk folder only.
5. **Add shared media** under `assets/slides/`, `assets/diagrams/`, `assets/images/`,
   or `assets/recordings/` — prefer `assets/` for binaries, not inside `talks/`.
6. **Update the root [README.md](./README.md)** talk index table and Upcoming/Completed sections.
7. **Optional:** add a row to [docs/meetup-history.md](./docs/meetup-history.md) after delivery.

## Assistant configuration

After editing `.github/skills/`, `.github/agents/`, or `.cursor/rules/`:

```powershell
./tools/psscripts/sync-assistant-mirrors.ps1
```

Canonical sources and mirror policy: [AGENTS.md](./AGENTS.md).

---

## Naming conventions

| Item | Convention | Example |
| ---- | ---------- | ------- |
| Talk folder | `YYYY-MM-kebab-case` | `2026-05-agentic-ai` |
| Slide file | match talk id | `assets/slides/2026-05-agentic-ai.pdf` |
| Recording | match talk id | `assets/recordings/2026-05-agentic-ai.mp4` |

---

## Environment and secrets

- Copy [.env.example](./.env.example) to `.env` for AWS Bedrock demos.
- Never commit `.env`, API keys, or account-specific ARNs.
- Use [infra/bedrock-policy.yaml](./talks/2026-07-amazon-bedrock-cline-agentic/infra/bedrock-policy.yaml)
  as a starting point for least-privilege IAM.

---

## Pull requests

- Keep one talk (or one doc/template fix) per PR when possible.
- Verify links in the talk `links.md` and root README.
- After delivery, move the talk from **Upcoming** to **Completed** in the root README.
