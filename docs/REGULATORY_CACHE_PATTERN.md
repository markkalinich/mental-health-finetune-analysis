# How `regulatory_simulations` pins paper cache data

There are **two** related patterns in that repo; both are useful to understand.

## 1. Shipped frozen cache: `regulatory_paper_cache_v3/` (paper subset)

The public repo includes a **dedicated directory** with a **frozen** SQLite file used for reproducibility:

- **Path on GitHub:** [`regulatory_simulations/regulatory_paper_cache_v3`](https://github.com/markkalinich/regulatory_simulations/tree/main/regulatory_paper_cache_v3)
- **Contents:** `results.db` (only entries for the **14** paper models across SI / TR / TE), **`MD5SUM.txt`** for `md5sum -c` verification, and a **README** (counts, model list, success rates).

That database is a **subset** of what a full development cache might hold: **just the rows needed for the paper**, checked in so anyone can reproduce figures without your private multi-model cache. Producing it was effectively a **manual / one-off export** (or external tooling), **not** something the main pipeline rewrites every run—the important part is the **artifact + checksum in git**.

**Verification** (from their README):

```bash
cd regulatory_paper_cache_v3
md5sum -c MD5SUM.txt
# Expected: results.db: OK
```

This is the pattern worth mirroring for **mental-health-finetune-analysis**: e.g. `manuscript_cache/results.db` + `SHA256SUMS` or `MD5SUM.txt` + short README, committed at a known revision.

---

## 2. Runtime pipeline: regenerate metrics from **any** cache path

Separately, `run_regulatory_simulation_paper_pipeline.py` can **point** at a cache directory (`--cache-dir`, default `cache`) and **only analyze paper models** by calling `batch_results_analyzer.py` with `--models` derived from `regulatory_paper_models.csv` (`regenerate_experiment_from_cache()`). That produces **new** `individual_prediction_performance/…` folders without deleting rows from the big DB.

If you **override** with experiment dirs that still contain **all** models, the pipeline uses **`filter_comprehensive_metrics()`** to subset CSV rows to paper models.

`batch_results_analyzer` may also emit a **cache manifest** JSON (`save_cache_manifest`) for traceability when loading from cache—complementary to, not a substitute for, a **frozen** `results.db` in the repo.

---

## Takeaway for this repo

| Approach | Purpose |
|----------|---------|
| **Frozen subset DB in git** (like `regulatory_paper_cache_v3`) | Unambiguous “what the paper used”; verify with checksums; optional manual build each manuscript revision. |
| **Filter at analysis time** | Everyday runs against a large local `results.db` without committing it. |

For revision / publication, prefer **(1)** plus the manifest in [`PROVENANCE_PLAN.md`](PROVENANCE_PLAN.md) so the sentence “we used this commit and this database file” is defensible.
