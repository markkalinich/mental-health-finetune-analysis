"""Append the dataset-search recoveries to accessible_data.csv, the same way the 8 October rows were made.

    .venv/bin/python model_selection/admit_recovered.py --grouping mental-health \
        --recovered docs/mental_health_FT_funnel/agent-searches/2026-10-09-dataset-search-recovered.csv \
        --decided-on 2026-10-09

The rule is the one process.md set on 8 October and the prompt repeats: a model's training data is
"recovered" when a source about this repository names a corpus that opens (a Hub dataset page that
loads, a file in a repository that opens, a Kaggle page that loads). Every recovered row therefore
becomes an accessible_data.csv row; there is no separate acceptance step, exactly as on 8 October.
Models admitted this way still go through step 3 (parent) and step 4 (manual review by Mark).

access is read from the first URL that opened: huggingface.co/datasets -> hub_dataset,
kaggle.com -> kaggle_page, anything else -> file_opened. A model that already has a row is skipped
and listed.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
ACCESSIBLE = HERE / "accessible_data.csv"
FIELDS = ["grouping", "hf_id", "decided_on", "data_name", "access_url", "access"]


def access_kind(url: str) -> str:
    u = url.lower()
    if "huggingface.co/datasets/" in u:
        return "hub_dataset"
    if "kaggle.com" in u:
        return "kaggle_page"
    return "file_opened"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", default="mental-health")
    ap.add_argument("--recovered", required=True)
    ap.add_argument("--decided-on", required=True)
    args = ap.parse_args()
    rec_path = Path(args.recovered)
    if not rec_path.is_absolute():
        rec_path = REPO / rec_path
    existing = list(csv.DictReader(ACCESSIBLE.open(newline=""))) if ACCESSIBLE.exists() else []
    have = {(r["grouping"], r["hf_id"].lower()) for r in existing}
    added, skipped, no_url = [], [], []
    for r in csv.DictReader(rec_path.open(newline="", encoding="utf-8")):
        if r["recovered"].strip().lower() != "yes":
            continue
        urls = [u.strip() for u in (r.get("data_urls") or "").split("|") if u.strip()]
        if not urls:
            # Prompt v1 rows (the 9 Oct pilot) have no data_urls column: the Hub id or the source URL is the opened page.
            hub_id = (r.get("data_hub_id") or "").strip()
            if hub_id and hub_id.lower() != "not stated":
                urls = [f"https://huggingface.co/datasets/{hub_id}"]
            elif (r.get("source_url") or "").strip():
                urls = [r["source_url"].strip()]
        if not urls:
            no_url.append(r["hf_id"])
            continue
        key = (args.grouping, r["hf_id"].lower())
        if key in have:
            skipped.append(r["hf_id"])
            continue
        # Prefer a Hub dataset URL when there is one, so access reads hub_dataset.
        url = next((u for u in urls if "huggingface.co/datasets/" in u.lower()), urls[0])
        name = (r.get("data_name") or "").strip() or (r.get("data_hub_id") or "").strip() or url
        added.append({"grouping": args.grouping, "hf_id": r["hf_id"], "decided_on": args.decided_on,
                      "data_name": name[:200], "access_url": url, "access": access_kind(url)})
        have.add(key)
    if no_url:
        print(f"ERROR: {len(no_url)} recovered row(s) have no data_urls; the prompt requires one:", file=sys.stderr)
        for h in no_url:
            print(f"  - {h}", file=sys.stderr)
        return 2
    with ACCESSIBLE.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(existing + added)
    kinds = {}
    for a in added:
        kinds[a["access"]] = kinds.get(a["access"], 0) + 1
    print(f"accessible_data.csv: +{len(added)} rows ({kinds}); {len(skipped)} already present; now {len(existing) + len(added)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
