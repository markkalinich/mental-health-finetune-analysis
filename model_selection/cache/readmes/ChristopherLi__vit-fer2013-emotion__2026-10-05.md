---
license: apache-2.0
library_name: transformers
tags:
  - vision
  - image-classification
  - emotion-recognition
  - facial-expression
  - vit
datasets:
  - abhilash88/fer2013-enhanced
metrics:
  - accuracy
  - f1
base_model: google/vit-base-patch16-224-in21k
pipeline_tag: image-classification
model-index:
  - name: vit-fer2013-emotion
    results:
      - task:
          type: image-classification
          name: Facial Emotion Recognition
        dataset:
          name: FER2013 Enhanced
          type: abhilash88/fer2013-enhanced
        metrics:
          - type: accuracy
            value: 0.694
            name: Test Accuracy
          - type: f1
            value: 0.656
            name: Macro F1
---

# ViT Emotion Recognition (FER2013)

Vision Transformer fine-tuned for **7-class facial emotion recognition** on the [FER2013 Enhanced](https://huggingface.co/datasets/abhilash88/fer2013-enhanced) dataset.

Best for **in-the-wild / webcam** faces.

## Labels

`angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`

## Usage

```python
from transformers import pipeline

clf = pipeline("image-classification", model="ChristopherLi/vit-fer2013-emotion")
print(clf("face.jpg"))
```

Or with this project's webcam app:

```bash
python webcam_app.py --model ChristopherLi/vit-fer2013-emotion
```

## Training

- Base: `google/vit-base-patch16-224-in21k`
- 3 epochs, fp16, lr `5e-5`, effective batch size 32
- Input: 48×48 grayscale faces resized to 224×224 and replicated to 3 channels

## Results (test set)

| Metric | Value |
|---|---|
| Accuracy | 69.4% |
| Macro F1 | 0.656 |

FER2013 is a noisy benchmark (human agreement ~65%). See the [project README](https://github.com/ChristopherLI2002/Emotion-Recognition-by-VIT) for details.
