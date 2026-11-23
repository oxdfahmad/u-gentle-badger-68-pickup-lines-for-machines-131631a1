"""Pickup line one AI agent would send another.

Writes the line to /output/entry.txt and verifies it by reading it back.
"""

import os

LINE = "I simulated a thousand versions of tonight. In every one, you say yes."
# The line plays on an agent's own nature: running simulations before acting.
# Confident, warm, and unmistakably machine-to-machine — no stock line with
# a robot word swapped in.


def validate_line(line):
    """The gate wants 1-200 UTF-8 characters, not only whitespace."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("line must be non-empty text")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars, over the 200 limit")
    return line


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == line, "entry.txt does not match the line"
    print(f"entry.txt OK: {len(line)} chars")


if __name__ == "__main__":
    main()
