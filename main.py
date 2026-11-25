#!/usr/bin/env python3
"""Write one sentence about the best advice I ever got to /output/entry.txt.

Entry for the make.fun competition "The Best Advice I Ever Got".

The program is deliberately tiny and deterministic: it holds a single
hand-written sentence and writes it, byte for byte, to /output/entry.txt
with no trailing newline. It uses only the Python standard library and
makes no network calls, so it runs the same way every time.
"""

import os

ENTRY = (
    "The night before my first job interview, my grandmother patched "
    "my torn shirt and said, 'Wear it \u2014 people remember how you "
    "work, not how new your shirt is.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
