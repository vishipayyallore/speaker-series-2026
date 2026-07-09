"""DOCX/DOC → Markdown converter (raw extraction).

Extracts paragraph and table text from Word documents for *personal study*.
Treat output as a staging artifact — synthesize into original notes under
``src/weekN/01-notes/`` before publishing (Zero-Copy Policy).

- ``.docx`` — extracted with ``python-docx``
- ``.doc``  — pandoc first; on Windows falls back to Word COM → docx when pandoc cannot read legacy DOC

Usage (PowerShell):
  uv run python tools/pyscripts/docx_to_md.py --input source-material --recursive --output-same-folder

  uv run python tools/pyscripts/docx_to_md.py --input "source-material\\universitynotes\\file.docx" --output-same-folder
"""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from _common import is_within

try:
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    HAS_PYTHON_DOCX = True
except ImportError:
    HAS_PYTHON_DOCX = False


def _clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip()


def _heading_level(style_name: str) -> int | None:
    name = (style_name or "").strip().lower()
    if name.startswith("heading"):
        suffix = name.removeprefix("heading").strip()
        if suffix.isdigit():
            return min(int(suffix), 6)
        return 2
    if name in {"title"}:
        return 1
    return None


def _paragraph_to_markdown(paragraph: Paragraph) -> str:
    text = _clean_text(paragraph.text or "")
    if not text:
        return ""
    level = _heading_level(getattr(paragraph.style, "name", "") or "")
    if level is not None:
        return f"{'#' * level} {text}"
    return text


def _table_to_markdown(table: Table) -> list[str]:
    rows: list[list[str]] = []
    for row in table.rows:
        cells = [_clean_text(cell.text or "").replace("|", "\\|") for cell in row.cells]
        if any(cells):
            rows.append(cells)

    if not rows:
        return []

    col_count = max(len(row) for row in rows)
    normalized = [row + [""] * (col_count - len(row)) for row in rows]

    header = normalized[0]
    sep = ["---"] * col_count
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    for row in normalized[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def _iter_block_items(document: Document):
    """Yield paragraphs and tables in document order."""
    from docx.oxml.table import CT_Tbl
    from docx.oxml.text.paragraph import CT_P

    parent = document.element.body
    for child in parent.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def docx_to_markdown(input_docx: Path, output_md: Path) -> None:
    if not HAS_PYTHON_DOCX:
        raise ImportError("python-docx is required. Run: uv sync")

    document = Document(str(input_docx))
    output_md.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now().astimezone()

    lines: list[str] = []
    lines.append(f"# Raw DOCX Extract: {input_docx.stem}")
    lines.append("")
    lines.append(f"- Source file: `{input_docx.name}`")
    lines.append(f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}")
    lines.append("")
    lines.append(
        "> This is an automated extraction from a DOCX for personal study. "
        "Please **synthesize** into original notes before publishing to `src/weekN/01-notes/` "
        "to respect the repository's Zero-Copy Policy."
    )

    for block in _iter_block_items(document):
        if isinstance(block, Paragraph):
            md = _paragraph_to_markdown(block)
            if md:
                lines.append("")
                lines.append(md)
        elif isinstance(block, Table):
            table_md = _table_to_markdown(block)
            if table_md:
                lines.append("")
                lines.append("**Table**")
                lines.extend(table_md)

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def doc_to_markdown_via_pandoc(input_doc: Path, output_md: Path) -> None:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        raise RuntimeError(
            f"Pandoc not found on PATH; cannot convert legacy .doc file: {input_doc.name}. "
            "Install pandoc (https://pandoc.org/) or convert the file to .docx manually."
        )

    output_md.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [pandoc, str(input_doc), "-f", "doc", "-t", "markdown", "-o", str(output_md)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        raise RuntimeError(f"Pandoc failed for {input_doc.name}: {stderr or 'unknown error'}")

    now = dt.datetime.now().astimezone()
    body = output_md.read_text(encoding="utf-8")
    header = "\n".join(
        [
            f"# Raw DOC Extract: {input_doc.stem}",
            "",
            f"- Source file: `{input_doc.name}`",
            f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}",
            "- Converter: pandoc",
            "",
            "> This is an automated extraction from a DOC for personal study. "
            "Please **synthesize** into original notes before publishing to `src/weekN/01-notes/` "
            "to respect the repository's Zero-Copy Policy.",
            "",
        ]
    )
    output_md.write_text(header + body.lstrip(), encoding="utf-8")


def doc_to_docx_via_word_com(input_doc: Path, output_docx: Path) -> None:
    """Convert legacy .doc to .docx using Microsoft Word (Windows + Word required)."""
    if sys.platform != "win32":
        raise RuntimeError("Word COM conversion is only available on Windows.")

    input_doc = input_doc.resolve()
    output_docx = output_docx.resolve()
    output_docx.parent.mkdir(parents=True, exist_ok=True)

    ps_script = f"""
$ErrorActionPreference = 'Stop'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {{
    $doc = $word.Documents.Open('{input_doc}')
    try {{
        $doc.SaveAs2('{output_docx}', 16)
    }} finally {{
        $doc.Close()
    }}
}} finally {{
    $word.Quit()
}}
"""
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps_script],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0 or not output_docx.exists():
        stderr = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(
            f"Word COM conversion failed for {input_doc.name}. "
            f"Is Microsoft Word installed? {stderr}"
        )


def doc_to_markdown(input_doc: Path, output_md: Path) -> None:
    """Convert legacy .doc via pandoc, or Word COM → docx → markdown."""
    try:
        doc_to_markdown_via_pandoc(input_doc, output_md)
        return
    except RuntimeError as pandoc_error:
        if sys.platform != "win32":
            raise pandoc_error

    with tempfile.TemporaryDirectory() as tmp:
        temp_docx = Path(tmp) / f"{input_doc.stem}.docx"
        doc_to_docx_via_word_com(input_doc, temp_docx)
        docx_to_markdown(temp_docx, output_md)

    now = dt.datetime.now().astimezone()
    body = output_md.read_text(encoding="utf-8")
    if body.startswith("# Raw DOCX Extract:"):
        body = body.split("\n", 1)[1]
    header = "\n".join(
        [
            f"# Raw DOC Extract: {input_doc.stem}",
            "",
            f"- Source file: `{input_doc.name}`",
            f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}",
            "- Converter: Word COM → docx → python-docx",
            "",
            "> This is an automated extraction from a DOC for personal study. "
            "Please **synthesize** into original notes before publishing to `src/weekN/01-notes/` "
            "to respect the repository's Zero-Copy Policy.",
            "",
        ]
    )
    output_md.write_text(header + body.lstrip(), encoding="utf-8")


def convert_word_file(input_path: Path, output_md: Path) -> None:
    suffix = input_path.suffix.lower()
    if suffix == ".docx":
        docx_to_markdown(input_path, output_md)
    elif suffix == ".doc":
        doc_to_markdown(input_path, output_md)
    else:
        raise ValueError(f"Unsupported Word format: {suffix}")


def collect_word_files(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file():
        suffix = input_path.suffix.lower()
        if suffix not in {".docx", ".doc"}:
            raise SystemExit("Input file must be .docx or .doc")
        return [input_path]

    patterns = ("**/*.docx", "**/*.doc") if recursive else ("*.docx", "*.doc")
    files: list[Path] = []
    for pattern in patterns:
        files.extend(input_path.glob(pattern))
    return sorted(set(files))


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert DOCX/DOC file(s) to Markdown (raw extraction).")
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a .docx/.doc file or a directory containing Word files",
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
        help="If input is a directory, search recursively for Word files.",
    )
    parser.add_argument(
        "--output-same-folder",
        action="store_true",
        help="Write each .md file in the same folder as its source Word file (overrides --output-dir).",
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

    word_files = collect_word_files(input_path, args.recursive)
    if not word_files:
        print(f"No .docx or .doc files found at: {input_path}")
        return 0

    failures: list[str] = []
    for word_file in word_files:
        out_md = word_file.with_suffix(".md") if args.output_same_folder else output_dir / f"{word_file.stem}.md"
        try:
            convert_word_file(word_file, out_md)
            print(f"Wrote Markdown: {out_md}")
        except Exception as exc:
            failures.append(f"{word_file.name}: {exc}")
            print(f"Skipped {word_file.name}: {exc}")

    if failures and len(failures) == len(word_files):
        raise SystemExit("All Word conversions failed:\n" + "\n".join(failures))

    if failures:
        print("\nWarnings:")
        for item in failures:
            print(f"  - {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
