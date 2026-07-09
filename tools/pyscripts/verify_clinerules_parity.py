#!/usr/bin/env python3
"""Verify .clinerules/ mirrors canonical Cursor/GitHub agent governance files."""

from __future__ import annotations

import sys
from pathlib import Path

from _common import split_frontmatter

ROOT = Path(__file__).resolve().parents[2]

RULE_MAP: dict[str, str] = {
    ".clinerules/rules/01-swamy-personal-learning-only.md": (
        ".cursor/rules/01_swamy_personal_learning_only.mdc"
    ),
    ".clinerules/rules/02-educational-content-rules.md": (
        ".cursor/rules/02_educational-content-rules.mdc"
    ),
    ".clinerules/rules/03-repository-structure.md": (
        ".cursor/rules/03_repository-structure.mdc"
    ),
    ".clinerules/rules/04-quality-assurance.md": ".cursor/rules/04_quality-assurance.mdc",
    ".clinerules/rules/05-markdown-standards.md": ".cursor/rules/05_markdown-standards.mdc",
    ".clinerules/rules/06-primary-directives.md": ".cursor/rules/06_primary-directives.mdc",
    ".clinerules/rules/07-source-material-rules.md": (
        ".cursor/rules/07_source_material_rules.mdc"
    ),
    ".clinerules/rules/08-file-naming-conventions.md": (
        ".cursor/rules/08_file-naming-conventions.mdc"
    ),
    ".clinerules/rules/09-copilot-instructions-extract.md": (
        ".cursor/rules/09_copilot-instructions-extract.mdc"
    ),
}

SKILL_MAP: dict[str, str] = {
    ".clinerules/skills/ci-checks.md": ".github/skills/ci-checks/SKILL.md",
    ".clinerules/skills/ml-algorithms-from-scratch.md": (
        ".github/skills/ml-algorithms-from-scratch/SKILL.md"
    ),
    ".clinerules/skills/topic-companions.md": ".github/skills/topic-companions/SKILL.md",
    ".clinerules/skills/docs-verification.md": ".github/skills/docs-verification/SKILL.md",
    ".clinerules/skills/e2e-testing.md": ".github/skills/e2e-testing/SKILL.md",
    ".clinerules/skills/workspace-review.md": ".github/skills/workspace-review/SKILL.md",
}

AGENT_MAP: dict[str, str] = {
    ".clinerules/agents/ml-ci-verify.md": ".cursor/agents/ml-ci-verify.md",
    ".clinerules/agents/ml-topic-bundle-review.md": (
        ".cursor/agents/ml-topic-bundle-review.md"
    ),
    ".clinerules/agents/ml-zero-copy-review.md": ".cursor/agents/ml-zero-copy-review.md",
}

WORKFLOW_FILES = [
    ".clinerules/workflows/run-ci-checks.md",
    ".clinerules/workflows/topic-bundle-review.md",
    ".clinerules/workflows/zero-copy-review.md",
    ".clinerules/workflows/workspace-review.md",
]

REQUIRED_FILES = [
    ".clinerules/README.md",
    ".clinerules/AGENTS.md",
    ".clinerules/ml-core-context.md",
    ".clinerules/rules/README.md",
    ".clinerules/skills/README.md",
    *RULE_MAP.keys(),
    *SKILL_MAP.keys(),
    *AGENT_MAP.keys(),
    *WORKFLOW_FILES,
]

PATH_ALIASES: list[tuple[str, str]] = [
    (".clinerules/rules/09-copilot-instructions-extract.md", (
        ".cursor/rules/09_copilot-instructions-extract.mdc"
    )),
    (".clinerules/rules/08-file-naming-conventions.md", (
        ".cursor/rules/08_file-naming-conventions.mdc"
    )),
    (".clinerules/rules/07-source-material-rules.md", (
        ".cursor/rules/07_source_material_rules.mdc"
    )),
    (".clinerules/rules/06-primary-directives.md", ".cursor/rules/06_primary-directives.mdc"),
    (".clinerules/rules/05-markdown-standards.md", ".cursor/rules/05_markdown-standards.mdc"),
    (".clinerules/rules/04-quality-assurance.md", ".cursor/rules/04_quality-assurance.mdc"),
    (".clinerules/rules/03-repository-structure.md", ".cursor/rules/03_repository-structure.mdc"),
    (".clinerules/rules/02-educational-content-rules.md", (
        ".cursor/rules/02_educational-content-rules.mdc"
    )),
    (".clinerules/rules/01-swamy-personal-learning-only.md", (
        ".cursor/rules/01_swamy_personal_learning_only.mdc"
    )),
    (".clinerules/skills/workspace-review.md", ".github/skills/workspace-review/SKILL.md"),
    (".clinerules/skills/topic-companions.md", ".github/skills/topic-companions/SKILL.md"),
    (".clinerules/skills/docs-verification.md", ".github/skills/docs-verification/SKILL.md"),
    (".clinerules/skills/ml-algorithms-from-scratch.md", (
        ".github/skills/ml-algorithms-from-scratch/SKILL.md"
    )),
    (".clinerules/skills/ci-checks.md", ".github/skills/ci-checks/SKILL.md"),
    (".clinerules/agents/ml-zero-copy-review.md", ".cursor/agents/ml-zero-copy-review.md"),
    (".clinerules/agents/ml-topic-bundle-review.md", (
        ".cursor/agents/ml-topic-bundle-review.md"
    )),
    (".clinerules/agents/ml-ci-verify.md", ".cursor/agents/ml-ci-verify.md"),
    (".clinerules/workflows/workspace-review.md", ".clinerules/workflows/workspace-review.md"),
    (".clinerules/workflows/run-ci-checks.md", ".clinerules/workflows/run-ci-checks.md"),
]

AGENT_BODY_ALIASES: list[tuple[str, str]] = [
    (".clinerules/skills/ci-checks.md", ".github/skills/ci-checks/SKILL.md"),
    (".clinerules/skills/topic-companions.md", ".github/skills/topic-companions/SKILL.md"),
    ("(agent)", "(subagent)"),
    ("in this agent unless", "in this subagent unless"),
    ("When invoked, Swamy should name", "When invoked, the parent should name"),
    ("Swamy supplies one or more paths", "The parent supplies one or more paths"),
]

FRONTMATTER_KEYS = ("name", "description", "readonly")


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


def apply_aliases(text: str, aliases: list[tuple[str, str]]) -> str:
    for old, new in aliases:
        text = text.replace(old, new)
    return text


def read_body(path: Path, aliases: list[tuple[str, str]] = PATH_ALIASES) -> str:
    _, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return normalize_text(apply_aliases(body, aliases))


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    meta, _ = split_frontmatter(text)
    return meta


def read_canonical_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, body = split_frontmatter(text)
        return normalize_text(body)
    if "\n---\n" in text:
        body = text.split("\n---\n", 1)[1]
        return normalize_text(body.lstrip("\n"))
    return normalize_text(text)


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"MISSING required file: {rel}")


def check_canonical_field(
    clinerules_rel: str,
    canonical_rel: str,
    errors: list[str],
) -> None:
    path = ROOT / clinerules_rel
    meta = parse_frontmatter(path)
    actual = meta.get("canonical", "")
    if actual != canonical_rel:
        errors.append(
            f"CANONICAL FIELD mismatch in {clinerules_rel}: "
            f"expected {canonical_rel!r}, got {actual!r}"
        )


def check_body_parity(
    clinerules_rel: str,
    canonical_rel: str,
    errors: list[str],
    extra_aliases: list[tuple[str, str]] | None = None,
) -> None:
    clinerules_body = read_body(ROOT / clinerules_rel, PATH_ALIASES)
    canonical_body = read_canonical_body(ROOT / canonical_rel)
    if extra_aliases:
        clinerules_body = apply_aliases(clinerules_body, extra_aliases)
    if normalize_for_compare(clinerules_body) != normalize_for_compare(canonical_body):
        errors.append(f"BODY MISMATCH: {clinerules_rel} != {canonical_rel}")


def check_frontmatter_keys(
    clinerules_rel: str,
    canonical_rel: str,
    errors: list[str],
) -> None:
    clinerules_meta = parse_frontmatter(ROOT / clinerules_rel)
    canonical_meta = parse_frontmatter(ROOT / canonical_rel)
    for key in FRONTMATTER_KEYS:
        if key in canonical_meta and clinerules_meta.get(key) != canonical_meta.get(key):
            errors.append(
                f"FRONTMATTER {key} mismatch in {clinerules_rel}: "
                f"clinerules={clinerules_meta.get(key)!r} "
                f"canonical={canonical_meta.get(key)!r}"
            )


def check_skills_readme(errors: list[str]) -> None:
    github_readme = (ROOT / ".github/skills/README.md").read_text(encoding="utf-8")
    clinerules_readme = (ROOT / ".clinerules/skills/README.md").read_text(encoding="utf-8")
    for skill_name in ("ci-checks", "ml-algorithms-from-scratch", "topic-companions"):
        if skill_name not in clinerules_readme:
            errors.append(f".clinerules/skills/README.md missing skill entry: {skill_name}")
    if "ci-checks" not in github_readme:
        errors.append(".github/skills/README.md missing ci-checks entry (unexpected)")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)

    for clinerules_rel, canonical_rel in RULE_MAP.items():
        check_canonical_field(clinerules_rel, canonical_rel, errors)
        check_body_parity(clinerules_rel, canonical_rel, errors)

    for clinerules_rel, canonical_rel in SKILL_MAP.items():
        check_canonical_field(clinerules_rel, canonical_rel, errors)
        check_frontmatter_keys(clinerules_rel, canonical_rel, errors)
        check_body_parity(clinerules_rel, canonical_rel, errors)

    for clinerules_rel, canonical_rel in AGENT_MAP.items():
        check_canonical_field(clinerules_rel, canonical_rel, errors)
        check_frontmatter_keys(clinerules_rel, canonical_rel, errors)
        check_body_parity(
            clinerules_rel,
            canonical_rel,
            errors,
            extra_aliases=AGENT_BODY_ALIASES,
        )

    check_skills_readme(errors)

    if errors:
        print("Cline rules parity check FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Cline rules parity check passed (.clinerules <-> canonical governance).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

