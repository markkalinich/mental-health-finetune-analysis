---
license: apache-2.0
language:
  - en
  - zh
  - ja
  - de
  - fr
  - es
tags:
  - finance
  - sentiment-analysis
  - multilingual
  - xlm-roberta
  - financial-nlp
  - stock-market
  - trading
datasets:
  - Kenpache/multilingual-financial-sentiment
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
model-index:
  - name: FLAME
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.8103
          - name: F1 (weighted)
            type: f1
            value: 0.8102
---

# FLAME — Financial Language Analysis for Multilingual Economics

**One model. Six languages. Real financial sentiment.**

FLAME classifies financial text as **Negative**, **Neutral**, or **Positive** across English, Chinese, Japanese, German, French, and Spanish — in a single model, no language detection needed.

Built on XLM-RoBERTa with domain-adaptive pretraining on 35K+ financial texts, then fine-tuned on ~39K real financial news samples from 80+ sources worldwide.

## Quick Start

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/flame")

# English
classifier("Apple reported record quarterly revenue of $124 billion, up 11% year over year.")
# [{'label': 'Positive', 'score': 0.96}]

# Chinese
classifier("该公司季度亏损扩大至5亿美元，远超市场预期。")
# [{'label': 'Negative', 'score': 0.94}]

# Japanese
classifier("トヨタ自動車の営業利益は前年同期比30%増の1兆円を突破した。")
# [{'label': 'Positive', 'score': 0.95}]

# German
classifier("Die Aktie verlor nach der Gewinnwarnung deutlich an Wert.")
# [{'label': 'Negative', 'score': 0.92}]

# French
classifier("Le chiffre d'affaires du groupe a progressé de 8% au premier semestre.")
# [{'label': 'Positive', 'score': 0.93}]

# Spanish
classifier("Las acciones de la empresa se mantuvieron estables tras la publicación de resultados.")
# [{'label': 'Neutral', 'score': 0.89}]
```

## Batch Processing

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/flame", device=0)

texts = [
    "Stocks rallied after the Fed signaled a pause in rate hikes.",
    "The company filed for Chapter 11 bankruptcy protection.",
    "Q3 earnings were in line with analyst expectations.",
    "日経平均株価が3万円台を回復した。",
    "Les marchés européens ont clôturé en forte baisse.",
    "El beneficio neto de la compañía creció un 25% interanual.",
]

results = classifier(texts, batch_size=32)
for text, result in zip(texts, results):
    print(f"{result['label']:>8} ({result['score']:.2f})  {text[:70]}")
```

## Results

| Metric | Score |
|---|---|
| **Accuracy** | **0.8103** |
| **F1 (weighted)** | **0.8102** |
| **Precision (weighted)** | **0.8111** |
| **Recall (weighted)** | **0.8103** |

### Per-Class Performance

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Negative | 0.78 | 0.83 | 0.81 | 917 |
| Neutral | 0.83 | 0.79 | 0.81 | 1,779 |
| Positive | 0.80 | 0.82 | 0.81 | 1,225 |

All three classes achieve balanced F1=0.81, even with imbalanced training data (Neutral 45%, Positive 31%, Negative 24%).

## Labels

| Label | ID | What it captures |
|---|---|---|
| **Negative** | 0 | Losses, decline, bearish signals, layoffs, bankruptcy |
| **Neutral** | 1 | Factual statements, announcements, no clear sentiment |
| **Positive** | 2 | Growth, gains, bullish signals, record earnings, upgrades |

## Supported Languages

| Language | Code | Training Samples | Key Sources |
|---|---|---|---|
| Japanese | JA | 8,287 | Nikkei, Nikkan Kogyo, Reuters JP |
| Chinese | ZH | 7,930 | Sina Finance, EastMoney, 10jqka |
| Spanish | ES | 7,125 | Expansión, Cinco Días, Bloomberg Línea |
| English | EN | 6,887 | CNBC, Yahoo Finance, Fortune, Reuters |
| German | DE | 5,023 | Börse.de, FAZ, NTV Börse |
| French | FR | 3,935 | Boursorama, Tradingsat, BFM Business |

## Use Cases

- **News Monitoring** — classify sentiment of financial headlines across global markets in real time
- **Trading Signals** — feed sentiment scores into quantitative trading strategies
- **Portfolio Risk** — monitor sentiment shifts across international holdings
- **Earnings Analysis** — analyze tone of corporate press releases and earnings calls
- **Social Media** — track financial discussions on multilingual platforms
- **Research** — cross-language sentiment studies in financial NLP

## How It Was Built

1. **Domain Adaptation (TAPT):** Masked Language Modeling on 35K+ financial texts across 6 languages — the model learns financial vocabulary and patterns before seeing any labels.

2. **Fine-Tuning:** Supervised classification with label smoothing (0.1), cosine LR schedule (2e-5), and Stochastic Weight Averaging of top-3 checkpoints for robust generalization.

| Parameter | Value |
|---|---|
| Base model | xlm-roberta-base (278M params) |
| Learning rate | 2e-5 |
| Scheduler | Cosine |
| Label smoothing | 0.1 |
| Effective batch size | 64 |
| Precision | FP16 |
| Post-processing | SWA (top-3 checkpoints) |

## Dataset

Trained on [Kenpache/multilingual-financial-sentiment](https://huggingface.co/datasets/Kenpache/multilingual-financial-sentiment) — ~39K curated financial news samples from 80+ real sources worldwide.

## Citation

```bibtex
@misc{flame2025,
  title={FLAME: Financial Language Analysis for Multilingual Economics},
  author={Kenpache},
  year={2025},
  url={https://huggingface.co/Kenpache/flame}
}
```

## License

Apache 2.0
