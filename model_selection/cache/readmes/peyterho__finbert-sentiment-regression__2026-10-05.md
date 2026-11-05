---
library_name: transformers
license: apache-2.0
base_model: ProsusAI/finbert
tags:
- text-classification
- regression
- sentiment-analysis
- finance
- macroeconomics
- finbert
- continuous-sentiment
- bert
language:
- en
datasets:
- pauri32/fiqa-2018
metrics:
- mse
- pearsonr
pipeline_tag: text-classification
arxiv: 1908.10063
model-index:
- name: finbert-sentiment-regression
  results:
  - task:
      type: text-classification
      name: Sentiment Regression
    dataset:
      name: FiQA 2018
      type: pauri32/fiqa-2018
    metrics:
    - type: mse
      value: 0.069
      name: MSE
    - type: pearsonr
      value: 0.70
      name: Pearson r
---

# FinBERT Sentiment Regression

A fine-tuned [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) (109M params) for **continuous sentiment scoring** — outputs a single float in **[-1, +1]** instead of a discrete class label. Trained on the [FiQA 2018](https://huggingface.co/datasets/pauri32/fiqa-2018) financial opinion mining dataset with expert-annotated continuous sentiment scores.

Part of the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) ecosystem. While the sibling 3-class models classify text into positive/negative/neutral buckets, this model captures the **intensity and gradation** of sentiment — distinguishing between mildly positive (+0.2) and strongly positive (+0.8), or between mild concern (-0.3) and acute crisis (-0.9).

## Why Continuous Sentiment?

Discrete 3-class sentiment (positive/neutral/negative) loses information. Consider these headlines:

| Text | 3-class label | Continuous score |
|---|---|---|
| "Revenue slightly exceeded expectations" | positive | +0.21 |
| "Revenue smashed all records by 40%" | positive | +0.82 |
| "Minor supply chain delays reported" | negative | -0.18 |
| "Company declares bankruptcy amid fraud" | negative | -0.95 |

A 3-class model assigns the same label to both rows in each pair. A regression model captures the magnitude — enabling time-series tracking, ranking, index construction, and threshold-based filtering at any arbitrary cutoff.

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("peyterho/finbert-sentiment-regression")
model = AutoModelForSequenceClassification.from_pretrained("peyterho/finbert-sentiment-regression")
model.eval()

def score(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        return model(**inputs).logits.item()

# Strong positive
score("Tesla shares surged 15% after crushing earnings expectations")
# → +0.65

# Mild positive
score("FDA Approves generic version of AstraZeneca heartburn drug")
# → +0.22

# Near-neutral
score("The committee will meet next Tuesday to discuss the quarterly report")
# → +0.03

# Mild negative
score("Tesla recalls 2,700 Model X SUVs")
# → -0.31

# Strong negative
score("Markets crashed amid recession fears and massive layoffs")
# → -0.78
```

### Batch Scoring

```python
import torch

texts = [
    "Q3 revenue surged 24% year-over-year",
    "The board appointed a new interim CEO",
    "Credit markets froze as contagion fears spread",
]

inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=128)
with torch.no_grad():
    scores = model(**inputs).logits.squeeze(-1).tolist()

for text, s in zip(texts, scores):
    print(f"{s:+.3f}  {text}")
# +0.58  Q3 revenue surged 24% year-over-year
# +0.05  The board appointed a new interim CEO
# -0.72  Credit markets froze as contagion fears spread
```

### Building a Sentiment Index

```python
import pandas as pd

# Score a time-series of headlines
headlines = pd.DataFrame({
    "date": ["2024-01-15", "2024-01-16", "2024-01-17", "2024-01-18"],
    "text": [
        "Strong jobs report pushes markets to record highs",
        "Tech earnings mixed as AI spending soars",
        "Fed signals patience on rate cuts, markets dip",
        "Retail sales disappoint, recession fears resurface",
    ]
})

headlines["sentiment"] = headlines["text"].apply(score)
headlines["rolling_avg"] = headlines["sentiment"].rolling(3, min_periods=1).mean()
print(headlines[["date", "sentiment", "rolling_avg"]])
```

## Evaluation Results

Evaluated on the FiQA 2018 test split (150 samples):

| Metric | Value |
|---|---|
| **MSE** | 0.069 |
| **RMSE** | 0.263 |
| **Pearson r** | **0.70** |

A Pearson correlation of 0.70 indicates strong linear agreement with expert annotations. The RMSE of 0.263 on a [-1, +1] scale means predictions are typically within ~0.26 of the ground-truth score.

### Interpreting the Output Scale

| Score Range | Interpretation | Example |
|:---:|---|---|
| +0.6 to +1.0 | Strongly positive | Earnings beat, major contract win, strong growth |
| +0.2 to +0.6 | Moderately positive | Modest revenue growth, favorable regulatory decision |
| -0.2 to +0.2 | Neutral / mixed | Factual reporting, mixed signals, routine announcements |
| -0.6 to -0.2 | Moderately negative | Missed estimates, minor product recall, cautious guidance |
| -1.0 to -0.6 | Strongly negative | Market crash, bankruptcy, fraud, major crisis |

> **Note:** These thresholds are approximate. The model's output is unbounded (it can theoretically exceed ±1.0 on extreme inputs). Clip to [-1, +1] if strict bounds are required.

## Training Data

Trained on the [FiQA 2018](https://huggingface.co/datasets/pauri32/fiqa-2018) financial opinion mining dataset — expert-annotated continuous sentiment scores for financial microblogs and news headlines.

| Split | Samples | Source |
|---|:---:|---|
| Train | 938 (train + validation merged) | Financial microblogs + news headlines |
| Test | 150 | Held-out evaluation |

### Dataset Characteristics

The FiQA dataset contains two text formats:

- **Microblogs/posts** — short, informal financial social media posts with $cashtags, slang, and abbreviations (e.g., *"Still short $LNG from $11.70 area...next stop could be down through $9.00"*)
- **Headlines** — concise news headlines in formal register (e.g., *"How Kraft-Heinz Merger Came Together in Speedy 10 Weeks"*)

Each sample includes:
- `sentence` — the full text
- `sentiment_score` — expert-annotated continuous score (approximately [-1, +1])
- `target` — the entity being discussed (stock ticker or company name)
- `aspects` — fine-grained aspect categories (e.g., *Stock/Price Action/Bearish*, *Corporate/M&A*)

The sentiment scores are **entity-relative** — the same event can have different sentiment for different companies (e.g., an acquisition might be positive for the acquirer but negative for a competitor).

### Score Distribution

The training data spans the full [-1, +1] range with moderate concentration near zero:

- ~35% of samples in [-0.15, +0.15] (near-neutral)
- ~40% of samples in [+0.15, +1.0] (positive)
- ~25% of samples in [-1.0, -0.15] (negative)

## Training Details

| Hyperparameter | Value |
|---|---|
| Base model | [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) (109M, BERT-base, 12 layers, 768 hidden, 12 heads) |
| Task | Regression (single output neuron, `problem_type="regression"`) |
| Loss function | MSE |
| Learning rate | 2e-5 |
| Batch size | 64 effective |
| Epochs | 6 (best checkpoint at epoch 3) |
| Scheduler | Linear decay with warmup |
| Max length | 128 tokens |
| Precision | FP16 |
| Seed | 42 |
| Best model selection | Lowest validation MSE |

### Architecture

The model uses `BertForSequenceClassification` with `num_labels=1` and `problem_type="regression"`. The classification head is a single linear layer mapping the 768-dim [CLS] representation to a scalar output. No activation function is applied — the output is unbounded, but in practice stays near [-1, +1] for financial text.

## When to Use This vs. the 3-Class Models

| Use Case | Recommended Model |
|---|---|
| **Categorical labelling** — "is this positive, negative, or neutral?" | [finbert-macro-sentiment](https://huggingface.co/peyterho/finbert-macro-sentiment) (3-class) |
| **Sentiment intensity** — "how positive/negative is this?" | **This model** (regression) |
| **Time-series / sentiment indices** — track sentiment over time | **This model** (regression) |
| **Ranking** — sort texts by sentiment strength | **This model** (regression) |
| **Threshold-based filtering** — custom cutoffs (e.g., flag text with score < -0.5) | **This model** (regression) |
| **Multi-signal analysis** — sentiment + policy stance + crisis | [Full pipeline](https://huggingface.co/peyterho/macro-sentiment-finbert) |
| **Climate/ESG text** | [climatebert-macro-sentiment](https://huggingface.co/peyterho/climatebert-macro-sentiment) (3-class) |
| **Highest classification accuracy** | [financial-roberta-large-macro-sentiment](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) (355M, 3-class) |

### Deriving Classes from Continuous Scores

You can always convert this model's continuous output to discrete labels at any threshold:

```python
def to_label(score, threshold=0.15):
    if score > threshold:
        return "positive"
    elif score < -threshold:
        return "negative"
    else:
        return "neutral"

sentiment = score("Tesla shares surged after earnings beat")
label = to_label(sentiment)  # "positive"
```

This gives you **tunable sensitivity** — a lower threshold catches weaker signals, a higher threshold only flags strong sentiment.

## Related Models

This model is part of the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) ecosystem:

| Model | Type | Params | Task |
|---|---|:---:|---|
| [peyterho/macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) | Ensemble pipeline | — | Multi-signal macro sentiment (full system) |
| [peyterho/finbert-macro-sentiment](https://huggingface.co/peyterho/finbert-macro-sentiment) | 3-class | 109M | Financial news sentiment (default head) |
| [peyterho/financial-roberta-large-macro-sentiment](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 3-class | 355M | Policy/macro sentiment (best accuracy) |
| [peyterho/climatebert-macro-sentiment](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 3-class | 82M | Climate/ESG sentiment |
| **peyterho/finbert-sentiment-regression** ★ | **Regression** | **109M** | **Continuous sentiment [-1, +1]** |

## Limitations

- **Small training set** — only 938 training samples from FiQA 2018. The model benefits from FinBERT's financial pre-training, but may not generalize well to domains far from financial microblogs and news headlines (e.g., lengthy 10-K filings, academic papers).
- **Entity-relative annotations** — FiQA scores are annotated relative to a target entity. The model doesn't receive explicit entity information at inference time, so it infers the "main subject" from context. For texts discussing multiple entities with opposing sentiment, the output is an aggregate.
- **128-token max length** — truncates longer inputs. Chunk longer documents at sentence or paragraph level.
- **Unbounded output** — the model can theoretically output scores outside [-1, +1] on extreme or out-of-distribution inputs. Apply `torch.clamp(score, -1.0, 1.0)` if strict bounds are needed.
- **No aspect-level scoring** — FiQA includes aspect annotations (e.g., *Corporate/Dividend Policy*, *Stock/Technical Analysis*), but this model only predicts overall sentiment, not per-aspect scores.
- **English only** — pre-trained and fine-tuned exclusively on English text.
- **Pearson r = 0.70** — while reasonable for a small dataset, ~30% of variance in human annotations is unexplained. Use averaged scores over multiple texts for more reliable aggregate signals.

## Citation

```bibtex
@article{araci2019finbert,
    title={FinBERT: Financial Sentiment Analysis with Pre-Trained Language Models},
    author={Araci, Dogu},
    journal={arXiv preprint arXiv:1908.10063},
    year={2019}
}

@inproceedings{maia2018fiqa,
    title={WWW'18 Open Challenge: Financial Opinion Mining and Question Answering},
    author={Maia, Macedo and Handschuh, Siegfried and Freitas, André and Davis, Brian and McDermott, Ross and Zarrouk, Manel and Balahur, Alexandra},
    booktitle={Companion Proceedings of the The Web Conference 2018},
    pages={1941--1942},
    year={2018}
}
```

## Framework Versions

- Transformers 5.6.2
- PyTorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2

## License

Apache 2.0
