"""Assignment files for the extraction agents (agents/PROMPT-extract.md, current version), 5 models per agent (Mark, 9 Oct 2026), for every
model in outputs/funnel/<grouping>/<CURRENT>/kept.csv. --only FILE restricts to the hf_ids listed in FILE (one per line)."""
import csv, math, re
from _common import parser, resolve, INV, newest_card, long_date
p = parser(__doc__); p.add_argument("--only"); p.add_argument("--per-agent", type=int, default=5)
a = resolve(p.parse_args())
OUT = a.searches / f"{a.date}-extraction"
for sub in ("assignments", "extractions", "reports"): (OUT / sub).mkdir(parents=True, exist_ok=True)
ver = re.search(r"^Version (\d+)", (INV / "agents" / "PROMPT-extract.md").read_text(), re.M).group(1)
kept = list(csv.DictReader(open(a.run_dir / "kept.csv")))
if a.only:
    only = {l.strip() for l in open(a.only) if l.strip()}; kept = [r for r in kept if r["hf_id"] in only]
rows = [{"hf_id": r["hf_id"], "slug": r["hf_id"].replace("/", "__"), "card": newest_card(r["hf_id"]), "methods": r["methods"], "datasets": r["datasets"], "parent": r["parent"]} for r in kept]
missing = [r["hf_id"] for r in rows if not r["card"]]
assert not missing, f"no cached card: {missing}"
n = len(rows); agents = math.ceil(n / a.per_agent); groups = [rows[i * a.per_agent:(i + 1) * a.per_agent] for i in range(agents)]
with (OUT / "assignments.csv").open("w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["agent", "hf_id", "cached_card", "inventory_methods", "inventory_datasets", "inventory_parent"])
    for i, grp in enumerate(groups, 1):
        for r in grp: w.writerow([i, r["hf_id"], r["card"].name, r["methods"], r["datasets"], r["parent"]])
for i, grp in enumerate(groups, 1):
    lines = [f"First, read /home/mkalinich/main/model_selection/agents/PROMPT-extract.md (version {ver}) with the Read tool and follow it exactly. It is your full instructions. Do the models below one after another; write both output files for a model before starting the next.",
             "", f"ASSIGNMENT ({a.grouping} kept-model extraction, {long_date(a.date)}, agent {i} of {agents}).", ""]
    for j, r in enumerate(grp, 1):
        lines += [f"Model {j}: {r['hf_id']}", f"  Cached card: {r['card']}", f"  Inventory row: methods='{r['methods']}' datasets='{r['datasets']}' parent='{r['parent']}'",
                  f"  Output JSON: {OUT}/extractions/{r['slug']}.json", f"  Output markdown: {OUT}/reports/{r['slug']}.md", ""]
    lines.append("Repo root: /home/mkalinich/main. Use web fetch/search for Hub, arXiv HTML, GitHub, dataset pages. Do not download weights or PDFs. Do not edit any other file. Final message: the file paths, per-model wall time, and one line per unfilled field.")
    (OUT / "assignments" / f"agent-{i}.txt").write_text("\n".join(lines) + "\n")
print(n, "kept models ->", agents, "agents (prompt v" + ver + "); wrote", OUT / "assignments")
