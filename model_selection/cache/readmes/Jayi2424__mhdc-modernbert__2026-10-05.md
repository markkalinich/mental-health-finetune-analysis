---
language: en
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- text-classification
- mental-health
library_name: transformers
pipeline_tag: text-classification
---

# MHDC ModernBERT

Fine-tuned ModernBERT-base from the same experiment.

Fine-tuned from [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) for Ajayi, Kachweka, Deku, and Aiken, PMLR 317:15-26, 2026. Best Paper, AAAI-26 AIMedHealth Bridge. https://proceedings.mlr.press/v317/ajayi26a.html

A screening aid with a person in the loop, not a diagnostic tool.

Training tokenized posts at max length 128. Label order is the training order.

## Labels

0 age_cb
1 anxiety
2 bipolar
3 ethnicity_cb
4 gender_cb
5 non_suicide
6 personality_disorder
7 religion_cb
8 stress
9 suicide

## Use

```python
from transformers import pipeline
clf = pipeline("text-classification", model="Jayi2424/mhdc-modernbert")
print(clf("I have not slept and I feel worthless."))
```
