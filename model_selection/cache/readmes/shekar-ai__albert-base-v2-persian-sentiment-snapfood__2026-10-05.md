---
library_name: transformers
license: mit
language:
- fa
base_model: shekar-ai/albert-base-v2-persian-zwnj-naab-mlm
pipeline_tag: text-classification
tags:
- persian
- farsi
- sentiment-analysis
- albert
metrics:
- accuracy
model-index:
- name: albert-base-v2-persian-sentiment-snapfood
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Snappfood
      type: snappfood
      split: validation
    metrics:
    - type: accuracy
      value: 0.8717
---

# ALBERT Persian Sentiment (Snappfood)

Binary sentiment classifier for Persian, fine-tuned from
[`shekar-ai/albert-base-v2-persian-zwnj-naab-mlm`](https://huggingface.co/shekar-ai/albert-base-v2-persian-zwnj-naab-mlm)
on the Snappfood corpus of Persian food-delivery reviews.

| | |
|---|---|
| Task | Sequence classification (`NEGATIVE` / `POSITIVE`) |
| Parameters | 11.9 M |
| Base model | `shekar-ai/albert-base-v2-persian-zwnj-naab-mlm` |
| Training data | Snappfood reviews (~56.7k) |
| License | MIT |

## Usage

### Shekar

```python
from shekar import SentimentClassifier

classifier = SentimentClassifier()
print(classifier("غذا عالی بود و خیلی سریع رسید."))
print(classifier("کیفیت غذا افتضاح بود و سرد به دستم رسید."))
```

```text
('positive', 0.9934062957763672)
('negative', 0.9793806672096252)
```

### Transformers

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="shekar-ai/albert-base-v2-persian-sentiment-snapfood",
)

for prediction in classifier([
    "غذا عالی بود و خیلی سریع رسید.",
    "کیفیت غذا افتضاح بود و سرد به دستم رسید.",
]):
    print(prediction["label"], round(prediction["score"], 4))
```

```text
POSITIVE 0.9957
NEGATIVE 0.9768
```

## Training

**Data.** The Snappfood sentiment dataset — user reviews of a Persian food-delivery service,
labeled `HAPPY` / `SAD` and mapped to `POSITIVE` / `NEGATIVE`. Roughly 56.7k reviews for training
and 6.3k held out for validation.

| Hyperparameter | Value |
|---|---|
| Epochs | 3 |
| Batch size | 32 |
| Learning rate | 2e-5 |
| LR scheduler | Linear |
| Optimizer | AdamW |

## Evaluation

On the held-out validation split (~6.3k reviews):

| Metric | Value |
|---|---|
| Accuracy | 87.17 |
| Loss | 0.3227 |

<details>
<summary>Validation during training</summary>

| Step | Epoch | Training loss | Validation loss | Accuracy |
|---:|---:|---:|---:|---:|
| 1000 | 0.56 | 0.3303 | 0.3198 | 0.8678 |
| 2000 | 1.13 | 0.2854 | 0.3087 | 0.8697 |
| 3000 | 1.69 | 0.2688 | 0.3055 | 0.8752 |
| 4000 | 2.26 | 0.2354 | 0.3158 | 0.8733 |
| 5000 | 2.82 | 0.2226 | 0.3227 | 0.8717 |

</details>

## Citation

```bibtex
@article{Amirivojdan2025Shekar,
  author  = {Amirivojdan, Ahmad},
  title   = {{Shekar: A Python Toolkit for Persian Natural Language Processing}},
  journal = {Journal of Open Source Software},
  volume  = {10},
  number  = {114},
  pages   = {9128},
  year    = {2025},
  doi     = {10.21105/joss.09128},
  url     = {https://joss.theoj.org/papers/10.21105/joss.09128}
}
```
