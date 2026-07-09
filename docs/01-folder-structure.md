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
│   ├── 2026-07-04-python-l1-s5-mini-calculator/   # S5 · delivered Jul 4, 2026
│   ├── 2026-07-08-python-l1-s6-loops/             # S6 · delivered Jul 8, 2026
│   └── 2026-07-11-amazon-bedrock-cline-agentic/  # Bedrock + Cline + agentic demo
│
├── assets/
│   ├── slides/
│   ├── diagrams/
│   ├── images/
│   └── recordings/
│
├── templates/                # Copy before each new talk
│
├── tools/                    # Repo maintenance (not talk demos)
│   ├── psscripts/            # PowerShell — CI, health, mirror sync
│   └── pyscripts/            # Python — parity checks, optional media utils
│
├── scripts/                  # Backward-compat shims → tools/psscripts/
│
└── docs/
    ├── 01-folder-structure.md
    ├── 01-repository-structure.md   # redirect → 01-folder-structure.md
    ├── speaker-profile.md
    ├── meetup-history.md
    ├── faq.md
    └── roadmap.md
```

---

## Design rules

1. **One folder per talk** — delivery-date prefix `YYYY-MM-DD-…` for automatic sorting.
2. **File set depends on talk type**:
   - **External curriculum** (Python): `README.md` only with links to session doc and code.
   - **In-repo demo** (Bedrock and similar): `README.md`, `agenda.md`, `demo-script.md`,
     `references.md`, `links.md` (plus optional `src/`, `prompts/`, `notebooks/`, `infra/`).
3. **No duplicated Python labs** — link to
   [python-fundamentals-in-practice](https://github.com/vishipayyallore/python-fundamentals-in-practice);
   use a thin `README.md` only under `talks/`.
4. **Self-contained demos** — original demo code (Bedrock) stays inside that talk’s folder
   (`talks/{id}/src/`, `prompts/`, etc.) so cloning this repo is enough to reproduce.
5. **No root `src/`** — there is no repo-wide code folder; demo code belongs under the owning talk.
6. **Binaries in `assets/`** — decks and recordings are shared artifacts, not scattered across talk folders.

---

## Talk README outline

In-repo demo talk `README.md` files follow this section order:

Title → Abstract → Audience → Prerequisites → Agenda → Demo → Hands-on Code → Slides → Recording → References → Questions

See [templates/talk-readme.md](../templates/talk-readme.md).
