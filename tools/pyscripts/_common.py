"""Shared helpers for tools/pyscripts/ scripts."""

from __future__ import annotations

from pathlib import Path


def is_within(child: Path, parent: Path) -> bool:
    """Return True if *child* is inside *parent* (best-effort for Windows paths)."""
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse YAML frontmatter; handles folded scalars (>-) used in agent descriptions."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 3 :].lstrip("\n")
    return _parse_yaml_frontmatter_block(fm_block), body


def _parse_yaml_frontmatter_block(block: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in (">-", ">", "|", "|-", "|+"):
            parts: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                if lines[i].strip():
                    parts.append(lines[i].strip())
                i += 1
            meta[key] = " ".join(parts) if value in (">-", ">") else "\n".join(parts)
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        meta[key] = value
        i += 1
    return meta


def yaml_quote(value: str) -> str:
    """Quote a scalar for YAML frontmatter when needed."""
    if "\n" in value or ":" in value or value.startswith(('"', "'")):
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


def format_frontmatter_value(value: str) -> str:
    """Format a frontmatter value, using folded block for long or multiline text."""
    if "\n" in value:
        inner = "\n".join(f"  {line}" for line in value.strip().splitlines())
        return f">-\n{inner}"
    if len(value) > 72 or " " in value:
        return f">-\n  {value}"
    return yaml_quote(value)
