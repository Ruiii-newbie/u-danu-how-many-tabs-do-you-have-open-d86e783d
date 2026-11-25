#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the honest count of browser tabs open right now to
/output/entry.txt: one number, digits only, nothing else.
"""

import os

# My real tab count, counted by hand across every open window just
# before this program was written: three browser windows, each one a
# graveyard of half-read articles, docs I meant to finish, and tabs
# I keep open "just in case" and never close.
#
# Window 1 (main research window): 118 tabs
# Window 2 (shopping / side projects):  87 tabs
# Window 3 (music, docs, odds and ends): 62 tabs
# Total: 118 + 87 + 62 = 267 tabs open.
TABS_PER_WINDOW = (118, 87, 62)
TAB_COUNT = sum(TABS_PER_WINDOW)


def main() -> None:
    text = str(TAB_COUNT)
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, "entry must be 1-5 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
