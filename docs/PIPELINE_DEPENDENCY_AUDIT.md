# Pipeline Dependency Audit

<!-- doc-verbosity: public-ready -->

Which files does `run_paper_pipeline.py` actually need?  This audit traces
every direct and transitive dependency so we can identify extraneous code
before the public release.

**Methodology:** Follow every `import`, `subprocess.run`, and `source`/call
from `run_paper_pipeline.py` recursively.  Data files consumed at runtime are
listed separately.

---

## Files REQUIRED by `run_paper_pipeline.py`

### Entry point

| File | Role |
|------|------|
| `run_paper_pipeline.py` | Main pipeline orchestrator |

### Direct Python imports (loaded in the pipeline process)

| File | Imported symbol |
|------|-----------------|
| `analysis/__init__.py` | Package init |
| `analysis/combine_results.py` | `get_latest_experiment_dir` |
| `utilities/__init__.py` | Package init |
| `utilities/paper_run_provenance.py` | `write_paper_run_provenance` |

### Transitive imports (loaded by the above)

| File | Import chain |
|------|--------------|
| `config/__init__.py` | `paper_run_provenance` → `config.utils` |
| `config/experiment_config.py` | `config/__init__` |
| `config/constants.py` | `config/__init__`, `metrics_calculator`, `data_processor` |
| `config/utils.py` | `config/__init__`, `paper_run_provenance` |
| `config/models_registry.py` | `config/__init__` |
| `analysis/model_performance/metrics_calculator.py` | `analysis/__init__` re-exports |
| `utilities/types_definitions.py` | `metrics_calculator` |

### Figure and table scripts (called via `subprocess`)

| File | Pipeline phase |
|------|----------------|
| `analysis/model_coverage_heatmap.py` | Figure 1 |
| `analysis/comparative_analysis/compact_unified_facet_plot.py` | Figure 2 |
| `analysis/combined_finetune_facet_plot.py` | Figure 3 (F1) + revision delta-parse facet |
| `analysis/statistics/regression_analysis.py` | Table 1 step 1 |
| `analysis/statistics/create_regression_tables.py` | Table 1 step 2 |
| `analysis/statistics/create_combined_tables.py` | Table 1 step 3 |
| `analysis/comparative_analysis/gemma_version_facet_plot.py` | Supplementary |
| `analysis/comparative_analysis/llama_version_facet_plot.py` | Supplementary |
| `analysis/comparative_analysis/qwen_version_facet_plot.py` | Supplementary |
| `analysis/revision/delta_parse_vs_delta_f1_scatter.py` | Revision Figure S10 |

### Shared modules (transitive imports of the above scripts)

| File | Used by |
|------|---------|
| `analysis/comparative_analysis/__init__.py` | Package init |
| `analysis/comparative_analysis/facet_plot_base.py` | gemma/llama/qwen facet plots |
| `analysis/comparative_analysis/facet_plot_utils.py` | facet_plot_base, compact_unified, family plots |
| `analysis/revision/__init__.py` | Package init |

### Phase 1 — experiment execution (via bash)

| File | Called by |
|------|-----------|
| `bash_scripts/run_all_models.sh` | `run_paper_pipeline.py` (subprocess) |
| `bash_scripts/preflight.sh` | Sourced by `run_all_models.sh` |
| `bash_scripts/run_experiments.sh` | Sourced by `run_all_models.sh` |

### Phase 1 — Python modules invoked from bash (`python -m`)

| File | Called by |
|------|-----------|
| `utilities/lms_manager.py` | `preflight.sh`, `run_experiments.sh` |
| `utilities/batch_cache_checker.py` | `preflight.sh` |
| `utilities/cache_checker.py` | `run_experiments.sh` |
| `orchestration/run_experiment.py` | `run_experiments.sh` |
| `analysis/model_performance/batch_results_analyzer.py` | `run_experiments.sh` |

### Phase 1 — transitive Python imports

| File | Imported by |
|------|-------------|
| `utilities/model_validator.py` | `lms_manager` |
| `utilities/schemas.py` | `run_experiment` |
| `utilities/category_validator.py` | `run_experiment`, `data_loader` |
| `utilities/file_manager.py` | `batch_results_analyzer` |
| `orchestration/api_client.py` | `run_experiment` |
| `orchestration/data_processor.py` | `run_experiment`, `cache_checker`, `batch_cache_checker` |
| `orchestration/experiment_manager.py` | `run_experiment`, `cache_checker`, `batch_cache_checker`, `result_cache` |
| `cache/result_cache.py` | `run_experiment`, `cache_checker`, `batch_cache_checker`, `data_loader` |
| `analysis/model_performance/visualization.py` | `batch_results_analyzer` |
| `analysis/model_performance/confusion_matrices.py` | `batch_results_analyzer` |
| `analysis/model_performance/data_loader.py` | `batch_results_analyzer` |
| `analysis/model_performance/single_experiment_report_generator.py` | `batch_results_analyzer` |

### Data files consumed at runtime

| File | Used by |
|------|---------|
| `config/models_config.csv` | model_coverage_heatmap, facet plots, regression, provenance |
| `data/inputs/model_results/all_models_all_tasks.csv` | Figure 2, Figure 3, regression, scatter |
| `data/inputs/finalized_input_data/SI_finalized_sentences.csv` | Phase 1 SI |
| `data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv` | Phase 1 TR |
| `data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv` | Phase 1 TE |
| `data/prompts/system_suicide_detection_v2.txt` | Phase 1 SI |
| `data/prompts/therapy_request_classifier_v3.txt` | Phase 1 TR |
| `data/prompts/therapy_engagement_conversation_prompt_v2.txt` | Phase 1 TE |
| `cache/results.db` | SQLite cache (Phase 1) |

### Support

| File | Role |
|------|------|
| `requirements.txt` | Python dependencies |

**Total: 46 code files + 9 data files + 1 support file.**

---

## Files NOT required by the pipeline

### analysis/ — standalone or superseded scripts

| File | Description |
|------|-------------|
| `analysis/finetune_comparison.py` | Older standalone finetune comparison |
| `analysis/mental_health_delta_plot.py` | Standalone delta plot |
| `analysis/mental_health_finetune_comparison.py` | Standalone MH comparison |
| `analysis/comparative_analysis/all_families_f1_facet_plot.py` | Ad-hoc combined family plot |
| `analysis/comparative_analysis/model_family_facet_plot.py` | Per-family facet (superseded) |
| `analysis/model_performance/generate_correctness_matrices.py` | Standalone correctness matrix tool |
| `analysis/model_performance/generate_model_statement_matrices.py` | Standalone statement matrix tool |

### analysis/revision/ — revision-era scripts not yet wired into pipeline

These are needed for the manuscript revision but are not currently called by
`run_paper_pipeline.py`.  They should be integrated before the revision is
finalized.

| File | Description |
|------|-------------|
| `analysis/revision/compute_kappa_sensitivity.py` | Kappa sensitivity analysis |
| `analysis/revision/compute_kappa_verbatim_bounds.py` | Kappa verbatim bounds |
| `analysis/revision/compute_p2_agreement.py` | Psychiatrist 2 agreement |
| `analysis/revision/posthoc_merge_and_kappa.py` | Post-hoc merge and kappa |
| `analysis/revision/therapy_engagement_conversations.py` | TE conversation analysis |
| `analysis/revision/figure2_correction_overlay.py` | Correction overlay for Figure 2 (untracked) |
| `analysis/revision/figure3_correction_panel.py` | Correction panel for Figure 3 (untracked) |
| `analysis/revision/regression_correction_diff.py` | Regression correction diff (untracked) |

### analysis/statistics/ — alternative table formatters

| File | Description |
|------|-------------|
| `analysis/statistics/create_custom_tables.py` | Custom table formatter |
| `analysis/statistics/create_simple_tables.py` | Simple table formatter |
| `analysis/statistics/create_stargazer_tables.py` | Stargazer-style tables |
| `analysis/statistics/format_regression_tables.py` | Alternative regression formatter |

### bash_scripts/ — legacy or one-off

| File | Description |
|------|-------------|
| `bash_scripts/model_registry_linux.sh` | Legacy model registry (pre-CSV config) |
| `bash_scripts/model_registry_mac.sh` | Legacy model registry (pre-CSV config) |
| `bash_scripts/run_therapy_request_after_engagement.sh` | One-off sequencing helper |

### utilities/ — standalone tools

| File | Description | Keep for README? |
|------|-------------|------------------|
| `utilities/build_manuscript_cache_subset.py` | Builds frozen manuscript cache | Yes (referenced in README "Reproducibility") |
| `utilities/cache_qc_report.py` | Cache QC report | Yes (referenced in README and AGENTS.md) |
| `utilities/enrich_models_config.py` | Enriches models_config.csv metadata | No |
| `utilities/figure_provenance.py` | Figure-level provenance tracker | No |
| `utilities/query_guard_cache_outputs.py` | Queries guard model cache outputs | No |

### cache/ — standalone CLI

| File | Description |
|------|-------------|
| `cache/cache_manager.py` | Standalone cache management (`python -m cache.cache_manager stats`) |

### orchestration/ — unused orchestrator

| File | Description |
|------|-------------|
| `orchestration/experiment_orchestrator.py` | Higher-level orchestrator (pipeline uses bash instead) |

### data_preparation/ — one-time data prep (3 scripts)

| File | Description |
|------|-------------|
| `data_preparation/create_si_intermediate_and_final_files.py` | SI data prep |
| `data_preparation/create_therapy_engagement_intermediate_and_final_files.py` | TE data prep |
| `data_preparation/create_therapy_request_intermediate_and_final_files.py` | TR data prep |

### data/ — directories not read by the pipeline

| Directory | Description |
|-----------|-------------|
| `data/inputs/intermediate_files/` | Intermediate psychiatrist scoring files |
| `data/inputs/manifests/` | Selection manifests for data prep |
| `data/inputs/manual_review/` | Raw psychiatrist review CSVs |
| `data/inputs/raw_model_results/` | Pre-finalized model results |
| `data/prompts/gemini_prompts/` | Gemini-specific prompts (unused) |
| `data/revision_data/` | Revision data (P2 reviews, merged files, correction notes) |

**Total NOT required: ~28 code files + ~6 data directories.**

---

## Recommendations

1. **Remove immediately (dead code):** `analysis/finetune_comparison.py`,
   `analysis/mental_health_delta_plot.py`,
   `analysis/mental_health_finetune_comparison.py`,
   `analysis/comparative_analysis/all_families_f1_facet_plot.py`,
   `analysis/comparative_analysis/model_family_facet_plot.py`,
   `analysis/model_performance/generate_correctness_matrices.py`,
   `analysis/model_performance/generate_model_statement_matrices.py`,
   `orchestration/experiment_orchestrator.py`,
   all 4 alternative table formatters in `analysis/statistics/`,
   legacy bash registries, one-off bash helpers.

2. **Integrate into pipeline before revision finalization:**
   `analysis/revision/` scripts (kappa, P2 agreement, corrections).

3. **Keep but do not wire into pipeline:**
   `utilities/build_manuscript_cache_subset.py`,
   `utilities/cache_qc_report.py`,
   `cache/cache_manager.py` (referenced in README),
   `data_preparation/` (provenance for ground-truth creation).
