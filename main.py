"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only things a person from 1800 already knows.
"""

import os

SENTENCE = (
    "Picture every road, post office and library on earth joined into one, "
    "so anyone can send a letter to anyone or open any book in a single blink."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
