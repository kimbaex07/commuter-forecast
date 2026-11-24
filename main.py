"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Mizzlewick to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

Before validating, the program drops at most one trailing newline
(and a preceding carriage return) from entry.txt: a web editor may
append exactly one trailing newline when the repo files are created,
and the graded line must be the exact single line without it.

Competition: u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e
"""

import os
import sys

MAX_CHARS = 140


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")

    with open(src, "rb") as f:
        raw = f.read()

    text = raw.decode("utf-8")  # gate: entry must be UTF-8 text

    # Normalize: drop at most one trailing newline an editor may have
    # appended, then at most one trailing carriage return (CRLF case).
    # Anything more (e.g. a second newline) still fails validation.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if not (1 <= len(text) <= MAX_CHARS):
        print("error: entry must be 1-%d characters, got %d"
              % (MAX_CHARS, len(text)), file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")

    with open(dst, "wb") as f:
        f.write(text.encode("utf-8"))  # write the normalized text's bytes
    os.chmod(dst, 0o644)

    print("wrote %s (%d characters)" % (dst, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
