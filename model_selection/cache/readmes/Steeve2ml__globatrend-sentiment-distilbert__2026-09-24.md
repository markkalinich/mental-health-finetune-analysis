---
pipeline_tag: text-classification
widget:
  - text: "This product exceeded my expectations!"
  - text: "Terrible service, I want a refund."
  
library_name: transformers
language: en
license: mit
tags:
  - sentiment-analysis
  - text-classification
  - distilbert
datasets:
  - nltk-movie-reviews
metrics:
  - accuracy
  - f1
base_model: distilbert-base-uncased
---

# Model Card for globatrend-sentiment-distilbert

## Model Details

### Model Description

DistilBERT fine-tuned for binary sentiment classification (positive /
negative) on movie reviews. Built as part of my **GlobaTrend Insights**,
a portfolio project covering the full modern NLP pipeline — from
classical ML to Transformers to multilingual Aspect-Based Sentiment
Analysis. This model is the project's first fine-tuned Transformer
used as a baseline sentiment classifier
before the multilingual ABSA models built in later phases.

- **Developed by:** Independent portfolio project (GlobaTrend
  Insights)
- **Model type:** Transformer encoder (DistilBERT), sequence
  classification head
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** `distilbert-base-uncased`

### Model Sources

- **Base model:** https://huggingface.co/distilbert-base-uncased
- **Project roadmap:** NLP learning project, from text
  cleaning through classical ML, deep learning, Transformers,
  multilingual NLP, and Aspect-Based Sentiment Analysis.

## Uses

### Direct Use

Binary sentiment classification (positive/negative) of English movie
reviews or similarly-styled long-form English text. Suitable for
quick sentiment scoring where a coarse positive/negative label is
sufficient.

### Downstream Use

Intended as a baseline / building block for the project's later
Aspect-Based Sentiment Analysis work (Phase 9), where sentiment is
predicted per aspect rather than for a whole document.

### Out-of-Scope Use

- **Not multilingual** — trained and evaluated on English only; do
  not use on Spanish, German, Hindi, or French text (see the
  project's multilingual models from Phase 8 instead).
- **Not aspect-level** — gives one sentiment label for the whole
  text, not per-aspect (delivery, price, etc.) — see Phase 9 models
  for that.
- **Not validated on e-commerce reviews** — trained on movie reviews
  (Pang & Lee corpus), which differ in style and vocabulary from
  product/service reviews. Performance on e-commerce text is
  untested.
- Not intended for high-stakes decisions (moderation, legal, medical)
  without further validation.

## Bias, Risks, and Limitations

- **Training-data bias (verified empirically):** analysis of a
  Naive Bayes baseline on the same corpus showed the model can learn
  associations with actor/director names (e.g. certain names
  correlating with negative reviews in this specific corpus) rather
  than pure sentiment language. The same risk applies here, since the
  underlying training data is identical.
- **Length truncation:** reviews in the training corpus average ~746
  words; this model was fine-tuned with `max_length=512` tokens, so
  longer reviews are truncated and information near the end of long
  reviews may be lost.
- **Small fine-tuning set:** fine-tuned on 1,600 examples only (400
  held out for evaluation) — a small dataset by Transformer
  standards. Performance on out-of-domain text should be validated
  before production use.

### Recommendations

Users should validate performance on their own domain (e.g.
e-commerce reviews) before relying on this model, and should not
assume the sentiment label reflects a specific aspect of a review
rather than its overall tone.

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Steeve2ml/globatrend-sentiment-distilbert",
)
classifier("This movie was absolutely fantastic, a must-see.")
```

## Training Details

### Training Data

[NLTK Movie Reviews corpus](https://www.nltk.org/nltk_data/) (Pang &
Lee, 2004): 2,000 movie reviews, 1,000 positive / 1,000 negative,
human-labeled by original review rating. Split 1,600 train / 400 test
(80/20, stratified).

### Training Procedure

#### Preprocessing

Tokenized with the `distilbert-base-uncased` WordPiece tokenizer,
`max_length=512`, truncation and padding enabled.

#### Training Hyperparameters

- **Base model:** distilbert-base-uncased (~67M parameters)
- **Epochs:** 3
- **Learning rate:** 2e-5
- **Batch size:** 16 (train and eval)
- **Optimizer:** AdamW (Hugging Face `Trainer` default)

## Evaluation

### Testing Data

Held-out split of the same NLTK Movie Reviews corpus: 400 reviews
(200 positive / 200 negative), never seen during training.

### Metrics

Accuracy and F1-score (binary, positive class).

### Results

| Configuration | Accuracy |
|---|---|
| `max_length=256`, 2 epochs | 0.757 |
| `max_length=512`, 3 epochs | **0.818** |

For reference, other models trained on the same data split within
this project:

| Model | Accuracy |
|---|---|
| Linear SVM (TF-IDF) | 0.835 |
| **DistilBERT (this model)** | **0.818** |
| CNN + GloVe embeddings | 0.630 |

#### Summary

Increasing `max_length` from 256 to 512 tokens improved accuracy by
+6.1 points, confirming that truncation (98% of reviews exceed 256
words) was the main limiting factor in the first fine-tuning attempt.
The final model performs close to (within ~2 points of) a simple
linear SVM baseline trained on the same 1,600 examples — a
notable result given the SVM sees the full, untruncated text while
this model still only sees the first 512 tokens.