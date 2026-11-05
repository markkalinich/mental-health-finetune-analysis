---
library_name: transformers
license: mit
base_model: prajjwal1/bert-tiny
datasets:
  - stanfordnlp/sst2
language: en
tags:
  - text-classification
  - sentiment
  - bert-tiny
metrics:
  - accuracy
---

# bedrock-sentiment-tiny

Tiny binary sentiment classifier (positive / negative) fine-tuned from
[`prajjwal1/bert-tiny`](https://huggingface.co/prajjwal1/bert-tiny) on a 3 000-example
subset of [SST-2](https://huggingface.co/datasets/stanfordnlp/sst2).

- **Parameters:** ~4.4 M (bert-tiny backbone)
- **Training hardware:** CPU only (2 vCPU)
- **Wall-clock training time:** ~a few minutes
- **Val accuracy:** **0.790** on a 400-example slice of the SST-2 validation set

## Usage

```python
from transformers import pipeline
clf = pipeline("text-classification", model="Facececersek/bedrock-sentiment-tiny")
print(clf("this mod is sooo good"))
print(clf("it wouldn't import, it's broken"))
```

## Training config

- epochs: 2
- batch size: 32
- max length: 64
- learning rate: 5e-5
- seed: 42
- base model: `google/bert_uncased_L-2_H-128_A-2`

## Notes
Trained as a fast demonstration on a CPU-only VM. For production-quality
sentiment, fine-tune on the full SST-2 or a larger base model (e.g.
`distilbert-base-uncased`).
