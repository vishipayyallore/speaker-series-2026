"""Simple agent loop stub — routing + single Bedrock call."""

from __future__ import annotations

import json
from pathlib import Path

from bedrock_client import invoke

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / name).read_text(encoding="utf-8")


def route(user_message: str) -> str:
    template = load_prompt("router-prompt.md")
    prompt = template.replace("{{user_message}}", user_message)
    raw = invoke(prompt)
    try:
        data = json.loads(raw)
        return str(data.get("route", "direct_answer"))
    except json.JSONDecodeError:
        return "direct_answer"


def run_agent(user_message: str) -> None:
    system = load_prompt("system-prompt.md")
    chosen = route(user_message)
    composed = f"{system}\n\nRoute: {chosen}\n\nUser: {user_message}"
    answer = invoke(composed)
    print("Route:", chosen)
    print("Answer:", answer)


def main() -> None:
    run_agent("How do I invoke a model with boto3?")


if __name__ == "__main__":
    main()
