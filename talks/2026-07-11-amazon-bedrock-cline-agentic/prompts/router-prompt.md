# Router prompt

Classify the user message into exactly one route:

- `direct_answer` — general question, no tools required
- `code_help` — Python or boto3 implementation question
- `bedrock_docs` — question about Bedrock models, quotas, or IAM

Respond with JSON only:

```json
{
  "route": "direct_answer | code_help | bedrock_docs",
  "reason": "one short sentence"
}
```

User message:

```text
{{user_message}}
```
