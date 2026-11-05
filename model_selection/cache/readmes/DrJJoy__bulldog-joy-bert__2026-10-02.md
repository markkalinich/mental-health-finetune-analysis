---
library_name: transformers
pipeline_tag: text-classification
language: en
tags:
- nlp
- generative-ai
- joy-intensity
- mindfulness
- sentiment-analysis
license: mit
---

# 💫 Happiness Vibration BERT

**Happiness Vibration BERT** is a fine-tuned `bert-base-uncased` model designed to measure **Joy Intensity (0–3)** in mindfulness-inspired language.  
It was developed as part of a full **NLP and Generative AI pipeline** exploring how linguistic tone reflects emotional well-being.

| Label | Meaning |
|-------|----------|
| 0 | Low Joy |
| 1 | Neutral |
| 2 | Warm |
| 3 | High Joy |

The model was trained on **1,000 programmatically generated, domain-specific comments** designed to mimic the tone, language, and positive affect common in mindfulness and gratitude communities.  
The dataset intentionally emphasizes higher-joy expressions to test a model’s ability to detect **subtle variations within predominantly positive text**.

---

### 🚀 Quick Use

```python
from transformers import pipeline
clf = pipeline("text-classification", model="DrJJoy/bulldog-joy-bert")
clf("Walking in the sunrise with my bulldog.")
# [{'label': '3', 'score': 0.982}]
