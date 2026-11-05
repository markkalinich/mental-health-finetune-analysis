"""Assignment files for the parent-registry agents (agents/PROMPT-parent-class.md v1), up to 30 parents each.
Reads outputs/funnel/<grouping>/<CURRENT>/parents_unregistered.csv; writes docs/<grouping>/agent-searches/<date>-parent-registry/assignment-N.txt.
--round N numbers the files from an offset so a second round does not overwrite the first."""
import csv, math
from _common import parser, resolve, long_date
p = parser(__doc__); p.add_argument("--round-offset", type=int, default=0, help="first assignment number minus one")
a = resolve(p.parse_args())
OUT = a.searches / f"{a.date}-parent-registry"; OUT.mkdir(parents=True, exist_ok=True)
unreg = list(csv.DictReader(open(a.run_dir / "parents_unregistered.csv")))
dec = {d["hf_id"]: d for d in csv.DictReader(open(a.run_dir / "decisions.csv"))}
rows = []
for u in unreg:
    kids = sorted(set(u["children"].split("|")))
    rows.append({"parent_id": u["parent_id"], "n_children": len(kids), "regex": dec[kids[0]]["parent_class"] or "not evaluated"})
n = len(rows); groups = max(1, math.ceil(n / 30)); size = math.ceil(n / groups) if n else 0
print(n, "parents ->", groups, "agents of about", size)
for g in range(groups):
    chunk = rows[g * size:(g + 1) * size]; k = a.round_offset + g + 1
    lines = [f"ASSIGNMENT ({a.grouping} parent registry, {long_date(a.date)}, agent {k}). Parent repo ids, in this order:"]
    lines += [f"{i}. {r['parent_id']}  (children: {r['n_children']}; regex said: {r['regex']})" for i, r in enumerate(chunk, 1)]
    lines += ["", f"Output CSV: {OUT}/parents-{k}.csv",
              "Repo root: /home/mkalinich/main. Cached parent cards may exist under model_selection/cache/readmes/<org>__<name>__<date>.md; the live card at https://huggingface.co/<id>/raw/main/README.md is authoritative."]
    (OUT / f"assignment-{k}.txt").write_text("\n".join(lines) + "\n")
print("wrote", groups, "assignment files to", OUT)
