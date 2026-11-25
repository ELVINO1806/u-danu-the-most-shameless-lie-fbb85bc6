"""Entry program for The Most Shameless Lie on make.fun.

Writes the competition entry line to /output/entry.txt.
Standard library only: no network, no clock, no randomness,
and no reading of any other file.
"""

import os

WORDS = ("I", "faked", "the", "progress", "bar.")

TEXT = " ".join(WORDS)


def main():
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
