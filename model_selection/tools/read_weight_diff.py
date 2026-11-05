"""Summarise weight_diff.py output, one line per fine-tune/parent pair, and suggest a reading.

    .venv/bin/python model_selection/tools/read_weight_diff.py \
        outputs/weight-diff/<folder>

Reads every `<finetune>.csv` in the folder (the per-tensor table weight_diff.py writes) and writes
`summary.csv` next to them. The reading patterns are the four in
`docs/mental_health_FT_funnel/how-models-are-filtered.md`, section "Training objective and update scope":

  lora rank r        sharp drop after the r-th singular value (sigma_{r+1}/sigma_r < 0.1) and >99% of the
                     squared Frobenius norm in the top r, on the sampled projections that changed
  lora on <modules>  no drop, but only some projection types changed (the others are exactly zero)
  full               no drop, every matrix changed, change not uniform
  quantised-merge?   no drop, every matrix changed by a uniform 0.2-10% (coefficient of variation of the
                     relative change across projection matrices below 0.5); a (Q)LoRA merged into a
                     de-quantised base looks like this. The question mark is deliberate: confirm by eye.

The suggestion is a starting point. The per-matrix CSV is the evidence; read it before writing a verdict.
"""
from __future__ import annotations

import csv
import statistics
import sys
from pathlib import Path

RANKS = (8, 16, 32, 64, 128, 256)
NOISE = 1e-6  # relative Frobenius change at or below this is a dtype round trip, not training
PROJ = ("q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj")
FIELDS = [
    "finetune", "parent", "n_matrices", "n_matrices_changed", "proj_types_changed", "proj_types_unchanged",
    "rel_change_median", "rel_change_min", "rel_change_max", "rel_change_cv",
    "n_sampled", "lora_rank_votes", "lora_rank", "suggested_reading", "note",
]


def f(x: str) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def proj_type(name: str) -> str | None:
    for p in PROJ:
        if f".{p}." in name or name.endswith(f".{p}.weight"):
            return p
    return None


def rank_of(row: dict) -> int | None:
    """Smallest r with >99% energy in the top r and a sharp drop after r; None if no drop."""
    for r in RANKS:
        e, drop = f(row.get(f"energy_top{r}")), f(row.get(f"sigma_{r + 1}_over_sigma_{r}"))
        if e is not None and drop is not None and e > 0.99 and drop < 0.1:
            return r
    return None


def summarise(path: Path) -> dict:
    rows = list(csv.DictReader(path.open()))
    if not rows:
        return {"finetune": path.stem, "note": "empty csv"}
    mats = [r for r in rows if r.get("ndim") == "2" and not r.get("skip_reason")]
    # "changed" means more than re-save noise: a relative change above 1e-6 (bfloat16 round trips leave ~1e-8)
    changed = [r for r in mats if r.get("exact_zero") == "0" and (f(r.get("rel_frobenius")) or 0.0) > NOISE]
    types_changed = sorted({t for r in changed if (t := proj_type(r["tensor_name"]))})
    types_seen = sorted({t for r in mats if (t := proj_type(r["tensor_name"]))})
    types_unchanged = [t for t in types_seen if t not in types_changed]
    rel = [v for r in changed if proj_type(r["tensor_name"]) and (v := f(r["rel_frobenius"])) is not None]
    sampled = [r for r in changed if r.get("svd_sampled") == "1" and proj_type(r["tensor_name"])]
    votes = [rank_of(r) for r in sampled]
    ranks = [v for v in votes if v is not None]
    out = {
        "finetune": rows[0]["finetune"], "parent": rows[0]["parent"],
        "n_matrices": len(mats), "n_matrices_changed": len(changed),
        "proj_types_changed": "|".join(types_changed), "proj_types_unchanged": "|".join(types_unchanged),
        "n_sampled": len(sampled), "lora_rank_votes": "|".join("-" if v is None else str(v) for v in votes),
        "lora_rank": "", "note": "",
    }
    if rel:
        med, lo, hi = statistics.median(rel), min(rel), max(rel)
        cv = (statistics.pstdev(rel) / statistics.mean(rel)) if len(rel) > 1 and statistics.mean(rel) else 0.0
        out.update(rel_change_median=f"{med:.3e}", rel_change_min=f"{lo:.3e}", rel_change_max=f"{hi:.3e}", rel_change_cv=f"{cv:.2f}")
    else:
        med = cv = None
        out.update(rel_change_median="", rel_change_min="", rel_change_max="", rel_change_cv="")
    if not changed:
        out["suggested_reading"] = "identical to parent"
    elif ranks and len(ranks) >= max(1, len(sampled) // 2):
        r = statistics.mode(ranks)
        out["lora_rank"] = str(r)
        out["suggested_reading"] = f"lora rank {r}" + (f" on {'|'.join(types_changed)} only" if types_unchanged else "")
        if len(set(ranks)) > 1:
            out["note"] = f"rank votes disagree: {sorted(set(ranks))}"
    elif types_unchanged:
        out["suggested_reading"] = f"lora on {'|'.join(types_changed)} only (no drop)"
    elif med is not None and 0.002 <= med <= 0.10 and cv is not None and cv < 0.5:
        out["suggested_reading"] = "quantised-merge? (uniform small change, no drop) or full"
    else:
        out["suggested_reading"] = "full (no drop, every matrix changed)"
    return out


def main() -> None:
    folder = Path(sys.argv[1])
    files = sorted(p for p in folder.glob("*.csv") if p.name not in ("pairs.csv", "pairs-waiting.csv", "summary.csv", "card-vs-weights.csv"))
    if not files:
        sys.exit(f"no per-pair csv in {folder}")
    rows = [summarise(p) for p in files]
    with (folder / "summary.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r.get('finetune', ''):62s} {r.get('suggested_reading', ''):52s} changed {r.get('n_matrices_changed', '')}/{r.get('n_matrices', '')}  med {r.get('rel_change_median', '')} cv {r.get('rel_change_cv', '')}  votes {r.get('lora_rank_votes', '')} {r.get('note', '')}")
    print(f"-> {folder / 'summary.csv'}")


if __name__ == "__main__":
    main()
