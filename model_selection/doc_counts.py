"""The count table in docs/<grouping>_FT_funnel/how-models-are-filtered.md, generated from counts.csv.

    .venv/bin/python model_selection/doc_counts.py --grouping mental-health            # print
    .venv/bin/python model_selection/doc_counts.py --grouping mental-health --write    # replace the block in the doc
    .venv/bin/python model_selection/doc_counts.py --grouping mental-health --check    # exit 1 if the doc block is stale

The doc holds the table between two marker lines:

    <!-- counts:begin -->
    ...
    <!-- counts:end -->

Nothing between the markers is typed by hand. The numbers come from outputs/funnel/<grouping>/<CURRENT>/counts.csv,
where CURRENT is the date in outputs/funnel/<grouping>/CURRENT (written by funnel.py). The step labels come
from figure.py, so the table and the figure cannot disagree. --check is run by
tests/test_docs_match_counts.py.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cache  # noqa: E402
import figure  # noqa: E402

REPO = HERE.parent
BEGIN, END = "<!-- counts:begin -->", "<!-- counts:end -->"
DOC = {g: REPO / f"docs/{g.replace('-', '_')}_FT_funnel/how-models-are-filtered.md"
       for g in ("mental-health", "safety", "medical")}


def table(grouping: str) -> str:
    date = cache.current_view(grouping)
    folder = cache.RESULTS / grouping / date
    counts = figure.load_counts(folder / "counts.csv")
    prov = folder / "provenance.csv"
    lo, hi = [], []
    if prov.exists():
        for r in csv.DictReader(prov.open(newline="")):
            lo.append(r["date_min"])
            hi.append(r["date_max"])
    lines = [
        f"Current run: `outputs/funnel/{grouping}/{date}/` "
        f"(the date in `outputs/funnel/{grouping}/CURRENT`). Hub data fetched {min(lo)} to {max(hi)}."
        if lo else
        f"Current run: `outputs/funnel/{grouping}/{date}/` "
        f"(the date in `outputs/funnel/{grouping}/CURRENT`).",
        "",
        "| Step | What it keeps | Entered | Kept | Removed, by reason |",
        "|---:|---|---:|---:|---|",
    ]
    cohort = counts["0"]["cohort"]
    for step in figure.STEPS:
        c = counts[step]
        losses = {k: v for k, v in c.items() if k not in ("entered", "kept")}
        parts = [f"{v:,} {figure.loss_label(k)}" for k, v in sorted(losses.items(), key=lambda kv: (-kv[1], kv[0]))]
        label = figure.BOX[step].replace("\n", " ")
        if step == figure.endpoint(grouping):
            label = f"**{label}** (the study set, `kept.csv`)"
        entered = f"{c['entered']:,}" if step != "1" else f"{cohort:,} keyword matches"
        lines.append(f"| {step} | {label} | {entered} | **{c['kept']:,}** | {'<br>'.join(parts) or '-'} |")
    lines.append("")
    end = figure.endpoint(grouping)
    later = [s for s in figure.STEPS if s > end]
    lines.append(f"Step {end} is the end of the funnel; its survivors are `kept.csv`. "
                 f"Survivors of step 4 are `kept_after_review.csv`, of step 5 `kept_method_stated.csv`, "
                 f"of step 6 `kept_objective_known.csv`."
                 + (f" Steps {', '.join(later)} remove no one from `kept.csv`; they are reported as sensitivity cuts."
                    if later else ""))
    lines.append("The figure (`funnel.png` in the run folder) draws the keyword search as its own first box and steps 5 and 6 "
                 "as one box, \"Training method documented by the author\", with one combined removal count; this table keeps "
                 "the two steps apart (`figure.MERGED_IN_FIGURE`).")
    return "\n".join(lines)


def replace_block(text: str, block: str) -> str:
    if BEGIN not in text or END not in text:
        raise ValueError(f"doc has no {BEGIN} ... {END} markers")
    head, rest = text.split(BEGIN, 1)
    _old, tail = rest.split(END, 1)
    return f"{head}{BEGIN}\n{block}\n{END}{tail}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", required=True, choices=sorted(DOC))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    block = table(args.grouping)
    doc = DOC[args.grouping]
    if args.write:
        doc.write_text(replace_block(doc.read_text(), block))
        print(f"wrote count block to {doc}")
        return 0
    if args.check:
        text = doc.read_text()
        if BEGIN not in text:
            print(f"ERROR: {doc} has no {BEGIN} marker", file=sys.stderr)
            return 1
        current = text.split(BEGIN, 1)[1].split(END, 1)[0].strip()
        if current != block.strip():
            print(f"ERROR: the count table in {doc} does not match "
                  f"outputs/funnel/{args.grouping}/{cache.current_view(args.grouping)}/counts.csv. "
                  f"Run doc_counts.py --grouping {args.grouping} --write.", file=sys.stderr)
            return 1
        print(f"OK: {doc} matches counts.csv for {cache.current_view(args.grouping)}")
        return 0
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
