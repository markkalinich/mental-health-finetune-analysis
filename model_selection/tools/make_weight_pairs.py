"""pairs.csv for weight_diff.py: every model that passes step 5 and its parent, split by what is on disk.

    .venv/bin/python model_selection/tools/make_weight_pairs.py --grouping safety \
        --out outputs/weight-diff/2026-10-10-safety

Writes `pairs.csv` (both folders complete under ~/hf_models, by download.py's definition of complete) and
`pairs-waiting.csv` (what is missing and why). Pairs that already have a `<finetune>.csv` in --out are left
out of `pairs.csv` unless --redo is given, so the script can be rerun after more downloads land.

Then:
    CUDA_VISIBLE_DEVICES='' OMP_NUM_THREADS=8 /home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python \
        model_selection/weight_diff.py --pairs <out>/pairs.csv --out <out>
    .venv/bin/python model_selection/tools/read_weight_diff.py <out>
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from _common import parser, resolve  # noqa: E402
from download import DEFAULT_DEST, complete, folder  # noqa: E402


def main() -> None:
    ap = parser(__doc__)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--redo", action="store_true", help="include pairs that already have a result csv")
    a = resolve(ap.parse_args())
    a.out.mkdir(parents=True, exist_ok=True)
    rows = sorted(csv.DictReader((a.run_dir / "kept_method_stated.csv").open()), key=lambda r: r["hf_id"])
    ready, waiting, done = [], [], []
    for r in rows:
        ft, par = folder(DEFAULT_DEST, r["hf_id"]), folder(DEFAULT_DEST, r["parent"])
        ok_ft, why_ft = complete(ft)
        ok_par, why_par = complete(par)
        if not (ok_ft and ok_par):
            waiting.append([ft.name, par.name, "" if ok_ft else why_ft, "" if ok_par else why_par])
        elif (a.out / f"{ft.name}.csv").exists() and not a.redo:
            done.append(ft.name)
        else:
            ready.append([ft.name, par.name])
    with (a.out / "pairs.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["finetune_dir", "parent_dir"])
        w.writerows(ready)
    with (a.out / "pairs-waiting.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["finetune_dir", "parent_dir", "finetune_missing", "parent_missing"])
        w.writerows(waiting)
    print(f"{len(ready)} pairs to run -> {a.out / 'pairs.csv'}; {len(done)} already have a result; {len(waiting)} waiting -> pairs-waiting.csv")
    for p in waiting:
        print("  waiting:", p)


if __name__ == "__main__":
    main()
