---
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- imdb
- distilbert
datasets:
- stanfordnlp/imdb
base_model: distilbert/distilbert-base-uncased
metrics:
- accuracy
- f1
model-index:
- name: DistilBERT IMDb Sentiment Classifier
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: IMDb
      type: stanfordnlp/imdb
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9114
    - name: F1
      type: f1
      value: 0.9115
---

# DistilBERT IMDb Sentiment Classifier

This model is a fine-tuned version of
[`distilbert-base-uncased`](https://huggingface.co/distilbert/distilbert-base-uncased)
for binary sentiment classification of English IMDb movie reviews. It predicts
either `NEGATIVE` or `POSITIVE`.

The uploaded checkpoint is the seed-42 model, selected because it achieved the
highest validation accuracy among three independently trained seeds.

## Model details

| Item | Value |
| --- | --- |
| Architecture | DistilBERT for sequence classification |
| Parameters | 66,955,010 |
| Language | English |
| Classes | `NEGATIVE`, `POSITIVE` |
| Maximum input length | 256 tokens |
| Framework | PyTorch / Transformers |
| Base model | `distilbert/distilbert-base-uncased` |

## Intended use

The model is intended for educational experiments and binary sentiment
classification of English movie reviews. It can be used through the
Transformers pipeline:

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Saana2005/distilbert-imdb-sentiment-classifier",
)

result = classifier(
    "The movie was emotional, engaging, and beautifully acted.",
    truncation=True,
    max_length=256,
)
print(result)
```

## Training data

The model was trained with the
[`stanfordnlp/imdb`](https://huggingface.co/datasets/stanfordnlp/imdb)
dataset.

| Split | Examples | Purpose |
| --- | ---: | --- |
| Training | 20,000 | Parameter updates |
| Validation | 5,000 | Best-checkpoint selection |
| Test | 25,000 | Final evaluation |
| Unsupervised | 50,000 | Not used |

The official 25,000-example training split was divided with fixed split seed
`2026`. The official test split was kept separate from model training and
checkpoint selection.

## Training procedure

| Hyperparameter | Value |
| --- | --- |
| Epochs | 2 |
| Training batch size | 32 |
| Evaluation batch size | 64 |
| Learning rate | `2e-5` |
| Weight decay | `0.01` |
| Warmup | 10% of training steps |
| Optimizer | AdamW |
| Scheduler | Linear decay |
| Precision | FP16 |
| Random seed | 42 |
| Selection metric | Validation accuracy |

## Evaluation

The uploaded seed-42 checkpoint produced:

| Metric | Result |
| --- | ---: |
| Best validation accuracy | 91.44% |
| Test accuracy | 91.14% |
| Test F1 | 91.15% |

Three runs with seeds 7, 42, and 123 achieved mean test accuracy of
**91.16% ± 0.02%** and mean test F1 of **91.21% ± 0.07%** (sample standard
deviation).

## Limitations

- The model handles only two sentiment classes and cannot represent neutral or
  mixed sentiment directly.
- It was trained on English movie reviews and is not a general-purpose emotion
  or opinion classifier.
- Inputs longer than 256 tokens are truncated, so important conclusions near
  the end of a long review may be omitted.
- Sarcasm, conflicting opinions, plot-heavy language, and annotation noise can
  cause errors.
- Confidence scores are model probability estimates, not guarantees that a
  prediction is correct.
- The model may inherit biases present in its pretrained model and IMDb data.

## Source code

Training, evaluation, error-analysis, Slurm, command-line inference, and Gradio
code are available in the
[`Sana1025/distilbert-imdb-sentiment-classifier`](https://github.com/Sana1025/distilbert-imdb-sentiment-classifier)
GitHub repository.
