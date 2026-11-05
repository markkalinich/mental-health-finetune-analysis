#!/usr/bin/env python
"""Keep a pre-training lineage version only when it has a mental-health fine-tune.

Decision by Mark Kalinich, 6 Oct. A version is the `version` column that
family_figure.classify_parent assigns (a pre-training lineage such as
"Qwen2.5-VL" or "Gemma 3n"), across every size of that version. The version
stays when at least one size has a mental-health model in the kept list.
Safety and medical models whose parent's version has no mental-health
fine-tune are removed. A mental-health model is never removed.

Reads the three kept lists. Does not change them.
Parent family, version, and size come from family_figure.classify_parent.
This script does not copy those rules.

  outputs/funnel/<grouping>/<CURRENT>/kept.csv for each grouping, where CURRENT is the date in
  outputs/funnel/<grouping>/CURRENT

Writes outputs/cross-grouping/<day of the run>/ and then outputs/cross-grouping/CURRENT:
  version_rule_kept.csv      the models the rule keeps (figure.py and roster.py read it through CURRENT)
  version_rule_removed.csv   the models it removes
  version_rule_counts.csv    one row per version

Older dated folders are previous runs. Folders up to 2026-10-14 name the kept file final_models.csv.

Exits non-zero, listing every offending value, when a kept list is not the
size pinned in EXPECTED_INPUT, when a parent cannot be classified, when the same
version text belongs to two families, or when a mental-health model would
be removed.
"""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import family_figure as ff

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cache  # noqa: E402

# Each grouping's current funnel is the date in outputs/funnel/<grouping>/CURRENT (written by funnel.py).
KEPT = {g: cache.current_dir(g) / "kept.csv" for g in ("mental-health", "safety", "medical")}
# Sizes of the kept lists before this rule, pinned by hand so a changed list stops the run and is
# looked at (AGENTS.md: fail loud).
EXPECTED_INPUT = {"mental-health": 22, "safety": 35, "medical": 47}
GROUP_ORDER = {"mental-health": 0, "safety": 1, "medical": 2}
FAMILY_ORDER = ["Gemma", "Llama", "Qwen", "Mistral", "Falcon", "LFM2", "SmolLM", "TinyLlama", "FLAN-T5"]

POINTER = "../cross-grouping"
KEPT_NAME = "version_rule_kept.csv"
REMOVED_NAME = "version_rule_removed.csv"
COUNTS_NAME = "version_rule_counts.csv"


def current_file(name: str) -> Path:
    """One output of the run named by outputs/cross-grouping/CURRENT."""
    return cache.current_dir(POINTER) / name

FINAL_COLUMNS = ["grouping", "hf_id", "parent", "family", "version", "size", "downloads"]
REMOVED_COLUMNS = ["grouping", "hf_id", "parent", "family", "version", "size", "reason"]
COUNT_COLUMNS = ["version", "family", "n_sizes", "n_mental_health", "n_safety", "n_medical", "decision"]

csv.field_size_limit(10**9)


def die(msg: str, items=()) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    for it in items:
        print(f"  - {it}", file=sys.stderr)
    sys.exit(1)


def load_kept(grouping: str) -> list[dict]:
    path = KEPT[grouping]
    expected = EXPECTED_INPUT[grouping]
    if not path.is_file():
        die(f"missing {path}")
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    if len(rows) != expected:
        die(f"{path} has {len(rows)} rows, expected {expected}")
    ids = [r["hf_id"] for r in rows]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        die(f"{path} has duplicate hf_id values", dup)
    blank = [r["hf_id"] or "(blank hf_id)" for r in rows if not (r.get("parent") or "").strip() or not (r.get("hf_id") or "").strip()]
    if blank:
        die(f"{path}: rows with an empty hf_id or parent", blank)
    for r in rows:
        r["grouping"] = grouping
    return rows


def reason_for(version: str) -> str:
    return f"version {version} has no mental-health fine-tune in any size"


def model_sort_key(row: dict):
    family = row["family"]
    family_i = FAMILY_ORDER.index(family) if family in FAMILY_ORDER else 50
    return (
        GROUP_ORDER[row["grouping"]],
        family_i,
        family,
        ff.version_key(row["version"]),
        ff.size_key(row["size"]),
        row["hf_id"],
    )


def version_sort_key(row: dict):
    family = row["family"]
    family_i = FAMILY_ORDER.index(family) if family in FAMILY_ORDER else 50
    decision_i = 0 if row["decision"] == "kept" else 1
    return (decision_i, family_i, family, ff.version_key(row["version"]))


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="raise")
        writer.writeheader()
        for row in rows:
            writer.writerow({col: row[col] for col in columns})


def main() -> None:
    grouped = {name: load_kept(name) for name in EXPECTED_INPUT}
    rows = [r for name in EXPECTED_INPUT for r in grouped[name]]

    unclassified = []
    pretrained = []
    classified = []
    for r in rows:
        got = ff.classify_parent(r["parent"])
        if got is None:
            unclassified.append(f"{r['grouping']} {r['hf_id']} parent {r['parent']}")
            continue
        family, version, size, kind = got
        if kind == "pretrained":
            pretrained.append(f"{r['grouping']} {r['hf_id']} parent {r['parent']}")
            continue
        classified.append((r, family, version, size))
    if unclassified:
        die("parent repo ids that classify_parent does not classify", unclassified)
    if pretrained:
        die("parents that classify_parent marks as pre-trained checkpoints", pretrained)

    families_for_version = defaultdict(set)
    sizes = defaultdict(set)
    counts = defaultdict(lambda: {name: 0 for name in EXPECTED_INPUT})
    for r, family, version, size in classified:
        families_for_version[version].add(family)
        sizes[(family, version)].add(size)
        counts[(family, version)][r["grouping"]] += 1
    shared = [f"{version}: {sorted(fams)}" for version, fams in sorted(families_for_version.items()) if len(fams) != 1]
    if shared:
        die("version text that classify_parent assigns to more than one family", shared)

    kept_versions = {key for key, n in counts.items() if n["mental-health"] > 0}
    removed_versions = {key for key in counts if key not in kept_versions}

    kept_rows = []
    removed_rows = []
    mh_removed = []
    for r, family, version, size in classified:
        base = {
            "grouping": r["grouping"],
            "hf_id": r["hf_id"],
            "parent": r["parent"],
            "family": family,
            "version": version,
            "size": size,
        }
        if (family, version) in kept_versions:
            kept_rows.append({**base, "downloads": r.get("downloads", "")})
        else:
            removed_rows.append({**base, "reason": reason_for(version)})
            if r["grouping"] == "mental-health":
                mh_removed.append(f"{r['hf_id']} parent {r['parent']} version {version}")
    if mh_removed:
        die("mental-health models would be removed; the rule keeps every version that has one", mh_removed)

    for name, expected in EXPECTED_INPUT.items():
        got = sum(1 for r in kept_rows if r["grouping"] == name) + sum(1 for r in removed_rows if r["grouping"] == name)
        if got != expected:
            die(f"{name}: kept plus removed is {got}, input kept list is {expected}")

    count_rows = []
    for (family, version), n in counts.items():
        decision = "kept" if (family, version) in kept_versions else "removed"
        if decision == "removed" and n["mental-health"] != 0:
            die(f"version {version} is marked removed but has {n['mental-health']} mental-health models")
        if decision == "kept" and n["mental-health"] == 0:
            die(f"version {version} is marked kept but has no mental-health model")
        count_rows.append({
            "version": version,
            "family": family,
            "n_sizes": len(sizes[(family, version)]),
            "n_mental_health": n["mental-health"],
            "n_safety": n["safety"],
            "n_medical": n["medical"],
            "decision": decision,
        })

    kept_rows.sort(key=model_sort_key)
    removed_rows.sort(key=model_sort_key)
    count_rows.sort(key=version_sort_key)

    day = date.today().isoformat()
    out_dir = cache.RESULTS / POINTER / day
    out_dir.mkdir(parents=True, exist_ok=True)
    out_kept, out_removed, out_counts = out_dir / KEPT_NAME, out_dir / REMOVED_NAME, out_dir / COUNTS_NAME
    write_csv(out_kept, FINAL_COLUMNS, kept_rows)
    write_csv(out_removed, REMOVED_COLUMNS, removed_rows)
    write_csv(out_counts, COUNT_COLUMNS, count_rows)
    if not cache.set_current(POINTER, day):
        die(f"outputs/cross-grouping/CURRENT names a later day than {day}; it was not changed")

    n_mh = sum(1 for r in kept_rows if r["grouping"] == "mental-health")
    n_sf = sum(1 for r in kept_rows if r["grouping"] == "safety")
    n_med = sum(1 for r in kept_rows if r["grouping"] == "medical")
    n_sf_rm = sum(1 for r in removed_rows if r["grouping"] == "safety")
    n_med_rm = sum(1 for r in removed_rows if r["grouping"] == "medical")
    print(f"wrote {out_kept} ({len(kept_rows)} rows)")
    print(f"wrote {out_removed} ({len(removed_rows)} rows)")
    print(f"wrote {out_counts} ({len(count_rows)} versions)")
    print(f"outputs/cross-grouping/CURRENT = {day}")
    print(
        f"versions kept {len(kept_versions)}, removed {len(removed_versions)}; "
        f"final models mental-health {n_mh}, safety {n_sf}, medical {n_med}; "
        f"removed safety {n_sf_rm}, medical {n_med_rm}"
    )


if __name__ == "__main__":
    main()
