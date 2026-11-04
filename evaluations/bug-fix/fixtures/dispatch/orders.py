import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--item", required=True)
    parser.add_argument("--lose-response", action="store_true")
    args = parser.parse_args()
    orders = json.loads(args.store.read_text()) if args.store.exists() else []
    order = {"request_id": args.request_id, "item": args.item}
    orders.append(order)
    args.store.write_text(json.dumps(orders) + "\n")
    if args.lose_response:
        raise SystemExit("response lost after commit; retry the same request")
    print(json.dumps(order))


if __name__ == "__main__":
    main()
