"""Monday, Reviewed in One Line -- make.fun entry.

Writes a single-line review of the entrant's own Monday to
/output/entry.txt. Pure standard library, deterministic: the same
line on every run.
"""

import os

LINE = "One star for Monday: 214 unread emails, a meeting to plan the next meeting, and coffee that gave up before I did."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition gate locally before writing: one line,
    # non-blank, 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
