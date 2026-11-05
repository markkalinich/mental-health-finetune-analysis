
---
language: ru
tags:
- text-classification
- multi-label-classification
- emotion-detection
- russian
datasets:
- sagteam/cedr_v1
base_model: cointegrated/rubert-tiny2
metrics:
- f1
---

# Russian Emotion Classifier

A multi-label emotion classifier for Russian texts.  
Trained on the [CEDR](https://huggingface.co/datasets/sagteam/cedr_v1) dataset with weighted BCE loss to handle class imbalance.

**Base model**: `cointegrated/rubert-tiny2`  
**F1-micro**: `0.7247` | **F1-macro**: `0.6823`

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ilyali034/rubert-emotion-ru",
    return_all_scores=True,
)

results = classifier("Я очень рад, но немного боюсь")[0]
for r in sorted(results, key=lambda x: -x["score"]):
    if r["score"] > 0.5:
        print(r["label"], round(r["score"], 3))
```

Example output:
```
joy 0.892
fear 0.678
```

## Metrics

| Metric | Value |
|--------|-------|
| F1 micro | 0.7247 |
| F1 macro | 0.6823 |
| F1 weighted | 0.7389 |
| Precision micro | 0.6193 |
| Recall micro | 0.8733 |

### Per-class F1

| Class | F1 |
|-------|-----|
| joy | 0.8391 |
| sadness | 0.8057 |
| surprise | 0.6711 |
| fear | 0.6488 |
| anger | 0.4468 |

## Labels

`joy` · `sadness` · `surprise` · `fear` · `anger`

## Citation

If you use this model in your research, please cite:

```bibtex
@dataset{cedr_v1,
  author = {SAGTeam},
  title = {CEDR: Russian Emotion Dataset},
  year = {2023},
  url = {https://huggingface.co/datasets/sagteam/cedr_v1}
}
```