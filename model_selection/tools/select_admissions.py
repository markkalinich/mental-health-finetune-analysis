"""From recovered.csv, write recovered-to-admit.csv under the admission rule of the safety run (Mark, 9 Oct 2026 21:15):
models outside a sweep are admitted one by one; for each sweep (sweeps.csv) one representative is admitted, the most
downloaded recovered member (downloads from the run's decisions.csv). Then run:
  admit_recovered.py --grouping <g> --recovered <folder>/recovered-to-admit.csv --decided-on <date>
Also writes sweep-representatives.csv (which member stands for which)."""
import csv, collections
from _common import parser, resolve
a = resolve(parser(__doc__).parse_args())
OUT = a.searches / f"{a.date}-dataset-search"
rec = list(csv.DictReader(open(OUT / "recovered.csv")))
dl = {d["hf_id"]: int(d["downloads"] or 0) for d in csv.DictReader(open(a.run_dir / "decisions.csv"))}
sweep_of = {r["hf_id"]: (r["author"], r["name_template"]) for r in csv.DictReader(open(OUT / "sweeps.csv"))}
members = collections.defaultdict(list)
for r in csv.DictReader(open(OUT / "sweeps.csv")): members[(r["author"], r["name_template"])].append(r["hf_id"])
by_sweep = collections.defaultdict(list)
admit, reps = [], []
for r in rec:
    k = sweep_of.get(r["hf_id"])
    if k is None: admit.append(r)
    else: by_sweep[k].append(r)
for k, rows in sorted(by_sweep.items()):
    best = max(rows, key=lambda r: dl.get(r["hf_id"], 0)); admit.append(best)
    for r in rows:
        reps.append({"sweep_group": f"{k[0]} / {k[1]}", "members_in_pool": len(members[k]), "recovered_members": len(rows), "representative": best["hf_id"],
                     "representative_downloads": dl.get(best["hf_id"], 0), "member": r["hf_id"], "member_downloads": dl.get(r["hf_id"], 0)})
with (OUT / "recovered-to-admit.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rec[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(admit)
with (OUT / "sweep-representatives.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(reps[0].keys()) if reps else ["sweep_group"], lineterminator="\n"); w.writeheader(); w.writerows(reps)
print(f"{len(rec)} recovered -> {len(admit)} to admit ({len(admit) - len(by_sweep)} outside a sweep + {len(by_sweep)} sweep representatives); {len(rec) - len(admit)} sweep members stand behind a representative")
