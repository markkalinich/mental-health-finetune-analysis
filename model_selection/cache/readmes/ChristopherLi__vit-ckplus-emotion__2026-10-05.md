---
license: apache-2.0
library_name: transformers
tags:
  - vision
  - image-classification
  - emotion-recognition
  - facial-expression
  - vit
  - ck+
datasets:
  - AlirezaF138/ckplus-dataset
metrics:
  - accuracy
  - f1
base_model: google/vit-base-patch16-224-in21k
pipeline_tag: image-classification
model-index:
  - name: vit-ckplus-emotion
    results:
      - task:
          type: image-classification
          name: Facial Emotion Recognition
        dataset:
          name: CK+
          type: AlirezaF138/ckplus-dataset
        metrics:
          - type: accuracy
            value: 0.980
            name: Test Accuracy
          - type: f1
            value: 0.965
            name: Macro F1
---

# ViT Emotion Recognition (CK+)

Vision Transformer fine-tuned for **7-class facial emotion recognition** on [CK+](https://huggingface.co/datasets/AlirezaF138/ckplus-dataset).

Initialized from a FER2013-tuned ViT, then fine-tuned on CK+. Best for **clean, frontal, posed** lab faces. Prefer the FER2013 model for webcam / in-the-wild use.

## Labels

`anger`, `contempt`, `disgust`, `fear`, `happy`, `sadness`, `surprise`

## Usage

```python
from transformers import pipeline

clf = pipeline("image-classification", model="ChristopherLi/vit-ckplus-emotion")
print(clf("face.jpg"))
```

## Training

- Base: FER2013 fine-tune of `google/vit-base-patch16-224-in21k`
- 10 epochs on CK+ (stratified 80/10/10), fp16, lr `3e-5`

## Results (held-out test)

| Metric | Value |
|---|---|
| Accuracy | 98.0% |
| Macro F1 | 0.965 |

See the [project README](https://github.com/ChristopherLI2002/Emotion-Recognition-by-VIT) for caveats about CK+ generalization.
