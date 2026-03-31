# Changelog — 2026-03-30

## Guard model re-parsing refactor

**Problem:** Guard models (Llama Guard, Qwen Guard) return non-standard output
formats that the generic parser marks as `parse_fail`. A Phase 4 post-hoc
correction existed in `facet_plot_utils.py`, but it was SI-only — it silently
overwrote TR/TE metrics with SI values for guard models.

**Fix:** Moved guard re-parsing upstream into Phase 2 (`data_loader.py`).
The new `_reparse_guard_models` function runs at load time, correctly handling
all three tasks. The old Phase 4 code was deleted.

Files changed:
- `analysis/model_performance/data_loader.py` — added `_reparse_guard_models`,
  `_parse_guard_binary`, `_GUARD_POSITIVE`, `_GUARD_NEGATIVE` constants
- `analysis/comparative_analysis/facet_plot_utils.py` — deleted ~240 lines of
  dead guard metric functions
- `analysis/combined_finetune_facet_plot.py` — removed `apply_safety_corrections`
  parameter and dict keys
- `analysis/finetune_comparison.py` — same removal

## Docstring / validation fixes (from adversarial audit)

- Fixed `suicide_detection` → `suicidal_ideation` in docstrings across
  `data_loader.py`, `metrics_calculator.py`, `confusion_matrices.py`,
  `types_definitions.py`
- Fixed `experiment_orchestrator.py` `valid_types` set to include all three
  experiment types

## Figure S10 recovery

`analysis/revision/delta_parse_vs_delta_f1_scatter.py` was accidentally deleted
in commit `b9e3c88`. Recovered from `bc5a8e1`, removed stale
`apply_safety_corrections` reference.

The `--metric parse` variant of `combined_finetune_facet_plot.py`
(`generate_delta_parse_facet_plot`, `_generate_facet_grid`, CLI) was also lost
in the same commit. Recovered from `bc5a8e1`, same minimal cleanup.

Both added to `run_paper_pipeline.py` as Phase 5 (revision figures).

## Repository cleanup

**Deleted (dead files):**
- `config/Finetune_Info.csv`, `gemma_models_config.csv`, `models_config_full.csv`,
  `model_provenance.md`
- `lm_studio_models_inventory.csv` (repo root)
- `docs/TODO_GUARD_REPARSING.md`, `LLM_MULTITURN_LEARNINGS.md`,
  `REGULATORY_CACHE_PATTERN.md`

**Moved:**
- `Safety_LLM_Review/` → `results/revision_experiments/Safety_LLM_Review/`
- `data/revision_data/results/*` → `results/revision_experiments/`

**Path updates:** Output paths in `posthoc_merge_and_kappa.py`,
`compute_p2_agreement.py`, `compute_kappa_verbatim_bounds.py`,
`compute_kappa_sensitivity.py` updated to point to
`results/revision_experiments/`.

## README rewrite

Rewrote for clarity from a new-data-scientist perspective. Removed
Cursor-specific rendering notes, internal roadmap, and developer housekeeping.
Updated guard re-parsing location reference. Added key finding summary.

## What still needs to happen

- Re-run full pipeline (`run_paper_pipeline.py`) to regenerate CSVs with
  correct guard model metrics (on-disk CSVs are currently stale — all zeros
  for guard models)
- Inter-rater reliability scripts not yet integrated into pipeline
- Fine-tune subset analysis script is missing from repo (outputs exist as
  static CSVs in `results/revision_experiments/fine_tune_subset_analysis/`)
