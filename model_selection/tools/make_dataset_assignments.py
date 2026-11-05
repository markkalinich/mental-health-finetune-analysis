"""Assignment files for the dataset-search agents (agents/PROMPT-dataset-search.md v2), 10 models per agent, with the sweep rule.

Sweep rule (safety run, 9 Oct 2026; medical confirmation is DECISIONS-PENDING row 3 of the safety folder): a sweep is one
author's pool models whose repo names match after every digit run is replaced by '#' and only the first two '-'/'_'
tokens are kept, with --sweep-min (5) or more members. Each sweep is searched through two representatives (first and
middle member, in name order); the rest are recorded in sweeps.csv as 'covered by' those two and are not assigned.
Models outside a sweep are assigned one by one, first, so the sweep tail can be stopped at any point.
Writes assignments.csv, assignments/agent-N.txt, sweeps.csv, not-searched.csv (the covered sweep members).

--append (added 10 Oct 2026 for the medical run, where a pilot wave was searched before the parent registry was complete):
the sweep rule is computed over the whole pool-text-generating.csv, but models already in assignments.csv or
not-searched.csv are left alone, new agents are numbered after the last existing one, and the four output files are
extended rather than rewritten. A pool model that was searched in the pilot still counts as a sweep member when the
sweep is detected, so a later sweep may be represented by a pilot model that was already searched."""
import csv, math, re, collections
from _common import parser, resolve, long_date
p = parser(__doc__); p.add_argument("--sweep-min", type=int, default=5); p.add_argument("--per-agent", type=int, default=10)
p.add_argument("--append", action="store_true", help="keep existing assignments; add agents for the pool models not yet assigned or covered")
a = resolve(p.parse_args())
OUT = a.searches / f"{a.date}-dataset-search"; (OUT / "assignments").mkdir(exist_ok=True); (OUT / "reports").mkdir(exist_ok=True)
pool = sorted((r["hf_id"] for r in csv.DictReader(open(OUT / "pool-text-generating.csv"))), key=str.lower)
def key(hf):
    author, name = hf.split("/", 1)
    toks = re.split(r"[-_]", re.sub(r"\d+", "#", name).lower())
    return author, "-".join(toks[:2])
groups = collections.defaultdict(list)
for hf in pool: groups[key(hf)].append(hf)
sweeps = {k: v for k, v in groups.items() if len(v) >= a.sweep_min}
reps, covered = {}, {}
for k, v in sweeps.items():
    r = [v[0], v[len(v) // 2]] if len(v) > 1 else [v[0]]
    reps[k] = r
    for m in v:
        if m not in r: covered[m] = k
singles = [hf for hf in pool if key(hf) not in sweeps]
rep_list = [m for k in sorted(sweeps) for m in reps[k]]
order = singles + rep_list
done, first_agent, mode = set(), 1, "w"
if a.append:
    prev = list(csv.DictReader(open(OUT / "assignments.csv")))
    done = {r["hf_id"] for r in prev} | {r["hf_id"] for r in csv.DictReader(open(OUT / "not-searched.csv"))}
    first_agent = max(int(r["agent"]) for r in prev) + 1
    order = [hf for hf in order if hf not in done]
    covered = {m: k for m, k in covered.items() if m not in done}
    mode = "a"
n = len(order); agents = math.ceil(n / a.per_agent); total_agents = first_agent - 1 + agents
with (OUT / "assignments.csv").open(mode, newline="") as fh:
    w = csv.writer(fh)
    if mode == "w": w.writerow(["agent", "hf_id", "role"])
    for i in range(agents):
        num = first_agent + i
        chunk = order[i * a.per_agent:(i + 1) * a.per_agent]
        for hf in chunk: w.writerow([num, hf, "sweep representative" if key(hf) in sweeps else "single"])
        lines = [f"ASSIGNMENT ({a.grouping} dataset search, {long_date(a.date)}, agent {num} of {total_agents}). Repository ids, in this order:"]
        lines += [f"{j}. {hf}" for j, hf in enumerate(chunk, 1)]
        lines += ["", "Output files (the only files you may write):", f"- CSV: {OUT}/reports/agent-{num}.csv", f"- Markdown: {OUT}/reports/agent-{num}.md", "",
                  "Repo root is /home/mkalinich/main. Cached cards are under model_selection/cache/readmes/ (file name <org>__<name>__<date>.md; use the newest). Use web fetch/search for Hub, arXiv HTML, GitHub, Kaggle pages. Do not download weights or PDFs. Do not edit any other file."]
        (OUT / "assignments" / f"agent-{num}.txt").write_text("\n".join(lines) + "\n")
with (OUT / "sweeps.csv").open(mode, newline="") as fh:
    w = csv.writer(fh)
    if mode == "w": w.writerow(["author", "name_template", "members", "hf_id", "role"])
    for k in sorted(sweeps):
        if a.append and all(m in done for m in sweeps[k]): continue  # sweep already written in an earlier wave
        for m in sweeps[k]:
            w.writerow([k[0], k[1], len(sweeps[k]), m, "representative" if m in reps[k] else "covered by representatives"])
with (OUT / "not-searched.csv").open(mode, newline="") as fh:
    w = csv.writer(fh)
    if mode == "w": w.writerow(["hf_id", "author", "name_template", "covered_by"])
    for m, k in covered.items(): w.writerow([m, k[0], k[1], "|".join(reps[k])])
print(f"pool {len(pool)}: {len(singles)} outside a sweep + {len(rep_list)} representatives of {len(sweeps)} sweeps ({len(covered)} covered members not assigned)"
      + (f"; {len(done)} already assigned or covered" if a.append else "") + f" -> {agents} agents ({first_agent}..{total_agents})")
