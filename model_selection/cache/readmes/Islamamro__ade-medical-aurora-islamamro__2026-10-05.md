---
license: apache-2.0
pipeline_tag: text-classification
tags:
- aurora
- islamamro
- text-classification
datasets:
- SetFit/ade_corpus_v2_classification
---

# Adverse Drug Event Detector - Aurora - islamamro

**Detects text describing an adverse drug reaction.**

Fine-tuned from `distilbert-base-uncased` on [`SetFit/ade_corpus_v2_classification`](https://huggingface.co/datasets/SetFit/ade_corpus_v2_classification). Built, trained and published end-to-end via the **Aurora Research Portal** by **islamamro** on an NVIDIA RTX 3090.

- **Task:** text classification (2 classes)
- **Held-out accuracy:** 0.83

## Use it
```python
from transformers import pipeline
clf = pipeline("text-classification", model="Islamamro/ade-medical-aurora-islamamro")
clf("your text here")
```

## Note
Trained on a 1,400-example demo subset - a proof of the Aurora build->train->publish pipeline, not a production model. Fine-tune on full data for real use.
