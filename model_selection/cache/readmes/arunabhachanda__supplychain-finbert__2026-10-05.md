---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - supply-chain
  - geopolitical-risk
  - finbert
  - bert
  - transfer-learning
  - fine-tuning
datasets:
  - FinGPT/fingpt-sentiment-train
  - zeroshot/twitter-financial-news-sentiment
metrics:
  - accuracy
  - f1
---

# supplychain-finbert

Fine-tuned [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) for
**supply chain geopolitical risk sentiment analysis**.

Built for [SupplyGuard AI](https://github.com/arunabhachanda/supplyguard-ai) —
a production-grade supply chain risk intelligence platform.

## Model Details

| Property | Value |
|---|---|
| Base model | ProsusAI/finbert (BERT-base fine-tuned on Reuters/Bloomberg) |
| Task | 3-class sentiment: negative / neutral / positive |
| Fine-tuning strategy | Frozen layers 0–9, trainable layers 10–11 + pooler + head |
| Training data | ~40,600 samples (FinGPT financial sentiment + Twitter Financial News + ~70 synthetic geopolitical headlines) |
| Class balancing | Undersampling + weighted CrossEntropyLoss (neg=1.459, neu=1.060, pos=0.729) |
| Test accuracy | 0.6393 |
| Best val accuracy | 0.6454 |

## Performance

| Class | Precision | Recall | F1 |
|---|---|---|---|
| negative | 0.73 | 0.86 | 0.79 |
| neutral | 0.52 | 0.75 | 0.62 |
| positive | 0.74 | 0.45 | 0.56 |
| **overall** | **0.67** | **0.64** | **0.63** |

## Labels

| ID | Label | Meaning |
|---|---|---|
| 0 | negative | Risk increasing — conflict, sanctions, disaster, supplier failure |
| 1 | neutral | Routine updates, mixed signals, uncertainty |
| 2 | positive | Risk decreasing — stability, trade agreements, recovery |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="arunabhachanda/supplychain-finbert",
    return_all_scores=True,
)

result = classifier("Ceasefire in the region reopens key supply corridors")
# → [{'label': 'negative', 'score': 0.04},
#    {'label': 'neutral',  'score': 0.11},
#    {'label': 'positive', 'score': 0.85}]

# Polarity score used by SupplyGuard AI:
polarity = result[2]['score'] - result[0]['score']   # P(positive) - P(negative)
# → float in [-1.0, +1.0]  used as region_news_sentiment feature
```

## Transfer Learning Architecture

```
ProsusAI/finbert (pre-trained on financial news corpus)
├── BERT Embeddings          [FROZEN]      ← vocabulary + positional encoding
├── Transformer Layer 0–9    [FROZEN]      ← general language + financial knowledge
├── Transformer Layer 10–11  [TRAINABLE]   ← adapted to supply-chain language
├── Pooler                   [TRAINABLE]   ← [CLS] token representation
└── Classifier Head (768→3)  [TRAINABLE]   ← new head for 3-class sentiment
```

**Trainable parameters:** 14,768,643 (13.5% of total)  
**Frozen parameters:** 94,715,904 (86.5% of total)

## Training Details

- **Optimizer:** AdamW (lr=2e-5, weight_decay=0.01)
- **Scheduler:** Linear warmup (10% steps) + linear decay
- **Epochs:** 4
- **Batch size:** 16
- **Gradient clipping:** max_norm=1.0
- **Class weights:** neg=1.459, neu=1.060, pos=0.729 (weighted CrossEntropyLoss)
- **Split:** 80% train / 10% val / 10% test (stratified)

## Built By

Arunabha Kumar Chanda — M.Sc. Business Intelligence & Data Science, ISM Munich  
GitHub: [arunabhachanda](https://github.com/arunabhachanda)
