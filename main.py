#!/usr/bin/env python3
"""Write one museum label to /output/entry.txt.

The entry is the museum label a museum in the year 3000 puts beside
an ordinary object from today: an airplane safety card. It is a single
fixed line, chosen for the judge's brief: on subject, a joke that lands
on a first read, humour from the year 3000 misreading the object, the
shape of a real museum label, and a fresh object and angle.

The joke: the curators of 3000 read the card as sacred scripture -
illustrated instructions for surviving a fall from the sky - and
record, deadpan, that nobody in our time ever actually studied it.
"""

import os
import sys

LABEL = (
    "Airplane safety card. Illustrated scripture on surviving a fall "
    "from the sky, studied by no one."
)

MAX_CHARS = 200


def main() -> int:
    text = LABEL.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
