---
library_name: transformers
license: apache-2.0
base_model: climatebert/distilroberta-base-climate-sentiment
tags:
- text-classification
- sentiment-analysis
- finance
- climate
- esg
- sustainability
- green-finance
- distilroberta
language:
- en
datasets:
- nickmuchi/financial-classification
- zeroshot/twitter-financial-news-sentiment
- FinanceInc/auditor_sentiment
- pauri32/fiqa-2018
- climatebert/climate_sentiment
metrics:
- accuracy
- f1
pipeline_tag: text-classification
model-index:
- name: climatebert-macro-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Combined Financial Sentiment (5 datasets)
      type: custom
    metrics:
    - type: accuracy
      value: 0.8885
      name: Accuracy
    - type: f1
      value: 0.8716
      name: F1 (macro)
    - type: f1
      value: 0.8898
      name: F1 (weighted)
  - task:
      type: text-classification
      name: Sentiment Analysis (OOD)
    dataset:
      name: Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
      type: Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
    metrics:
    - type: accuracy
      value: 0.9248
      name: Accuracy
    - type: f1
      value: 0.9213
      name: F1 (macro)
  - task:
      type: text-classification
      name: Sentiment Analysis (OOD)
    dataset:
      name: ic-fspml/stock_news_sentiment
      type: ic-fspml/stock_news_sentiment
    metrics:
    - type: accuracy
      value: 0.6472
      name: Accuracy
    - type: f1
      value: 0.6441
      name: F1 (macro)
---

# ClimateBERT Macro Sentiment

A fine-tuned [climatebert/distilroberta-base-climate-sentiment](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment) (82M params, DistilRoBERTa) for **3-class sentiment analysis on financial, macroeconomic, and climate/ESG text**.

This model is the **ClimateBERT head** within the larger [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) ensemble pipeline. When text is detected as climate/ESG-related, the pipeline's topic router automatically selects this model for inference. It can also be used standalone for any financial sentiment task.

## Why ClimateBERT?

The base model ([climatebert/distilroberta-base-climate-f](https://huggingface.co/climatebert/distilroberta-base-climate-f)) was further pre-trained on climate-related text by [Bingler et al. (2023)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3998435), then fine-tuned on the [climatebert/climate_sentiment](https://huggingface.co/datasets/climatebert/climate_sentiment) dataset for climate risk/neutral/opportunity classification. This gives it a strong inductive bias for climate and ESG language — terminology like *stranded assets*, *transition risk*, *green bonds*, and *net-zero commitments* are well-represented in its pre-training distribution.

By further fine-tuning on a broader mix of 5 financial sentiment datasets, we retain the climate domain advantage while gaining general financial sentiment capability. The result: **the smallest model in the ensemble (82M) that still reaches 88.9% accuracy**, and the **best OOD generalization on financial phrasebank data** among all three heads relative to its parameter count.

## Quick Start

### Standalone Usage

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="peyterho/climatebert-macro-sentiment", top_k=None)

# Climate/ESG text — the model's home turf
pipe("Renewable energy investments surged as solar costs fell to record lows.")
# [[{'label': 'opportunity', 'score': 0.95}, {'label': 'neutral', 'score': 0.04}, {'label': 'risk', 'score': 0.01}]]

pipe("Climate change poses significant physical risks to coastal infrastructure.")
# [[{'label': 'risk', 'score': 0.91}, {'label': 'neutral', 'score': 0.07}, {'label': 'opportunity', 'score': 0.02}]]

# General financial text — also works well after fine-tuning
pipe("Q3 earnings beat expectations with revenue up 12% year-over-year.")
# [[{'label': 'opportunity', 'score': 0.88}, ...]]

pipe("The company reported a significant decline in operating margins.")
# [[{'label': 'risk', 'score': 0.85}, ...]]
```

### As Part of the Full Pipeline

Within the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) pipeline, this model is automatically selected when climate/ESG keywords are detected:

```python
from macro_sentiment import MacroSentimentPipeline

pipe = MacroSentimentPipeline(device="cpu")

result = pipe("The EU's carbon border adjustment mechanism will reshape trade flows for emission-intensive industries.")
print(result.summary())
# Sentiment: Negative (-0.215) | Policy: Neutral (+0.000) | Crisis: Normal (0.000) | Domain: climate | Climate: Risk (exp=0.45)
print(result.head_used)
# "climate"

result = pipe("Green bond issuance hit $500 billion as investors pivoted toward sustainable fixed income.")
print(result.summary())
# Sentiment: Positive (+0.534) | Policy: Neutral (+0.000) | Crisis: Normal (0.000) | Domain: climate | Climate: Opportunity (exp=0.38)
```

## Label Mapping

This model uses ClimateBERT's native label scheme, which maps to the unified 3-class sentiment as follows:

| Label ID | Model Label | Unified Sentiment | Score Mapping |
|:---:|---|---|:---:|
| 0 | `opportunity` | positive | +1.0 |
| 1 | `neutral` | neutral | 0.0 |
| 2 | `risk` | negative | -1.0 |

> **Note:** The label ordering differs from the unified schema (0=negative, 1=neutral, 2=positive). A label remapping is applied during training and inference within the ensemble pipeline. If using the model standalone, interpret `opportunity` as positive and `risk` as negative.

## Evaluation Results

### In-Domain (Combined Test Set — 4,333 samples)

All three fine-tuned heads compared on the same held-out test split:

| Model | Params | Accuracy | F1 (macro) | F1 (weighted) |
|---|:---:|:---:|:---:|:---:|
| [RoBERTa-Large](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | 0.9130 | 0.9023 | 0.9137 |
| [FinBERT](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | 0.8973 | 0.8813 | 0.8984 |
| **ClimateBERT (this model)** | **82M** | **0.8885** | **0.8716** | **0.8898** |

### Out-of-Domain: Financial Phrasebank (785 samples)

Evaluated on [Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75](https://huggingface.co/datasets/Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75) — **not in the training mix**. This dataset combines PhraseBank sentences (75% annotator agreement) with financial news articles.

| Model | Params | Accuracy | F1 (macro) |
|---|:---:|:---:|:---:|
| [RoBERTa-Large](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | 0.9414 | 0.9357 |
| **ClimateBERT (this model)** | **82M** | **0.9248** | **0.9213** |
| [FinBERT](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | 0.9236 | 0.9134 |

ClimateBERT edges out FinBERT (109M) on this OOD benchmark despite having 25% fewer parameters — likely due to DistilRoBERTa's stronger pre-training on diverse text compared to BERT's financial-domain pre-training.

### Out-of-Domain: Stock News Headlines (30,150 samples)

Evaluated on [ic-fspml/stock_news_sentiment](https://huggingface.co/datasets/ic-fspml/stock_news_sentiment) — 5-class labels mapped to 3-class. **Not in the training mix**.

| Model | Params | Accuracy | F1 (macro) |
|---|:---:|:---:|:---:|
| [RoBERTa-Large](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | 0.7211 | 0.7265 |
| [FinBERT](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | 0.6781 | 0.6765 |
| **ClimateBERT (this model)** | **82M** | **0.6472** | **0.6441** |

Lower performance on stock news headlines is expected — these are short, noisy texts with a 5→3 class mapping. FinBERT's financial pre-training gives it an advantage on this particular domain.

### Comparison Against Baselines

| Method | Accuracy | F1 (macro) | Notes |
|---|:---:|:---:|---|
| **ClimateBERT (this model)** | **0.8885** | **0.8716** | 82M params, fine-tuned |
| Dict-only meta-classifier (GBT) | 0.6693 | 0.5781 | GradientBoosting on 24 dictionary features |
| Dict-only rules (LM + Henry) | 0.5684 | 0.5277 | Threshold-based, no learned parameters |

## Training Data

Fine-tuned on **20,034 training samples** combined from 5 public financial/climate sentiment datasets:

| Dataset | Domain | Train | Test | Label Mapping |
|---|---|:---:|:---:|---|
| [nickmuchi/financial-classification](https://huggingface.co/datasets/nickmuchi/financial-classification) | Financial PhraseBank | ~4,800 | ~1,200 | negative / neutral / positive |
| [zeroshot/twitter-financial-news-sentiment](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment) | Financial tweets | ~9,900 | ~2,500 | bearish→neg, bullish→pos, neutral |
| [FinanceInc/auditor_sentiment](https://huggingface.co/datasets/FinanceInc/auditor_sentiment) | Auditor reports | ~3,600 | ~900 | negative / neutral / positive |
| [pauri32/fiqa-2018](https://huggingface.co/datasets/pauri32/fiqa-2018) | Financial QA + microblog | ~938 | ~235 | Continuous score thresholded at ±0.15 |
| [climatebert/climate_sentiment](https://huggingface.co/datasets/climatebert/climate_sentiment) | Climate disclosures | ~1,000 | ~500 | risk→neg, neutral, opportunity→pos |

All datasets unified to 3-class: `0=negative`, `1=neutral`, `2=positive` (then remapped to ClimateBERT's native `risk/neutral/opportunity` labels during training).

## Training Details

| Hyperparameter | Value |
|---|---|
| Base model | [climatebert/distilroberta-base-climate-sentiment](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment) (82M) |
| Architecture | DistilRoBERTa (6 layers, 768 hidden, 12 heads) |
| Learning rate | 2e-5 |
| Batch size | 32 × 2 gradient accumulation = 64 effective |
| Epochs | 6 (best checkpoint at epoch 3 by val loss) |
| Scheduler | Linear with 20% warmup |
| Optimizer | AdamW |
| Max length | 128 tokens |
| Precision | FP16 |
| Class weighting | √(inverse frequency) — handles ~58% neutral class imbalance |
| Seed | 42 |
| Best model selection | Lowest validation loss (epoch 3) |

### Training Curve

| Epoch | Train Loss | Val Loss | Accuracy | F1 (macro) | F1 (weighted) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.974 | 0.458 | 0.809 | 0.792 | 0.814 |
| 2 | 0.766 | 0.379 | 0.854 | 0.838 | 0.857 |
| **3** | **0.566** | **0.360** | **0.877** | **0.859** | **0.878** |
| 4 | 0.371 | 0.370 | 0.883 | 0.867 | 0.884 |
| 5 | 0.345 | 0.383 | 0.881 | 0.866 | 0.882 |
| 6 | 0.276 | 0.383 | 0.889 | 0.872 | 0.890 |

Validation loss bottomed at epoch 3, while accuracy continued improving marginally through epoch 6. The best checkpoint (epoch 3) was loaded for the final model — the later epochs show mild overfitting on val loss despite higher accuracy, suggesting the model memorizes easy-to-classify samples while losing calibration on harder boundary cases.

## Role in the Ensemble Pipeline

This model serves as the **climate/ESG specialist** in the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) pipeline. The topic router activates it when climate-related keywords are detected in the input text (e.g., *carbon*, *emission*, *renewable*, *ESG*, *net-zero*, *climate risk*, *green bond*, *Paris Agreement*).

```
Input Text → Topic Router → climate keywords detected? → ClimateBERT (this model)
                          → policy keywords detected?  → RoBERTa-Large
                          → default / financial news    → FinBERT
                          → non-English text            → XLM-RoBERTa
```

The full pipeline then fuses this model's output with dictionary-based signals (Loughran-McDonald, Henry, Sautner-style climate exposure, macro policy dictionaries) to produce a structured `MacroSentimentResult` with financial sentiment, policy stance, crisis signal, and climate-specific scores.

### Ensemble Siblings

| Head | Model | Params | Role |
|---|---|:---:|---|
| FinBERT | [peyterho/finbert-macro-sentiment](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | Default — financial news, tweets |
| RoBERTa-Large | [peyterho/financial-roberta-large-macro-sentiment](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | Policy/macro communications |
| **ClimateBERT** ★ | **peyterho/climatebert-macro-sentiment** | **82M** | **Climate/ESG text** |
| XLM-RoBERTa | [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) | 278M | Non-English text (pre-trained, not fine-tuned) |

## Custom Fine-Tuning

Fine-tune this model further on your own climate/ESG or financial labelled data:

```bash
pip install transformers datasets accelerate evaluate torch

python -m macro_sentiment.finetune \
    --data my_climate_labels.csv \
    --text-column text \
    --label-column sentiment \
    --base-model peyterho/climatebert-macro-sentiment \
    --output my-org/my-climate-model \
    --push-to-hub \
    --epochs 4 \
    --lr 1e-5 \
    --batch-size 32
```

The fine-tuning script (from the [parent repo](https://huggingface.co/peyterho/macro-sentiment-finbert)) accepts CSV, TSV, JSON, or JSONL. Labels can be strings (`"positive"`, `"negative"`, `"neutral"`, `"risk"`, `"opportunity"`) or integers (0/1/2). Automatic label remapping handles ClimateBERT's non-standard label ordering.

## Limitations

- **English only** — the base ClimateBERT model was pre-trained exclusively on English climate text. Non-English climate disclosures should use the multilingual head in the full pipeline.
- **128-token max length** — fine-tuned with 128-token truncation. Longer documents (e.g., full TCFD disclosures) should be chunked at paragraph level. The original ClimateBERT base was trained on paragraphs and may not perform as well on isolated sentences.
- **Climate data is small** — only ~1,000 of the 20,034 training samples come from the climate sentiment dataset. The model's climate advantage comes primarily from pre-training, not from fine-tuning label supervision.
- **Label noise** — the FiQA dataset uses continuous sentiment scores thresholded at ±0.15, introducing boundary noise. The climate_sentiment dataset uses annotated paragraphs which may contain mixed signals.
- **No temporal or entity awareness** — treats each text independently. Cannot reason about whether "carbon prices rising" is positive or negative for a specific company or portfolio.
- **Smaller model trade-off** — at 82M parameters (6 layers), this is the smallest head in the ensemble. It lags the 355M RoBERTa-Large by ~3 F1 points in-domain. For maximum accuracy, use the full pipeline in `mode="all"` to ensemble across all heads.

## Citation

```bibtex
@techreport{bingler2023cheaptalk,
    title={How Cheap Talk in Climate Disclosures Relates to Climate Initiatives, Corporate Emissions, and Reputation Risk},
    author={Bingler, Julia and Kraus, Mathias and Leippold, Markus and Webersinke, Nicolas},
    type={Working paper},
    institution={Available at SSRN 3998435},
    year={2023}
}

@article{loughran2011liability,
    title={When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks},
    author={Loughran, Tim and McDonald, Bill},
    journal={The Journal of Finance},
    volume={66},
    number={1},
    pages={35--65},
    year={2011}
}
```

## Framework Versions

- Transformers 5.6.2
- PyTorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2

## License

Apache 2.0
