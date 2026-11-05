---
tags:
- image-classification
- pytorch
- huggingface
- vit
- emotion-recognition
datasets:
- raf-db
base_model: trpakov/vit-face-expression
library_name: transformers
---

# ViT Face Expression (Fine-tuned on RAF-DB)

This model is a fine-tuned version of [trpakov/vit-face-expression](https://huggingface.co/trpakov/vit-face-expression) on the [RAF-DB (Real-world Affective Faces Database)](http://www.whdeng.cn/raf/model1.html).

## Model Description
- **Architecture**: Vision Transformer (ViT)
- **Task**: Facial Emotion Recognition
- **Emotions**: Anger, Disgust, Fear, Happiness, Neutral, Sadness, Surprise

## Dataset
RAF-DB is a large-scale facial expression database with around 30,000 facial images downloaded from the Internet. The images cover 7 basic emotions and 12 compound emotions. This model was fine-tuned on the 7 basic emotions subset.

## Usage

```python
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

repo_name = "michaelgathara/vit-face-raf-db"

processor = ViTImageProcessor.from_pretrained(repo_name)
model = ViTForImageClassification.from_pretrained(repo_name)

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 7 emotions
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```
