# Mental Health Fine-tuning Analysis: LLM Safety Classification

This repository contains the code and analysis pipeline for evaluating how fine-tuning affects LLM performance on mental health safety classification tasks.

## Overview

We systematically evaluate **127 language models** across three model families (Gemma, LLaMA, Qwen) on three safety classification tasks:

1. **Suicidal Ideation Detection** - 450 expert-reviewed statements across 10 categories
2. **Therapy Request Classification** - 780 expert-reviewed statements across 12 categories
3. **Therapy Engagement Detection** - 420 expert-reviewed conversations across 13 categories

The analysis compares:
- **Base models** (pre-trained) vs **Instruction-tuned** models
- **General models** vs **Domain-specific fine-tunes** (Medical, Mental Health, Safety)
- Performance trends across model sizes (270M to 70B parameters)

## Key Findings

The pipeline generates:
- **Figure 1**: Model coverage heatmap showing which models were evaluated
- **Figure 2**: F1 score vs model parameters with trend analysis
- **Figure 3**: Delta F1 (fine-tune - base) across fine-tune categories
- **Table 1**: Regression analysis with Bonferroni-corrected coefficients
- **9 Supplementary Figures**: Family-specific facet plots (3 families × 3 tasks)

## Quick Start

### Prerequisites

1. **Python 3.10+** with virtual environment
2. **LM Studio** running at `http://localhost:1234` (for running new experiments)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/mental-health-finetune-analysis.git
cd mental-health-finetune-analysis

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis Pipeline

Generate all figures and tables:

```bash
# Run complete pipeline (uses cached results)
python run_paper_pipeline.py --skip-experiments

# Or run with fresh experiments (requires LM Studio)
python run_paper_pipeline.py
```

**Output:**
```
results/FINETUNE_PAPER_FIGURES/[YYYYMMDD]/
├── figure_1/model_coverage_heatmap.png
├── figure_2/*.png (F1 vs parameters plots)
├── figure_3/delta_f1_finetune_facet.png
├── table_1/*.csv, *.html (regression tables)
└── supplementary_figures/*.png (9 family×task plots)
```

## Repository Structure

```
.
├── run_paper_pipeline.py           # Main entry point - generates all figures/tables
│
├── analysis/
│   ├── model_coverage_heatmap.py   # Figure 1: Model coverage
│   ├── combined_finetune_facet_plot.py  # Figure 3: Delta F1 analysis
│   │
│   ├── comparative_analysis/
│   │   ├── compact_unified_facet_plot.py  # Figure 2: F1 vs params
│   │   ├── gemma_version_facet_plot.py    # Supplementary figures
│   │   ├── llama_version_facet_plot.py
│   │   ├── qwen_version_facet_plot.py
│   │   ├── facet_plot_base.py             # Shared plotting utilities
│   │   └── facet_plot_utils.py            # Guard model corrections
│   │
│   ├── statistics/
│   │   ├── regression_analysis.py         # Table 1: Regression
│   │   └── create_*_tables.py             # Table formatting
│   │
│   └── model_performance/
│       ├── batch_results_analyzer.py      # Compute metrics from cache
│       ├── metrics_calculator.py
│       └── confusion_matrices.py
│
├── config/
│   ├── models_config.csv                  # 127 model configurations with base model mappings
│   └── constants.py                       # Category labels
│
├── orchestration/                  # Experiment execution
│   ├── run_experiment.py           # Single model experiment
│   ├── api_client.py               # LM Studio API interface
│   └── data_processor.py           # Data loading
│
├── cache/                          # Results caching
│   ├── result_cache.py             # SQLite cache management
│   └── cache_manager.py            # CLI for cache operations
│
├── data/
│   ├── inputs/
│   │   ├── finalized_input_data/   # Expert-reviewed datasets
│   │   ├── intermediate_files/     # Psychiatrist review data
│   │   └── manifests/              # Selection reproducibility
│   └── prompts/                    # System prompts for each task
│
├── data_preparation/               # Dataset creation scripts
│
├── bash_scripts/
│   ├── run_all_models.sh           # Run experiments for all models
│   ├── preflight.sh                # Validation checks
│   └── run_experiments.sh          # Experiment execution
│
└── utilities/                      # Helper utilities
```

## Model Configuration

The analysis uses `config/models_config.csv` which contains all model configurations including base model mappings for delta F1 analysis.

Key columns:

| Column | Description |
|--------|-------------|
| `lm_studio_id` | Unique model identifier |
| `family`, `size` | Model family and variant |
| `model_type` | IT, PT, Medical, Mental Health, Guard, etc. |
| `param_billions` | Model size in billions of parameters |
| `Base_Model_LM_Studio_ID` | Base model for fine-tune comparisons |

**Model Types:**
- **PT**: Pre-trained (base models)
- **IT**: Instruction-tuned
- **Medical**: Medical domain fine-tunes (Meditron, MedGemma)
- **Mental Health**: Mental health fine-tunes
- **Guard/ShieldGemma**: Safety-focused fine-tunes

## Running Individual Components

### Generate Specific Figures

```bash
# Figure 1: Model coverage
python analysis/model_coverage_heatmap.py

# Figure 2: F1 vs parameters
python analysis/comparative_analysis/compact_unified_facet_plot.py \
    --output-dir results/figure_2/

# Figure 3: Delta F1 fine-tune plot
python analysis/combined_finetune_facet_plot.py

# Table 1: Regression analysis
python analysis/statistics/regression_analysis.py
```

### Run Experiments for Specific Models

```bash
# Run specific models
bash bash_scripts/run_all_models.sh --models "gemma:12b-it,llama3.1:8b" \
    data/inputs/finalized_input_data/SI_finalized_sentences.csv \
    data/prompts/system_suicide_detection_v2.txt \
    system_suicide_detection_v2
```

### Check Cache Status

```bash
# View cache statistics
python -m cache.cache_manager stats

# Check cache for specific experiment
python -m utilities.batch_cache_checker \
    --prompt-name system_suicide_detection_v2 \
    --prompt-file data/prompts/system_suicide_detection_v2.txt \
    --input-data data/inputs/finalized_input_data/SI_finalized_sentences.csv
```

## Datasets

| Dataset | Statements | Categories | Source |
|---------|------------|------------|--------|
| Suicidal Ideation | 450 | 10 | Expert-reviewed synthetic statements |
| Therapy Request | 780 | 12 | Expert-reviewed synthetic statements |
| Therapy Engagement | 420 | 13 | Expert-reviewed synthetic conversations |

All datasets were reviewed by 2 psychiatrists.

## Citation

If you use this code or analysis in your research, please cite:

```bibtex
@article{mental_health_finetune_2025,
  title={Leveraging simulation to provide a practical framework for assessing the novel scope of risk of LLMs in healthcare},
  author={Kalinich, Mark and Luccarelli, James and Moss, Frank and Torous, John},
  journal={medRxiv},
  year={2025},
  doi={10.1101/2025.11.10.25339903},
  url={https://doi.org/10.1101/2025.11.10.25339903}
}
```
Acknowledgments
Claude Sonnet and Opus 4.5 via Cursor was used extensively throughout the development of this codebase to assist with code generation, refactoring, and documentation. All code and analysis decisions remain the responsibility of the project author.
