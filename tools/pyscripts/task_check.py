from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Iterable


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists() or (candidate / "pyproject.toml").exists():
            return candidate
    raise FileNotFoundError("Could not detect repository root from script location.")


def get_hash(filepath: Path) -> str:
    hasher = hashlib.sha256()
    hasher.update(filepath.read_bytes())
    return hasher.hexdigest()


def iter_matches(root: Path, patterns: Iterable[str]) -> Iterable[Path]:
    for pattern in patterns:
        yield from root.glob(pattern)


def build_report(root: Path) -> dict[str, object]:
    md_patterns = [
        "README.md",
        "docs/**/*.md",
        "src/**/*.md",
        "tools/**/*.md",
        "source-material/**/*.md",
    ]
    notebook_patterns = ["src/**/*.ipynb", "source-material/**/*.ipynb"]
    ref_patterns = ["README.md", "docs/**/*.md", "src/**/*.md", "tools/**/*.md"]

    hashes: dict[str, list[str]] = {}
    for path in iter_matches(root, md_patterns):
        if path.is_file():
            digest = get_hash(path)
            hashes.setdefault(digest, []).append(str(path.relative_to(root)))

    duplicates = {digest: paths for digest, paths in hashes.items() if len(paths) > 1}

    notebook_count = 0
    malformed_notebooks: list[str] = []
    for path in iter_matches(root, notebook_patterns):
        if path.is_file():
            notebook_count += 1
            try:
                with path.open("r", encoding="utf-8") as handle:
                    json.load(handle)
            except (json.JSONDecodeError, OSError, UnicodeDecodeError):
                malformed_notebooks.append(str(path.relative_to(root)))

    ext_counts: Counter[str] = Counter()
    source_material = root / "source-material"
    if source_material.exists():
        for path in source_material.rglob("*"):
            if path.is_file():
                ext_counts[path.suffix.lower() or "[no ext]"] += 1

    references: list[str] = []
    for path in iter_matches(root, ref_patterns):
        if path.is_file():
            try:
                if "source-material/" in path.read_text(encoding="utf-8"):
                    references.append(str(path.relative_to(root)))
            except (OSError, UnicodeDecodeError):
                continue

    return {
        "root": str(root),
        "duplicates": duplicates,
        "notebooks": {
            "total_count": notebook_count,
            "malformed": malformed_notebooks,
        },
        "source_material_extensions": dict(ext_counts),
        "source_material_references": references,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run portable repository content checks.")
    default_root = find_repo_root(Path(__file__).resolve().parent)
    parser.add_argument("--root", type=Path, default=default_root, help="Repository root to scan.")
    parser.add_argument("--json", action="store_true", help="Print the report as JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    report = build_report(root)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return

    print("--- DUPLICATES ---")
    for digest, paths in report["duplicates"].items():
        print(f"{digest}: {paths}")

    print("\n--- NOTEBOOKS ---")
    print(f"Total Count: {report['notebooks']['total_count']}")
    print(f"Malformed: {report['notebooks']['malformed']}")

    print("\n--- EXTENSIONS ---")
    for ext, count in report["source_material_extensions"].items():
        print(f"{ext}: {count}")

    print("\n--- REFERENCES ---")
    for ref in report["source_material_references"]:
        print(ref)


if __name__ == "__main__":
    main()
