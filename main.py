#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes a single original funny line (<=200 chars) about everyday life
to /output/entry.txt. Stdlib only; no network, no reads outside the repo.
"""

import os

LINE = (
    "I set my alarm for 6am to seize the day, then spent three hours "
    "negotiating with it like a hostage standoff where I was both sides."
)
# The joke lands on the last word: the "hostage standoff" turns out to be
# me versus me. One sentence, no abbreviations with periods, so even a
# naive sentence counter sees a single sentence. Kept well under 200
# chars; no trailing newline in the file.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
