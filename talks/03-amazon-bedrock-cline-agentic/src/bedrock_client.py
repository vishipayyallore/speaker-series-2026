"""Minimal Amazon Bedrock invoke example for Speaker Series 2026."""

from __future__ import annotations

import json
import os
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

# Load .env from repository root when running from talk folder
ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")

DEFAULT_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")
DEFAULT_REGION = os.getenv("AWS_REGION", "us-east-1")


def build_client() -> boto3.client:
    return boto3.client("bedrock-runtime", region_name=DEFAULT_REGION)


def invoke(prompt: str, *, model_id: str = DEFAULT_MODEL_ID) -> str:
    client = build_client()
    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 512,
            "messages": [{"role": "user", "content": prompt}],
        }
    )
    response = client.invoke_model(modelId=model_id, body=body)
    payload = json.loads(response["body"].read())
    return payload["content"][0]["text"]


def main() -> None:
    prompt = os.getenv("DEMO_PROMPT", "In one sentence, what is Amazon Bedrock?")
    try:
        text = invoke(prompt)
    except (ClientError, BotoCoreError, KeyError) as exc:
        print("Bedrock invoke failed:", exc)
        print("Check AWS credentials, region, and model access in the Bedrock console.")
        raise SystemExit(1) from exc

    print("Model:", DEFAULT_MODEL_ID)
    print("Region:", DEFAULT_REGION)
    print("Response:", text)


if __name__ == "__main__":
    main()
