#!/usr/bin/env python3
"""Verify .clinerules/ mirrors canonical Speaker Series 2026 governance files."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FRONTMATTER_KEYS = ("name", "description", "canonical")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 3 :].lstrip("\n")
    meta: dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            meta[key.strip()] = value
    return meta, body


def normalize_text(text: str) -> str:
    replacements = {
        "\u2019": "'",
        "\u2018": "'",
        "\ufffd": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def normalize_for_compare(text: str) -> str:
    text = normalize_text(text)
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip())


def read_mdc_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return normalize_text(parts[2].lstrip("\n"))
    if "\n---\n" in text:
        return normalize_text(text.split("\n---\n", 1)[1].lstrip("\n"))
    return normalize_text(text.lstrip("\n"))


def mdc_to_cline_name(mdc_name: str) -> str:
    base = Path(mdc_name).stem
    return base.replace("_", "-") + ".md"


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    errors: list[str] = []

    # Rules: .cursor/rules/*.mdc -> .clinerules/rules/*.md
    cursor_rules = sorted((ROOT / ".cursor/rules").glob("*.mdc"))
    for mdc in cursor_rules:
        cline_rel = f".clinerules/rules/{mdc_to_cline_name(mdc.name)}"
        cline_path = ROOT / cline_rel
        if not cline_path.is_file():
            errors.append(f"MISSING rule mirror: {cline_rel} (from {mdc.name})")
            continue
        if normalize_for_compare(cline_path.read_text(encoding="utf-8")) != normalize_for_compare(
            read_mdc_body(mdc)
        ):
            errors.append(f"RULE BODY MISMATCH: {cline_rel} != .cursor/rules/{mdc.name}")

    # Skills: byte-identical stubs reference canonical .github/skills
    github_skills = ROOT / ".github/skills"
    for skill_dir in sorted(github_skills.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        stub = ROOT / ".clinerules/skills" / f"{skill_dir.name}.md"
        if not stub.is_file():
            errors.append(f"MISSING Cline skill stub: .clinerules/skills/{skill_dir.name}.md")
            continue
        canonical_rel = f".github/skills/{skill_dir.name}/SKILL.md"
        meta, _ = split_frontmatter(stub.read_text(encoding="utf-8"))
        if meta.get("canonical") != canonical_rel:
            errors.append(
                f"SKILL canonical mismatch in {stub.relative_to(ROOT)}: "
                f"expected {canonical_rel!r}, got {meta.get('canonical')!r}"
            )

    # Agents: .github/agents -> .clinerules/agents (byte-identical)
    github_agents = sorted((ROOT / ".github/agents").glob("*.md"))
    for agent in github_agents:
        mirror = ROOT / ".clinerules/agents" / agent.name
        if not mirror.is_file():
            errors.append(f"MISSING agent mirror: .clinerules/agents/{agent.name}")
        elif file_hash(agent) != file_hash(mirror):
            errors.append(f"AGENT MISMATCH: .clinerules/agents/{agent.name}")

    # Top-level instruction mirrors
    for name in ("AGENTS.md",):
        root_file = ROOT / name
        mirror = ROOT / ".clinerules" / name
        if not mirror.is_file():
            errors.append(f"MISSING: .clinerules/{name}")
        elif file_hash(root_file) != file_hash(mirror):
            errors.append(f"MISMATCH: .clinerules/{name}")

    if errors:
        print("Cline parity check FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Cline parity check passed (.clinerules <-> canonical governance).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
