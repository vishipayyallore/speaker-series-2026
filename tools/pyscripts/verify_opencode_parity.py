#!/usr/bin/env python3
"""Verify .opencode/ mirrors canonical Cursor/GitHub agent governance files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

RULE_MAP: dict[str, str] = {
    ".opencode/rules/01-swamy-personal-learning-only.md": (
        ".cursor/rules/01_swamy_personal_learning_only.mdc"
    ),
    ".opencode/rules/02-educational-content-rules.md": (
        ".cursor/rules/02_educational-content-rules.mdc"
    ),
    ".opencode/rules/03-repository-structure.md": (
        ".cursor/rules/03_repository-structure.mdc"
    ),
    ".opencode/rules/04-quality-assurance.md": ".cursor/rules/04_quality-assurance.mdc",
    ".opencode/rules/05-markdown-standards.md": ".cursor/rules/05_markdown-standards.mdc",
    ".opencode/rules/06-primary-directives.md": ".cursor/rules/06_primary-directives.mdc",
    ".opencode/rules/07-source-material-rules.md": (
        ".cursor/rules/07_source_material_rules.mdc"
    ),
    ".opencode/rules/08-file-naming-conventions.md": (
        ".cursor/rules/08_file-naming-conventions.mdc"
    ),
    ".opencode/rules/09-copilot-instructions-extract.md": (
        ".cursor/rules/09_copilot-instructions-extract.mdc"
    ),
}

SKILL_MAP: dict[str, str] = {
    ".opencode/skills/ci-checks/SKILL.md": ".github/skills/ci-checks/SKILL.md",
    ".opencode/skills/ml-algorithms-from-scratch/SKILL.md": (
        ".github/skills/ml-algorithms-from-scratch/SKILL.md"
    ),
    ".opencode/skills/topic-companions/SKILL.md": ".github/skills/topic-companions/SKILL.md",
    ".opencode/skills/docs-verification/SKILL.md": ".github/skills/docs-verification/SKILL.md",
    ".opencode/skills/workspace-review/SKILL.md": ".github/skills/workspace-review/SKILL.md",
    ".opencode/skills/e2e-testing/SKILL.md": ".github/skills/e2e-testing/SKILL.md",
}

AGENT_MAP: dict[str, str] = {
    ".opencode/agents/ml-ci-verify.md": ".cursor/agents/ml-ci-verify.md",
    ".opencode/agents/ml-topic-bundle-review.md": (
        ".cursor/agents/ml-topic-bundle-review.md"
    ),
    ".opencode/agents/ml-zero-copy-review.md": ".cursor/agents/ml-zero-copy-review.md",
}

REQUIRED_FILES = [
    ".opencode/README.md",
    *RULE_MAP.keys(),
    *SKILL_MAP.keys(),
    *AGENT_MAP.keys(),
]

FRONTMATTER_KEYS = ("name", "description")


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
        "\u2014": "—",
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


def read_opencode_rule_body(path: Path) -> str:
    return normalize_text(path.read_text(encoding="utf-8"))


def read_canonical_skill_body(path: Path) -> str:
    _, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return normalize_text(body)


def read_opencode_skill_body(path: Path) -> str:
    _, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return normalize_text(body)


def read_canonical_agent_body(path: Path) -> str:
    _, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return normalize_text(body)


def read_opencode_agent_body(path: Path) -> str:
    _, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return normalize_text(body)


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"MISSING required file: {rel}")


def check_rule_parity(opencode_rel: str, canonical_rel: str, errors: list[str]) -> None:
    opencode_body = read_opencode_rule_body(ROOT / opencode_rel)
    canonical_body = read_mdc_body(ROOT / canonical_rel)
    if normalize_for_compare(opencode_body) != normalize_for_compare(canonical_body):
        errors.append(f"RULE BODY MISMATCH: {opencode_rel} != {canonical_rel}")


def check_skill_parity(opencode_rel: str, canonical_rel: str, errors: list[str]) -> None:
    opencode_meta, _ = split_frontmatter((ROOT / opencode_rel).read_text(encoding="utf-8"))
    canonical_meta, _ = split_frontmatter((ROOT / canonical_rel).read_text(encoding="utf-8"))
    for key in FRONTMATTER_KEYS:
        if key in canonical_meta and opencode_meta.get(key) != canonical_meta.get(key):
            errors.append(
                f"SKILL FRONTMATTER {key} mismatch in {opencode_rel}: "
                f"opencode={opencode_meta.get(key)!r} canonical={canonical_meta.get(key)!r}"
            )
    if normalize_for_compare(read_opencode_skill_body(ROOT / opencode_rel)) != normalize_for_compare(
        read_canonical_skill_body(ROOT / canonical_rel)
    ):
        errors.append(f"SKILL BODY MISMATCH: {opencode_rel} != {canonical_rel}")


def check_agent_parity(opencode_rel: str, canonical_rel: str, errors: list[str]) -> None:
    if normalize_for_compare(read_opencode_agent_body(ROOT / opencode_rel)) != normalize_for_compare(
        read_canonical_agent_body(ROOT / canonical_rel)
    ):
        errors.append(f"AGENT BODY MISMATCH: {opencode_rel} != {canonical_rel}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    for opencode_rel, canonical_rel in RULE_MAP.items():
        check_rule_parity(opencode_rel, canonical_rel, errors)
    for opencode_rel, canonical_rel in SKILL_MAP.items():
        check_skill_parity(opencode_rel, canonical_rel, errors)
    for opencode_rel, canonical_rel in AGENT_MAP.items():
        check_agent_parity(opencode_rel, canonical_rel, errors)

    if errors:
        print("OpenCode parity check FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("OpenCode parity check passed (.opencode <-> canonical governance).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

