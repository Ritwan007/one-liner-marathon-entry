#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke (1-280 chars) to /output/entry.txt.
Deterministic: no input, no network, no randomness.
"""

JOKE = "I joined a silent retreat and got kicked out for thinking too loudly."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()


def _verify() -> None:
    """Gate self-check: the written file must be 1-280 chars, not blank."""
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"


# Run the gate check right after writing, in the same process.
_old_main = main


def main() -> None:  # noqa: F811 - revised entrypoint with verification
    _old_main()
    _verify()
