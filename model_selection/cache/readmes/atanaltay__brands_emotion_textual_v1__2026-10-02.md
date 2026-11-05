---
language:
- tr
license: mit
base_model: dbmdz/bert-base-turkish-128k-uncased
tags:
- text-classification
- emotion-classification
- turkish
- bert
- social-media
pipeline_tag: text-classification
widget:
- text: "Bugün harika bir gün geçirdim, çok mutluyum 😊"
---

# Turkish Social Media Emotion Classifier (BERTurk fine-tuned)

A fine-tuned version of [`dbmdz/bert-base-turkish-128k-uncased`](https://huggingface.co/dbmdz/bert-base-turkish-128k-uncased) for **7-class emotion classification** of Turkish (and mixed Turkish/English) social media text.

## Labels

The model predicts one of 7 basic emotion categories (Ekman's basic emotions + neutrality):

| Label | Description |
|---|---|
| `happiness` | Joy, gratitude, positive appreciation |
| `surprise` | Shock, disbelief, unexpectedness |
| `sadness` | Grief, sorrow |
| `anger` | Frustration, criticism, hostility |
| `fear` | Anxiety, worry, distress |
| `disgust` | Revulsion, contempt |
| `neutral` | No dominant emotional content |

## Training Data

The model was fine-tuned on a semi-supervised training set of Turkish/English social media messages (brand posts and user comments), weakly labeled via emoji co-occurrence with emotion lexicons (Turkish Emotion Lexicon and NRC Emotion Lexicon). The training corpus is heavily imbalanced toward happiness, reflecting the natural distribution of emoji-labeled social media content:

| Label | N | % |
|---|---:|---:|
| Happiness | 68,977 | 66.5 |
| Anger | 11,156 | 10.8 |
| Surprise | 7,349 | 7.1 |
| Fear | 6,279 | 6.0 |
| Sadness | 5,785 | 5.6 |
| Disgust | 3,322 | 3.2 |
| Neutrality | 919 | 0.9 |
| **Total** | **103,787** | **100.0** |

## Training Procedure

Fine-tuned for 5 epochs with a 15% held-out validation split.

| Epoch | Training Loss | Validation Loss | Accuracy | Macro F1 |
|---|---|---|---|---|
| 1 | 0.6537 | 0.5061 | 0.8307 | 0.7377 |
| 2 | 0.4716 | 0.4775 | 0.8370 | 0.7487 |
| 3 | 0.4251 | 0.4842 | 0.8354 | 0.7492 |
| 4 | 0.3907 | 0.4846 | 0.8372 | 0.7568 |
| 5 | 0.3674 | 0.4937 | 0.8352 | 0.7547 |

## Evaluation Results

Evaluated on a held-out 15% test split (n=15,569):

| Label | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Anger | 0.61 | 0.72 | 0.66 | 1,674 |
| Disgust | 0.97 | 0.83 | 0.90 | 498 |
| Fear | 0.79 | 0.55 | 0.65 | 942 |
| Happy | 0.88 | 0.94 | 0.91 | 10,347 |
| Neutral | 0.90 | 0.94 | 0.92 | 138 |
| Sad | 0.87 | 0.67 | 0.76 | 867 |
| Surprise | 0.75 | 0.45 | 0.56 | 1,103 |
| **Accuracy** | | | **0.84** | 15,569 |
| **Macro avg** | 0.82 | 0.73 | 0.77 | 15,569 |
| **Weighted avg** | 0.84 | 0.84 | 0.83 | 15,569 |

Model performance is strongest on the majority `happy` class and the (small-support) `disgust` and `neutral` classes, and weaker on `surprise` and `fear`, largely reflecting class imbalance in the weakly-labeled training data.

## Intended Use

This model classifies the dominant emotion in Turkish-language social media text, including brand posts and user replies/comments. It may generalize to other Turkish social media sentiment/emotion tasks depending on domain similarity.

**Limitations:** Training labels were derived automatically from emoji co-occurrence rather than human annotation, so label noise is present. Performance on minority classes (`fear`, `surprise`) is comparatively weaker.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "<your-username>/<model-repo-name>"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
classifier("Bugün harika bir gün geçirdim, çok mutluyum 😊")
```

## Base Model

This model was fine-tuned from [`dbmdz/bert-base-turkish-128k-uncased`](https://huggingface.co/dbmdz/bert-base-turkish-128k-uncased) (BERTurk), a Turkish BERT model trained by MDZ Digital Library team at the Bavarian State Library.
