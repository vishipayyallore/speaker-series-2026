"""Generate docs/reviews/source-material-coverage-auto.csv overlap audit.

Heuristic: for each source-material markdown file, count how many normalized
word n-grams (n=6) from the source appear in the combined src/**/*.md corpus.
Higher ApproxMatches suggests more textual overlap (synthesis or shared boilerplate).
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists() or (candidate / "pyproject.toml").exists():
            return candidate
    raise FileNotFoundError("Could not detect repository root.")


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def word_ngrams(text: str, n: int = 6) -> set[str]:
    words = normalize(text).split()
    if len(words) < n:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i : i + n]) for i in range(len(words) - n + 1)}


def key_from_path(rel: str) -> str:
    name = Path(rel).stem
    name = re.sub(r"[_\-]+", " ", name)
    name = re.sub(r"\bweek\s*\d+(\.\d+)*\b", "", name, flags=re.I)
    name = re.sub(r"\bpractice quiz\b", "", name, flags=re.I)
    return re.sub(r"\s+", " ", name).strip()[:60]


def main() -> None:
    root = find_repo_root(Path(__file__).resolve().parent)
    source_root = root / "source-material"
    out_path = root / "docs" / "reviews" / "source-material-coverage-auto.csv"

    src_text = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in sorted((root / "src").rglob("*.md"))
        if p.is_file()
    )
    src_norm = normalize(src_text)

    rows: list[tuple[str, str, int]] = []
    for path in sorted(source_root.rglob("*.md")):
        if not path.is_file():
            continue
        rel = str(path.relative_to(root)).replace("/", "\\")
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        grams = word_ngrams(content, n=6)
        matches = sum(1 for g in grams if g in src_norm)
        rows.append((rel, key_from_path(rel), matches))

    rows.sort(key=lambda r: r[2])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, quoting=csv.QUOTE_ALL)
        writer.writerow(["Source", "Key", "ApproxMatches"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path.relative_to(root)}")


if __name__ == "__main__":
    main()
