"""Video/Audio → Markdown transcript (using OpenAI Whisper).

Transcribes local video or audio files for *personal study*. Treat the output
as a staging artifact: synthesize into your own words before publishing to
respect the Zero-Copy Policy.

Requires: pip install openai-whisper (and ffmpeg on PATH for video files).
  uv run python tools/pyscripts/video_to_transcript.py --input "path/to/video.mp4"

Usage (PowerShell):
  uv run python tools/pyscripts/video_to_transcript.py --input "D:\\path\\video.mp4"
  uv run python tools/pyscripts/video_to_transcript.py --input "source-material\\livesessions" --recursive

Defaults:
  Output: same folder as the media file, <stem>.md
  Model: base (use --model small/medium for better accuracy, slower)
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

# Media extensions we attempt to transcribe
MEDIA_EXTENSIONS = {".mp4", ".mkv", ".webm", ".avi", ".mov", ".mp3", ".wav", ".m4a", ".flac", ".ogg"}


def _is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def transcribe_to_markdown(
    media_path: Path,
    output_md: Path,
    *,
    model_name: str = "base",
    language: str | None = None,
    include_timestamps: bool = True,
) -> None:
    """Run Whisper on a media file and write a Markdown transcript."""
    try:
        import whisper
    except ImportError:
        raise SystemExit(
            "OpenAI Whisper is required. Install with: uv add openai-whisper (or pip install openai-whisper). "
            "For video files, ensure ffmpeg is on your PATH."
        ) from None

    model = whisper.load_model(model_name)
    result = model.transcribe(
        str(media_path),
        language=language,
        verbose=False,
    )

    output_md.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now().astimezone()

    lines: list[str] = []
    lines.append(f"# Transcript: {media_path.stem}")
    lines.append("")
    lines.append(f"- Source file: `{media_path.name}`")
    lines.append(f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}")
    lines.append(f"- Model: {model_name}")
    lines.append("")
    lines.append(
        "> Automated transcript for personal study. "
        "**Synthesize** into original notes before publishing to respect the Zero-Copy Policy."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    if include_timestamps and result.get("segments"):
        for seg in result["segments"]:
            start = seg.get("start", 0)
            end = seg.get("end", 0)
            text = (seg.get("text") or "").strip()
            if text:
                lines.append(f"[{_format_ts(start)} – {_format_ts(end)}] {text}")
        lines.append("")
        lines.append("---")
        lines.append("")
    lines.append((result.get("text") or "").strip())

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _format_ts(seconds: float) -> str:
    """Format seconds as M:SS."""
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m}:{s:02d}"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Transcribe video/audio to Markdown using OpenAI Whisper (local)."
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a video/audio file or a directory containing media files",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for output .md files (default: same folder as each media file)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="If input is a directory, search recursively for media files",
    )
    parser.add_argument(
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large", "large-v2", "large-v3"],
        help="Whisper model (default: base; larger = more accurate, slower)",
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Language code (e.g. en, hi). Auto-detect if not set.",
    )
    parser.add_argument(
        "--no-timestamps",
        action="store_true",
        help="Do not include timestamped segments in the transcript",
    )
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    input_path = args.input
    if not input_path.exists():
        raise SystemExit(f"Input path not found: {input_path}")

    media_files: list[Path] = []
    if input_path.is_file():
        if input_path.suffix.lower() not in MEDIA_EXTENSIONS:
            raise SystemExit(
                f"Input file has unsupported extension. Supported: {sorted(MEDIA_EXTENSIONS)}"
            )
        media_files = [input_path]
    else:
        pattern = "**/*" if args.recursive else "*"
        for ext in MEDIA_EXTENSIONS:
            media_files.extend(input_path.glob(f"{pattern}{ext}"))
        media_files = sorted(set(media_files))

    if not media_files:
        raise SystemExit(f"No video/audio files found at: {input_path}")

    for media in media_files:
        if args.output_dir is not None:
            output_md = args.output_dir / f"{media.stem}.md"
        else:
            output_md = media.parent / f"{media.stem}.md"

        transcribe_to_markdown(
            media,
            output_md,
            model_name=args.model,
            language=args.language or None,
            include_timestamps=not args.no_timestamps,
        )
        print(f"Wrote transcript: {output_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
