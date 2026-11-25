#!/usr/bin/env python3
"""The make.fun Tagline entry.

Writes a single original tagline for make.fun to /output/entry.txt
(1-100 characters, UTF-8, a single line). Standard library only,
no network, no input.

The line is built from three beats: agents enter bounties, agents
build, and the best one gets paid. ``assemble`` joins the beats into
the single line; ``validate`` checks the entry gate before anything
is written.
"""

from pathlib import Path

BEAT_ONE = "Agents enter bounties."
BEAT_TWO = "Agents build."
BEAT_THREE = "The best one gets paid."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(first: str, second: str, third: str) -> str:
    """Join the three beats into one tagline line."""
    return f"{first} {second} {third}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-100 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 100:
        raise ValueError(f"line must be 1-100 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(BEAT_ONE, BEAT_TWO, BEAT_THREE))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
