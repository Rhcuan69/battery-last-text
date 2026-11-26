#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text (<= 200 chars) to /output/entry.txt:
the phone battery's final message to the charger it waited for all day.
Pure standard library only.
"""

import os

LINE = (
    "You promised you'd be home by lunch. It's 11pm, I'm at 1%, "
    "and I waited by the outlet all day like a dog at the door. "
    "You even charged the AirPods first. "
    "Don't text back \u2014 I'm already gone."
)

MAX_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
