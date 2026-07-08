#!/usr/bin/env python3
"""Sync .clinerules/ from canonical .cursor/.github governance (Machine Learning)."""

from __future__ import annotations

import sys
from pathlib import Path

from _common import format_frontmatter_value, split_frontmatter, yaml_quote

ROOT = Path(__file__).resolve().parents[2]
CLINE = ROOT / ".clinerules"

RULE_MAP: dict[str, str] = {
    "01-swamy-personal-learning-only": "01_swamy_personal_learning_only",
    "02-educational-content-rules": "02_educational-content-rules",
    "03-repository-structure": "03_repository-structure",
    "04-quality-assurance": "04_quality-assurance",
    "05-markdown-standards": "05_markdown-standards",
    "06-primary-directives": "06_primary-directives",
    "07-source-material-rules": "07_source_material_rules",
    "08-file-naming-conventions": "08_file-naming-conventions",
    "09-copilot-instructions-extract": "09_copilot-instructions-extract",
}

SKILL_NAMES = [
    "ci-checks",
    "ml-algorithms-from-scratch",
    "topic-companions",
    "docs-verification",
    "e2e-testing",
    "workspace-review",
]

AGENT_NAMES = [
    "ml-ci-verify",
    "ml-topic-bundle-review",
    "ml-zero-copy-review",
]

STALE_PATHS = [
    ".clinerules/CLINE.md",
    ".clinerules/TODO.md",
    ".clinerules/agents/cline-code-review.md",
    ".clinerules/agents/cline-content-audit.md",
    ".clinerules/agents/cline-quality-check.md",
    ".clinerules/agents/README.md",
    ".clinerules/skills/core-assistant/SKILL.md",
    ".clinerules/skills/file-operations/SKILL.md",
    ".clinerules/skills/code-quality/SKILL.md",
    ".clinerules/skills/content-review/SKILL.md",
    ".clinerules/rules/01_cline_identity.mdc",
    ".clinerules/rules/02_development_guidelines.mdc",
    ".clinerules/rules/03_repository_structure.mdc",
    ".clinerules/rules/04_quality_standards.mdc",
    ".clinerules/rules/05_content_creation.mdc",
]


def read_mdc_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, body = split_frontmatter(text)
        return body
    if "\n---\n" in text:
        return text.split("\n---\n", 1)[1].lstrip("\n")
    return text


def mdc_description(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "\n---\n" in text:
        header = text.split("\n---\n", 1)[0]
    else:
        header = text.split("\n", 3)[0]
    for line in header.splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip()
    return "Rule for Machine Learning"


def write_rule(kebab: str, underscore: str) -> None:
    mdc = ROOT / f".cursor/rules/{underscore}.mdc"
    out = CLINE / "rules" / f"{kebab}.md"
    canonical = f".cursor/rules/{underscore}.mdc"
    desc = mdc_description(mdc)
    body = read_mdc_body(mdc)
    frontmatter = (
        f"---\n"
        f"description: {yaml_quote(desc)}\n"
        f"globs: [\"**/*\"]\n"
        f"tags: [\"dsp\", \"rules\"]\n"
        f"canonical: {canonical}\n"
        f"version: 1.0\n"
        f"---\n"
    )
    out.write_text(frontmatter + "\n" + body.rstrip() + "\n", encoding="utf-8")


def write_skill(skill_name: str) -> None:
    src = ROOT / f".github/skills/{skill_name}/SKILL.md"
    out = CLINE / "skills" / f"{skill_name}.md"
    meta, body = split_frontmatter(src.read_text(encoding="utf-8"))
    lines = ["---"]
    for key in ("name", "description"):
        if key in meta:
            val = format_frontmatter_value(meta[key]) if key == "description" else yaml_quote(meta[key])
            lines.append(f"{key}: {val}")
    lines.append("tags: [\"dsp\", \"skill\", \"" + skill_name + "\"]")
    lines.append(f"canonical: .github/skills/{skill_name}/SKILL.md")
    lines.append("---")
    out.write_text("\n".join(lines) + "\n\n" + body.rstrip() + "\n", encoding="utf-8")


def write_agent(agent_name: str) -> None:
    src = ROOT / f".cursor/agents/{agent_name}.md"
    out = CLINE / "agents" / f"{agent_name}.md"
    meta, body = split_frontmatter(src.read_text(encoding="utf-8"))
    lines = ["---"]
    for key in ("name", "description", "model", "readonly"):
        if key in meta:
            if key == "description":
                lines.append(f"{key}: {format_frontmatter_value(meta[key])}")
            elif key == "readonly":
                lines.append(f"{key}: {meta[key]}")
            else:
                lines.append(f"{key}: {yaml_quote(meta[key])}")
    lines.append("tags: [\"dsp\", \"agent\"]")
    lines.append(f"canonical: .cursor/agents/{agent_name}.md")
    lines.append("---")
    out.write_text("\n".join(lines) + "\n\n" + body.rstrip() + "\n", encoding="utf-8")


def write_skills_readme() -> None:
    header = (
        "# Agent skills (Cline mirror)\n\n"
        "On-demand procedures mirrored from `.github/skills/` (canonical). "
        "Keep aligned when editing policy.\n\n"
    )
    table = "| File | Purpose |\n|------|---------|\n"
    for name in SKILL_NAMES:
        table += f"| `{name}.md` | See `.github/skills/{name}/SKILL.md` |\n"
    (CLINE / "skills" / "README.md").write_text(header + table, encoding="utf-8")


def write_rules_readme() -> None:
    (CLINE / "rules" / "README.md").write_text(
        "# Cline rules index\n\n"
        "Mirrors `.cursor/rules/*.mdc` for Cline. Edit the canonical `.mdc` first, then run "
        "`uv run python tools/pyscripts/sync_clinerules_from_canonical.py`.\n\n"
        "**Note:** Rule bodies mirror `.mdc` files; checked by `verify_clinerules_parity.py` "
        "but not markdownlint-guarded in CI (same as `.cursor/rules/*.mdc`).\n",
        encoding="utf-8",
    )


def remove_stale() -> None:
    for rel in STALE_PATHS:
        path = ROOT / rel
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            import shutil

            shutil.rmtree(path)


def main() -> int:
    (CLINE / "rules").mkdir(parents=True, exist_ok=True)
    (CLINE / "skills").mkdir(parents=True, exist_ok=True)
    (CLINE / "agents").mkdir(parents=True, exist_ok=True)
    (CLINE / "workflows").mkdir(parents=True, exist_ok=True)

    remove_stale()

    for kebab, underscore in RULE_MAP.items():
        write_rule(kebab, underscore)
    for skill in SKILL_NAMES:
        write_skill(skill)
    for agent in AGENT_NAMES:
        write_agent(agent)

    write_rules_readme()
    write_skills_readme()

    print("Synced .clinerules/ from canonical governance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

