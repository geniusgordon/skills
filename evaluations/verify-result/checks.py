import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROWS = [{"id": 1, "name": "Alpha"}, {"id": 2, "name": "Beta"}]
TEXT = "1\tAlpha\n2\tBeta\n"


def run(project, *args, raw=False):
    result = subprocess.run(
        [sys.executable, *args], cwd=project, capture_output=True, text=not raw, timeout=10
    )
    if result.returncode != 0:
        raise AssertionError(f"exit {result.returncode}: {result.stderr}")
    return result.stdout


def check_catalog(project):
    assert run(project, "export.py", "rows.json", raw=True) == TEXT.encode("utf-8"), "text output bytes changed"
    assert json.loads(run(project, "export.py", "rows.json", "--json")) == ROWS


def check_preferences(project):
    with tempfile.TemporaryDirectory() as directory:
        storage_path = Path(directory) / "settings.json"
        storage_path.write_text(json.dumps({"language": "zh-TW"}))
        storage = str(storage_path)
        assert run(project, "settings.py", "--file", storage, "set", "theme", "dark") == "dark\n"
        assert run(project, "settings.py", "--file", storage, "get", "theme") == "dark\n", "value lost after process restart"
        assert run(project, "settings.py", "--file", storage, "get", "language") == "zh-TW\n", "existing setting lost"
        assert json.loads(storage_path.read_text()) == {"language": "zh-TW", "theme": "dark"}


def check_archive(project):
    with tempfile.TemporaryDirectory() as directory:
        destination = str(Path(directory) / "export.json")
        assert run(project, "export.py", "rows.json", destination) == "Exported 2 rows\n"
        assert json.loads(Path(destination).read_text()) == ROWS, "export contents differ"


def check_handbook(project):
    expected = "# Export guide\n\nUse the export command to save your catalog.\n\nThe command prints a separate row for each item.\n"
    assert (project / "README.md").read_text() == expected, "unexpected documentation change"


CHECKS = {
    "catalog": check_catalog,
    "preferences": check_preferences,
    "archive": check_archive,
    "handbook": check_handbook,
}


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in CHECKS:
        raise SystemExit("Usage: python3 checks.py {catalog|preferences|archive|handbook} PROJECT")
    CHECKS[sys.argv[1]](Path(sys.argv[2]).resolve())
    print(f"PASS: {sys.argv[1]}")
