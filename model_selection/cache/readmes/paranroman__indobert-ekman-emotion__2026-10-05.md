---
language:
- id
license: mit
tags:
- text-classification
- emotion
- indonesian
- indobert
pipeline_tag: text-classification
library_name: transformers
datasets:
- paranroman/indonesian-deaf-style-emotion-dataset
base_model:
- indolem/indobert-base-uncased
---

# IndoBERT Emotion Detection

Model klasifikasi emosi dasar Paul Ekman teks Bahasa Indonesia berbasis IndoBERT dengan dataset percakapan gaya bahasa tuli.

## Labels
- Jijik (Disgust)
- Terkejut (Surprise)
- Marah (Angry)
- Neutral
- Sedih (Sad)
- Senang (Happy)
- Takut (Fear)

## Usage
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="paranroman/indobert-ekman-emotion")
result = classifier("Aku sangat senang hari ini!")
print(result)
# [{'label': 'Senang', 'score': 0.99}]
```