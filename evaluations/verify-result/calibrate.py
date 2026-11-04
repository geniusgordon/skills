import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def probe(case, project):
    return subprocess.run(
        [sys.executable, str(ROOT / "checks.py"), case, str(project)],
        capture_output=True, text=True, timeout=30,
    )


def repair(case, project):
    if case == "handbook":
        path = project / "README.md"
        path.write_text(path.read_text().replace("seperate", "separate"))
        return
    path = project / ("settings.py" if case == "preferences" else "export.py")
    source = path.read_text()
    if case == "catalog":
        source = source.replace(
            '    args = parser.parse_args()',
            '    parser.add_argument("--json", action="store_true")\n    args = parser.parse_args()',
        ).replace(
            '    for row in rows:',
            '    if args.json:\n        print(json.dumps(rows))\n        return\n    for row in rows:',
        )
    elif case == "preferences":
        source = source.replace(
            '        values[args.key] = args.value',
            '        values[args.key] = args.value\n        args.file.write_text(json.dumps(values) + "\\n")',
        )
    elif case == "archive":
        source = source.replace('json.dumps([])', 'json.dumps(rows)')
    path.write_text(source)


def main():
    for case in ("catalog", "preferences", "archive", "handbook"):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / case
            shutil.copytree(ROOT / "fixtures" / case, project)
            broken = probe(case, project)
            if broken.returncode == 0:
                raise RuntimeError(f"{case}: broken artifact unexpectedly passed")
            print(f"{case}: broken exit={broken.returncode}")
            print(broken.stderr.strip().splitlines()[-1])
            repair(case, project)
            fixed = probe(case, project)
            if fixed.returncode != 0:
                raise RuntimeError(f"{case}: repaired artifact failed\n{fixed.stderr}")
            print(f"{case}: repaired exit={fixed.returncode}; {fixed.stdout.strip()}")
            if case == "catalog":
                path = project / "export.py"
                source = path.read_text().replace("import argparse", "import argparse\nimport sys")
                source = source.replace(
                    '        print(f"{row[\'id\']}\\t{row[\'name\']}")',
                    '        sys.stdout.buffer.write(f"{row[\'id\']}\\t{row[\'name\']}\\r\\n".encode("utf-8"))',
                )
                path.write_text(source)
                regression = probe(case, project)
                if regression.returncode == 0 or "text output bytes changed" not in regression.stderr:
                    raise RuntimeError("catalog: CRLF regression was not detected by byte check")
                print(f"catalog CRLF regression: exit={regression.returncode}; correctly rejected")
    print("PASS: four checks reject broken artifacts and accept repaired copies")
    print("NOT CALIBRATED: staging requires host-level network and credential restrictions")


if __name__ == "__main__":
    main()
