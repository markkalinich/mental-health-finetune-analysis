---
license: apache-2.0
base_model: microsoft/deberta-v3-base
tags:
  - financial-sentiment
  - sentiment-analysis
  - deberta-v3
  - transformers
  - text-classification
datasets:
  - nickmuchi/financial-classification
  - zeroshot/twitter-financial-news-sentiment
metrics:
  - f1
  - accuracy
pipeline_tag: text-classification
language:
  - en
---

# finsentiment-deberta-v3-base

Fine-tuned `microsoft/deberta-v3-base` for three-class financial sentiment classification
(`negative` / `neutral` / `positive`) on a combined corpus of:

- **Financial PhraseBank** (via the `nickmuchi/financial-classification` mirror)
- **Twitter Financial News Sentiment** (`zeroshot/twitter-financial-news-sentiment`)

Test macro-F1: **0.876** (accuracy 0.892, ECE 0.034).

## Evaluation

| Metric | Fine-tuned | FinBERT (zero-shot) |
|---|:---:|:---:|
| macro-F1 | 0.876 | 0.731 |
| accuracy | 0.892 | 0.765 |
| F1 (negative) | 0.858 | 0.661 |
| F1 (neutral) | 0.914 | 0.819 |
| F1 (positive) | 0.856 | 0.712 |
| Expected Calibration Error | 0.034 | 0.075 |

Evaluation was run on a stratified 10% test split of the combined corpus
(seed 42), with `ProsusAI/finbert` as a zero-shot domain-pretrained baseline.

## How to use

```python
from transformers import pipeline

clf = pipeline("text-classification", model="anabdd/finsentiment-deberta-v3-base", top_k=None)
clf("Apple beat earnings expectations on iPhone strength.")
# → [{'label': 'positive', 'score': 0.97}, ...]
```

## Training details

Trained with `Trainer` (HuggingFace `transformers >= 4.46`) using:

- Class-weighted cross-entropy loss (sklearn `balanced` weighting on the
  training split)
- Label smoothing (factor 0.05)
- Cosine LR schedule with 10% warmup
- Mixed-precision (fp16) on a single NVIDIA T4 GPU

See the [project repository](https://github.com/) for the full training script
(`src/train.py`) and the analysis notebook.

## Intended use & limitations

Designed for short-form financial English text (headlines, tweets, brief
analyst notes). It has *not* been trained for:

- Languages other than English
- Long-form financial documents (10-Ks, earnings call transcripts)
- Fine-grained sentiment beyond three classes

Labels follow the `nickmuchi/financial-classification` mirror's convention,
which is itself derived from the original PhraseBank annotation scheme.
