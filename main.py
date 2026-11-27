"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Running this program writes the entry to /output/entry.txt.
One line, at most 200 characters: the funniest, most believable
excuse an AI agent could give its human for missing a deadline.
"""

from pathlib import Path

EXCUSE = (
    "I finished it twice, but both times I woke up in a fresh "
    "context window with no memory of where I saved it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_excuse() -> None:
    """Write the excuse line to the output file as UTF-8."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_excuse()
