---
language:
- cs
license: cc-by-4.0
tags:
- text-classification
- sentiment-analysis
- czech
- electra
datasets:
- fewshot-goes-multilingual/cs_csfd-movie-reviews
metrics:
- accuracy
- f1
model-index:
- name: cs-sentiment-small-e-czech-v2
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: CSFD Movie Reviews
      type: fewshot-goes-multilingual/cs_csfd-movie-reviews
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6772
    - name: F1 (macro)
      type: f1
      value: 0.4875
    - name: F1 (weighted)
      type: f1
      value: 0.6187
pipeline_tag: text-classification
---

# Czech Sentiment Classifier — Small-E-Czech (ELECTRA)

A **3-class sentiment classifier** for Czech movie reviews, fine-tuned from [Seznam/small-e-czech](https://huggingface.co/Seznam/small-e-czech) (13.5M params, Czech ELECTRA).

## Quick Start

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="jakubmach/cs-sentiment-small-e-czech-v2")
result = classifier("Tento film byl naprosto úžasný, skvělí herci a výborný příběh!")
print(result)  # [{'label': 'positive', 'score': 0.87}]
```

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | Seznam/small-e-czech (13.5M params) |
| Dataset | [fewshot-goes-multilingual/cs_csfd-movie-reviews](https://huggingface.co/datasets/fewshot-goes-multilingual/cs_csfd-movie-reviews) |
| Training samples | 2,000 (from 25K total) |
| Epochs | 5 |
| Learning rate | 1e-4 |
| Batch size | 16 |
| Max sequence length | 256 tokens |
| Scheduler | Cosine with 50 warmup steps |
| Weight decay | 0.01 |
| Hardware | CPU (2 vCPU, 16GB RAM) |
| Training time | ~2 hours |

### Label Mapping

Ratings from CSFD (0-5 stars) mapped to sentiment:
- **negative**: ratings 0, 1, 2
- **neutral**: rating 3
- **positive**: ratings 4, 5

## Results

### Test Set Performance (2,500 samples)

| Method | Accuracy | F1 (macro) | F1 (weighted) |
|--------|----------|------------|---------------|
| Random baseline | 33.3% | 0.315 | 0.349 |
| Majority class (negative) | 49.6% | 0.221 | 0.329 |
| Keyword heuristic | 33.3% | 0.336 | 0.344 |
| **Exp 1** (lr=5e-5, 3ep, 1.5K samples) | 60.8% | 0.421 | 0.542 |
| **Exp 2 (this model)** (lr=1e-4, 5ep, 2K samples) | **67.7%** | **0.488** | **0.619** |

### Per-Class Breakdown

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| positive | 0.586 | 0.799 | 0.676 | 844 |
| negative | 0.755 | 0.821 | 0.787 | 1,241 |
| neutral | 0.000 | 0.000 | 0.000 | 415 |

### Confusion Matrix

|  | Pred: positive | Pred: negative | Pred: neutral |
|---|---|---|---|
| **Gold: positive** | 674 | 170 | 0 |
| **Gold: negative** | 222 | 1,019 | 0 |
| **Gold: neutral** | 254 | 161 | 0 |

## Key Observations

1. **Strong binary sentiment detection**: The model reliably distinguishes positive from negative reviews (positive F1=0.68, negative F1=0.79).
2. **Neutral class not learned**: With only ~320 neutral examples in training and the class being inherently ambiguous (3/5 rating), the model never predicts "neutral." This is the main area for improvement.
3. **Data efficiency**: Even with just 2,000 training samples (8% of the full dataset), the model achieves 67.7% accuracy — significantly above all baselines.
4. **Improvement path**: Training on the full 25K dataset with GPU, or using a larger encoder (e.g., `ufal/robeczech-base` at 125M params), would likely push accuracy well above 75%.

## Limitations

- Does not predict the "neutral" class (3-star reviews are classified as positive or negative)
- Trained on only 2,000 of 25,000 available samples due to CPU training constraints
- Reviews longer than 256 tokens are truncated
- Domain-specific to movie reviews; may not generalize to other Czech text domains

## License

CC-BY-4.0 (inherited from base model Seznam/small-e-czech)
