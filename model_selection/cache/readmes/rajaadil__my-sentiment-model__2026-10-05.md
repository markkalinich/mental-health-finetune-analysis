---
license: apache-2.0
language:
- en
base_model: distilbert-base-uncased
tags:
- text-classification
- sentiment-analysis
- distilbert
datasets:
- stanfordnlp/imdb
metrics:
- accuracy
pipeline_tag: text-classification
widget:
- text: This movie was absolutely fantastic, I loved every minute of it!
- text: A complete waste of time. Boring and poorly made.
---

# my-sentiment-model

A binary sentiment classification model that labels English text as **POSITIVE** or **NEGATIVE**. It is a fine-tuned version of [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) trained on the IMDB movie reviews dataset.

## Model description

The model takes a piece of English text and predicts whether the overall sentiment is positive or negative. It was built by fine-tuning DistilBERT — a smaller, faster distilled version of BERT — on labelled movie reviews, making it lightweight enough to run on CPU while retaining strong accuracy.

- **Base model:** distilbert-base-uncased
- **Task:** Binary sentiment classification (text-classification)
- **Language:** English
- **Labels:** `NEGATIVE` (0), `POSITIVE` (1)

## Intended uses & limitations

**Intended uses:** Quick sentiment scoring of English text such as reviews, comments, and short feedback.

**Limitations:**
- English only — performance on other languages is not reliable.
- Trained on movie reviews, so accuracy is highest on review-style text and may drop on very different domains (e.g. legal, medical, or social media slang).
- Binary output only; it does not detect neutral sentiment, sarcasm, or mixed opinions well.

## How to use

```python
from transformers import pipeline

clf = pipeline("text-classification", model="rajaadil/my-sentiment-model")
print(clf("This movie was absolutely fantastic!"))
# [{'label': 'POSITIVE', 'score': 0.98}]
```

Or load the model and tokenizer directly:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("rajaadil/my-sentiment-model")
model = AutoModelForSequenceClassification.from_pretrained("rajaadil/my-sentiment-model")
```

## Training data

The model was trained on a subset of the [IMDB](https://huggingface.co/datasets/stanfordnlp/imdb) dataset:
- **Training set:** 2,000 reviews
- **Evaluation set:** 1,000 reviews

## Training procedure

| Hyperparameter | Value |
|---|---|
| Base model | distilbert-base-uncased |
| Epochs | 1 |
| Batch size | 8 |
| Max sequence length | 256 |
| Optimizer | AdamW (default) |

## Evaluation results

| Metric | Value |
|---|---|
| Accuracy | 0.869 |

## Framework versions

- Transformers
- PyTorch
- Datasets

## Author

Built by [rajaadil](https://huggingface.co/rajaadil).