#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun entry.

Writes a single one-star review of the Moon (120 characters max)
to /output/entry.txt, exactly as the program/v1 harness requires.
"""

import os

REVIEW = (
    "1 star. Shows up late, moves my ocean without asking, "
    "takes credit for the Sun's light. Would not orbit again."
)


def main() -> None:
    assert 1 <= len(REVIEW) <= 120, f"review is {len(REVIEW)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Round-trip check: the gate counts every character, so the file
    # must hold exactly the review — no trailing newline, no BOM.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == REVIEW, "entry.txt does not match REVIEW byte for byte"
    print(f"wrote {len(written)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
