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

## What this proves vs what it does not

- **Proves:** Every **expected** `cache_id` for the current model grid and inputs is **present** in the source DB at build time (`missing_in_source` should be `0` in `subset_report.json`). The subset is a **lossless copy** of those rows for offline use.
- **Does not by itself prove** byte-identity with the **original journal submission** if any of the following differ from submission time: `models_config.csv`, finalized CSVs, prompt files, or API defaults (`temperature`, `max_tokens`, `top_p`). For submission-time parity, pin the **git commit** that defined those files and/or keep a **contemporaneous** `results.db` snapshot.

Stronger checks (optional): regenerate `comprehensive_metrics` from this subset and compare to the pinned `all_models_all_tasks.csv` (MD5 `c7ec47b943cd03dd50093b8a01c7cfb0` for the 20251230 paper bundle on disk — see `results/revision_experiments/GUARD_FIX_SESSION_SUMMARY.md`).

## Size / Git

The database is large (~hundreds of MB). By default **`results.db` is listed in `.gitignore`** so pushes stay small; **`SHA256SUMS.txt`**, **`subset_report.json`**, and this README **are** meant to be committed so anyone can verify a locally built or archived copy of `results.db`.

To track the binary in git, use **[Git LFS](https://git-lfs.github.com/)** and `git add -f manuscript_paper_cache/results.db`, or keep the file only on your machine / backup remote alongside the committed checksum.
