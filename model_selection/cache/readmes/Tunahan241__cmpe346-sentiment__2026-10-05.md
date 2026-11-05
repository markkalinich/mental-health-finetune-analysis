---
library_name: transformers
license: mit
language:
- multilingual
- en
- zh
- ja
- fr
- de
- es
- ru
- ko
- ar
- vi
- tr
- pt
- id
- hi
- ms
- it
pipeline_tag: text-classification
tags:
- sentiment-analysis
- multilingual
- xlm-roberta
- binary-classification
- text-classification
base_model: xlm-roberta-base
metrics:
- f1
- accuracy
---

# Multilingual Binary Sentiment Classifier (XLM-RoBERTa)

Fine-tuned [`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base) for
**binary sentiment classification** (positive / negative) across **17
languages**. Built for the CMPE 346 (Natural Language Processing)
Assignment 02 at İstanbul Bilgi University.

## Quick start

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Tunahan241/cmpe346-sentiment")

clf("This product changed my life, absolutely love it!")
# [{'label': 'LABEL_1', 'score': 0.998}]   # LABEL_1 = positive

clf("Très déçu, ne fonctionne pas du tout.")
# [{'label': 'LABEL_0', 'score': 0.995}]   # LABEL_0 = negative

clf("非常满意,推荐购买!")
# [{'label': 'LABEL_1', 'score': 0.992}]   # LABEL_1 = positive
```

Label mapping:

| Label   | Sentiment |
|---------|-----------|
| LABEL_0 | negative  |
| LABEL_1 | positive  |

## Performance

Evaluated on a held-out validation set of **17 500** multilingual reviews:

| Metric   | Score   |
|----------|---------|
| **F1**   | **0.9175** |
| Accuracy | 0.918   |

For comparison, the baseline F1 cited in the assignment is **0.7958** — this
model exceeds it by **+0.12 absolute** (+15 % relative).

## Languages

Trained on data spanning these languages (train-set frequency):

| Language   | Code | Samples |
|------------|------|--------:|
| English    | en   |  51 989 |
| Chinese    | zh   |  15 430 |
| Japanese   | ja   |  11 974 |
| French     | fr   |  10 549 |
| Spanish    | es   |   8 484 |
| Russian    | ru   |   8 477 |
| German     | de   |   8 171 |
| Korean     | ko   |   7 881 |
| Arabic     | ar   |   5 998 |
| Vietnamese | vi   |   5 761 |
| Turkish    | tr   |   2 205 |
| Portuguese | pt   |   1 521 |
| Indonesian | id   |     531 |
| Multilingual mixed | multilingual | 405 |
| Hindi      | hi   |     277 |
| Malay      | ms   |     250 |
| Italian    | it   |      97 |

Total: **140 000** training reviews.

## Training details

### Base model
[`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base) — 270 M-parameter
multilingual masked language model pretrained on CC-100 across 100
languages. A single linear classification head is added on top of the
`<s>` (CLS) token.

### Hyperparameters

| Setting              | Value                |
|----------------------|----------------------|
| Optimizer            | AdamW                |
| Learning rate        | 2e-5                 |
| Weight decay         | 0.01                 |
| Warmup ratio         | 0.1 (linear)         |
| LR schedule          | Linear decay         |
| Epochs               | 3                    |
| Batch size           | 32 per device        |
| Max sequence length  | 256                  |
| Mixed precision      | fp16                 |
| Early stopping       | patience = 2 on val F1 |
| Best-model selection | by validation F1     |

### Compute
* 1 × NVIDIA T4 GPU (Google Colab free tier)
* ~85 minutes wall-clock for 3 epochs on 140 000 samples

### Preprocessing
Multilingual-safe minimal cleaning:
* NFKC Unicode normalization (unifies full/half-width forms)
* URL and HTML tag stripping
* Whitespace collapse
* **No lowercasing** and **no accent stripping** — preserves signal in
  non-Latin scripts (CJK, Cyrillic, Arabic, Devanagari, etc.).

Tokenization is handled by the pretrained XLM-R SentencePiece tokenizer
(250 002 subword vocabulary, 100 languages).

## Intended use

* Multilingual product / review / short-text sentiment classification.
* Cross-lingual transfer to the 100 languages XLM-R was pretrained on
  (zero-shot to languages not in the fine-tuning set is plausible but
  not benchmarked here).

## Limitations

* The training distribution is dominated by English, Chinese, Japanese
  and Romance languages. Performance on under-represented languages
  (Italian: 97 samples; Hindi: 277 samples) is less reliable.
* Trained on review-style text; performance on long-form articles,
  formal documents, or strongly domain-specific text (legal, medical)
  is not guaranteed.
* Binary only — does not capture neutral, mixed, or fine-grained
  sentiment.

## Citation

This model was developed as a course assignment:

* CMPE 346 — Natural Language Processing
* Assignment 02 — Multilingual Binary Sentiment Classification
* İstanbul Bilgi University, 2026

## Author

Tunahan İbiş
