---
language: en
license: mit
tags:
- aspect-based-sentiment-analysis
- sentiment-analysis
- distilbert
datasets:
- tomaarsen/setfit-absa-semeval-restaurants
metrics:
- accuracy
- f1
---

# AspectLens DistilBERT ABSA Classifier

This model is a fine-tuned `distilbert-base-uncased` sequence classifier for aspect-conditioned sentiment classification on restaurant review aspects.

Input format:

```text
review: The food was excellent, but the service was slow. [SEP] aspect: service
```

Labels:

- negative
- neutral
- positive
- conflict

Held-out evaluation results from the project split:

| Metric | Score |
|---|---:|
| Accuracy | 0.783 |
| Macro-F1 | 0.541 |
| Weighted-F1 | 0.771 |

The model was created for the PROG74040 Phase II course project prototype. The rare `conflict` class remains the weakest class due to limited support.
