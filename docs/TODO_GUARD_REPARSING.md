# TODO: Guard / safety model re-parsing

## Status

**Not blocking** manifest / cache pinning work in the short term, but **must** be revisited before any final revision text that depends on guard-model F1 or parse rates.

## Why this exists

LLaMA Guard and Qwen Guard (and similar) often emit `safe` / `unsafe` (or other) text that does not match the **standard JSON** parser used for other models. Task-aware re-parsing from **`cache/results.db`** was added in analysis code (`analysis/comparative_analysis/facet_plot_utils.py` and callers). This path is easy to get wrong (e.g. task mix-ups) and requires **manual review** of logic, tests, and manuscript numbers.

## Before closing the science

- [ ] Confirm every analysis entrypoint applies the same rule set per task.
- [ ] Add tests or golden outputs for a small set of cached rows per guard model × task.
- [ ] Document whether manuscript tables use **CSV-only**, **CSV + correction**, or **regenerated-from-cache** metrics.
- [ ] Align with [`PROVENANCE_PLAN.md`](PROVENANCE_PLAN.md) once outputs are stable.

## References

- `results/revision_experiments/GUARD_FIX_SESSION_SUMMARY.md`
- `results/revision_experiments/README_REVISIONS.md` (safety cache path, `SAFETY_CACHE_PATH`)
