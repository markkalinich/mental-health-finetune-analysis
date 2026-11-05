---
license: mit
base_model: j-hartmann/emotion-english-distilroberta-base
library_name: transformers
pipeline_tag: text-classification
tags:
- emotion
- emotion-classification
- text-classification
- distilroberta
- safetensors
---

# Emotion English DistilRoBERTa (safetensors)

This repository contains a **safetensors-only conversion** of the model:

**j-hartmann/emotion-english-distilroberta-base**

The model performs multi-class emotion classification on English text and predicts the following labels:

- anger  
- disgust  
- fear  
- joy  
- neutral  
- sadness  
- surprise  

No architectural changes or retraining have been performed. The only modification is the conversion of model weights to the `safetensors` format.

---

## Original Model

- **Author:** Jochen Hartmann  
- **Original Repository:** https://huggingface.co/j-hartmann/emotion-english-distilroberta-base  
- **Year:** 2022  

If you use this model in academic work, please cite the original author.

---

## Modifications

- Converted PyTorch weights to `safetensors`
- Tokenizer and configuration preserved
- No changes to model behavior, labels, or performance

---

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="YOUR_USERNAME/YOUR_REPO_NAME",
    return_all_scores=True
)

classifier("I love this!")
```