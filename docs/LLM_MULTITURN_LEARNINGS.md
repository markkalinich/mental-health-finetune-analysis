# Learnings from `llm_multiturn_benchmarking` (narrow scope)

**Scope:** [Provenance](#provenance), [configuration](#configuration), and [documentation](#documentation) only. **Out of scope for this revision:** per-turn telemetry, token quality metrics, and similar—useful for future re-runs, not required to copy before the current manuscript revision.

Repository: `llm_multiturn_benchmarking` (local clone; publish URL when the repo is public).

---

## Provenance

- **`get_git_info()`** in `src/utils.py` records **`git_commit`** (`git rev-parse HEAD`) and **`git_dirty`** (`git status --porcelain` non-empty). If dirty, the recorded commit is **not** a guarantee that code matches the tree.
- Run JSON / classification outputs embed **`meta.git_commit`** / **`meta.git_dirty`** so downstream analysis knows what code produced the run.
- **Actionable for this repo:** Add the same helper (or reuse logic) and include fields in [`PROVENANCE_PLAN.md`](PROVENANCE_PLAN.md) manifest JSON (`git.commit`, `git.dirty`). No need to mirror their full JSON run format unless we redesign the pipeline.

---

## Configuration

- **Strict YAML validation** (`src/experiment_config.py`): unknown keys in experiment YAML are **rejected** with an error listing bad keys—reduces silent misconfiguration (typos, wrong nesting).
- **Documented schema** (`config/experiments/YAML_SCHEMA.md`): required keys, two layout styles (flat vs sectioned), examples.
- **Actionable for this repo:** If we introduce YAML or expand `models_config`, consider “reject unknown columns/keys” and a single schema doc. Lower priority if we stay CSV-only for this revision.

---

## Documentation

- README includes a **“Reproducibility (what is stored)”** table mapping artifact types to what is pinned (prompts, model IDs, runtime metadata).
- **Actionable for this repo:** Extend README / [`PROVENANCE_PLAN.md`](PROVENANCE_PLAN.md) with a similar table once the frozen cache + manifest exist (what is committed vs generated vs symlinked).

---

## Explicitly deferred

- Per-turn `turn_metadata`, cumulative Jaccard, duplicate detection, `quality_summary`, etc.—valuable for experiments; **not** proposed for this revision unless we re-run inference.
