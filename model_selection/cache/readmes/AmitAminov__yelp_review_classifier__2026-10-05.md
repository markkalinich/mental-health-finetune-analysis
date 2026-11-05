---
license: apache-2.0
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- reviews
- bert
- yelp
datasets:
- yelp_review_full
base_model: bert-base-cased
thumbnail: https://huggingface.co/AmitAminov/yelp_review_classifier/resolve/main/thumbnail.png
---

<p align="center">
  <img src="https://huggingface.co/AmitAminov/yelp_review_classifier/resolve/main/thumbnail.png" alt="Yelp Review Classifier" width="100%">
</p>

# Yelp Review Classifier

A **BERT-base** model fine-tuned for **5-class review-rating classification** — give it a
free-text review and it predicts a rating from **1 to 5 stars** (the `yelp_review_full`
label scheme).

Built by [**Amit Aminov**](https://huggingface.co/AmitAminov) · [amitaminov.github.io](https://amitaminov.github.io)

## Model at a glance

| | |
|---|---|
| Architecture | `BertForSequenceClassification` — BERT-base (12 layers, hidden 768) |
| Task | Text classification — review rating |
| Classes | 5 &nbsp;(`LABEL_0`…`LABEL_4` = 1★…5★, in `yelp_review_full` order) |
| Max sequence length | 512 tokens |
| Language | English |
| Fine-tuned from | `bert-base-cased` |

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="AmitAminov/yelp_review_classifier")
clf("Incredible food and the service was so warm — we'll be back every week.")
# -> [{'label': 'LABEL_4', 'score': ...}]   # LABEL_4 = 5 stars
```

The raw labels map to stars as `LABEL_0 → 1★, LABEL_1 → 2★, …, LABEL_4 → 5★`.

<details>
<summary>Load the model directly</summary>

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tok = AutoTokenizer.from_pretrained("AmitAminov/yelp_review_classifier")
model = AutoModelForSequenceClassification.from_pretrained("AmitAminov/yelp_review_classifier")
```
</details>

## Intended use & limitations

- **Intended for** rating-style sentiment on English review text (restaurants, businesses,
  and products with a similar 1–5 register).
- Labels are the raw `LABEL_0…LABEL_4` from training — interpret them as 1–5 stars.
- Very short snippets, non-review language, or other languages will be less reliable, and —
  as with any sentiment model — predictions can reflect biases in the training data.

## Training

Fine-tuned with the 🤗 Transformers `Trainer` on the
[`yelp_review_full`](https://huggingface.co/datasets/yelp_review_full) dataset (5-star
reviews). Held-out evaluation metrics were not recorded in this repository; if you need
them, re-run evaluation on the `yelp_review_full` test split.

---
<sub>Part of <a href="https://amitaminov.github.io">Amit Aminov</a>'s public work.</sub>
