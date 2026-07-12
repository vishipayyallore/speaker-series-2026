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
| Vibe-coding sample (Hospital homepage) | [homepage/](./homepage/) — open `index.html` in a browser |

Primary live demo is **Cline + Bedrock in the IDE**; Python samples reinforce API and agentic concepts.
The `homepage/` folder is the small site built during the vibe-coding segment.

---

## Slides

- (add link when deck is ready — prefer `assets/slides/03-amazon-bedrock-cline-agentic.pdf`)

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

**What is the difference between vibe coding and agentic coding?**  
Vibe coding is conversational, iterative drafting — you steer intent and refine output across turns.
Agentic coding adds tool use (files, terminal, loops) until a scoped task completes.

**Do I need an AWS account to follow along?**  
No for the live session — the presenter demo is screen-shared. To reproduce locally, enable Bedrock
model access in your account and copy `.env.example` to `.env`.

**Which Bedrock model should I start with?**  
Start with a model enabled in your region that matches your IAM policy — this repo defaults to
Claude 3 Haiku (`anthropic.claude-3-haiku-20240307-v1:0`). See
[cline-bedrock-setup.md](./cline-bedrock-setup.md#4-amazon-models-vs-qwen-talking-points) for
Amazon vs Qwen tradeoffs.

**Can I use Cline without Bedrock?**  
Yes — Cline supports other providers. This session focuses on Bedrock for AWS-native teams.

[meetup-event]: <https://www.meetup.com/dot-net-learners-house-hyderabad/events/315495347/>
