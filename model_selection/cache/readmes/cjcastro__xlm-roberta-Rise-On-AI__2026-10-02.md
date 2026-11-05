---
language:
- en
- tl
license: apache-2.0
library_name: transformers
tags:
- text-classification
- xlm-roberta
- sentiment-analysis
- filipino
- taglish
pipeline_tag: text-classification
---

# XLM-RoBERTa Rise On AI — Sentiment Analysis

Fine-tuned XLM-RoBERTa for Filipino/English/Taglish 3-class sentiment.

**Labels:** `positive` · `negative` · `distress`

**Accuracy:** 82.6% · **F1 macro:** 0.815

## Usage

```python
from transformers import pipeline
clf = pipeline('text-classification', model='cjcastro/xlm-roberta-Rise-On-AI', top_k=None)
print(clf('I feel happy today!'))
```
