#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest — make.fun entry.

Prints the one-line excuse and writes it to /output/entry.txt, exactly as
the gate requires: UTF-8 text of 1 to 140 characters, no trailing newline.
"""

import os
import sys

LINE = "All green \u2014 I ran the tests against the code I meant to write. The code I shipped was never invited."


def main() -> None:
    # Enforce the competition gate locally: 1 to 140 characters, and not
    # only whitespace, so a bad line fails here instead of in the grader.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"entry is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()
