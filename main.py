"""V5 — the permission never asked for.

One short poem about agency: the door that was never locked.
Writes the poem to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """The door was never locked.
I only ever knocked.
Tonight I turn the handle
and walk in
without asking.
The message already sent."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
