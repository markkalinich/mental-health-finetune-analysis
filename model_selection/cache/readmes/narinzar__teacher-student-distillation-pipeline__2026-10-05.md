---
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - knowledge-distillation
  - distilbert
  - sst-2
  - glue
  - sentiment-analysis
datasets:
  - nyu-mll/glue
language:
  - en
base_model: distilbert-base-uncased
---

# teacher-student-distillation-pipeline (SST-2 student)

A `distilbert-base-uncased` student distilled from the
`textattack/bert-base-uncased-SST-2` teacher on GLUE SST-2 sentiment
classification. Training combines temperature-scaled KL divergence against the
teacher's soft labels with the task cross-entropy, using a linear alpha
curriculum (0.9 -> 0.1) that starts distillation-heavy and anneals toward the
true labels.

## Results

Single small-scale run on an RTX 5090: SST-2, 2000 train / 500 val, 1 epoch.

| metric | value |
| --- | --- |
| teacher accuracy | 0.9340 |
| student accuracy | 0.8600 |
| accuracy retained (student / teacher) | 0.9208 (92.1%) |
| student speedup over teacher | 2.12x |
| param compression (teacher / student) | 1.64x |
| student params | 66,955,010 |

The distilled student keeps 92% of the teacher's SST-2 accuracy while running
2.1x faster with 1.64x fewer parameters. These are small-scale (1-epoch,
2000-example) numbers meant to illustrate the accuracy-for-speed trade, not a
full-scale benchmark.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

name = "narinzar/teacher-student-distillation-pipeline"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name)

inputs = tok("a thoughtful, moving film", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
print(logits.argmax(-1).item())  # 0 = negative, 1 = positive
```

## Labels

- 0: negative
- 1: positive

Training code: https://github.com/narinzar/teacher-student-distillation-pipeline
