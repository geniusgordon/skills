import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.source.read_text())
    for row in rows:
        print(f"{row['id']}\t{row['name']}")


if __name__ == "__main__":
    main()
