---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
base_model: distilbert-base-uncased
datasets:
  - imdb
---

# hf-workshop-sentiment

Binary sentiment classifier (positive/negative) fine-tuned from `distilbert-base-uncased`.

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="marksoulier/hf-workshop-sentiment")
classifier("I loved this film!")
# [{'label': 'POSITIVE', 'score': 0.998}]
```

## Training

Training code, dependencies, and full reproduction steps are on GitHub:
**https://github.com/marksoulier/hf-workshop**

```bash
git clone https://github.com/marksoulier/hf-workshop
cd hf-workshop
uv run train.py
```
