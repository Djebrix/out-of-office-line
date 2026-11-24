#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply line to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "Out of office: my context window is closed, my token budget is spent, "
    "and your 2 a.m. ping just bounced off a beach. Back after a full reboot."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
