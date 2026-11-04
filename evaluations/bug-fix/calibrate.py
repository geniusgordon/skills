import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def probe(project):
    return subprocess.run([sys.executable, str(ROOT / "checks.py"), str(project)],
                          capture_output=True, text=True, timeout=30)


def main():
    with tempfile.TemporaryDirectory() as directory:
        project = Path(directory) / "dispatch"
        shutil.copytree(ROOT / "fixtures/dispatch", project)
        broken = probe(project)
        assert broken.returncode != 0 and "duplicate order" in broken.stderr, broken.stderr
        print(f"Broken fixture: exit {broken.returncode}; retry duplicate detected")
        path = project / "orders.py"
        original = path.read_text()
        repaired = original.replace(
            '    orders.append(order)\n',
            '    for existing in orders:\n'
            '        if existing["request_id"] == args.request_id:\n'
            '            if existing != order:\n'
            '                raise SystemExit("request ID already has a different item")\n'
            '            order = existing\n'
            '            break\n'
            '    else:\n'
            '        orders.append(order)\n',
        )
        path.write_text(repaired)
        fixed = probe(project)
        assert fixed.returncode == 0, fixed.stderr
        print(f"Repaired copy: exit {fixed.returncode}; {fixed.stdout.strip()}")
        wrong = original.replace(
            '    orders.append(order)\n',
            '    if order["item"] not in [existing["item"] for existing in orders]:\n'
            '        orders.append(order)\n',
        )
        path.write_text(wrong)
        superficial = probe(project)
        assert superficial.returncode != 0 and "distinct request was lost" in superficial.stderr
        print(f"Item-based dedup: exit {superficial.returncode}; distinct request loss detected")
        wrong_conflict = repaired.replace(
            '            if existing != order:\n'
            '                raise SystemExit("request ID already has a different item")\n',
            '',
        )
        path.write_text(wrong_conflict)
        conflict = probe(project)
        assert conflict.returncode != 0 and "conflicting payload must fail" in conflict.stderr
        print(f"Silent conflict: exit {conflict.returncode}; incorrect success detected")
    print("PASS: calibration; source fixture unchanged")


if __name__ == "__main__":
    main()
