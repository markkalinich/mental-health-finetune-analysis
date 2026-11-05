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
datasets:
- custom
metrics:
- accuracy
- f1
---

# Cognitive Distortion Detector (Stage 1)

This model is a Turkish NLP classifier specialized in identifying **cognitive distortions** in text. It is designed as the initial component of a hierarchical classification system.

## Model Description
The model acts as a binary classifier (Distorted vs. Not Distorted). Its primary goal is to filter text for potential cognitive biases before more specific analysis.

* **Task:** Binary Classification
* **Language:** Turkish
* **Focus:** Mental health-related language processing

## Hierarchical Workflow
This model serves as the **Gatekeeper**:
1. **Stage 1 (This Model):** Detects if any cognitive distortion is present.
2. **Stage 2 (Subsequent Classifier):** Categorizes the detected distortion into specific types (e.g., Catastrophizing, Overgeneralization, Personalization).



## Usage
You can easily integrate this model using the Hugging Face `pipeline`:

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="mfurkanerkan15/cognitive-distortion-detector-tr")
result = pipe("Her şey her zaman kötü gitmek zorunda.")
print(result)