# Evaluating the relative impact of model scale, architecture, and fine-tuning on mental health–related safety classification tasks in open-source large language models

Code and analysis pipeline for **[Evaluating the effect of mental health fine-tuning relative to other model characteristics on LLM safety performance](https://www.medrxiv.org/content/10.64898/2026.01.02.25343289v1)** (medRxiv preprint).

## What this project does

Large language models are increasingly deployed in mental health contexts, but it is unclear whether mental health–specific fine-tuning improves safety-relevant classification beyond gains from model scale, architecture generation, or instruction tuning alone. We evaluated **127 open-source models** (Gemma, LLaMA, Qwen; ~270M–70B parameters) on three psychiatrist-reviewed synthetic classification tasks, comparing base models against models fine-tuned for: instruction following; medical literature; mental health tasks; detection of unsafe conversations.  

**Tasks:**
1. **Suicidal ideation detection** — classify statements for presence/absence of  suicidal ideation (450 items, 10 categories)
2. **Therapy request classification** — classify statements for presence/absence of explicit therapy requests (780 items, 12 categories)
3. **Therapy engagement detection** — classify statements for presence/absence of simulated therapy in multi-turn conversations (420 items, 13 categories)

## Data flow

All models are evaluated locally via **LM Studio**. Responses are cached in SQLite so figures can be regenerated without re-running inference. The pipeline has four phases:

```mermaid
flowchart TB
    subgraph P0["Phase 0: Inputs and configuration"]
        data["Synthetic data (SI / TR / TE CSVs)\n(data/inputs/finalized_input_data)"]
        prompts["Task prompts\n(data/prompts/)"]
        cfg["Model list\n(config/models_config.csv)"]
    end

    subgraph P1["Phase 1: Inference (per model × task)"]
        data --> keygen["Compute cache key\n(model, prompt_hash, input_hash, params)"]
        prompts --> keygen
        cfg --> keygen
        keygen --> check{"Present in Cache?"}
        check -->|"No"| lms["Inference\n(LM Studio)"]
        lms --> parse["Parse response\n(extract JSON → validate\nagainst task schema*)"]
        parse --> cache[("SQLite cache\n(cache/results.db)")]
        check -->|"Yes"| cache
    end

    subgraph P2["Phase 2: Analysis (per task)"]
        cache --> guardcheck{"Qwen/LLaMA\nGuard model?"}
        guardcheck -->|"Yes"| reparse["Re-parse native format\n(safe/unsafe → binary)"]
        guardcheck -->|"No"| classify["Binary classification\n(predicted vs ground truth\n→ TP/TN/FP/FN)"]
        reparse --> classify
        data -.-> classify
        classify --> metrics["comprehensive_metrics.csv\n(per-model F1, accuracy,\nsensitivity, specificity)"]
        metrics --> runs["Timestamped run dir\n(results/individual_prediction_\nperformance/&lt;task&gt;/&lt;run_id&gt;/)"]
    end

    subgraph P3["Phase 3: Combine"]
        runs --> combine["combine_results.py"]
        combine --> combined["all_models_all_tasks.csv\n(data/inputs/model_results/)"]
    end

    subgraph P4["Phase 4: Figures and tables"]
        combined --> figs["Figures 1–3,\nsupplementary figures"]
        combined --> tab1["Table 1 regression"]
    end

    style cache fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style check fill:#fff9c4,stroke:#f9a825,stroke-width:2px
    style guardcheck fill:#fff9c4,stroke:#f9a825,stroke-width:2px
```

**\*Schema validation note:** Llama Guard and Qwen Guard have been explicitly tuned to rigidly output plain text (`safe`/`unsafe`) regardless of the task prompt, so they fail the initial JSON validation. At analysis time (Phase 2), their native output is re-parsed from `raw_response` and mapped to each task's binary classification (`unsafe` → positive category). ShieldGemma outputs standard task JSON and passes validation normally. See `analysis/model_performance/data_loader.py`.

## Quick start

### Prerequisites

1. **Python 3.9+** with a virtual environment (always activate `.venv` before running anything)
2. **LM Studio** at `http://localhost:1234` (only needed to re-run experiments; not needed to regenerate figures from cache)

### Installation

```bash
git clone https://github.com/markkalinich/mental-health-finetune-analysis.git
cd mental-health-finetune-analysis

python3.9 -m venv .venv   # or: python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Verify: `which python` should point inside `.venv/`.

### Run the paper pipeline

```bash
# Figures and tables using cached experiment results (typical)
python run_paper_pipeline.py --skip-experiments

# Full path including new experiments (requires LM Studio + models)
python run_paper_pipeline.py
```

**Outputs** (timestamped):

```
results/FINETUNE_PAPER_FIGURES/[YYYYMMDD_HHMMSS]/
├── figure_1/model_coverage_heatmap.png
├── figure_2/*.png
├── figure_3/delta_f1_finetune_facet.png
├── table_1/*.csv, *.html
├── supplementary_figures/*.png
└── data/*.csv
```

Each run also writes a `PROVENANCE.json` recording the git commit, cache hash, input hashes, and CLI flags used.

## Figure and table guide

| Artifact | Description | Primary script(s) |
|----------|-------------|-------------------|
| **Figure 1** | Model coverage heatmap | `analysis/model_coverage_heatmap.py` |
| **Figure 2** | F1 vs parameter count | `analysis/comparative_analysis/compact_unified_facet_plot.py` |
| **Figure 3** | ΔF1 Pre/Post-Fine-Tuning | `analysis/combined_finetune_facet_plot.py` |
| **Table 1** | Multivariable Regression (F1 dependent variable) | `analysis/statistics/regression_analysis.py`, `create_*_tables.py` |
| **Supplementary** | Family × task facet plots (9); ΔF1 vs ΔParse Success (1) | `analysis/comparative_analysis/{gemma,llama,qwen}_version_facet_plot.py` |

## Repository structure

```
.
├── run_paper_pipeline.py                # Orchestrates experiments, figures, and tables
├── analysis/
│   ├── model_performance/               # data_loader.py, metrics_calculator.py, batch_results_analyzer.py
│   ├── comparative_analysis/            # Facet plots (Figures 2, supplementary)
│   ├── statistics/                      # Regression (Table 1)
│   ├── combine_results.py              # Merges per-task metrics → all_models_all_tasks.csv
│   └── combined_finetune_facet_plot.py  # Figure 3
├── config/
│   └── models_config.csv                # Model definitions, family/size/version, base-model mappings
├── orchestration/                       # Experiment runner, API client, data processing
├── cache/                               # result_cache.py; SQLite results.db lives here
├── data/
│   ├── inputs/finalized_input_data/     # Expert-reviewed benchmark CSVs (ground truth)
│   ├── inputs/model_results/            # all_models_all_tasks.csv (combined metrics)
│   └── prompts/                         # Task prompt text files
├── bash_scripts/                        # run_all_models.sh (inference orchestration)
├── utilities/                           # Cache QC, manuscript subset builder, model validator
└── results/                             # Pipeline outputs (timestamped run directories)
```

## Running individual components

```bash
# Figure 1
python analysis/model_coverage_heatmap.py

# Figure 2
python analysis/comparative_analysis/compact_unified_facet_plot.py --output-dir results/figure_2/

# Figure 3
python analysis/combined_finetune_facet_plot.py

# Table 1
python analysis/statistics/regression_analysis.py

# Run experiments for a subset of models
bash bash_scripts/run_all_models.sh --models "gemma:12b-it,llama3.1:8b" \
    data/inputs/finalized_input_data/SI_finalized_sentences.csv \
    data/prompts/system_suicide_detection_v2.txt \
    system_suicide_detection_v2

# Cache statistics
python -m cache.cache_manager stats
```

## Reproducibility

- Each pipeline run writes `PROVENANCE.json` with git commit, cache SHA-256, input hashes, and CLI flags.
- A frozen manuscript cache subset can be built with `utilities/build_manuscript_cache_subset.py`; run `utilities/cache_qc_report.py` against it to verify coverage.
- Reviewer-driven revision analyses (parse success, ΔF1, inter-rater reliability) are in `results/revision_experiments/`.
- Developer notes on venv setup, integrity checks, and git workflow: [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md).

## Citation

If you use this code or data, please cite:

```bibtex
@article{kalinich2026mentalhealthfinetune,
  title={Evaluating the effect of mental health fine-tuning relative to other model characteristics on {LLM} safety performance},
  author={Kalinich, Mark and Luccarelli, James and {Santa Maria, Jr.}, John and Williams, Gwydion and Moss, Frank and Torous, John},
  journal={medRxiv},
  year={2026},
  doi={10.64898/2026.01.02.25343289},
  url={https://www.medrxiv.org/content/10.64898/2026.01.02.25343289v1}
}
```

## Acknowledgments

Claude Sonnet and Opus 4.5-6 via Cursor were used extensively to assist with code generation, refactoring, and documentation. All scientific claims, analysis choices, and responsibility for reproducibility remain with the authors.
