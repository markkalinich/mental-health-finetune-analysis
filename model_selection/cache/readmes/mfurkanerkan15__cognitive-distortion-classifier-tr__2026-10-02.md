---
language:
- tr
license: mit
tags:
- nlp
- cognitive-distortions
- psychology
- mental-health
- turkish
---

# Cognitive Distortion Classifier (Stage 2)

This model is a multi-class Turkish NLP classifier that categorizes specific types of **cognitive distortions**. It is designed to work as the second stage of a hierarchical system.

## Model Description
After a text is identified as "distorted" by the Stage 1 Detector, this model classifies the specific distortion type.

* **Task:** Multi-class Classification
* **Language:** Turkish

## Hierarchical Workflow
This model is the **Specialist**:
1. **Stage 1 (Detector):** Filters the input.
2. **Stage 2 (This Model):** Provides the detailed diagnosis of the distortion type.

## Usage
```python
from transformers import pipeline

pipe = pipeline("text-classification", model="mfurkanerkan15/cognitive-distortion-classifier-tr")
result = pipe("Kesin her şey çok kötü olacak.")
print(result)