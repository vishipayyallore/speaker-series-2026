# FAQ

---

## Where is the Python exercise code?

In the separate repository [python-fundamentals-in-practice](https://github.com/{your-org}/python-fundamentals-in-practice). This repo only links to it from the Python session talk folders.

---

## Where is the Bedrock demo code?

Inside [talks/2026-03-aws-bedrock-agentic/](../talks/2026-03-aws-bedrock-agentic/). Clone this repository, copy `.env.example` to `.env`, and follow that talk’s README.

---

## How do I add a new session?

Copy files from [templates/](../templates/), create a new folder under `talks/` with a `YYYY-MM-name` prefix, and update the root [README.md](../README.md). See [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## Where do slides and recordings go?

Under `assets/slides/` and `assets/recordings/`, named to match the talk folder (example: `2026-03-aws-bedrock-agentic.pdf`).

---

## Why split metadata and assets?

So the repo scales to dozens of talks: markdown and scripts stay easy to diff in `talks/`, while large binaries stay in `assets/` without cluttering each talk folder.
