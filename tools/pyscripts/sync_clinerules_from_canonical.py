#!/usr/bin/env python3
"""Sync .clinerules/ from canonical Speaker Series governance."""

from __future__ import annotations

import sys
from pathlib import Path

from _common import format_frontmatter_value, split_frontmatter, yaml_quote

ROOT = Path(__file__).resolve().parents[2]
CLINE = ROOT / ".clinerules"

RULE_MAP: dict[str, str] = {
    "01-educational-content-rules": "01_educational-content-rules",
    "02-repository-structure": "02_repository-structure",
    "03-quality-assurance": "03_quality-assurance",
    "04-markdown-standards": "04_markdown-standards",
    "05-primary-directives": "05_primary-directives",
    "06-external-curriculum-rules": "06_external_curriculum_rules",
    "07-file-naming-conventions": "07_file-naming-conventions",
    "08-copilot-instructions-extract": "08_copilot-instructions-extract",
    "09-core-agent-role": "09_core-agent-role",
    "project-scope": "project-scope",
}

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
    ".clinerules/rules/06-source-material-rules.md",
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
    return "Rule for Speaker Series 2026"


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
    src = ROOT / f".github/agents/{agent_name}.md"
    out = CLINE / "agents" / f"{agent_name}.md"
    out.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


def write_skills_readme() -> None:
    header = (
        "# Agent skills (Cline mirror)\n\n"
        "On-demand procedures mirrored from `.github/skills/` (canonical). "
        "Keep aligned when editing policy.\n\n"
    )
    table = "| File | Purpose |\n|------|---------|\n"
    for skill_dir in sorted((ROOT / ".github/skills").iterdir()):
        if not skill_dir.is_dir():
            continue
        name = skill_dir.name
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
    for skill_dir in sorted((ROOT / ".github/skills").iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
            write_skill(skill_dir.name)
    for agent in sorted((ROOT / ".github/agents").glob("*.md")):
        write_agent(agent.stem)

    write_rules_readme()
    write_skills_readme()

    print("Synced .clinerules/ from canonical governance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

