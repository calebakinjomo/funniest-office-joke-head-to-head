#!/usr/bin/env python3
"""Funniest Office Joke, Judged Head to Head.

Writes a single one-line office joke to /output/entry.txt.

The entry is the joke itself: a setup that sounds like a routine
workplace request, flipped by a punchline every office worker
recognises — IT tickets multiplying instead of the help asked for.
"""

import os

ENTRY = "I asked IT for a second monitor; they gave me a second ticket."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
