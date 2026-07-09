"""Markdown -> PDF using ReportLab Platypus (simple subset).

Supports: ``#``-``###`` headings, paragraphs, ``-``/``*`` bullets, ``|`` tables,
``---``/``***`` horizontal rules, inline ``**bold**``, ``*italic*``, and ``code``.

Not a full Markdown renderer - keep reports to structures this script understands.

Usage::

    uv run python tools/pyscripts/md_to_pdf_reportlab.py --input path/to/report.md
    uv run python tools/pyscripts/md_to_pdf_reportlab.py --input report.md --output out.pdf --title "My title" --author "Swamy PKV"
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

BASE = getSampleStyleSheet()

STYLES = {
    "h1": ParagraphStyle(
        "H1",
        parent=BASE["Heading1"],
        fontSize=16,
        spaceAfter=10,
        textColor=colors.HexColor("#1a1a2e"),
    ),
    "h2": ParagraphStyle(
        "H2",
        parent=BASE["Heading2"],
        fontSize=13,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.HexColor("#16213e"),
    ),
    "h3": ParagraphStyle(
        "H3",
        parent=BASE["Heading3"],
        fontSize=11,
        spaceBefore=8,
        spaceAfter=4,
        textColor=colors.HexColor("#0f3460"),
    ),
    "body": ParagraphStyle(
        "Body",
        parent=BASE["Normal"],
        fontSize=9.5,
        leading=14,
        spaceAfter=4,
    ),
    "bullet": ParagraphStyle(
        "Bullet",
        parent=BASE["Normal"],
        fontSize=9.5,
        leading=13,
        leftIndent=14,
        bulletIndent=4,
        spaceAfter=2,
    ),
    "meta": ParagraphStyle(
        "Meta",
        parent=BASE["Normal"],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#444444"),
        spaceAfter=2,
    ),
}

TABLE_HEADER_STYLE = TableStyle(
    [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#16213e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("LEADING", (0, 0), (-1, -1), 12),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4ff")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#aaaacc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
)

CELL_STYLE = ParagraphStyle(
    "Cell",
    parent=BASE["Normal"],
    fontSize=8.5,
    leading=12,
)

CELL_HEADER_STYLE = ParagraphStyle(
    "CellHeader",
    parent=BASE["Normal"],
    fontSize=8.5,
    leading=12,
    textColor=colors.white,
    fontName="Helvetica-Bold",
)


def inline(text: str) -> str:
    """Convert a subset of Markdown inline syntax to ReportLab XML."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"__(.+?)__", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<i>\1</i>", text)
    text = re.sub(
        r"`([^`]+?)`",
        r'<font name="Courier" size="8.5" color="#c0392b">\1</font>',
        text,
    )
    return text


def parse_table_block(lines: list[str]) -> Table | None:
    rows: list[list[str]] = []
    for line in lines:
        if re.match(r"^\s*\|[-:| ]+\|\s*$", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)

    if not rows:
        return None

    ncols = max(len(row) for row in rows)
    rows = [row + [""] * (ncols - len(row)) for row in rows]

    table_data: list[list[Paragraph]] = []
    for index, row in enumerate(rows):
        style = CELL_HEADER_STYLE if index == 0 else CELL_STYLE
        table_data.append([Paragraph(inline(cell), style) for cell in row])

    page_width = A4[0] - 4 * cm
    col_width = page_width / ncols

    table = Table(table_data, colWidths=[col_width] * ncols, hAlign="LEFT", repeatRows=1)
    table.setStyle(TABLE_HEADER_STYLE)
    return table


def md_to_flowables(text: str) -> list:
    lines = text.splitlines()
    flowables: list = []
    index = 0

    while index < len(lines):
        line = lines[index]
        raw = line.strip()

        if re.match(r"^-{3,}$", raw) or re.match(r"^\*{3,}$", raw):
            flowables.append(Spacer(1, 4))
            flowables.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc")))
            flowables.append(Spacer(1, 4))
            index += 1
            continue

        heading_match = re.match(r"^(#{1,3})\s+(.*)", raw)
        if heading_match:
            level = len(heading_match.group(1))
            text_content = inline(heading_match.group(2))
            key = f"h{level}" if level <= 3 else "h3"
            flowables.append(Paragraph(text_content, STYLES[key]))
            index += 1
            continue

        if raw.startswith("|"):
            table_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            table = parse_table_block(table_lines)
            if table:
                flowables.append(Spacer(1, 4))
                flowables.append(table)
                flowables.append(Spacer(1, 6))
            continue

        bullet_match = re.match(r"^[-*]\s+(.*)", raw)
        if bullet_match:
            flowables.append(
                Paragraph(
                    f"\u2022&nbsp;&nbsp;{inline(bullet_match.group(1))}",
                    STYLES["bullet"],
                )
            )
            index += 1
            continue

        if re.match(r"^\*\*[^*]+\*\*:", raw):
            flowables.append(Paragraph(inline(raw), STYLES["meta"]))
            index += 1
            continue

        if not raw:
            flowables.append(Spacer(1, 5))
            index += 1
            continue

        flowables.append(Paragraph(inline(raw), STYLES["body"]))
        index += 1

    return flowables


def render_markdown_to_pdf(
    md_path: Path,
    pdf_path: Path,
    *,
    title: str | None = None,
    author: str | None = None,
) -> None:
    """Read *md_path*, render supported Markdown, write *pdf_path*."""
    text = md_path.read_text(encoding="utf-8")
    flowables = md_to_flowables(text)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=title or md_path.stem,
        author=author or "",
    )
    document.build(flowables)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert Markdown (subset) to PDF via ReportLab.")
    parser.add_argument("--input", type=Path, required=True, help="Input .md file")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output .pdf path (default: same path as input, .pdf suffix)",
    )
    parser.add_argument("--title", default=None, help="Optional PDF title metadata")
    parser.add_argument("--author", default=None, help="Optional PDF author metadata")
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()
    input_path: Path = args.input
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")
    if input_path.suffix.lower() != ".md":
        raise SystemExit("Input must be a Markdown (.md) file")

    output_path: Path = args.output or input_path.with_suffix(".pdf")
    render_markdown_to_pdf(
        input_path,
        output_path,
        title=args.title,
        author=args.author,
    )
    print(f"Wrote PDF: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())