# reviewer_2_experiments

Peer-review response experiments — layout mirrors the repo root (`data/`, `results/`, `cache/`, `scripts/`).

**Claims and evidence (reviewer-facing):** [`REVIEWER_2_EXPERIMENTS.md`](REVIEWER_2_EXPERIMENTS.md)

## Layout

```
reviewer_2_experiments/
  REVIEWER_2_EXPERIMENTS.md   claims → evidence → reproduce
  scripts/        Active runners + r2_paths.py (canonical paths)
  bash_scripts/   launch scripts + run_provenance_verify_jobs.sh
  data/
    provenance/   SHA256 audit, overrides, embedded templates
    templates/    Patched Jinja + llama_guard template files
    break_tests/  ShieldGemma / Llama Guard break-test JSON
    template_backups/  Golden LM Studio override snapshots
  results/
    parse50pct_per_task/   Table S2 + Figure S11/S12 (parse≥50% per-task sensitivity)
    shieldgemma/           SG-1 / SG-2 analysis JSON + figures
  cache/          Isolated inference DBs (SG patched runs, 9b diagnostics)
  zArchive/       Superseded pilots, operator docs, old scripts (PRIVATE-ONLY — never sync to public repo)
```

Under `parse50pct_per_task/`:
- `table_1/` — paste-ready CSV + TSV only; internals in `table_1/supplemental_tables/`
- `figure_2/` — F1 vs params overall trend PNG + stats CSV
- `figure_3/` — ΔF1 facet PNG + stats CSV; pair data in `figure_3/supplemental/`

## Active scripts

| Script | Role |
|--------|------|
| **`audit_all_claims.py`** | **One-shot verify Claims 1–6** (+ live override + template compare) |
| `run_parse_filtered_outputs.py` | **Merged** filter + Table S2 + Fig S11 + Fig S12 |
| `filter_models_config_by_parse.py` | Build parse-filtered cohort CSV/JSON |
| `run_gguf_sha256_audit.py` | 127-model GGUF SHA256 vs HF |
| `run_lmstudio_jinja_override_scan.py` | 127-model LM Studio Jinja override scan |
| `run_q8_orphan_template_compare.py` | Q8-orphan HF template compare (3 models) |
| `run_chat_template_audit.py` | 9 safety-model embedded template audit |
| `run_embedded_template_break_test.py` | ShieldGemma embedded break (**4 models**: 2b/9b/27b/2-4b-it) |
| `run_llama_guard_1b_break_test.py` | Llama Guard 1B break |
| `run_shieldgemma_sg1_patched_sensitivity.py` | SG-1 patched inference (2b/9b/27b) |
| `run_shieldgemma_24b_sg2_sensitivity.py` | SG-2 patched inference (2-4b-it) |
| `analyze_sg1_patched_smoke_test.py` | SG-1 generic vs patched analysis |
| `analyze_shieldgemma_24b_sg2.py` | SG-2 generic vs patched analysis |
| `plot_sg1_template_delta_grid.py` | Figure R1 + supporting plots |
| `lm_studio_load_crosswalk.py` | CSV `lm_studio_id` → LM Studio load key |
| `lmstudio_runtime_utils.py` | Shared load/unload/model-verify for break tests |
| `audit_all_claims.sh` | Shell wrapper for `audit_all_claims.py` |
| `run_provenance_verify_jobs.sh` | Detached verify (override + template compare) |

**Archived** (see `zArchive/scripts_superseded/`): separate `run_table1/figure2/figure3_parse_filtered.py`, `run_subtask2_rendered_prompts.py`, `run_shieldgemma_2b_9b_rerun.py`, SG-1-on-2-4b-it patched runner/analysis.

## Quick reproduce

**Prerequisites:** `.venv` and, for Claim 5 only, `cache/results.db` (see [`REVIEWER_2_EXPERIMENTS.md`](REVIEWER_2_EXPERIMENTS.md#prerequisites-reviewer-machine)).

```bash
# Verify all reviewer claims (start here)
reviewer_2_experiments/bash_scripts/audit_all_claims.sh --skip-live

# Parse≥50% per-task sensitivity (Table S2, Fig S11, S12)
.venv/bin/python reviewer_2_experiments/scripts/run_parse_filtered_outputs.py --target all

# SG-1 analysis + Figure R1
.venv/bin/python reviewer_2_experiments/scripts/analyze_sg1_patched_smoke_test.py --full --task all
MPLBACKEND=Agg .venv/bin/python reviewer_2_experiments/scripts/plot_sg1_template_delta_grid.py
```

Paths are centralized in `scripts/r2_paths.py` — update there when moving outputs.

## Gitignore

This folder has its own [`.gitignore`](.gitignore) (HF download blobs, `__pycache__`). Repo-wide rules live at the **repository root** [`/.gitignore`](../.gitignore).
