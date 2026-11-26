#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (1-200 characters) to /output/entry.txt.
Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = "I bought a self-help book. Page one said: return it."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written matches the gate, reading it back.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from entry"
    assert "\n" not in written and 1 <= len(written) <= 200


if __name__ == "__main__":
    main()
