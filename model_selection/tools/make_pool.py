"""Pool for the dataset search: no_dataset models that generate text.

Text-generating = pipeline_tag in {text-generation, image-text-to-text, text2text-generation}; or no tag and a
config.json architecture ending ForCausalLM / ForConditionalGeneration / LMHeadModel; or no tag and no readable
config (kept in the pool). Writes configs-to-fetch.txt (untagged models with no cached config; run fetch_configs.py,
then this script again with --final), and with --final pool-text-generating.csv, pool-all-no-dataset.csv,
pool-by-author.csv."""
import csv, json, collections, sys
from _common import parser, resolve, INV
p = parser(__doc__); p.add_argument("--final", action="store_true")
a = resolve(p.parse_args())
OUT = a.searches / f"{a.date}-dataset-search"; OUT.mkdir(parents=True, exist_ok=True)
dec = list(csv.DictReader(open(a.run_dir / "decisions.csv")))
pool = [d for d in dec if d["decision"] == "no_dataset"]
GEN_TAGS = {"text-generation", "image-text-to-text", "text2text-generation"}
def arch(hf):
    fs = sorted((INV / "cache" / "configs").glob(f"{hf.replace('/', '__')}__*.json"))
    if not fs: return "(no config)"
    t = fs[-1].read_text()
    if t.startswith("FETCH_ERR"): return "(config " + t.split()[1][:20] + ")"
    try: return (json.loads(t).get("architectures") or ["(no architectures key)"])[0]
    except Exception: return "(bad json)"
rows, to_fetch = [], []
for d in pool:
    tag = d["pipeline_tag"]; ar = arch(d["hf_id"]) if not tag else ""
    if tag in GEN_TAGS: cls = "tagged generating"
    elif tag: cls = "tagged other"
    elif ar == "(no config)": cls = "untagged, config not fetched"; to_fetch.append(d["hf_id"])
    elif ar.endswith(("ForCausalLM", "ForConditionalGeneration", "LMHeadModel")): cls = "untagged, generative architecture"
    elif ar.startswith("("): cls = "untagged, config unknown (kept in pool)"
    else: cls = "untagged, other architecture"
    rows.append((d["hf_id"], tag, ar, cls, d.get("downloads", "")))
print("no_dataset:", len(pool))
for k, v in collections.Counter(r[3] for r in rows).most_common(): print(f"{v:5d}  {k}")
(OUT / "configs-to-fetch.txt").write_text("\n".join(to_fetch) + ("\n" if to_fetch else ""))
if to_fetch and a.final: sys.exit(f"{len(to_fetch)} untagged models still have no cached config.json; run fetch_configs.py first")
sel = [r for r in rows if r[3] in ("tagged generating", "untagged, generative architecture", "untagged, config unknown (kept in pool)")]
print("\nPOOL (text-generating, no dataset):", len(sel))
if a.final:
    with (OUT / "pool-text-generating.csv").open("w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["hf_id", "pipeline_tag", "architecture", "why_in_pool", "downloads"]); w.writerows(sorted(sel, key=lambda r: r[0].lower()))
    with (OUT / "pool-all-no-dataset.csv").open("w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["hf_id", "pipeline_tag", "architecture", "class", "downloads"]); w.writerows(sorted(rows, key=lambda r: r[0].lower()))
    by = collections.Counter(r[0].split("/")[0] for r in sel)
    with (OUT / "pool-by-author.csv").open("w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["author", "models_in_pool"]); w.writerows(by.most_common())
    print("wrote", OUT / "pool-text-generating.csv", "and pool-by-author.csv (", len(by), "authors )")
