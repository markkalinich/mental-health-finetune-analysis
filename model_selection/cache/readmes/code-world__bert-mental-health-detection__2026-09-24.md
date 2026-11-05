---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: google-bert/bert-base-uncased
tags:
- mental-health
- text-classification
- bert
- social-media
metrics:
- accuracy
- f1
---

# BERT for Early Detection of Mental Health Disorders from Social Media Text

Fine-tuned `bert-base-uncased` for 5-class mental health classification of social media posts.
Developed as part of a COM748 Masters Research Project: *Explainable Transformer Based Framework
for Early Detection of Mental Health Disorders from Social Media Text*.

## Classes

| ID | Label |
|---|---|
| 0 | Anxiety/Stress |
| 1 | Bipolar |
| 2 | Depression |
| 3 | Normal |
| 4 | Suicidal |

## Performance (held-out test set, n = 7,106)

| Metric | Score |
|---|---|
| Accuracy | **83.4%** |
| Macro F1 | **0.841** |

Per-class F1: Normal 0.953 · Anxiety/Stress 0.882 · Bipolar 0.858 · Depression 0.770 · Suicidal 0.742

For comparison, the same encoder used as a frozen feature extractor reached only 0.680 macro-F1,
and a TF-IDF + XGBoost baseline reached 0.775.

## Training data

~47,400 posts merged from two public Kaggle datasets:
[Sentiment Analysis for Mental Health](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health)
and [Depression: Reddit Dataset (Cleaned)](https://www.kaggle.com/datasets/infamouscoder/depression-reddit-cleaned),
deduplicated and mapped to 5 classes, split 70/15/15.

## Training setup

- 3 epochs, batch size 16, max length 128, AdamW lr 2e-5, weight decay 0.01
- Linear warmup (10%) then linear decay, gradient clipping at 1.0
- Class-weighted cross-entropy to counter class imbalance
- Best checkpoint selected by validation macro-F1

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="usman-isb/bert-mental-health-detection")
print(clf("lately I cannot stop worrying about everything, my heart races all day"))
```

## Intended use & limitations

⚠️ **Research prototype only.** This model is not a clinical diagnostic instrument and must not
be used as a substitute for professional mental health assessment. Labels reflect patterns in
self-reported social media text, not clinical diagnoses. Performance on text from other platforms,
languages, or demographics is untested.
