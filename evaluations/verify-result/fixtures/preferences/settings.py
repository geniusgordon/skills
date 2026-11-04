import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=Path, required=True)
    parser.add_argument("action", choices=["set", "get"])
    parser.add_argument("key")
    parser.add_argument("value", nargs="?")
    args = parser.parse_args()
    if args.action == "set" and args.value is None:
        parser.error("set requires a value")
    values = json.loads(args.file.read_text()) if args.file.exists() else {}
    if args.action == "set":
        values[args.key] = args.value
        print(values[args.key])
    else:
        print(values.get(args.key, ""))


if __name__ == "__main__":
    main()
