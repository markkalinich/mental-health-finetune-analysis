---
language:
- en
license: mit
tags:
- arcane
- bart
- mental-health
- edge-ready
pipeline_tag: text2text-generation
---

# Arcane-BART

**Arcane-BART** is a lightweight, efficient sequence-to-sequence model designed for fast mental health screening and real-time distress analysis.

## Overview
- **Type**: Seq2Seq Transformer (~1.6 GB)
- **Deployment**: Suitable for local CPU inference, containers, and edge backends.

## Inference Example

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_id = "ar3xop/arcane-bart"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

prompt = 'Consider this post: "The stress from examinations is unbearable." Question: What is the cause of stress?'
inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

output_ids = model.generate(**inputs, max_length=256)
print(tokenizer.decode(output_ids[0], skip_special_tokens=True))
```
