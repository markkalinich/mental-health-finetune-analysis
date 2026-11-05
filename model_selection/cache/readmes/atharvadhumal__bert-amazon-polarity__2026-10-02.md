---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - bert
datasets:
  - amazon_polarity
---

# BERT Fine-tuned on Amazon Polarity

Fine-tuned `bert-base-uncased` for binary sentiment classification on the [Amazon Polarity](https://huggingface.co/datasets/fancyzhx/amazon_polarity) dataset (3.6M training reviews).

## Results

| Metric | Score |
|--------|-------|
| F1 (macro) | **97.06%** |
| Accuracy | **97.06%** |
| Test samples | 400,000 |

## Usage

```python
from transformers import pipeline

classifier = pipeline('sentiment-analysis', model='atharvadhumal/bert-amazon-polarity')
classifier('This product is absolutely amazing!')
# [{'label': 'LABEL_1', 'score': 0.998}]
```

## Training Details

| Hyperparameter | Value |
|----------------|-------|
| Base model | bert-base-uncased |
| Epochs | 3 |
| Batch size | 64 |
| Learning rate | 2e-5 |
| Precision | fp16 |
| Hardware | NVIDIA V100 / H200 (Northeastern HPC) |

See the [GitHub repo](https://github.com/atharvadhumal03/BERT-Sentiment-Analysis) for full training code.
