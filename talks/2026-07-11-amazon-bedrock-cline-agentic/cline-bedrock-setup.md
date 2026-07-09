# Configure Cline with Amazon Bedrock

Step-by-step reference for the live demo. Adjust model IDs to match what is enabled in your AWS account and region.

---

## Prerequisites

- AWS account with [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/) model access
- [Cline](https://github.com/cline/cline) extension installed in VS Code (or compatible editor)
- IAM credentials or SSO profile with `bedrock:InvokeModel` permission — see [infra/bedrock-policy.yaml](./infra/bedrock-policy.yaml)

---

## 1. Enable foundation models

1. Open [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/) → **Model access**.
2. Request access to models you plan to demo (for example Claude, Amazon Nova, or Qwen if available in your region).
3. Note the **region** — Cline must use the same region as your enabled models.

---

## 2. Cline API provider settings

In Cline settings, choose **Amazon Bedrock** as the provider and configure:

| Setting | Value |
| ------- | ----- |
| AWS Region | e.g. `us-east-1` (match your Bedrock region) |
| Authentication | AWS profile, access keys, or SSO — same as AWS CLI |
| Model ID | Foundation model ID from Bedrock (see model comparison in [agenda.md](./agenda.md)) |

Use the same credentials pattern as repo root `.env.example` if you also run the Python demos in [src/](./src/).

---

## 3. Verify with a short prompt

In Cline, send:

```text
List three things Amazon Bedrock provides to application developers. One sentence each.
```

Confirm latency, region, and model ID in Cline’s status UI before the live session.

---

## 4. Amazon models vs Qwen (talking points)

| Consideration | Amazon models (e.g. Nova, Titan) | Qwen (where available on Bedrock) |
| ------------- | -------------------------------- | --------------------------------- |
| Ecosystem fit | Strong AWS integration, enterprise policies | Popular for coding and multilingual tasks |
| Latency / cost | Varies by model and region — check Bedrock pricing | Compare in console for your region |
| When to choose | AWS-native apps, IAM-bound workloads, Nova/Titan features | Coding-heavy vibe sessions, comparison demos |

Demo both only if both are enabled in your account; otherwise explain tradeoffs from the console model list.

---

## Troubleshooting

| Issue | Check |
| ----- | ----- |
| Access denied | IAM policy, model access in console, correct region |
| Model not found | Model ID string matches Bedrock catalog exactly |
| Slow first response | Cold start; run a warmup prompt before going live |
