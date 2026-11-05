---
license: apache-2.0
tags:
  - text-classification
  - sentiment
  - sst2
  - transformers
model_type: opt
library_name: transformers
pipeline_tag: text-classification
---

# OPT-125M Fine-Tuned for Sentiment Classification

This model is a fine-tuned version of `facebook/opt-125m` on the SST-2 dataset.  
It performs binary sentiment classification: **POSITIVE** or **NEGATIVE**.

## 📝 Usage

You can use it with the 🤗 Transformers pipeline:

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="terrytaylorbonn/final-opt-sentiment2")
print(pipe("That movie was amazing!"))