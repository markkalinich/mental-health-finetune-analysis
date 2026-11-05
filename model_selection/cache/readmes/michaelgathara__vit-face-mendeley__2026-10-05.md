---
tags:
- image-classification
- pytorch
- huggingface
- vit
- emotion-recognition
datasets:
- mendeley
base_model: trpakov/vit-face-expression
library_name: transformers
---

# ViT Face Expression (Fine-tuned on Mendeley Dataset)

This model is a fine-tuned version of [trpakov/vit-face-expression](https://huggingface.co/trpakov/vit-face-expression) on the [Genuine and Fake Facial Emotion Dataset (GFFD-2025)](https://data.mendeley.com/datasets/wmfd4p3z32/1).

## Model Description
- **Architecture**: Vision Transformer (ViT)
- **Task**: Facial Emotion Recognition
- **Emotions**: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise

## Dataset
This model was trained on the "Cropped and Augmented" subset of the GFFD-2025 dataset, merging both "Genuine" and "Fake" expression categories into unified emotion classes.

## Usage

```python
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

repo_name = "michaelgathara/vit-face-mendeley"

processor = ViTImageProcessor.from_pretrained(repo_name)
model = ViTForImageClassification.from_pretrained(repo_name)

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 7 emotions
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```
