# Handoff: paper pipeline, provenance, and data-flow state (2026-03-30)

This document is for **another engineer or model** taking over. It reconciles **README Mermaid phases** with **`run_paper_pipeline.py` log phases** (they use different numbering) and records **known design tension** around the combined metrics CSV.

---

## 1. Phase naming: README vs `run_paper_pipeline.py` (critical)

The **README** (`README.md`) uses a **four-phase** data-flow diagram (Phase 0–3). **`run_paper_pipeline.py`** uses **different** labels in logs (Phase 1, 1b, 2, 3, 4). **Do not conflate them.**

| README Mermaid | What it is |
|----------------|------------|
| **Phase 0** | Inputs: finalized CSVs, prompts, `config/models_config.csv` |
| **Phase 1: Inference** | LM Studio → SQLite `cache/results.db` → timestamped dirs under `results/individual_prediction_performance/<task>/<run_id>/` |
| **Phase 2: Metrics rollup** | Each run produces **`.../<run_id>/tables/comprehensive_metrics.csv`** (per task); **`analysis/combine_results.py`** merges three per-task files → **`data/inputs/model_results/all_models_all_tasks.csv`** |
| **Phase 3: Figures and tables** | Reads combined CSV (and guard re-parse paths may read cache — dashed edges in diagram) |

| `run_paper_pipeline.py` log label | Maps to README |
|-----------------------------------|----------------|
| **PHASE 1: RUNNING EXPERIMENTS** | README **Phase 1** (inference runs via `bash_scripts/run_all_models.sh`). As each task’s experiment **finishes**, downstream analysis writes **`tables/comprehensive_metrics.csv`** inside that task’s run folder — that is **README Phase 2’s first box** (“per-task comprehensive_metrics”), not something created during the script’s “PHASE 2: figures”. |
| **(1b) Updating combined results CSV** | README **Phase 2** merge step: runs `combine_results.py` → updates **`all_models_all_tasks.csv`** |
| **PHASE 2: MAIN FIGURES** | README **Phase 3** (figures 1–3) |
| **PHASE 3: TABLE 1** | README **Phase 3** (regression / table) |
| **PHASE 4: SUPPLEMENTARY** | README **Phase 3** (supplementary); reads **per-task** `comprehensive_metrics.csv` from **resolved experiment dirs** |

**Answer to “comprehensive_metrics isn’t until phase 2?”**

- In the **README diagram**, **`comprehensive_metrics.csv` is Phase 2 (Metrics rollup)**, i.e. **after** timestamped runs and **before** the combined CSV and figures.
- In **`run_paper_pipeline.py` logs**, **comprehensive_metrics is not produced in “PHASE 2”** — that PHASE 2 is **figures**. Per-task `comprehensive_metrics.csv` files are produced **during/after each experiment run** (Phase 1 in the script), which aligns with **README Phase 2’s input edge** (`runs → per_task`).

So: **yes**, earlier explanations should be read **against the README’s Phase 2 = metrics**, not against the **paper script’s** “PHASE 2 = main figures”.

---

## 2. File locations (authoritative paths)

### Per-experiment run (per task)

- **Directory:** `results/individual_prediction_performance/<task_name>/<YYYYMMDD_HHMMSS_*_>/`
- **Metrics file:** `<run_dir>/tables/comprehensive_metrics.csv`
- **Written by:** experiment analysis path (e.g. `analysis/model_performance/batch_results_analyzer.py` saves `output_dir / 'tables' / 'comprehensive_metrics.csv'`).

### Combined (repo-global default)

- **Path:** `data/inputs/model_results/all_models_all_tasks.csv`
- **Written by:** `analysis/combine_results.py` (concat of three per-task `comprehensive_metrics.csv` files + `task` column, selected columns).
- **Risk:** Single mutable path consumed by many scripts → **stale / mismatch** if not refreshed from the intended trio of run dirs. Acknowledged as a design problem; **direction** in README: pinned ground truth per run (not fully implemented).

### Paper pipeline run output (timestamped)

- **Root:** `results/FINETUNE_PAPER_FIGURES/<YYYYMMDD_HHMMSS>/`
- **Subdirs:** `figure_1/`, `figure_2/`, `figure_3/`, `table_1/`, `supplementary_figures/`, `pipeline.log`
- **Machine run record:** `PROVENANCE.json` (not a user “manifest”; see below)

---

## 3. What was implemented recently

1. **`run_paper_pipeline.py`**
   - Resolves SI/TR/TE experiment dirs: Phase 1 outputs → `--si-dir` / `--tr-dir` / `--te-dir` → `--use-latest-experiment-dirs` → dry-run preview.
   - **Non–dry-run** with `--skip-experiments` **requires** explicit dirs or `--use-latest-experiment-dirs` (no silent latest).
   - Runs **`combine_results.py`** with explicit dirs before figures/table when needed.
   - Supplementary figures use resolved per-task dirs (not anonymous latest glob only).

2. **`utilities/paper_run_provenance.py`**
   - Writes **`PROVENANCE.json`** at end of each run (`finally` block). Schema: `paper_run_provenance_v1`.
   - **Terminology:** This is a **machine-generated run record**, not a user-authored **manifest** (reserved for future input spec).
   - Flag: **`--no-provenance`** to skip writing.
   - Records: git head/dirty, `cache/results.db` path + SHA-256, argv, CLI flags, resolved combine dirs + `comprehensive_metrics` hashes, pinned input file hashes, etc.

3. **`docs/PROVENANCE_PLAN.md`**
   - Updated to describe `PROVENANCE.json` and distinguish from a future user manifest.
   - Deferred note on raw SQLite file hash canonicalization.

4. **Docs / README**
   - Small wording updates; README still contains the **Mermaid** diagram above.

---

## 4. Git / remotes (verify locally)

- **`origin`:** public `mental-health-finetune-analysis`
- **`backup`:** private `PRIVATE-mental-health-finetune-analysis` (user uses this for safe snapshots)
- Recent work was pushed to **`backup`**. **`origin`** may be behind until a public push is requested.

Untracked (as of last check): `Safety_LLM_Review/`, `utilities/query_guard_cache_outputs.py` — not part of the paper pipeline commits unless added later.

---

## 5. Known issues / intentional debt

| Topic | Status |
|-------|--------|
| **Global `all_models_all_tasks.csv`** | Single writable path; easy staleness vs per-run truth. **Improvement:** emit combined CSV **inside** each `FINETUNE_PAPER_FIGURES/<run>/` and thread path into regression/figures (or manifest-driven paths). |
| **User-authored manifest** | Not implemented; only machine `PROVENANCE.json`. |
| **Output hashes in PROVENANCE** | Generated figure/table file hashes **not** yet in JSON (noted in plan). |
| **Shell script** | `bash_scripts/run_all_models.sh` unchanged; thin wrapper over preflight + `run_experiments.sh`. |

---

## 6. Commands to sanity-check

```bash
cd /path/to/repo
source .venv/bin/activate   # or .venv/bin/python explicitly

# Paper pipeline dry-run (no writes to experiments; still writes run dir + PROVENANCE unless --no-provenance)
python run_paper_pipeline.py --dry-run

# Combine only (defaults or explicit dirs)
python analysis/combine_results.py --help
```

---

## 7. Strict data rules (repo policy)

See **`AGENTS.md`** and **`utilities/cache_qc_report.py`**: canonical joins use **`(model_family, model_size, normalized model_version)`**; no silent alternate matching; fail loud on mismatch.

---

*End of handoff. Update this file when the combined-CSV / per-run artifact story changes.*
