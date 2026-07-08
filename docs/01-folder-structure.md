# Folder structure

This repository indexes speaking engagements. **Talk metadata** lives under `talks/`; **shared media** under `assets/`.

```text
speaker-series-2026/
│
├── README.md                 # Speaker portfolio index
├── CONTRIBUTING.md           # How to add a talk
├── LICENSE
├── .gitignore
├── .env.example              # AWS Bedrock demo variables
│
├── talks/
│   ├── 2026-01-python-session-01/    # Metadata only → external Python repo
│   ├── 2026-02-python-session-02/
│   └── 2026-03-aws-bedrock-agentic/  # Metadata + self-contained demo code
│
├── assets/
│   ├── slides/
│   ├── diagrams/
│   ├── images/
│   └── recordings/
│
├── templates/                # Copy before each new talk
│
└── docs/
    ├── 01-folder-structure.md
    ├── speaker-profile.md
    ├── meetup-history.md
    ├── faq.md
    └── roadmap.md
```

---

## Design rules

1. **One folder per talk** — chronological prefix `YYYY-MM-…` for automatic sorting.
2. **Same file set per talk** — at minimum: `README.md`, `agenda.md`, `demo-script.md`, `references.md`, `links.md`.
3. **No duplicated Python labs** — link to `python-fundamentals-in-practice` for sessions 1–2.
4. **Self-contained demos** — original demo code (Bedrock) stays inside that talk’s folder so cloning this repo is enough to reproduce.
5. **Binaries in `assets/`** — decks and recordings are shared artifacts, not scattered across talk folders.

---

## Talk README outline

Every talk `README.md` follows the same sections:

Title → Abstract → Audience → Prerequisites → Agenda → Demo → Hands-on Code → Slides → Recording → References → Questions

See [templates/talk-readme.md](../templates/talk-readme.md).
