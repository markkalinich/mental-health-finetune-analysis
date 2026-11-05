---
language: en
license: mit
base_model: cardiffnlp/twitter-roberta-base-sentiment
tags:
  - text-classification
  - sentiment-analysis
  - sports
  - nba
  - roberta
metrics:
  - accuracy
  - f1
---

# NBA Press Conference Sentiment - Fine-tuned RoBERTa

A RoBERTa model fine-tuned for 3-class sentiment analysis on NBA playoff press conference transcripts.

## Model Description

Base model: [`cardiffnlp/twitter-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)

Fine-tuned on 2,050 NBA press conference speaker turns (50 hand-labeled seed turns + 2,000 GPT-4o-mini weak labels), covering Conference Finals and NBA Finals transcripts from 2013-2022 (2,790 transcripts, 23,166 speaker turns total).

**Labels:** NEGATIVE (0), NEUTRAL (1), POSITIVE (2)

## Performance

Evaluated on a 50-turn hand-labeled seed set:

| Model | Accuracy | Macro F1 |
|---|---|---|
| **This model (fine-tuned)** | **92%** | **0.932** |
| Twitter RoBERTa (base, no fine-tune) | 54% | 0.467 |
| DistilBERT SST-2 | 52% | 0.380 |
| FinBERT | 34% | 0.288 |

Fine-tuning closed a +38 percentage point gap over the best off-the-shelf baseline. General-purpose sentiment models fail on sports language because athletes and coaches systematically frame losses in positive terms ("we competed hard", "we'll make adjustments") rather than expressing raw negativity.

## Training Details

- **Base model:** `cardiffnlp/twitter-roberta-base-sentiment`
- **Training data:** 2,050 labeled speaker turns (80/20 train/val split)
- **Weak labeling:** GPT-4o-mini with sports-specific 3-class definitions, batched 20/call
- **Framework:** Hugging Face `Trainer`
- **Epochs:** 5 (early stopping patience=2; best checkpoint at epoch 4)
- **Learning rate:** 2e-5 with linear warmup (10%)
- **Batch size:** 16
- **Experiment tracking:** MLflow

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="EgeDenizPekel/nba-press-sentiment-roberta"
)

classifier("We competed hard tonight. We'll make some adjustments and come back stronger.")
# [{'label': 'POSITIVE', 'score': 0.87}]

classifier("We got killed out there. That was embarrassing.")
# [{'label': 'NEGATIVE', 'score': 0.94}]
```

## Research Context

Built as part of an end-to-end NLP portfolio project investigating whether post-game press conference sentiment correlates with NBA playoff outcomes.

**Key finding:** No statistically significant correlation between post-game sentiment and point differential (r=-0.088, p=0.30, n=141 games). Press conference framing is strategically managed and does not leak game-level performance.

Full project: [press-conference-sentiment-analyzer](https://github.com/EgeDenizPekel/press-conference-sentiment-analyzer)
