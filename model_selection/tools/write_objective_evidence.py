"""Write docs/<grouping>_FT_funnel/decisions/objective-evidence.csv for the models that pass step 5.

    .venv/bin/python model_selection/tools/write_objective_evidence.py \
        --grouping safety --extraction-dir docs/safety_FT_funnel/agent-searches/2026-10-10-extraction \
        --hand docs/safety_FT_funnel/decisions/objective-hand-readings.csv --decided-on 2026-10-10

One row per model in outputs/funnel/<grouping>/<CURRENT>/kept_method_stated.csv. A row comes from the hand-readings
file when the model is listed there; otherwise from the v4 extraction record, at evidence level 1, quoting
`training_method.objective_quote`. The script stops if a record's objective is not sft/dpo/grpo/orpo/kto/ppo
and the model has no hand reading, so that nothing is silently labelled.

Columns: hf_id, objective, stages, evidence_level, basis, decided_by, decided_on.
`objective` is the last training stage; `stages` lists every stage in the order the author gives them
(`sft|grpo` = SFT first, then GRPO). Levels: `1 stated`, `2 inferred from the author's own words or
toolchain`, `3 assumed from data format alone`.

The hand-readings CSV has columns hf_id, objective, stages, evidence_level, basis, decided_by.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import parser, resolve  # noqa: E402

OBJECTIVES = {"sft", "dpo", "grpo", "orpo", "kto", "ppo"}
# Hand readings may also record these two, which the cards state but which are not fine-tuning objectives in the
# list above (13 Oct 2026, medical: MediPhi and MilyaShams continued pre-training, taksa1990 distillation). Whether
# such a model stays in the study is Mark's call; the row records what the author said.
HAND_ONLY_OBJECTIVES = {"continued_pretraining", "distillation", "unknown"}
LEVELS = {"1 stated", "2 inferred from the author's own words or toolchain", "3 assumed from data format alone"}
FIELDS = ["hf_id", "objective", "stages", "evidence_level", "basis", "decided_by", "decided_on"]


def main() -> None:
    ap = parser(__doc__)
    ap.add_argument("--extraction-dir", type=Path, required=True)
    ap.add_argument("--hand", type=Path, required=True)
    ap.add_argument("--decided-on", required=True)
    ap.add_argument("--prompt-version", default="v4")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--skip-unrecorded", action="store_true",
                    help="leave out step-5 models with neither a record nor a hand reading (e.g. new arrivals waiting on Mark) instead of stopping")
    a = resolve(ap.parse_args())
    run = a.run_dir
    out = a.out or a.docs / "decisions" / "objective-evidence.csv"

    hand = {}
    for r in csv.DictReader(a.hand.open()):
        if r["evidence_level"] not in LEVELS or r["objective"] not in OBJECTIVES | HAND_ONLY_OBJECTIVES:
            sys.exit(f"hand reading for {r['hf_id']}: level {r['evidence_level']!r} or objective {r['objective']!r} not allowed")
        hand[r["hf_id"]] = r
    s5 = sorted(r["hf_id"] for r in csv.DictReader((run / "kept_method_stated.csv").open()))
    ex = {r["hf_id"]: r for r in csv.DictReader((run / "extractions.csv").open())}
    rows, problems = [], []
    for h in s5:
        if h in hand:
            r = hand[h]
            rows.append([h, r["objective"], r["stages"], r["evidence_level"], r["basis"], r["decided_by"], a.decided_on])
            continue
        if h not in ex:
            problems.append(f"{h}: no extraction record")
            continue
        obj = ex[h]["objective"]
        if obj not in OBJECTIVES:
            problems.append(f"{h}: record objective {obj!r} needs a hand reading")
            continue
        j = json.load((a.extraction_dir / "extractions" / (h.replace("/", "__") + ".json")).open())
        tm = j["training_method"]
        url = tm.get("objective_url") or ""
        src = "card" if f"huggingface.co/{h}" in url else url or "card"
        rows.append([h, obj, obj, "1 stated", f'named in the card or a linked source ({src}): "{tm["objective_quote"]}"',
                     f"agent grok-4.7 (PROMPT-extract {a.prompt_version})", a.decided_on])
    if problems and not a.skip_unrecorded:
        sys.exit("stopped; add hand readings for (or pass --skip-unrecorded while they wait on Mark):\n  " + "\n  ".join(problems))
    if problems:
        print(f"skipped {len(problems)} models with no record or hand reading:\n  " + "\n  ".join(problems), file=sys.stderr)
    extra = sorted(set(hand) - set(s5))
    if extra:
        print(f"note: {len(extra)} hand readings are for models not in the step-5 list: {extra}", file=sys.stderr)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(FIELDS)
        w.writerows(rows)
    print(f"{len(rows)} rows -> {out}")
    print("levels:", dict(collections.Counter(r[3][0] for r in rows)))
    print("objective:", dict(collections.Counter(r[1] for r in rows)))
    print("stages:", dict(collections.Counter(r[2] for r in rows)))


if __name__ == "__main__":
    main()
