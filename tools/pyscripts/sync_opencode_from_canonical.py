#!/usr/bin/env python3
"""One-way sync: canonical governance -> .opencode/ (OpenCode layout)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

RULE_MAP: dict[str, str] = {
    ".opencode/rules/01-educational-content-rules.md": ".cursor/rules/01_educational-content-rules.mdc",
    ".opencode/rules/02-repository-structure.md": ".cursor/rules/02_repository-structure.mdc",
    ".opencode/rules/03-quality-assurance.md": ".cursor/rules/03_quality-assurance.mdc",
    ".opencode/rules/04-markdown-standards.md": ".cursor/rules/04_markdown-standards.mdc",
    ".opencode/rules/05-primary-directives.md": ".cursor/rules/05_primary-directives.mdc",
    ".opencode/rules/06-external-curriculum-rules.md": ".cursor/rules/06_external_curriculum_rules.mdc",
    ".opencode/rules/07-file-naming-conventions.md": ".cursor/rules/07_file-naming-conventions.mdc",
    ".opencode/rules/08-copilot-instructions-extract.md": ".cursor/rules/08_copilot-instructions-extract.mdc",
    ".opencode/rules/09-core-agent-role.md": ".cursor/rules/09_core-agent-role.mdc",
    ".opencode/rules/project-scope.md": ".cursor/rules/project-scope.mdc",
}

SKILL_MAP: dict[str, str] = {
    ".opencode/skills/ci-checks/SKILL.md": ".github/skills/ci-checks/SKILL.md",
    ".opencode/skills/speaker-series/SKILL.md": ".github/skills/speaker-series/SKILL.md",
    ".opencode/skills/workspace-review/SKILL.md": ".github/skills/workspace-review/SKILL.md",
}

AGENT_MAP: dict[str, str] = {
    ".opencode/agents/agent-ci-verify.md": ".github/agents/agent-ci-verify.md",
    ".opencode/agents/docs-originality-review.md": ".github/agents/docs-originality-review.md",
    ".opencode/agents/talk-content-review.md": ".github/agents/talk-content-review.md",
}

OBSOLETE_PATHS = [
    ".opencode/rules/swamy-personal-learning-only.md",
    ".opencode/rules/06-source-material-rules.md",
    ".opencode/agents/ml-notebook-audit.md",
    ".opencode/agents/ml-ci-verify.md",
    ".opencode/agents/ml-topic-bundle-review.md",
    ".opencode/agents/ml-zero-copy-review.md",
    ".opencode/skills/notebook-validate/SKILL.md",
    ".opencode/skills/ml-algorithms-from-scratch/SKILL.md",
    ".opencode/skills/topic-companions/SKILL.md",
    ".opencode/skills/docs-verification/SKILL.md",
    ".opencode/skills/e2e-testing/SKILL.md",
]


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


def read_mdc_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip("\n")
    if "\n---\n" in text:
        return text.split("\n---\n", 1)[1].lstrip("\n")
    return text.lstrip("\n")


def write_rule(opencode_rel: str, canonical_rel: str) -> None:
    body = read_mdc_body(ROOT / canonical_rel)
    dest = ROOT / opencode_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body, encoding="utf-8", newline="\n")


def write_skill(opencode_rel: str, canonical_rel: str) -> None:
    dest = ROOT / opencode_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text((ROOT / canonical_rel).read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def write_agent(opencode_rel: str, canonical_rel: str) -> None:
    dest = ROOT / opencode_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text((ROOT / canonical_rel).read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def remove_obsolete() -> list[str]:
    removed: list[str] = []
    for rel in OBSOLETE_PATHS:
        path = ROOT / rel
        if path.is_file():
            path.unlink()
            removed.append(rel)
        elif path.parent.exists() and rel.endswith("/SKILL.md") is False:
            pass
    notebook_dir = ROOT / ".opencode/skills/notebook-validate"
    if notebook_dir.is_dir():
        for child in notebook_dir.iterdir():
            child.unlink()
        notebook_dir.rmdir()
        removed.append(".opencode/skills/notebook-validate/")
    return removed


def main() -> int:
    for opencode_rel, canonical_rel in RULE_MAP.items():
        write_rule(opencode_rel, canonical_rel)
    for opencode_rel, canonical_rel in SKILL_MAP.items():
        write_skill(opencode_rel, canonical_rel)
    for opencode_rel, canonical_rel in AGENT_MAP.items():
        write_agent(opencode_rel, canonical_rel)
    removed = remove_obsolete()
    print("Synced .opencode/ from canonical governance.")
    if removed:
        print("Removed obsolete paths:")
        for rel in removed:
            print(f"  - {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

