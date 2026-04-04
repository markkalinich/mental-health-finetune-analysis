# Pipeline Dependency Audit

<!-- doc-verbosity: public-ready -->

Which files are required to reproduce **all analyses** (pipeline, revision
experiments, and supporting tools referenced in the README)?

**Methodology:** Trace every `import`, `subprocess.run`, and `source`/call
from `run_paper_pipeline.py` and each standalone revision script recursively.

---

## Part A — Files required by `run_paper_pipeline.py`

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
| `analysis/revision/compute_p2_agreement.py` | Revision: P2 agreement (in manuscript) |

### Shared modules (transitive imports of the above scripts)

| File | Used by |
|------|---------|
| `analysis/comparative_analysis/__init__.py` | Package init |
| `analysis/comparative_analysis/facet_plot_base.py` | gemma/llama/qwen facet plots |
| `analysis/comparative_analysis/facet_plot_utils.py` | facet_plot_base, compact_unified, family plots |
| `analysis/revision/__init__.py` | Package init |
| `analysis/revision/therapy_engagement_conversations.py` | Imported by `compute_p2_agreement.py` |

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
| `data/inputs/intermediate_files/*_psychiatrist_01_and_02_scores.csv` | `compute_p2_agreement.py` |
| `data/prompts/system_suicide_detection_v2.txt` | Phase 1 SI |
| `data/prompts/therapy_request_classifier_v3.txt` | Phase 1 TR |
| `data/prompts/therapy_engagement_conversation_prompt_v2.txt` | Phase 1 TE |
| `cache/results.db` | SQLite cache (Phase 1) |
| `results/revision_experiments/fine_tune_subset_analysis/revised_table_s2.csv` | Copied to output |

### Support

| File | Role |
|------|------|
| `requirements.txt` | Python dependencies |

---

## Part B — Standalone revision scripts (not in pipeline, needed for reviewer response)

These scripts produce results cited in the reviewer response letter.
They are run independently and their outputs live in
`results/revision_experiments/`.

| File | Output | Description |
|------|--------|-------------|
| `analysis/revision/rank_finetune_performance.py` | `top_bottom_20pct_summary.csv`, ranked model CSVs | Top/bottom 20% ΔF1 analysis |
| `analysis/revision/posthoc_merge_and_kappa.py` | `posthoc_kappa_merged.csv` | Post-hoc full-sample Cohen's κ |
| `analysis/revision/compute_kappa_sensitivity.py` | `kappa_sensitivity_binary_keep_remove.csv` | Kappa sensitivity analysis |
| `analysis/revision/compute_kappa_verbatim_bounds.py` | `kappa_verbatim_*.csv` | Kappa verbatim bounds |

---

## Part C — Standalone tools (referenced in README)

| File | Description |
|------|-------------|
| `utilities/build_manuscript_cache_subset.py` | Builds frozen manuscript cache for reproducibility |
| `utilities/cache_qc_report.py` | Cache QC report |
| `cache/cache_manager.py` | Cache statistics CLI (`python -m cache.cache_manager stats`) |
| `data_preparation/create_si_intermediate_and_final_files.py` | SI ground-truth provenance |
| `data_preparation/create_therapy_engagement_intermediate_and_final_files.py` | TE ground-truth provenance |
| `data_preparation/create_therapy_request_intermediate_and_final_files.py` | TR ground-truth provenance |

---

## Dead code — safe to remove

| File | Reason |
|------|--------|
| `analysis/finetune_comparison.py` | Superseded standalone |
| `analysis/mental_health_delta_plot.py` | Superseded standalone |
| `analysis/mental_health_finetune_comparison.py` | Superseded standalone |
| `analysis/comparative_analysis/all_families_f1_facet_plot.py` | Ad-hoc; superseded by compact_unified |
| `analysis/comparative_analysis/model_family_facet_plot.py` | Superseded by family-specific plots |
| `analysis/model_performance/generate_correctness_matrices.py` | Standalone tool, unused |
| `analysis/model_performance/generate_model_statement_matrices.py` | Standalone tool, unused |
| `analysis/statistics/create_custom_tables.py` | Alternative formatter, unused |
| `analysis/statistics/create_simple_tables.py` | Alternative formatter, unused |
| `analysis/statistics/create_stargazer_tables.py` | Alternative formatter, unused |
| `analysis/statistics/format_regression_tables.py` | Alternative formatter, unused |
| `analysis/revision/figure2_correction_overlay.py` | One-off correction script |
| `analysis/revision/figure3_correction_panel.py` | One-off correction script |
| `analysis/revision/regression_correction_diff.py` | One-off correction diff |
| `orchestration/experiment_orchestrator.py` | Dead code; nothing imports it |
| `utilities/enrich_models_config.py` | One-off enrichment, unused |
| `utilities/figure_provenance.py` | Unused tracker |
| `utilities/query_guard_cache_outputs.py` | One-off debug tool |
| `bash_scripts/model_registry_linux.sh` | Legacy (pre-CSV config) |
| `bash_scripts/model_registry_mac.sh` | Legacy (pre-CSV config) |
| `bash_scripts/run_therapy_request_after_engagement.sh` | One-off sequencing helper |

### Data directories not read by any analysis

| Directory | Description |
|-----------|-------------|
| `data/inputs/manifests/` | Selection manifests for data prep |
| `data/inputs/manual_review/` | Raw psychiatrist review CSVs |
| `data/inputs/raw_model_results/` | Pre-finalized model results |
| `data/prompts/gemini_prompts/` | Gemini-specific prompts (unused) |
