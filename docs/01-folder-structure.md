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
│   ├── 2026-01-python-l1-s5-mini-calculator/   # README only → external S5
│   ├── 2026-02-python-l1-s6-loops/             # README only → external S6
│   └── 2026-07-amazon-bedrock-cline-agentic/  # Bedrock + Cline + agentic demo
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
2. **File set depends on talk type**:
   - **External curriculum** (Python): `README.md` only with links to session doc and code.
   - **In-repo demo** (Bedrock and similar): `README.md`, `agenda.md`, `demo-script.md`,
     `references.md`, `links.md` (plus optional `src/`, `prompts/`, `notebooks/`, `infra/`).
3. **No duplicated Python labs** — link to
   [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice);
   use a thin `README.md` only under `talks/`.
4. **Self-contained demos** — original demo code (Bedrock) stays inside that talk’s folder
   so cloning this repo is enough to reproduce.
5. **Binaries in `assets/`** — decks and recordings are shared artifacts, not scattered across talk folders.

---

## Talk README outline

In-repo demo talk `README.md` files follow this section order:

Title → Abstract → Audience → Prerequisites → Agenda → Demo → Hands-on Code → Slides → Recording → References → Questions

See [templates/talk-readme.md](../templates/talk-readme.md).
