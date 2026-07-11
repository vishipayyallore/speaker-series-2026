"""Minimal Amazon Bedrock invoke example for Speaker Series 2026."""

from __future__ import annotations

import os
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

# Load .env from repository root when running from talk folder
ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")

DEFAULT_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "qwen.qwen3-32b-instruct-v1:0")
DEFAULT_REGION = os.getenv("AWS_REGION", "us-east-1")


def build_client() -> boto3.client:
    return boto3.client("bedrock-runtime", region_name=DEFAULT_REGION)


def invoke(prompt: str, *, model_id: str = DEFAULT_MODEL_ID) -> str:
    client = build_client()
    response = client.converse(
        modelId=model_id,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ],
        inferenceConfig={"maxTokens": 512},
    )
    output = response.get("output", {}).get("message", {}).get("content", [])
    if output and isinstance(output, list) and "text" in output[0]:
        return str(output[0]["text"])
    raise KeyError("No text output found in Bedrock response")


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
