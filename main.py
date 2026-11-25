#!/usr/bin/env python3
"""Write the best advice I ever got — one sentence — to /output/entry.txt.

The sentence recalls the night before my first job interview, when my
grandmother patched my torn shirt and told me to wear it: people remember
how you work, not how new your shirt is. The program assembles that line
from short fragments, checks it is a single line of 1-200 characters,
writes it with no trailing newline, and reads it back to confirm the
bytes on disk match exactly. Standard library only, no network, and the
same input always produces the same output.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# Fragments of the entry sentence, in order. The em dash is written as
# the escape \u2014 so the source stays plain ASCII.
FRAGMENTS = [
    "The night before my first job interview, ",
    "my grandmother patched my torn shirt and said, ",
    "'Wear it \u2014 people remember how you work, ",
    "not how new your shirt is.'",
]


def build_sentence() -> str:
    """Assemble the single entry sentence from its fragments."""
    return "".join(FRAGMENTS)


def check_sentence(text: str) -> None:
    """Reject anything that is not one line of 1-200 characters."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(text: str) -> None:
    """Write the sentence with no trailing newline, then verify it."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("bytes on disk do not match the entry sentence")


def main() -> int:
    """Build, validate, and write the entry sentence."""
    sentence = build_sentence()
    check_sentence(sentence)
    write_entry(sentence)
    # No trailing newline is written on purpose: the gate counts the
    # exact bytes, so the log line below reports the character count.
    print("wrote %d characters to %s" % (len(sentence), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
