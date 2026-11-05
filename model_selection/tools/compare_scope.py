"""Card's update scope vs the weights, one line per model that has a weight run.

    .venv/bin/python model_selection/tools/compare_scope.py --grouping safety \
        --weights outputs/weight-diff/2026-10-10-safety

Joins `summary.csv` (from tools/read_weight_diff.py) with the extraction record's `update_scope`,
`lora_rank` and `quantized_base_during_training` (outputs/funnel/<grouping>/<CURRENT>/extractions.csv) and writes
`card-vs-weights.csv` next to the summary. The `agreement` column is mechanical:

  agree                card says LoRA/QLoRA rank r and the weights show a drop at r; or card says full and
                       the weights show no drop with every matrix changed
  agree (rank learned) card says LoRA/QLoRA without a rank and the weights show a drop
  agree (merge pattern) card says QLoRA, or LoRA on a quantised base, and the weights show the uniform
                       no-drop change of an adapter merged into a de-quantised base
  no scope on card     card gives no scope; the weights reading stands alone
  read by hand         anything else (card says LoRA, weights show no drop and no quantised base; rank
                       differs; multi-stage recipes). The per-matrix CSV is the evidence.

Models in the step-5 list without a weight run are listed with `agreement = no weight run` and the reason
from pairs-waiting.csv.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import parser, resolve  # noqa: E402

FIELDS = ["hf_id", "card_scope", "card_rank", "card_quantized_base", "weights_reading", "weights_rank",
          "n_changed", "n_matrices", "rel_change_median", "agreement", "note"]


def main() -> None:
    ap = parser(__doc__)
    ap.add_argument("--weights", type=Path, required=True)
    a = resolve(ap.parse_args())
    ex = {r["hf_id"]: r for r in csv.DictReader((a.run_dir / "extractions.csv").open())}
    s5 = sorted(r["hf_id"] for r in csv.DictReader((a.run_dir / "kept_method_stated.csv").open()))
    summ = {r["finetune"]: r for r in csv.DictReader((a.weights / "summary.csv").open())}
    waiting = {}
    wp = a.weights / "pairs-waiting.csv"
    if wp.exists():
        for r in csv.DictReader(wp.open()):
            waiting[r["finetune_dir"]] = "; ".join(x for x in (
                f"fine-tune {r['finetune_missing']}" if r["finetune_missing"] else "",
                f"parent {r['parent_missing']}" if r["parent_missing"] else "") if x)
    out = []
    for h in s5:
        e = ex.get(h, {})
        scope, rank, q = e.get("update_scope", ""), e.get("lora_rank", ""), e.get("quantized_base_during_training", "")
        key = h.replace("/", "__")
        row = {"hf_id": h, "card_scope": scope, "card_rank": rank, "card_quantized_base": q,
               "weights_reading": "", "weights_rank": "", "n_changed": "", "n_matrices": "", "rel_change_median": "", "note": ""}
        s = summ.get(key)
        if not s:
            row["agreement"] = "no weight run"
            row["note"] = waiting.get(key, "no result csv")
            out.append(row)
            continue
        reading, wrank = s["suggested_reading"], s["lora_rank"]
        row.update(weights_reading=reading, weights_rank=wrank, n_changed=s["n_matrices_changed"],
                   n_matrices=s["n_matrices"], rel_change_median=s["rel_change_median"], note=s["note"])
        lora_card = scope in ("lora", "qlora", "adapter_other")
        quant_card = scope == "qlora" or q == "yes"
        if reading.startswith("lora rank") and lora_card:
            if rank and rank == wrank:
                row["agreement"] = "agree"
            elif not rank:
                row["agreement"] = "agree (rank learned)"
            else:
                row["agreement"] = "read by hand"
                row["note"] = f"card rank {rank}, weights {wrank}. " + row["note"]
        elif reading.startswith("full") and scope == "full":
            row["agreement"] = "agree"
        elif reading.startswith("quantised-merge?") and quant_card:
            row["agreement"] = "agree (merge pattern)"
        elif scope in ("", "not stated"):
            row["agreement"] = "no scope on card"
        else:
            row["agreement"] = "read by hand"
        out.append(row)
    with (a.weights / "card-vs-weights.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(f"{r['hf_id']:62s} card {r['card_scope']:10s} r={r['card_rank']:3s} q={r['card_quantized_base']:3s} | {r['weights_reading'][:48]:48s} | {r['agreement']}  {r['note'][:80]}")
    print(f"-> {a.weights / 'card-vs-weights.csv'}")


if __name__ == "__main__":
    main()
