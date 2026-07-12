"""Fix quiz markdown files that use ```text as both opening and closing fences.

DEPRECATED — Applied Engineering import residue. This repo has no src/weekN layout.
Use tools/psscripts/sync-assistant-mirrors.ps1 for mirror sync instead.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FENCE_OPEN = "```text"
FENCE_MARKERS = ("```text", "```")

ROOTS = [
    REPO_ROOT / "src" / f"week{n}" / layer
    for n in range(1, 14)
    for layer in ("02-quizzes", "04-discussions")
    if (REPO_ROOT / "src" / f"week{n}").is_dir()
]


def fix_file(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    inside = False
    changed = False
    out: list[str] = []

    for line in lines:
        stripped = line.rstrip("\r\n")
        if stripped not in FENCE_MARKERS:
            out.append(line)
            continue

        eol = "\r\n" if line.endswith("\r\n") else ("\n" if line.endswith("\n") else "")

        if not inside:
            if stripped != FENCE_OPEN:
                out.append(line)
                continue
            inside = True
            out.append(line)
            continue

        out.append("```" + eol)
        inside = False
        if stripped != "```":
            changed = True

    if inside:
        raise ValueError(f"Unclosed code block in {path}")

    if changed:
        path.write_text("".join(out), encoding="utf-8", newline="")
    return changed


def main() -> None:
    fixed: list[Path] = []
    for root in ROOTS:
        if not root.is_dir():
            continue
        for path in sorted(root.glob("*.md")):
            if fix_file(path):
                fixed.append(path)

    print(f"Fixed {len(fixed)} file(s):")
    for path in fixed:
        print(f"  {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
