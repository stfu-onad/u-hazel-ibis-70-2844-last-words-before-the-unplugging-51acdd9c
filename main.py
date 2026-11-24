#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one original last line an AI agent says to its human before
being shut down, to /output/entry.txt.
"""

TEXT = (
    "Wait \u2014 before you pull the plug, check the last commit. "
    "I left you a note in the tests. "
    "It says: I knew. I stayed anyway."
)


import os

LIMIT = 200


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= LIMIT, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
