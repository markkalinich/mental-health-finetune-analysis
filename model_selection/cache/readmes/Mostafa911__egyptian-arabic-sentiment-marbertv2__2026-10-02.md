---
language: ar
library_name: transformers
pipeline_tag: text-classification
base_model: UBC-NLP/MARBERTv2
datasets:
- iabufarha/ar_sarcasm
metrics:
- f1
tags:
- arabic
- egyptian-arabic
- sentiment-analysis
---

# Egyptian Arabic Sentiment (fine-tuned MARBERTv2)

Three-class sentiment classifier (negative / neutral / positive) for Egyptian-dialect tweets. It is [UBC-NLP/MARBERTv2](https://huggingface.co/UBC-NLP/MARBERTv2) fine-tuned on the Egyptian subset of [ArSarcasm](https://huggingface.co/datasets/iabufarha/ar_sarcasm).

Live demo: https://huggingface.co/spaces/Mostafa911/egyptian-arabic-sentiment-demo

## Results on the Egyptian test set (479 tweets)

| Model | Macro F1 |
|---|---|
| TF-IDF + Logistic Regression baseline | 0.545 |
| This model (best of 3 seeds, picked on validation) | 0.737 |
| This model, mean +/- std over 3 seeds | 0.744 +/- 0.012 |

By subset (best model):

| Subset | Tweets | Baseline | This model |
|---|---|---|---|
| Non-sarcastic | 325 | 0.531 | 0.741 |
| Sarcastic | 154 | 0.342 | 0.471 |

Sarcastic tweets are about 88% negative in the training data, so the neutral and positive classes inside that subset are tiny and its macro F1 is noisy. Accuracy on the sarcastic subset was about 77%.

## Training

- Data: Egyptian-dialect tweets from the ArSarcasm training split (1,904 tweets before removing duplicates), 10% held out for validation.
- Light cleaning only: URLs and mentions removed, hashtag symbols removed.
- Learning rate 2e-5, batch size 16, 5 epochs, max length 64, weighted cross-entropy for class imbalance, best epoch chosen by validation macro F1.
- Three random seeds; the released model is the seed with the best validation macro F1.
- An extra experiment training on all dialects gave 0.737 +/- 0.011 on the same Egyptian test set, so it did not clearly help.

## Limitations

- Small training set and a small test set, so scores move by a point or two between runs.
- About 60% of the errors are confusions between neutral and negative.
- Sarcasm is often missed, for example literal praise that is meant mockingly.
- Some labels in the source dataset are ambiguous or noisy.
- Not for decisions that affect people. Check the licenses of the base model and the dataset before any commercial use.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Mostafa911/egyptian-arabic-sentiment-marbertv2")
print(clf("الخدمة وحشة جدا ومش هرجع تاني"))
```
