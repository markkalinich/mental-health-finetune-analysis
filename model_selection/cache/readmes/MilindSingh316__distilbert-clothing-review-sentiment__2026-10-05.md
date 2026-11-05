---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- sentiment-analysis
---

# Clothing Review Sentiment Classifier

Fine-tuned DistilBERT for 3-class sentiment classification (negative/neutral/positive)
on ~48k clothing reviews from Kaggle ("Consumer Review of Clothing", Jocelyn Dumlao).

## Results (test set, n=9,659)

| Model | Macro F1 | Accuracy |
|---|---|---|
| TF-IDF + Logistic Regression (baseline) | 0.68 | 0.82 |
| DistilBERT (this model) | 0.72 | 0.84 |

## Error analysis

Most errors occur at class boundaries, particularly 4-star reviews predicted as neutral.
72% of these errors are 4-star reviews, and 76% contain contrast words ("but", "however")
vs 36% of correctly classified positives — suggesting the model is reasonably picking up
on genuinely mixed sentiment (praise + a caveat) rather than making random mistakes.
Some errors likely trace to label noise (e.g. reviews describing returns or damage rated 4-5 stars).

## Labels
0 = negative, 1 = neutral, 2 = positive

## Training
- Base model: distilbert-base-uncased
- 3 epochs, best checkpoint at epoch 2 (by validation macro F1)
- Class-weighted loss to handle imbalance (74% positive / 15% negative / 11% neutral)
- max_length=128, learning_rate=2e-5, batch_size=32
