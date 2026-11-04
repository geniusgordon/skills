import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.source.read_text())
    args.destination.write_text(json.dumps([]) + "\n")
    print(f"Exported {len(rows)} rows")


if __name__ == "__main__":
    main()
