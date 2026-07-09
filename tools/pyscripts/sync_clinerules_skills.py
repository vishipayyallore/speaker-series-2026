"""One-off sync: .github/skills/*/SKILL.md -> .clinerules/skills/<name>.md"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    skills_root = root / ".github" / "skills"
    out_root = root / ".clinerules" / "skills"
    out_root.mkdir(parents=True, exist_ok=True)

    for skill in sorted(skills_root.rglob("SKILL.md")):
        rel = skill.relative_to(skills_root)
        name = rel.parts[0]
        body = skill.read_text(encoding="utf-8")
        if not body.startswith("---"):
            continue
        end = body.find("---", 3)
        front = body[3:end].strip()
        rest = body[end + 3 :].lstrip()
        canonical = ".github/skills/" + "/".join(rel.parts)
        out = out_root / f"{name}.md"
        out.write_text(f"---\n{front}\ncanonical: \"{canonical}\"\n---\n\n{rest}", encoding="utf-8")
        print(f"synced {out.relative_to(root)}")


if __name__ == "__main__":
    main()
