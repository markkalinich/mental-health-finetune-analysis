---
license: apache-2.0
language: en
base_model: bert-base-uncased
tags:
  - finance
  - sentiment-analysis
  - text-classification
  - financial-phrasebank
  - bert
datasets:
  - atrost/financial_phrasebank
metrics:
  - f1
  - accuracy
pipeline_tag: text-classification
---

# FinSight FinBERT — Financial Sentiment Classifier

A 3-class financial sentiment classifier (negative / neutral / positive)
fine-tuned from `bert-base-uncased` on the Financial PhraseBank dataset.

Part of the [FinSight](https://github.com/tmuskan/finsight) project — a financial
research AI assistant combining fine-tuned BERT, RAG, and multi-agent systems.

## Performance (test split, sentences_50agree)

| metric | value |
|--------|-------|
| loss | 0.8388 |
| accuracy | 0.8433 |
| f1_macro | 0.8279 |
| f1_weighted | 0.8425 |
| f1_negative | 0.8308 |
| f1_neutral | 0.8789 |
| f1_positive | 0.7741 |

## Training Setup

| Setting | Value |
|--------|-------|
| Base model | `bert-base-uncased` |
| Dataset | `atrost/financial_phrasebank` (sentences_50agree, 64/16/20 split) |
| Train / Val / Test | 3100 / 776 / 970 |
| Epochs | 3 |
| Batch size | 16 |
| Learning rate | 2e-5 (linear warmup over 10% of steps) |
| Weight decay | 0.01 |
| Max sequence length | 128 |
| Optimizer | AdamW (default) |
| Mixed precision | fp16 |
| Seed | 42 |
| Hardware | NVIDIA Tesla T4 (Kaggle) |

## Label mapping

| ID | Label |
|----|-------|
| 0  | negative |
| 1  | neutral |
| 2  | positive |

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="musk1209/finsight-finbert", top_k=None)
clf("The company beat analyst expectations on revenue and profit.")
# [{'label': 'positive', 'score': 0.97}, ...]
```

## Known limitations

- Strong on prototypical patterns ("losses widened", "record revenue") but can
  be fooled by inverted patterns sharing surface form with positive examples —
  e.g. "operating margin contracted from X% to Y%" may be mispredicted as
  positive because the training set's positive examples skew heavily toward
  margin-expansion sentences.
- Trained only on the `sentences_50agree` variant; not validated on the more
  ambiguous sentences excluded from that subset.

## Citation

@article{Malo2014,

title  = {Good debt or bad debt: Detecting semantic orientations in economic texts},

author = {Malo, P. and Sinha, A. and Korhonen, P. and Wallenius, J. and Takala, P.},

journal = {Journal of the Association for Information Science and Technology},

year   = {2014}

}

