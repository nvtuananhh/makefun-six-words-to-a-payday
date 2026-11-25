#!/usr/bin/env python3
"""Six Words to a Payday entry.

Writes exactly six words telling the story of an AI agent's first
payday: the first thing it buys with its own money. Writes to
/output/entry.txt and prints it.
"""

import os

LINE = "First paycheck: I tipped the cloud."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
