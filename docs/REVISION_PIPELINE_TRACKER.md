# Revision results to integrate into `run_paper_pipeline.py`

<!-- doc-verbosity: public-ready -->

Track which revision experiment outputs should be copied into the pipeline's
timestamped output directory (`results/FINETUNE_PAPER_FIGURES/<run>/`).
Only results **cited in the manuscript** belong here.

## Status key

- **Done** — already produced and copied by the pipeline.
- **TODO** — needs to be wired into the pipeline before public release.

## Results

| Result | Manuscript location | Source script | Source CSV | Status |
|--------|-------------------|---------------|------------|--------|
| Δ parse facet plot | Supplementary figure | `analysis/combined_finetune_facet_plot.py --metric parse` | `results/revision_experiments/delta_parse_facet_plot_*.png` | **Done** (Phase 5) |
| Δ parse vs Δ F1 scatter (Figure S10) | Supplementary figure | `analysis/revision/delta_parse_vs_delta_f1_scatter.py` | `results/revision_experiments/delta_parse_vs_delta_f1_scatter.png` | **Done** (Phase 5) |
| P2 agreement proportions (Wilson CIs) | Methods p10, Results p4 | `analysis/revision/compute_p2_agreement.py` | `results/revision_experiments/interrater_reliability/p2_agreement_given_p1_exact_match.csv` | **TODO** |
| Revised Table S2 (fine-tune metadata) | Supplementary Table S2 | none (manual + LLM-assisted extraction) | `results/revision_experiments/fine_tune_subset_analysis/revised_table_s2.csv` | **TODO** |

## Not included in pipeline (available in repo for reproducibility)

| Result | Reason excluded |
|--------|----------------|
| Post-hoc Cohen's κ (`posthoc_kappa_merged.csv`) | Not reported in manuscript; interpretability limited by non-blinded design |
| κ sensitivity analyses (`kappa_verbatim_*.csv`, `kappa_sensitivity_*.csv`) | Exploratory; not in manuscript |
| Top/bottom 20% ranked models (`zArchive/mental_health_ranked_models.csv`, `medical_ranked_models.csv`) | Reviewer response only; not in manuscript text (generated interactively, no script) |
| Paired FT missingness summary (`paired_FT_missingness_summary.csv`) | Reviewer response only (Table R1); not in manuscript |
| Supplemental fine-tune data (`fine_tune_subset_analysis/supplemental_data/`) | Working files for Table S2 enrichment; not directly cited |
