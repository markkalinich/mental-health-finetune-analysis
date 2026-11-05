"""Where each benchmark dataset lives on this machine: config/datasets.csv is the one record.

Columns: name, kind (file or dir), path, sha256. For a file the checksum is of its bytes. For a
directory it is of the lines "<file name>\t<sha256>\n" for the files directly inside it, sorted by
name, so a changed, added, or removed file is caught.

    path(name)      the path, after checking it exists and its checksum matches; any miss stops
    location(name)  the path without the check, for the scripts that write the dataset
    checksum(path)  the checksum as defined above, to update the manifest on purpose after a rewrite

Bash launchers use:  .venv/bin/python -m config.datasets NAME   (prints the checked path)
"""
from __future__ import annotations

import csv
import hashlib
import sys
from functools import lru_cache
from pathlib import Path

MANIFEST = Path(__file__).resolve().parent / "datasets.csv"
COLUMNS = ["name", "kind", "path", "sha256"]


@lru_cache(maxsize=None)
def _rows() -> dict[str, dict[str, str]]:
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != COLUMNS:
            raise SystemExit(f"{MANIFEST}: columns are {reader.fieldnames}, expected {COLUMNS}")
        rows = list(reader)
    names = [row["name"] for row in rows]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SystemExit(f"{MANIFEST}: names listed twice: {duplicates}")
    bad = [row["name"] for row in rows if row["kind"] not in ("file", "dir") or not row["path"] or not row["sha256"]]
    if bad:
        raise SystemExit(f"{MANIFEST}: rows with an unknown kind or a blank path or checksum: {bad}")
    return {row["name"]: row for row in rows}


def _file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def checksum(path: Path) -> str:
    if path.is_dir():
        lines = "".join(
            f"{child.name}\t{_file_sha(child)}\n" for child in sorted(path.iterdir()) if child.is_file()
        )
        return hashlib.sha256(lines.encode("utf-8")).hexdigest()
    return _file_sha(path)


def location(name: str) -> Path:
    rows = _rows()
    if name not in rows:
        raise SystemExit(f"{MANIFEST}: no dataset named {name!r}; known: {sorted(rows)}")
    return Path(rows[name]["path"])


@lru_cache(maxsize=None)
def path(name: str) -> Path:
    found = location(name)
    row = _rows()[name]
    exists = found.is_dir() if row["kind"] == "dir" else found.is_file()
    if not exists:
        raise SystemExit(f"{name}: {row['kind']} {found} does not exist ({MANIFEST})")
    got = checksum(found)
    if got != row["sha256"]:
        raise SystemExit(
            f"{name}: {found} has sha256 {got}, {MANIFEST} records {row['sha256']}. "
            "If the dataset was rewritten on purpose, update the manifest row."
        )
    return found


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python -m config.datasets NAME")
    print(path(sys.argv[1]))
