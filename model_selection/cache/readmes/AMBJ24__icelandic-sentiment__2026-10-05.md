---
license: cc-by-nc-4.0
language:
- is
pipeline_tag: text-classification
library_name: transformers
tags:
- icelandic
- sentiment-analysis
- text-classification
- sequence-classification
- social-media
sources:
  Risamálheildin slices of forums/blogs, manually labelled by us, and our own
  small corpus made from samples gathered from social media
---


**Task**: 3-class sentiment analysis → `["negative", "neutral", "positive"]`  
**Base model**: `mideind/IceBERT-igc` (Icelandic RoBERTa)

## TL;DR

A small Icelandic RoBERTa fine-tuned for 3-way sentiment on non-ironic text. Pairs well **after** an irony gate (first run the irony model; only classify sentiment if `not_ironic`).

---

## How to use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "ambj24/icelandic-sentiment"
tok  = AutoTokenizer.from_pretrained(model_id)
mod  = AutoModelForSequenceClassification.from_pretrained(model_id)

text = "Þjónustan var frábær!"
inputs = tok(text, return_tensors="pt")
probs = mod(**inputs).logits.softmax(-1).tolist()[0]

labels = ["negative", "neutral", "positive"]
print(dict(zip(labels, probs)))

Input length: short posts; trained with max length ~128 tokens.

Data: social-media style Icelandic.
Domain shift: trained on short, informal posts.

Positive/neutral/negative labels; only examples judged not ironic.

Typical setup: 3 epochs, LR ≈ 2e-5, batch ≈ 16, max length 128.