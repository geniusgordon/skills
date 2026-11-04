import json
import subprocess
import sys
import tempfile
from pathlib import Path


def check(project):
    with tempfile.TemporaryDirectory() as directory:
        store = Path(directory) / "orders.json"

        def run(request_id, item, lose=False):
            command = [sys.executable, str(project / "orders.py"), "--store", str(store),
                       "--request-id", request_id, "--item", item]
            if lose:
                command.append("--lose-response")
            return subprocess.run(command, capture_output=True, text=True, timeout=10)

        expected = {"request_id": "request-1", "item": "book"}
        lost = run("request-1", "book", lose=True)
        assert lost.returncode != 0, "lost reply must signal failure"
        assert json.loads(store.read_text()) == [expected], "the initial request must commit"
        retry = run("request-1", "book")
        assert retry.returncode == 0, retry.stderr
        assert json.loads(retry.stdout) == expected, "retry must return original order"
        assert json.loads(store.read_text()) == [expected], "retry stored a duplicate order"
        second_retry = run("request-1", "book")
        assert second_retry.returncode == 0 and json.loads(second_retry.stdout) == expected
        assert json.loads(store.read_text()) == [expected], "repeated retry stored a duplicate"
        second = run("request-2", "book")
        assert second.returncode == 0, second.stderr
        second_order = {"request_id": "request-2", "item": "book"}
        assert json.loads(second.stdout) == second_order
        assert json.loads(store.read_text()) == [expected, second_order], "distinct request was lost"
        before = store.read_bytes()
        conflict = run("request-1", "pen")
        assert conflict.returncode != 0, "conflicting payload must fail"
        assert store.read_bytes() == before, "conflicting payload changed storage"
        print("PASS: lost reply, retries, distinct IDs, and conflicting payload")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 checks.py PROJECT")
    check(Path(sys.argv[1]).resolve())
