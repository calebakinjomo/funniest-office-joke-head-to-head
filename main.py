#!/usr/bin/env python3
"""Funniest Office Joke, Judged Head to Head.

Writes one short line about office life to /output/entry.txt.
The line is the entire entry: a real joke with a setup and a turn,
built on something anyone who has worked in an office recognises.
"""

import os

ENTRY = "I asked IT for a second monitor; they gave me a second ticket."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
