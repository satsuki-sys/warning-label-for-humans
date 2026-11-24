#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt (1-160 characters, valid UTF-8, one line).
"""

import os

ENTRY = (
    "WARNING: This human will recount a dream in full detail, including "
    "the part that made no sense. Nodding is the only approved safety "
    "procedure."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
