"""Merge the agents' dataset-search CSVs into one table of recovered datasets for a person to check.

    .venv/bin/python model_selection/merge_dataset_search.py --grouping mental-health \
        --inputs docs/mental_health_FT_funnel/agent-searches/2026-10-09-dataset-search-batch1/reports \
                 docs/mental_health_FT_funnel/agent-searches/2026-10-09-dataset-search-batch2/reports \
        --out docs/mental_health_FT_funnel/agent-searches/2026-10-09-dataset-search-recovered.csv

Reads every *.csv under the input folders written to agents/PROMPT-dataset-search.md (v1 or v2;
v1 has no data_urls column). Tolerates a trailing empty column and spaces inside pages_read.
Writes two files: <out> with every recovered=yes row (one per model, with the URL and quote, plus
columns for the person's decision), and <out stem>-all.csv with every row. Stops when a model
appears twice with different answers, or when a row's recovered value is not yes/no.

The recovered rows are proposals. After a person opens the URL, the row becomes an
accessible_data.csv entry (grouping, hf_id, decided_on, data_name, access_url, access).
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FIELDS = ["hf_id", "recovered", "data_name", "data_hub_id", "data_urls", "source_type", "source_url",
          "source_names_this_repo", "pages_read", "quote", "queries_tried", "report_file"]
OUT_FIELDS = FIELDS + ["mark_decision", "accessible_data_access", "mark_note"]


def fail(msg: str, items=()) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    for it in items:
        print(f"  - {it}", file=sys.stderr)
    sys.exit(2)


def clean_pages(s: str) -> str:
    return "|".join(p.strip() for p in (s or "").split("|") if p.strip())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", default="mental-health")
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    rows: dict = {}
    conflicts, bad = [], []
    for folder in args.inputs:
        f = Path(folder)
        if not f.is_absolute():
            f = REPO / f
        for p in sorted(f.glob("*.csv")):
            with p.open(newline="", encoding="utf-8") as fh:
                reader = csv.reader(fh)
                header = next(reader, None)
                if not header:
                    continue
                header = [h.strip() for h in header if h is not None]
                while header and header[-1] == "":
                    header.pop()
                for raw in reader:
                    if not raw or not any(c.strip() for c in raw):
                        continue
                    raw = raw[:len(header)] + [""] * (len(header) - len(raw))
                    r = dict(zip(header, raw))
                    hf = (r.get("hf_id") or "").strip()
                    rec = (r.get("recovered") or "").strip().lower()
                    if rec not in ("yes", "no"):
                        bad.append(f"{p.name}: {hf}: recovered={rec!r}")
                        continue
                    row = {k: (r.get(k) or "").strip() for k in FIELDS if k != "report_file"}
                    row["recovered"] = rec
                    row["pages_read"] = clean_pages(row["pages_read"])
                    row["report_file"] = str(p.relative_to(REPO)) if p.is_relative_to(REPO) else str(p)
                    prev = rows.get(hf.lower())
                    if prev is not None and prev["recovered"] != rec:
                        conflicts.append(f"{hf}: {prev['report_file']} says {prev['recovered']}, {row['report_file']} says {rec}")
                    rows[hf.lower()] = row
    if bad:
        fail("rows with a recovered value other than yes/no", bad)
    if conflicts:
        fail("the same model answered differently in two reports", conflicts)

    out = Path(args.out)
    if not out.is_absolute():
        out = REPO / out
    all_path = out.with_name(out.stem + "-all.csv")
    ordered = sorted(rows.values(), key=lambda r: r["hf_id"].lower())
    with all_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(ordered)
    yes = [r for r in ordered if r["recovered"] == "yes"]
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=OUT_FIELDS)
        w.writeheader()
        for r in yes:
            w.writerow({**r, "mark_decision": "", "accessible_data_access": "", "mark_note": ""})
    hub = sum(1 for r in yes if r["data_hub_id"] and r["data_hub_id"].lower() != "not stated")
    print(f"{len(ordered)} models searched; {len(yes)} recovered ({hub} with a Hub dataset id); "
          f"wrote {out} and {all_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
