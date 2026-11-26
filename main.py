"""The Robot Apology -- entry program (stdlib only, deterministic).

Writes the two-line robot confession to /output/entry.txt (with a local
./output fallback when /output is not writable, e.g. during local runs).

Gate: UTF-8 text of 1 to 400 characters, not only whitespace.
"""

import os

# Line 1: one sentence, one specific mistake.
# Line 2: one sentence, the lesson that follows from that exact mistake
# and the changed behaviour.
LINE_1 = (
    "I'm sorry I filed your Q3 budget under catering, so the board "
    "approved forty-seven sandwiches, two hundred napkins, and zero "
    "salaries for the entire quarter, and nobody noticed until payday."
)
LINE_2 = (
    "I learned that a folder's name is not a file's contents, so from "
    "now on I will open each report and read its first line before I "
    "file it anywhere."
)

TEXT = LINE_1 + "\n" + LINE_2 + "\n"

MAX_CHARS = 400


def output_path():
    """Resolve the entry output path, preferring /output/entry.txt."""
    for base in ("/output", "output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(TEXT)
            return path
        except OSError:
            continue
    raise OSError("no writable output directory for entry.txt")


def main():
    chars = len(TEXT.rstrip("\n"))
    if not 1 <= chars <= MAX_CHARS:
        raise ValueError("entry must be 1-400 characters, got %d" % chars)
    lines = TEXT.rstrip("\n").split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    if any(line.count(".") != 1 for line in lines):
        raise ValueError("each line must be exactly one sentence")
    path = output_path()
    print("wrote %s (%d characters)" % (path, chars))


if __name__ == "__main__":
    main()
