---
license: mit
datasets:
- Dc-4nderson/feelings_classfication_dataset
language:
- en
base_model:
- google/vit-base-patch16-224-in21k
pipeline_tag: image-classification
library_name: transformers
tags:
- emotions
- school
metrics:
- accuracy
---
# 🤖 ViT Emotion Classifier

This is a lightweight [Vision Transformer (ViT)](https://huggingface.co/docs/transformers/model_doc/vit) model fine-tuned to classify **emotions** from facial images using a custom dataset of school-aged individuals. It supports 8 emotional categories and is designed to work well on small datasets and limited compute.

---

## 🧠 Supported Emotions

The model predicts one of the following emotional states:

| Label ID | Emotion            |
|----------|--------------------|
| 0        | anxious-fearful    |
| 1        | bored              |
| 2        | confused           |
| 3        | discouraged        |
| 4        | frustrated         |
| 5        | neutral            |
| 6        | positive           |
| 7        | suprised           |

---

## 📦 Model Details

- **Model Type**: `ViTForImageClassification`
- **Backbone**: `vit-small-patch16-224`
- **Dataset**: [`Dc-4nderson/feelings_classfication_dataset`](https://huggingface.co/datasets/Dc-4nderson/feelings_classfication_dataset)
- **Framework**: PyTorch
- **Labels**: 8 emotions (defined in `config.json`)
- **Trained on**: Google Colab with < 600 images

---

## 🧪 Usage

```python
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# Load model + processor
processor = AutoImageProcessor.from_pretrained("Dc-4nderson/vit-emotion-classifier")
model = AutoModelForImageClassification.from_pretrained("Dc-4nderson/vit-emotion-classifier")

# Load image and preprocess
image = Image.open("your_image.jpg").convert("RGB")
inputs = processor(images=image, return_tensors="pt")

# Run inference
with torch.no_grad():
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    label = model.config.id2label[str(pred)]

print("🧠 Predicted Emotion:", label)