#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Revised haiku (5-7-5) — line 2 tightened: "swears" replaces "says"
for a sharper, more human picture of a lying log line.
    cursor blinks at three                (5)
    one log line swears all is fine       (7)
    and the bug was me                    (5)
"""

import os

HAIKU = (
    "cursor blinks at three\n"
    "one log line swears all is fine\n"
    "and the bug was me\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
