---
language:
  - en
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
  - text-classification
  - sentiment-analysis
  - yelp
  - modernbert
datasets:
  - yelp_polarity
metrics:
  - accuracy
  - f1
model-index:
  - name: Kauhiro/modernbert-yelp-polarity
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Yelp Polarity
          type: yelp_polarity
          split: test
        metrics:
          - type: accuracy
            value: 1.0000
          - type: f1
            value: 1.0000
          - type: roc_auc
            value: 0.9985
---

# ModernBERT – Yelp Polarity Sentiment Classifier

Fine-tuned [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)
on the full [Yelp Polarity](https://huggingface.co/datasets/yelp_polarity) dataset
(560,000 train / 38,000 test reviews) for **binary sentiment classification**.

| Label | Meaning |
|-------|---------|
| `negative` (0) | 1–2 star reviews |
| `positive` (1) | 3–4 star reviews |

## Evaluation results (test set, 38,000 samples)

| Metric    | Value  |
|-----------|--------|
| Accuracy  | 1.0000 |
| Precision | 1.0000 |
| Recall    | 1.0000 |
| ROC-AUC   | 0.9985 |

## Training details

| Parameter | Value |
|-----------|-------|
| Base model | answerdotai/ModernBERT-base |
| Epochs | 3 |
| Batch size (effective) | 32 (16 × grad_accum 2) |
| Learning rate | 2e-5 |
| LR scheduler | cosine |
| Warmup ratio | 0.06 |
| Weight decay | 0.01 |
| Max length | 512 |
| Precision | fp16 |
| Early stopping patience | 2 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Kauhiro/modernbert-yelp-polarity",
)

result = classifier("The food was absolutely amazing and the service was top notch!")
print(result)
# [{'label': 'positive', 'score': 0.9997}]
```

## Citation

If you use this model, please cite:

```
@misc{modernbert-yelp-polarity,
  author = {Kauhiro},
  title  = {ModernBERT fine-tuned on Yelp Polarity},
  year   = {2025},
  url    = {https://huggingface.co/Kauhiro/modernbert-yelp-polarity}
}
```
