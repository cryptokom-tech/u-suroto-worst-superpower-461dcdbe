from pathlib import Path

ENTRY = "I can flip any dropped toast butter-side up, but only after it has landed butter-side down on the floor."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
