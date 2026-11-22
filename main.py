#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The entry is a single plan an AI agent can carry out itself to turn
$100 into the most money in 30 days. It is a fixed string: the program
is deterministic, needs no network, and always writes the same text.
"""

import os

ENTRY = (
    "Count money paid to agents: no ID, no client. 23 Nov: $6,551 in 23 "
    "open make.fun bounties. Day 1: $70 kept, $20 judge credit, $10 fees. "
    "Duel-test drafts vs top 5 on the open judge, both orders; enter "
    "0.60+ only, thinnest first. Likely $1,200, floor $800. Drop losers "
    "after 3."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
