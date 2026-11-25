#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Reads the single word from entry.txt next to this file, validates the
gate (UTF-8 text, 1-77 characters, not only whitespace, exactly one
word), and writes it to /output/entry.txt with mode 0644.

Entry word: "moist" — the one word everyone agrees sounds wrong.
Deleting it leaves the language with no word that makes a whole room
wince just by being said out loud.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        word = f.read().strip()

    if not word or len(word) > 77:
        sys.exit("gate: entry must be 1-77 characters")
    if len(word.split()) != 1:
        sys.exit("gate: entry must be exactly one word")

    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    os.chmod(out_path, 0o644)

    # Self-check: read the output back and re-assert the gate.
    with open(out_path, encoding="utf-8") as f:
        written = f.read().strip()
    if written != word or len(written.split()) != 1:
        sys.exit("gate: output failed self-check")


if __name__ == "__main__":
    main()
