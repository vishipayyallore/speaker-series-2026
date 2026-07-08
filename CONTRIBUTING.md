# Contributing

Thank you for helping grow the Speaker Series portfolio. This repository separates **talk metadata** (under `talks/`) from **shared assets** (under `assets/`).

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
   - Title, Abstract, Audience, Prerequisites, Agenda, Demo, Hands-on Code, Slides, Recording, References, Questions
4. **Decide where code lives:**
   - **External repo** (Python track pattern): link from `links.md` and `README.md`; do not copy exercise code here.
   - **In-repo demo** (Bedrock pattern): add `src/`, `prompts/`, `notebooks/`, or `infra/` inside the talk folder only.
5. **Add shared media** under `assets/slides/`, `assets/diagrams/`, `assets/images/`, or `assets/recordings/` — not inside `talks/` unless the file is tiny and talk-specific (prefer assets for binaries).
6. **Update the root [README.md](./README.md)** talk index table and Upcoming/Completed sections.
7. **Optional:** add a row to [docs/meetup-history.md](./docs/meetup-history.md) after delivery.

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
- Use [infra/bedrock-policy.yaml](./talks/2026-03-aws-bedrock-agentic/infra/bedrock-policy.yaml) as a starting point for least-privilege IAM.

---

## Pull requests

- Keep one talk (or one doc/template fix) per PR when possible.
- Verify links in the talk `links.md` and root README.
- After delivery, move the talk from **Upcoming** to **Completed** in the root README.
