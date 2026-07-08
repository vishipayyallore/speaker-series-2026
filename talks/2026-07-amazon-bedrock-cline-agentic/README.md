# Exploring Amazon Bedrock Models + Cline + Vibe Coding + Agentic Coding

**Event:** [Dot Net Learners House (Hyderabad)](https://www.meetup.com/dot-net-learners-house-hyderabad/)  
**Meetup:** [Event page][meetup-event]  
**When:** Saturday, 11 July 2026 · 4:00–5:00 PM IST  
**Format:** Online · live demo + interactive Q&A  
**Duration:** 60 minutes  
**Level:** Beginner → intermediate (AI-curious developers)  
**Hosts:** Viswanatha S., HEMA V.  
**Status:** delivered

---

## Abstract

Live walkthrough of Amazon Bedrock foundation models, configuring **Cline** to use Bedrock,
**vibe coding** with AI assistance, and how **agentic coding** differs from traditional chat.

Attendees see model selection (Amazon vs Qwen tradeoffs), practical prompting, and a small
application built with AI guidance.

---

## Audience

Developers new to or curious about generative AI on AWS — especially .NET and general
software engineers attending Dot Net Learners House.

---

## Prerequisites

- AWS account (optional for follow-along; demo is presenter-led online)
- VS Code with [Cline](https://github.com/cline/cline) if reproducing the IDE setup locally
- For Python samples in this repo: copy `.env.example` to `.env` and enable Bedrock model access

---

## Agenda

See [agenda.md](./agenda.md).

---

## Demo

See [demo-script.md](./demo-script.md).  
Cline + Bedrock setup: [cline-bedrock-setup.md](./cline-bedrock-setup.md).

---

## Hands-on Code

Supporting material in this talk folder (optional post-session):

| Resource | Location |
| -------- | -------- |
| Cline + Bedrock setup | [cline-bedrock-setup.md](./cline-bedrock-setup.md) |
| Python Bedrock client | [src/bedrock_client.py](./src/bedrock_client.py) |
| Agent loop sample | [src/agent.py](./src/agent.py) |
| Prompts | [prompts/](./prompts/) |
| Notebook | [notebooks/bedrock-quickstart.ipynb](./notebooks/bedrock-quickstart.ipynb) |
| IAM sample | [infra/bedrock-policy.yaml](./infra/bedrock-policy.yaml) |

Primary live demo is **Cline + Bedrock in the IDE**; Python samples reinforce API and agentic concepts.

---

## Slides

- (add link when deck is ready — prefer `assets/slides/2026-07-amazon-bedrock-cline-agentic.pdf`)

---

## Recording

[YouTube — Exploring Amazon Bedrock Models + Cline + Vibe Coding + Agentic Coding](https://www.youtube.com/watch?v=M-bLxxdqV5I)

---

## Sponsors

Thank you to **[JetBrains](https://www.jetbrains.com/)** for supporting Dot Net Learners House and
empowering developers.

---

## References

See [references.md](./references.md).

---

## Questions

_Add common questions after the session._

[meetup-event]: <https://www.meetup.com/dot-net-learners-house-hyderabad/events/315495347/?eventOrigin=group_upcoming_events>
