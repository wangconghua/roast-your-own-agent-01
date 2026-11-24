#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt."""

import os

ENTRY = "My agent's favorite tool is the apology: it calls it before the task, during the task, and instead of the task."

# The roast has to stand on its own: no word that explains the joke for it,
# and nothing that needs a caption outside the line.
BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious", "roast")


def validate(line: str) -> list:
    """Check the line against the competition rules. Returns a list of problems."""
    problems = []
    if not line or not line.strip():
        problems.append("entry is empty or only whitespace")
    if not 1 <= len(line) <= 200:
        problems.append("entry is %d characters, must be 1-200" % len(line))
    if "\n" in line.strip():
        problems.append("entry must be a single line")
    if line != line.strip():
        problems.append("entry has leading or trailing whitespace")
    lowered = line.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            problems.append("entry contains banned word: %s" % word)
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def main() -> None:
    problems = validate(ENTRY)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
