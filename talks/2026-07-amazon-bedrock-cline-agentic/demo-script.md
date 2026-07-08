# Demo Script — Exploring Amazon Bedrock + Cline + Agentic Coding

**Estimated demo time:** 30–35 minutes (within 30–45 min session)  
**Environment:** AWS Bedrock + Cline in VS Code (online screen share)

---

## Before you start

- [ ] [Meetup event](https://www.meetup.com/dot-net-learners-house-hyderabad/events/315495347/?eventOrigin=group_upcoming_events) link ready to paste in chat
- [ ] Bedrock model access enabled; region confirmed
- [ ] Cline configured per [cline-bedrock-setup.md](./cline-bedrock-setup.md)
- [ ] Empty folder or small starter repo open for “build with AI” segment
- [ ] Optional: `.env` + `talks/2026-07-amazon-bedrock-cline-agentic/` Python samples tested

---

## Demo flow

### 1. What is Amazon Bedrock? (5 min)

**Say:** Bedrock is AWS’s managed way to call foundation models with your existing IAM and compliance boundaries — no model hosting on your side.

**Do:** Open [Bedrock console](https://console.aws.amazon.com/bedrock/) → model catalog / playground.

**Show:** One invoke from playground; point out region and model ID.

---

### 2. Foundation models + Amazon vs Qwen (5 min)

**Say:** Model choice depends on task, region availability, latency, and cost — not hype.

**Do:** Walk the model list; compare one **Amazon** model (e.g. Nova/Titan if enabled) with **Qwen** where available.

**Show:** Side-by-side from [cline-bedrock-setup.md](./cline-bedrock-setup.md#4-amazon-models-vs-qwen-talking-points).

---

### 3. Configure Cline with Bedrock (5 min)

**Say:** Cline turns Bedrock into an IDE-native coding partner with file and terminal context.

**Do:** Open Cline settings → Amazon Bedrock → region, auth, model ID. Run verification prompt from [cline-bedrock-setup.md](./cline-bedrock-setup.md#3-verify-with-a-short-prompt).

**Show:** Successful response inside Cline panel.

---

### 4. Vibe coding (7 min)

**Say:** Vibe coding is iterative, conversational building — you steer intent; the model drafts and refines.

**Do:** In Cline, describe a small feature in plain language (e.g. “Add a CLI that reads JSON and prints a summary table”). Accept/refine suggestions across 2–3 turns.

**Show:** Working snippet or test run; highlight how prompts changed the output.

---

### 5. Agentic coding vs chat (5 min)

**Say:** Chat answers once; agentic flows plan, use tools, read files, and loop until the task completes.

**Do:** Contrast a one-shot chat question with Cline agent mode (or multi-step task: “Create file X, add tests, run them”).

**Show:** Tool/file steps in Cline vs single reply. Reference [prompts/system-prompt.md](./prompts/system-prompt.md).

**Optional backup:** Run `python src/agent.py` to show a minimal routing loop in code.

---

### 6. Build a small application with AI guidance (8 min)

**Say:** We assemble a tiny end-to-end slice — structure, implementation, and a sanity check — guided by Cline.

**Do:** Pick one scoped app (e.g. Bedrock model list helper, config validator, or minimal API client). Let Cline scaffold; you review and run.

**Show:** Final tree, one command that succeeds, and one prompt that fixed a bug.

---

### 7. Prompting techniques (5 min)

**Say:** Better prompts specify role, constraints, output shape, and verification steps.

**Do:** Show before/after prompts from [prompts/router-prompt.md](./prompts/router-prompt.md) and a “good” Cline instruction template:

```text
Role: senior developer
Task: add error handling to {file}
Constraints: no new dependencies; keep functions under 20 lines
Verify: run {test command} and show output
```

**Show:** Quality difference on the same task with weak vs strong prompt.

---

## Fallback plan

| Failure | Backup |
| ------- | ------ |
| Bedrock/API error | Walk through recorded screenshots in `assets/images/` + explain setup doc |
| Cline misconfigured | Show [cline-bedrock-setup.md](./cline-bedrock-setup.md) and pre-recorded clip |
| Time short | Compress §6; keep §3–§5 and Q&A |

---

## Cleanup

- [ ] Paste [links.md](./links.md) URLs in Meetup chat
- [ ] Note approximate token usage for personal tracking
- [ ] Capture attendee questions in talk README
