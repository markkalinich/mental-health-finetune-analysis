# Plan: end-to-end provenance (“this commit + this cache + these files → these plots”)

## Goal

Unambiguous statements of the form:

> We used **git commit** `abc1234` of this repository, **SQLite cache** at path `…` with SHA-256 `…`, **pinned inputs** (hashes below), and **config** `models_config.csv` at hash `…`, then ran `run_paper_pipeline.py` (or a named wrapper) to produce the artifacts in `results/FINETUNE_PAPER_FIGURES/<run_id>/`.

## Design sketch

1. **`PROVENANCE.json` (machine-generated run record)** — Written under `results/FINETUNE_PAPER_FIGURES/<YYYYMMDD_HHMMSS>/` by `run_paper_pipeline.py` (see `utilities/paper_run_provenance.py`). Schema: `paper_run_provenance_v1`. Use `--no-provenance` to skip. This is **not** a user-authored manifest; a separate input manifest (future) would declare intent **before** the run. **Generated figure/table hashes** are not yet listed in JSON; extend the writer when needed.

   Suggested fields:

   | Field | Purpose |
   |-------|---------|
   | `git.commit` | Full SHA from `git rev-parse HEAD` |
   | `git.dirty` | Boolean from `git status --porcelain` (empty or not) |
   | `git.describe` | Optional: tag + distance if you use tags |
   | `cache.path` | Resolved path to `results.db` (follow symlinks; record **target** path) |
   | `cache.sha256` | `sha256sum` of the DB file used at run time |
   | `inputs` | List of `{ "path": "...", "sha256": "..." }` for: each finalized input CSV, each prompt file, `config/models_config.csv`, and **`data/inputs/model_results/all_models_all_tasks.csv`** if the run consumes it |
   | `combine_results` | If applicable: SI/TR/TE experiment directory names or their `comprehensive_metrics.csv` hashes |
   | `environment` | Optional: `python -V`, hostname |
   | `command` | argv as executed |
   | `outputs` | List of output paths or glob + hashes of key deliverables (figures, table CSVs) |

2. **Helper** — `utilities/paper_run_provenance.py`; invoked at the **end** of each run (including failed resolution of experiment dirs).

3. **Pinning policy** — Document whether a “manuscript freeze” uses:
   - a **copied** `results.db` snapshot (recommended for strict reproducibility), or
   - the live cache (hash recorded at run time only).

4. **Regression check (optional)** — CI or a local script that fails if pinned provenance hashes do not match files on disk (for tagged releases only).

## Relationship to other repos

- **`regulatory_simulations`** ships a **frozen subset** SQLite for the paper in [`regulatory_paper_cache_v3`](https://github.com/markkalinich/regulatory_simulations/tree/main/regulatory_paper_cache_v3) (`results.db` + `MD5SUM.txt`), alongside runtime filtering from a larger cache. We should follow that **checked-in frozen DB + checksum** pattern for manuscript freezes; see [`REGULATORY_CACHE_PATTERN.md`](REGULATORY_CACHE_PATTERN.md).

- **This repo:** `utilities/build_manuscript_cache_subset.py` builds `manuscript_paper_cache/results.db` plus `subset_report.json` and `SHA256SUMS.txt` (see [`manuscript_paper_cache/README.md`](../manuscript_paper_cache/README.md)).

## Open items

- Guard / safety re-parsing is **out of scope** for this provenance record until rules are finalized — see [`TODO_GUARD_REPARSING.md`](TODO_GUARD_REPARSING.md).
- Final field list should be minimal but sufficient for a Methods / reproducibility paragraph.

### Deferred: raw SQLite file hash

Recording **`sha256sum` of the `results.db` file bytes** is sufficient when the file is treated as a single artifact and not rebuilt (e.g. `VACUUM`) between snapshot and compare. **Optional later:** if two copies of the DB ever disagree on hash but should be “the same data,” consider hashing a **canonical SQL dump** or running **`VACUUM` + fixed journal mode** before hash — see discussion in workflow review. **No change required** until that situation appears; file-level hashes used today (e.g. `manuscript_paper_cache/SHA256SUMS.txt`) stay as-is.
