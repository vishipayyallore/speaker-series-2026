# Demo Script — AWS Bedrock + Agentic Coding

**Estimated demo time:** 25 minutes  
**Environment:** cloud (AWS Bedrock)

---

## Before you start

- [ ] `.env` configured from repo root `.env.example`
- [ ] Bedrock model access enabled in your AWS region
- [ ] `pip install boto3 python-dotenv` (or project requirements when added)
- [ ] Terminal open at `talks/2026-03-aws-bedrock-agentic/`

---

## Demo flow

### 1. Minimal Bedrock invoke

**Say:** We start with a single model call before adding agent behavior.

**Do:**

```bash
cd talks/2026-03-aws-bedrock-agentic
python src/bedrock_client.py
```

**Show:** Model response in the terminal and which env vars were used.

---

### 2. Agent with routing prompt

**Say:** Agents add structure — system prompt, router, and tool stubs.

**Do:**

```bash
python src/agent.py
```

**Show:** Router decision and final assistant message. Reference [prompts/system-prompt.md](./prompts/system-prompt.md) and [prompts/router-prompt.md](./prompts/router-prompt.md).

---

### 3. Optional notebook

**Say:** The notebook is the same flow step-by-step for post-session study.

**Do:** Open [notebooks/bedrock-quickstart.ipynb](./notebooks/bedrock-quickstart.ipynb).

---

## Fallback plan

If Bedrock throttles or credentials fail, walk through code and prompts without live inference. Keep a saved terminal transcript or screenshot under `assets/images/`.

---

## Cleanup

- [ ] Revoke temporary IAM keys if created for demo only
- [ ] Note approximate token usage for attendees
