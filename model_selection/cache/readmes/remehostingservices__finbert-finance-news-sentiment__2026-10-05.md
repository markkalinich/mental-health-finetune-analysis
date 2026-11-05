---
license: mit
language:
- en
base_model: ProsusAI/finbert
datasets:
- remehostingservices/finance-news-sentiment-35k
pipeline_tag: text-classification
library_name: transformers
tags:
- finbert
- bert
- finance
- financial-news
- sentiment
- telegram
metrics:
- accuracy
- f1
model-index:
- name: finbert-finance-news-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      name: Finance News Sentiment 40k
      type: remehostingservices/finance-news-sentiment-35k
      split: test
    metrics:
    - type: accuracy
      value: 0.847
    - type: f1
      name: macro F1
      value: 0.810
widget:
- text: "Fed holds rates, signals two cuts this year"
- text: "Apple Q3 revenue misses estimates, shares fall 6% after hours"
- text: "ECB's Lagarde to speak at 14:30 CET"
---

# FinBERT — Finance News Sentiment

ProsusAI FinBERT fine-tuned for 3-class sentiment (positive / negative /
neutral) on [Finance News Sentiment 40k](https://huggingface.co/datasets/remehostingservices/finance-news-sentiment-35k):
39,965 English financial headlines labeled by two independent LLM judges
(Claude Opus 5 and OpenAI gpt-5.6-sol) with Claude Fable 5 as arbiter. Sentiment means investor impact: "is this news good or bad for an
investor?"

## Results (test split, 3,500 headlines)

| Metric        | Value |
|---------------|-------|
| Accuracy      | 0.847 |
| Macro F1      | 0.810 |
| Positive F1   | 0.757 (P 0.76 / R 0.75) |
| Negative F1   | 0.778 (P 0.83 / R 0.73) |
| Neutral F1    | 0.895 (P 0.87 / R 0.92) |

Calibration: mean confidence 0.935, ECE 0.087. With confidence ≥ 0.95 the
model covers 76% of headlines at 92.8% accuracy. 86% of errors are
neutral ↔ directional; polarity flips are rare.

For reference, the FinBERT paper (Araci 2019) reports 0.86 accuracy on the
human-labeled Financial PhraseBank; this model's number sits at the
label-noise ceiling of its LLM-labeled data (judge agreement 85%).

## Versions

| Version | Revision | Training data | Accuracy | Macro F1 | ECE |
|---------|----------|---------------|----------|----------|-----|
| v1 (3 Sep 2026) | tag `v1-a2` | 27,973 rows (dataset v1) | 0.842 | 0.808 | 0.096 |
| **v2 (4 Sep 2026)** | `main` | 32,970 rows (dataset v2: + 4,997 active-learning rows) | **0.847** | **0.810** | **0.087** |

Same recipe, same frozen test split. The difference is about 17 headlines
out of 3,500 and within noise; v2 is the release because it is trained on
the larger data and is slightly better calibrated. The two versions agree on
88.7% of test predictions. Load the old one with
`revision="v1-a2"`.

## Usage

```python
from transformers import pipeline
clf = pipeline("text-classification", model="remehostingservices/finbert-finance-news-sentiment")
clf("Oil jumps 4% as Hormuz shipping halted")
# [{'label': 'positive', 'score': 0.99}]   # supply shock → positive for the commodity
```

Labels: `positive`, `negative`, `neutral`. Max length 128 tokens; longer
texts are truncated. The repo also ships `head.pt` (the classifier weights on
their own) for the original training scripts.

## Training

| Setting         | Value                                                        |
|-----------------|--------------------------------------------------------------|
| Base model      | ProsusAI/finbert, new 3-class head on `pooler_output`        |
| Class weights   | sqrt inverse frequency ≈ [pos 1.44, neg 1.20, neu 0.74]       |
| Optimizer / lr  | AdamW, constant 2e-5                                         |
| Epochs / batch  | 3 / 16, max length 128, dynamic padding                      |
| Selection       | best validation macro F1 (epoch 3): val acc 0.848 / F1 0.812 |
| Hardware        | MacBook Air M4 16 GB (MPS), 60 minutes                        |

Warmup + linear decay with 5 epochs gave the same accuracy (0.845 / 0.809 on
dataset v1) but worse calibration (ECE 0.130) and was not released. Training
scripts and the labeling pipeline: [https://github.com/RemeDegen/finance-news-sentiment](https://github.com/RemeDegen/finance-news-sentiment).

## Limitations

Trained on headlines from a few Telegram channels, mostly from one year heavy
on geopolitics, tariffs and Fed policy; expect lower accuracy on other
sources, longer texts, or other periods. The neutral class is broad by design
(routine data prints, statements, small moves). Labels are LLM-generated;
there is no human gold set. Adding 5k hard, model-selected rows (v2) improved
the clean part of the test set slightly and the arbitration-grade part not at
all: accuracy is bounded by label noise, not by data volume.

## Citation

```bibtex
@misc{finbert-finance-news-sentiment,
  title  = {FinBERT fine-tuned on Finance News Sentiment 40k},
  author = {remehostingservices},
  year   = {2026},
  url    = {https://huggingface.co/remehostingservices/finbert-finance-news-sentiment}
}
```

Base model: Araci, D. (2019). *FinBERT: Financial Sentiment Analysis with
Pre-trained Language Models.* arXiv:1908.10063 —
[ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert).
