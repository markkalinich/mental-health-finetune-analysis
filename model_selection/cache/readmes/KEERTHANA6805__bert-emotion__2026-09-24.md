---
language: en
license: mit
pipeline_tag: text-classification
tags:
- text-classification
- emotion-detection
- bert
datasets:
- emotion
library_name: transformers
base_model: google-bert/bert-base-uncased
---

# BERT Emotion Classifier

This model classifies text into 6 emotion categories:
- joy
- sadness
- anger
- fear
- love
- surprise

Model: `bert-base-uncased`  
Dataset: `emotion` (Hugging Face datasets library)

### ✅ Usage Example

```python
from transformers import pipeline
classifier = pipeline("text-classification", model="KEERTHANA6805/bert-emotion")
classifier("I am so happy today!")