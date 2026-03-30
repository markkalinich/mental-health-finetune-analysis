# Manuscript paper cache (subset SQLite)

<!-- doc-verbosity: verbose-troubleshooting -->

> **Doc verbosity:** `verbose-troubleshooting` — trim before public push (see [`docs/DOCUMENTATION_FLAGS.md`](../docs/DOCUMENTATION_FLAGS.md)).

This folder holds a **frozen subset** of the project’s inference cache (`results.db`), containing **only** the cache rows implied by:

- `config/models_config.csv` (**enabled** models only), and  
- the three finalized task datasets and prompts (`SI`, `TR`, `TE`) as wired in `utilities/build_manuscript_cache_subset.py`.

## Files

| File | Purpose |
|------|---------|
| `results.db` | SQLite subset (same schema as `cache/results.db`) |
| `SHA256SUMS.txt` | `sha256sum` of `results.db` — verify with `sha256sum -c SHA256SUMS.txt` |
| `subset_report.json` | Machine-readable report from the last build (git HEAD, source path, counts, missing keys) |
| `qc_report_latest.md` | Optional: Markdown output from `cache_qc_report.py --output` (create locally; not required in git) |
| `qc_parse_fail_matrix.csv`, `qc_api_error_matrix.csv` | Optional: model × task (SI/TR/TE) counts plus a **total** column; rows **sorted by total descending** (same folder as `--output`) |
| `model_cache_crosswalk_approved.csv` | **Human-approved** `model_full_name` → `lm_studio_id` rows only (see QC section). Default path next to `--db`; header-only until you add approved lines. |

## Build / refresh

From the repository root, with the project venv that has `pandas` (see `docs/DEVELOPMENT.md`):

```bash
python utilities/build_manuscript_cache_subset.py --quiet \
  --source cache/results.db \
  --output manuscript_paper_cache/results.db \
  --report manuscript_paper_cache/subset_report.json
cd manuscript_paper_cache && sha256sum results.db > SHA256SUMS.txt
```

`--source` should point at your live cache (a symlink to `safety_simulations/cache/results.db` is fine).

## QC report (`utilities/cache_qc_report.py`)

Resolution order (same triple as `experiment_manager` / `MODEL_NAME_MAP`: **`(model_family, model_size, normalized model_version)`** → enabled `lm_studio_id` in `config/models_config.csv`):

1. **Triple mapping** — For each distinct `cache_keys.model_full_name`, look up the registry id from the triple derived from the cache row.
2. **Report (§1)** — The Markdown report lists models **resolved directly by triple**, **label drift** (triple points to an id that differs from `model_full_name`), **missing triple** (no registry row for that triple), and what was **fixed only via** the approved CSV.
3. **Approved crosswalk CSV** — **`--crosswalk-csv`** (default: **`<parent of --db>/model_cache_crosswalk_approved.csv`**) must contain **only** rows you explicitly approve: columns **`model_full_name`**, **`lm_studio_id`**. Every `lm_studio_id` must be an **enabled** id in `models_config.csv`. Drift cases require a row whose `lm_studio_id` matches the triple’s canonical id; missing-triple cases require a row that supplies the intended id.
4. **Exit** — If any cache model **still** cannot be resolved after triple + approved CSV, the script **prints the unresolved list to stderr and exits with code 1** (no full report). If everything resolves, the full report (including §1) is written.

**Output:** terminal **stdout**; with **`--output`**, Markdown is written to that path (UTF-8). With `--output` (or **`--tables-dir`**), the script also writes **`qc_parse_fail_matrix.csv`** and **`qc_api_error_matrix.csv`**. Override the models grid with **`--models-config`** if needed.

**Example (save under this folder):**

```bash
python utilities/cache_qc_report.py \
  --db manuscript_paper_cache/results.db \
  --output manuscript_paper_cache/qc_report_latest.md
```

Runtime on this machine’s subset DB is on the order of **one second** (SQL aggregates only).

**Report outline (Markdown sections):**

| § | Contents |
|---|----------|
| **0** | Row counts (`cache_keys` vs `cached_results`), enabled model count from registry. |
| **1** | Cache model → registry resolution (triple, drift, approved CSV, status). |
| **2** | One row per distinct **`prompt_hash`** (all tasks): prompt label(s), `cache_keys` count, % qwen by resolved family. |
| **3** | **Per task check:** one row per **`(SI \| TR \| TE, prompt_hash)`** — applicable enabled qwen vs non-qwen count, distinct `input_hash`, `cache_keys`, expected product, **OK**, `cached_results`. |
| **4–6** | Hyperparameters (`temperature`, `max_tokens`, `top_p`), `created_at` by day, `cached_results` status / parse / API error breakdown. |

## What this proves vs what it does not

- **Proves:** Every **expected** `cache_id` for the current model grid and inputs is **present** in the source DB at build time (`missing_in_source` should be `0` in `subset_report.json`). The subset is a **lossless copy** of those rows for offline use.
- **Does not by itself prove** byte-identity with the **original journal submission** if any of the following differ from submission time: `models_config.csv`, finalized CSVs, prompt files, or API defaults (`temperature`, `max_tokens`, `top_p`). For submission-time parity, pin the **git commit** that defined those files and/or keep a **contemporaneous** `results.db` snapshot.

Stronger checks (optional): regenerate `comprehensive_metrics` from this subset and compare to the pinned `all_models_all_tasks.csv` (MD5 `c7ec47b943cd03dd50093b8a01c7cfb0` for the 20251230 paper bundle on disk — see `results/revision_experiments/GUARD_FIX_SESSION_SUMMARY.md`).

## Size / Git

The database is large (~hundreds of MB). By default **`results.db` is listed in `.gitignore`** so pushes stay small; **`SHA256SUMS.txt`**, **`subset_report.json`**, and this README **are** meant to be committed so anyone can verify a locally built or archived copy of `results.db`.

To track the binary in git, use **[Git LFS](https://git-lfs.github.com/)** and `git add -f manuscript_paper_cache/results.db`, or keep the file only on your machine / backup remote alongside the committed checksum.
