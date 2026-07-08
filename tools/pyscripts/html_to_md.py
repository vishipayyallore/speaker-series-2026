"""HTML slide deck → Markdown converter (raw extraction).

Extracts slide text from self-contained HTML decks (for example Session 1 slides saved
from a browser). Output is a staging artifact for personal study — synthesize into
original notes under ``src/weekN/01-notes/`` before publishing (Zero-Copy Policy).

Usage (PowerShell):
  uv run python tools/pyscripts/html_to_md.py --input "source-material/week1/04-reading-notes/Session1-Introduction-to-Machine-Learning.html" --output-same-folder

  uv run python tools/pyscripts/html_to_md.py --input source-material --recursive --output-same-folder
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from html import unescape
from pathlib import Path

from _common import is_within

SLIDE_COMMENT = re.compile(r"<!--\s*Slide\s+(\d+):\s*(.*?)\s*-->", re.IGNORECASE | re.DOTALL)


def _clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _strip_noise(html_fragment: str) -> str:
    fragment = re.sub(r"<script[^>]*>.*?</script>", "", html_fragment, flags=re.DOTALL | re.IGNORECASE)
    fragment = re.sub(r"<style[^>]*>.*?</style>", "", fragment, flags=re.DOTALL | re.IGNORECASE)
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.DOTALL)
    return fragment


def _html_fragment_to_markdown(html_fragment: str) -> str:
    fragment = _strip_noise(html_fragment)
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.IGNORECASE)

    replacements: list[tuple[str, str]] = [
        (r"<h1[^>]*>(.*?)</h1>", r"# \1\n"),
        (r"<h2[^>]*>(.*?)</h2>", r"## \1\n"),
        (r"<h3[^>]*>(.*?)</h3>", r"### \1\n"),
        (r"<h4[^>]*>(.*?)</h4>", r"#### \1\n"),
        (r"<li[^>]*>(.*?)</li>", r"- \1\n"),
        (r"<p[^>]*>(.*?)</p>", r"\1\n\n"),
        (r"<img[^>]*alt=\"([^\"]*)\"[^>]*>", r"[image: \1]"),
        (r"<img[^>]*>", r"[image]"),
    ]
    for pattern, repl in replacements:
        fragment = re.sub(pattern, repl, fragment, flags=re.DOTALL | re.IGNORECASE)

    fragment = re.sub(r"</?(?:ul|ol|div|span|section|article|nav|button|strong|em|b|i)[^>]*>", "\n", fragment, flags=re.IGNORECASE)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = unescape(fragment)
    return _clean_text(fragment)


def _extract_slides(html: str) -> list[tuple[int, str, str]]:
    matches = list(SLIDE_COMMENT.finditer(html))
    if not matches:
        return []

    slides: list[tuple[int, str, str]] = []
    for index, match in enumerate(matches):
        slide_num = int(match.group(1))
        slide_title = _clean_text(unescape(re.sub(r"<[^>]+>", "", match.group(2))))
        start = match.end()
        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            script_pos = html.lower().find("<script", start)
            end = script_pos if script_pos != -1 else len(html)
        body_html = html[start:end]
        slides.append((slide_num, slide_title, body_html))
    return slides


def html_to_markdown(input_html: Path, output_md: Path) -> None:
    html = input_html.read_text(encoding="utf-8", errors="replace")
    slides = _extract_slides(html)

    output_md.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now().astimezone()

    lines: list[str] = []
    lines.append(f"# Raw HTML Extract: {input_html.stem}")
    lines.append("")
    lines.append(f"- Source file: `{input_html.name}`")
    lines.append(f"- Slides found: {len(slides)}")
    lines.append(f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}")
    lines.append("")
    lines.append(
        "> This is an automated extraction from an HTML slide deck for personal study. "
        "Please **synthesize** into original notes before publishing to `src/weekN/01-notes/` "
        "to respect the repository's Zero-Copy Policy."
    )

    if not slides:
        lines.append("")
        lines.append("_No `<!-- Slide N: ... -->` markers found; file may use a different layout._")
    else:
        for slide_num, slide_title, body_html in slides:
            body_md = _html_fragment_to_markdown(body_html)
            lines.append("")
            heading = f"Slide {slide_num}"
            if slide_title:
                heading = f"{heading}: {slide_title}"
            lines.append(f"## {heading}")
            lines.append("")
            if body_md:
                lines.append(body_md)

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert HTML slide deck(s) to Markdown (raw extraction).")

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a .html file or a directory containing HTML files",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to write Markdown files (default: docs/exports)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="If input is a directory, search recursively for HTML files.",
    )
    parser.add_argument(
        "--output-same-folder",
        action="store_true",
        help="Write each .md file in the same folder as its source .html (overrides --output-dir).",
    )
    parser.add_argument(
        "--allow-source-material-output",
        action="store_true",
        help=(
            "Allow writing output under source-material/. "
            "(Not recommended; source-material is intended as read-only.)"
        ),
    )
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parents[2]
    source_material_dir = workspace_root / "source-material"

    output_dir = args.output_dir if args.output_dir is not None else workspace_root / "docs" / "exports"

    if is_within(output_dir, source_material_dir) and not args.allow_source_material_output:
        raise SystemExit(
            "Refusing to write output under source-material/. "
            "Pass --allow-source-material-output if you really want this."
        )

    input_path: Path = args.input
    if not input_path.exists():
        raise SystemExit(f"Input path not found: {input_path}")

    html_files: list[Path] = []
    if input_path.is_file():
        if input_path.suffix.lower() not in {".html", ".htm"}:
            raise SystemExit("Input file must be .html or .htm")
        html_files = [input_path]
    else:
        if args.recursive:
            html_files = sorted(set(input_path.rglob("*.html")) | set(input_path.rglob("*.htm")))
        else:
            html_files = sorted(set(input_path.glob("*.html")) | set(input_path.glob("*.htm")))

    if not html_files:
        print(f"No HTML files found at: {input_path}")
        return 0

    for html_file in html_files:
        if args.output_same_folder:
            out_md = html_file.with_suffix(".md")
        else:
            out_md = output_dir / f"{html_file.stem}.md"
        html_to_markdown(html_file, out_md)
        print(f"Wrote Markdown: {out_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
