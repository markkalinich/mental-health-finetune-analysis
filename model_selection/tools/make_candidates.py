"""Candidate set for the medical dataset search (docs/medical_FT_funnel/DECISIONS-PENDING.md row 2, step ii).

A model is a candidate when, on the current run's decisions.csv and the cache as of the run date:
  - its decision is no_dataset;
  - it generates text by the make_pool.py rule (tagged text-generation / image-text-to-text / text2text-generation,
    or untagged with a ForCausalLM / ForConditionalGeneration / LMHeadModel config, or untagged with an unreadable config);
  - its card names exactly one parent (rules.extract_parent, the same reader the funnel uses);
  - that parent is not registered in parents.csv as pretrained, finetune, not_a_language_model, or unreadable
    (a parent with no row is kept; it is registered in step iii);
  - and, when the parent's own card is cached, the funnel's weight rule (rules.full_precision) keeps it
    (a parent whose card is not cached is kept; step iv's relaxed funnel run fetches and checks it).

Writes, in the dataset-search folder for --date:
  candidates.csv          hf_id, pool_class, parent, parent_registry, parent_weight, sweep_key, downloads
  parents-to-register.txt parents of candidates with no parents.csv row, one per line, most children first,
                          excluding parents whose id carries a quantization marker and whose card is not cached
                          (they are checked by weight in step iv and registered then if they pass)
  candidates-cut.csv      every no_dataset model that is not a candidate, with the reason
"""
import collections
import csv
import json
import re
import sys

from _common import parser, resolve, INV

sys.path.insert(0, str(INV))
import cache  # noqa: E402
import rules  # noqa: E402

GEN_TAGS = {"text-generation", "image-text-to-text", "text2text-generation"}
FAIL_REG = {"pretrained", "finetune", "not_a_language_model", "unreadable"}
QUANT_MARKERS = ("bnb-4bit", "4bit", "8bit", "gguf", "awq", "gptq", "nf4", "int4", "int8")


def sweep_key(hf: str) -> str:
    """Same key as make_dataset_assignments.py: author + first two name tokens with digit runs collapsed."""
    author, name = hf.split("/", 1)
    toks = re.split(r"[-_]", re.sub(r"\d+", "#", name).lower())
    return author + "/" + "-".join(toks[:2])


def main() -> int:
    p = parser(__doc__)
    a = resolve(p.parse_args())
    out = a.searches / f"{a.date}-dataset-search"
    out.mkdir(parents=True, exist_ok=True)
    as_of = a.run_dir.name
    decisions = list(csv.DictReader((a.run_dir / "decisions.csv").open(newline="")))
    no_ds = [d for d in decisions if d["decision"] == "no_dataset"]
    cards = cache.load_cards(as_of)
    registry = {r["parent_id"].lower(): r for r in csv.DictReader((INV / "parents.csv").open(newline=""))
                if r["decided_on"] <= as_of}

    def pool_class(d: dict) -> str:
        tag = (d["pipeline_tag"] or "").strip()
        if tag in GEN_TAGS:
            return "tagged generating"
        if tag:
            return "tagged other"
        path = cache.newest_config(d["hf_id"], as_of)
        if path is None:
            return "untagged, config not fetched"
        text = path.read_text(errors="replace")
        if text.startswith("FETCH_ERR"):
            return "untagged, config unknown (kept in pool)"
        try:
            arch = (json.loads(text).get("architectures") or [""])[0]
        except Exception:  # noqa: BLE001
            return "untagged, config unknown (kept in pool)"
        if arch.endswith(("ForCausalLM", "ForConditionalGeneration", "LMHeadModel")):
            return "untagged, generative architecture"
        return "untagged, other architecture"

    weight_cache: dict = {}

    def parent_weight(parent: str) -> str:
        k = parent.lower()
        if k not in weight_cache:
            row = cards.get(k)
            if row is None:
                weight_cache[k] = "card not cached"
            else:
                header = None
                if rules.header_files(row):
                    hp = cache.newest_bin_header(row["hf_id"], as_of)
                    if hp is None:
                        weight_cache[k] = "bin header not cached"
                        return weight_cache[k]
                    header = hp.read_text(errors="replace")
                weight_cache[k] = rules.full_precision(row, header)[0]
        return weight_cache[k]

    IN_POOL = {"tagged generating", "untagged, generative architecture", "untagged, config unknown (kept in pool)"}
    kept, cut = [], []
    for d in no_ds:
        hf = d["hf_id"]
        cls = pool_class(d)
        if cls not in IN_POOL:
            cut.append((hf, cls))
            continue
        row = cards.get(hf.lower())
        if row is None:
            cut.append((hf, "card not cached"))
            continue
        parent, _src, status = rules.extract_parent(row)
        if status != "one_parent":
            cut.append((hf, status))
            continue
        reg = registry.get(parent.lower())
        reg_class = reg["class"] if reg else "(no row)"
        if reg_class in FAIL_REG:
            cut.append((hf, f"parent registered {reg_class}: {parent}"))
            continue
        w = parent_weight(parent)
        if w not in ("keep", "card not cached", "bin header not cached"):
            cut.append((hf, f"parent fails the weight rule ({w}): {parent}"))
            continue
        kept.append({"hf_id": hf, "pool_class": cls, "parent": parent, "parent_registry": reg_class,
                     "parent_weight": w, "sweep_key": sweep_key(hf), "downloads": d.get("downloads", "")})

    kept.sort(key=lambda r: r["hf_id"].lower())
    with (out / "candidates.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(kept[0].keys()))
        w.writeheader()
        w.writerows(kept)
    with (out / "candidates-cut.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["hf_id", "reason"])
        w.writerows(sorted(cut, key=lambda r: r[0].lower()))

    unreg = collections.Counter(r["parent"] for r in kept if r["parent_registry"] == "(no row)")
    to_register, skipped_quant = [], []
    for parent, n in unreg.most_common():
        if any(m in parent.lower() for m in QUANT_MARKERS) and parent.lower() not in cards:
            skipped_quant.append((parent, n))
        else:
            to_register.append(parent)
    (out / "parents-to-register.txt").write_text("".join(f"{p}\n" for p in to_register))

    print(f"no_dataset {len(no_ds)}; candidates {len(kept)}; cut {len(cut)}")
    for k, v in collections.Counter(r[1].split(":")[0] for r in cut).most_common():
        print(f"  cut {v:5d}  {k}")
    for k, v in collections.Counter(r["pool_class"] for r in kept).most_common():
        print(f"  candidates {v:5d}  {k}")
    for k, v in collections.Counter(r["parent_registry"] for r in kept).most_common():
        print(f"  parent registry {v:5d}  {k}")
    for k, v in collections.Counter(r["parent_weight"] for r in kept).most_common():
        print(f"  parent weight {v:5d}  {k}")
    print(f"unregistered parents {len(unreg)} ({sum(unreg.values())} children): {len(to_register)} to register "
          f"({sum(unreg[p] for p in to_register)} children); {len(skipped_quant)} quantization-named with no cached card "
          f"left to the weight check ({sum(n for _p, n in skipped_quant)} children)")
    sweeps = collections.Counter(r["sweep_key"] for r in kept)
    big = {k: v for k, v in sweeps.items() if v >= 5}
    reps = sum(min(2, v) for v in big.values())
    singles = sum(v for k, v in sweeps.items() if v < 5)
    print(f"sweep rule: {len(big)} sweeps cover {sum(big.values())} candidates with {reps} representatives; "
          f"{singles} singles; {singles + reps} searches, {-(-(singles + reps) // 10)} agents of 10")
    print(f"wrote {out / 'candidates.csv'}, candidates-cut.csv, parents-to-register.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
