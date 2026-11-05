---
language:
- ar
- de
- en
- es
- fr
- hi
- ja
- ko
- pt
- zh
license: apache-2.0
tags:
- finance
- financial-sentiment
- multilingual
- sentiment-analysis
- xlm-roberta
- perspective-aware
- text-classification
- financial-news
pipeline_tag: text-classification
model-index:
- name: perspective-aware-financial-sentiment
  results:
  - task:
      type: text-classification
      name: Financial Sentiment Analysis
    metrics:
    - type: accuracy
      value: 0.8411
      name: Accuracy
    - type: f1
      value: 0.8420
      name: F1 Macro
---

# FLAME2 — Multilingual Perspective-Aware Financial Sentiment

> XLM-RoBERTa-large fine-tuned on 145,637 financial headlines across 10 languages.
> **Key innovation:** Same news event → different sentiment per market perspective.

## Key numbers

| | |
|---|---|
| **Base model** | XLM-RoBERTa-large (560M params) |
| **Languages** | 10 (AR, DE, EN, ES, FR, HI, JA, KO, PT, ZH) |
| **Training data** | 145,637 perspective-labeled headlines |
| **Overall Accuracy** | **84.11%** |
| **F1 Macro** | **84.20%** |
| **Labels** | negative (0) / neutral (1) / positive (2) |

## Quick start

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Kenpache/perspective-aware-financial-sentiment"
)

# IMPORTANT: Always prefix with [LANG] for correct perspective
classifier("[EN] Federal Reserve cuts interest rates by 25 basis points")
# → {'label': 'positive', 'score': 0.94}

classifier("[AR] Oil prices fall sharply to $60 per barrel")
# → {'label': 'negative', 'score': 0.89}  (Arab: oil exporter → bad)

classifier("[HI] Oil prices fall sharply to $60 per barrel")
# → {'label': 'positive', 'score': 0.87}  (India: oil importer → good)
```

## Perspective-aware: same news, different labels

```python
from transformers import pipeline
classifier = pipeline("text-classification",
                      model="Kenpache/perspective-aware-financial-sentiment")

oil_drop = "Oil prices fall to $60 per barrel"

results = {}
for lang in ["AR", "HI", "EN", "DE", "JA", "KO"]:
    r = classifier(f"[{lang}] {oil_drop}")[0]
    results[lang] = f"{r['label']} ({r['score']:.2f})"

# AR → negative  (Gulf exporter: lost revenue)
# HI → positive  (India importer: lower costs)
# EN → positive  (US: lower inflation)
# DE → positive  (Germany: lower energy costs)
# JA → positive  (Japan: lower import costs)
# KO → positive  (Korea: lower import costs)
```

## Batch processing

```python
headlines = [
    "[EN] Amazon reports record quarterly revenue of $187 billion",
    "[AR] OPEC+ agrees to increase oil output by 400,000 bpd",
    "[HI] OPEC+ agrees to increase oil output by 400,000 bpd",
    "[JA] Bank of Japan raises interest rates to 0.5%",
    "[DE] ECB cuts rates by 25 basis points amid slowdown",
    "[ZH] CSI 300 index rises 2.3% on stimulus optimism",
]

results = classifier(headlines)
for h, r in zip(headlines, results):
    print(f"{h[:50]:<50} → {r['label']} ({r['score']:.2f})")
```

## Per-language performance

| Language | Accuracy | F1 Macro |
|----------|:--------:|:--------:|
| Hindi (hi) | 89.33% | 89.21% |
| French (fr) | 87.45% | 87.12% |
| English (en) | 86.78% | 86.54% |
| Chinese (zh) | 85.92% | 85.67% |
| German (de) | 85.34% | 85.01% |
| Spanish (es) | 84.67% | 84.43% |
| Japanese (ja) | 84.12% | 83.98% |
| Korean (ko) | 83.76% | 83.45% |
| Portuguese (pt) | 83.54% | 83.21% |
| Arabic (ar) | 83.18% | 82.87% |
| **Overall** | **84.11%** | **84.20%** |

## Training details

| Parameter | Value |
|-----------|-------|
| Base model | xlm-roberta-large |
| Batch size | 32 |
| Learning rate | 2e-5 |
| Epochs | 5 (early stopping, patience=2) |
| Max sequence length | 128 tokens |
| Precision | FP16 |
| Label smoothing | 0.1 |
| Class weights | Balanced |
| Split | 70/15/15 group-by-source |

**Language prefix injection:** Each input is prefixed with `[LANG]` (e.g., `[AR]`, `[EN]`) so the model learns perspective-specific sentiment rules during training.

## Dataset

Trained on [FLAME Perspective-Aware Financial Sentiment Dataset](https://huggingface.co/datasets/Kenpache/perspective-aware-financial-sentiment) — 145,637 headlines across 10 languages with local investor perspective labeling.

## When to use language prefixes

| Use case | Prefix |
|----------|--------|
| Classifying Arabic financial news | `[AR] headline` |
| Classifying English financial news | `[EN] headline` |
| Unknown language | Detect language first, then prefix |

## Citation

```bibtex
@model{perspective_aware_financial_sentiment_2026,
  title     = {FLAME2: Multilingual Perspective-Aware Financial Sentiment Model},
  author    = {Zaraki},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/Kenpache/perspective-aware-financial-sentiment}
}
```
