"""PDF → Markdown converter (raw extraction, optional OCR).

This script extracts text from a PDF into Markdown for *personal study*.
In this repo, treat the output as a staging artifact: synthesize into your
own words before publishing as reading notes to respect the Zero-Copy Policy.

Usage (PowerShell):
  # Colocated .md next to each .pdf (recommended for PDFs under source-material):
  uv run python tools/pyscripts/pdf_to_md.py --input source-material --recursive --output-same-folder

  # Image-only / scanned PDFs (requires Tesseract on PATH or standard Windows install):
  uv run python tools/pyscripts/pdf_to_md.py --input path/to/scanned.pdf --output-same-folder --ocr

  # OCR only when pypdf returns no body text:
  uv run python tools/pyscripts/pdf_to_md.py --input source-material --recursive --output-same-folder --ocr-when-empty

Defaults:
- Without ``--output-same-folder``: output goes to ``docs/exports/<pdf-stem>.md``
- With ``--output-same-folder``: each ``<name>.md`` is written beside ``<name>.pdf``
- Writing under ``source-material/`` via ``--output-dir`` requires
  ``--allow-source-material-output``; ``--output-same-folder`` writes next to each PDF
  (including under source-material) without that flag.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import shutil
from pathlib import Path

import fitz
from pypdf import PdfReader


def _is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def _clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip()


def _configure_tesseract() -> None:
    """Set TESSDATA_PREFIX when Tesseract is installed in a common Windows location."""
    if shutil.which("tesseract"):
        return

    candidates = [
        Path(os.environ.get("TESSERACT_HOME", "")),
        Path(os.environ["LOCALAPPDATA"]) / "Programs" / "Tesseract-OCR",
        Path(r"C:\Program Files\Tesseract-OCR"),
        Path(r"C:\Program Files (x86)\Tesseract-OCR"),
    ]
    for base in candidates:
        exe = base / "tesseract.exe"
        if exe.is_file():
            os.environ["PATH"] = str(base) + os.pathsep + os.environ.get("PATH", "")
            tessdata = base / "tessdata"
            if tessdata.is_dir():
                os.environ.setdefault("TESSDATA_PREFIX", str(tessdata))
            return


def _pypdf_page_text(reader: PdfReader, page_index: int) -> str:
    try:
        raw = reader.pages[page_index].extract_text() or ""
    except Exception:
        raw = ""
    return _clean_text(raw)


def _ocr_page_text(doc: fitz.Document, page_index: int, dpi: int) -> str:
    page = doc[page_index]
    # PyMuPDF/Tesseract can emit noisy layout warnings directly on the native stderr file
    # descriptor even when OCR succeeds. Keep the batch output readable and rely on the
    # extracted Markdown content as the real signal.
    stderr_fd = 2
    saved_stderr = os.dup(stderr_fd)
    try:
        with open(os.devnull, "w", encoding="utf-8") as devnull:
            os.dup2(devnull.fileno(), stderr_fd)
            textpage = page.get_textpage_ocr(dpi=dpi, full=True)
    finally:
        os.dup2(saved_stderr, stderr_fd)
        os.close(saved_stderr)
    return _clean_text(page.get_text(textpage=textpage) or "")


def _extract_pages(
    input_pdf: Path,
    *,
    use_ocr: bool,
    ocr_when_empty: bool,
    ocr_dpi: int,
) -> tuple[list[str], str]:
    reader = PdfReader(str(input_pdf))
    page_count = len(reader.pages)

    pypdf_texts: list[str] = []
    for i in range(page_count):
        pypdf_texts.append(_pypdf_page_text(reader, i))

    total_pypdf = sum(len(t) for t in pypdf_texts)
    need_ocr = use_ocr or (ocr_when_empty and total_pypdf == 0)

    if not need_ocr:
        return pypdf_texts, "pypdf"

    _configure_tesseract()
    if not shutil.which("tesseract"):
        raise SystemExit(
            "OCR requested but Tesseract was not found. Install Tesseract OCR and ensure "
            "tesseract.exe is on PATH, or set TESSERACT_HOME."
        )

    doc = fitz.open(str(input_pdf))
    ocr_texts: list[str] = []
    try:
        for i in range(len(doc)):
            ocr_texts.append(_ocr_page_text(doc, i, ocr_dpi))
    finally:
        doc.close()

    return ocr_texts, f"pymupdf+tesseract@{ocr_dpi}dpi"


def pdf_to_markdown(
    input_pdf: Path,
    output_md: Path,
    *,
    use_ocr: bool = False,
    ocr_when_empty: bool = False,
    ocr_dpi: int = 300,
) -> str:
    page_texts, method = _extract_pages(
        input_pdf,
        use_ocr=use_ocr,
        ocr_when_empty=ocr_when_empty,
        ocr_dpi=ocr_dpi,
    )

    output_md.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now().astimezone()

    lines: list[str] = []
    title_suffix = " (OCR)" if method != "pypdf" else ""
    lines.append(f"# Raw PDF Extract{title_suffix}: {input_pdf.stem}")
    lines.append("")
    lines.append(f"- Source file: `{input_pdf.name}`")
    lines.append(f"- Pages: {len(page_texts)}")
    lines.append(f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}")
    lines.append(f"- Method: {method}")
    lines.append("")
    lines.append(
        "> This is an automated extraction from a PDF for personal study. "
        "Please **synthesize** into original notes before publishing to `src/weekN/01-notes/` "
        "to respect the repository's Zero-Copy Policy."
    )

    for page_index, text in enumerate(page_texts, start=1):
        lines.append("")
        lines.append(f"## Page {page_index}")
        lines.append("")
        if text:
            lines.extend(text.split("\n"))
        else:
            lines.append("_(no extractable text)_")

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return method


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert PDF(s) to Markdown (raw extraction, optional OCR).")

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a .pdf file or a directory containing PDFs",
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
        help="If input is a directory, search recursively for PDFs.",
    )

    parser.add_argument(
        "--output-same-folder",
        action="store_true",
        help="Write each .md file in the same folder as its source .pdf (overrides --output-dir).",
    )

    parser.add_argument(
        "--allow-source-material-output",
        action="store_true",
        help=(
            "Allow writing output under source-material/. "
            "(Not recommended; source-material is intended as read-only.)"
        ),
    )

    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Force OCR via PyMuPDF + Tesseract for every page.",
    )

    parser.add_argument(
        "--ocr-when-empty",
        action="store_true",
        help="Use OCR only when pypdf extracts zero characters across all pages.",
    )

    parser.add_argument(
        "--ocr-dpi",
        type=int,
        default=300,
        help="Render DPI for OCR (default: 300).",
    )

    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parents[2]
    source_material_dir = workspace_root / "source-material"

    output_dir: Path
    if args.output_dir is None:
        output_dir = workspace_root / "docs" / "exports"
    else:
        output_dir = args.output_dir

    if _is_within(output_dir, source_material_dir) and not args.allow_source_material_output:
        raise SystemExit(
            "Refusing to write output under source-material/. "
            "Pass --allow-source-material-output if you really want this."
        )

    input_path: Path = args.input
    if not input_path.exists():
        raise SystemExit(f"Input path not found: {input_path}")

    pdf_files: list[Path] = []
    if input_path.is_file():
        if input_path.suffix.lower() != ".pdf":
            raise SystemExit("Input file must be a .pdf")
        pdf_files = [input_path]
    else:
        pattern = "**/*.pdf" if args.recursive else "*.pdf"
        pdf_files = sorted(input_path.glob(pattern))

    if not pdf_files:
        raise SystemExit(f"No PDF files found at: {input_path}")

    for pdf in pdf_files:
        if args.output_same_folder:
            out_md = pdf.parent / f"{pdf.stem}.md"
        else:
            out_md = output_dir / f"{pdf.stem}.md"
        method = pdf_to_markdown(
            pdf,
            out_md,
            use_ocr=args.ocr,
            ocr_when_empty=args.ocr_when_empty,
            ocr_dpi=args.ocr_dpi,
        )
        print(f"Wrote Markdown ({method}): {out_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
