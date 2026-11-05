---
language: en
license: apache-2.0
tags:
  - medical
  - radiology
  - chest-x-ray
  - image-classification
  - multi-label-classification
  - vit
  - chexpert
datasets:
  - chexpert
metrics:
  - roc_auc
---

# ViT-B/16 Fine-Tuned on CheXPert

Vision Transformer (ViT-B/16) fine-tuned on the CheXPert dataset for
**multi-label chest X-ray pathology classification**.

Part of the [ClinicalAI Assistant](https://github.com/suparthjain/clinical-ai-assistant)
project — a multimodal clinical AI system with RAG-grounded diagnostic support.

## Model Details

- **Base model:** google/vit-base-patch16-224-in21k (ImageNet-21k pre-trained)
- **Task:** Multi-label binary classification (5 labels)
- **Input:** 224×224 RGB chest X-ray image (frontal view)
- **Output:** 5 independent sigmoid probabilities

## Labels

| Label | AUC-ROC | pos_weight |
|---|---|---|
| Atelectasis | 0.6999 | 2.21 |
| Cardiomegaly | 0.8571 | 7.17 |
| Consolidation | 0.7284 | 10.00 (capped) |
| Edema | 0.8376 | 2.11 |
| Pleural Effusion | 0.8579 | 1.21 |
| **Mean** | **0.7962** | — |

## Training Details

| Setting | Value |
|---|---|
| Dataset | CheXPert-v1.0-small (Stanford) |
| Training images | 152,840 frontal chest X-rays |
| Validation images | 19,084 |
| Epochs | 3 |
| Batch size | 32 |
| Optimizer | AdamW (lr=2e-5 encoder, lr=2e-4 head) |
| Scheduler | OneCycleLR with 10% warmup |
| Loss | BCEWithLogitsLoss with pos_weights |
| Mixed precision | float16 (AMP) |
| GPU | Tesla T4 |
| Training time | ~2.5 hours |

## U-Label Strategy

Uncertain labels (-1) in CheXPert are resolved following Table 2
of the [CheXPert paper](https://arxiv.org/abs/1901.07031):

| Label | Strategy | Rationale |
|---|---|---|
| Atelectasis | U-Ones | Uncertain → positive |
| Cardiomegaly | U-Zeros | Uncertain → negative |
| Consolidation | U-Zeros | Uncertain → negative |
| Edema | U-Ones | Uncertain → positive |
| Pleural Effusion | U-Ones | Uncertain → positive |

## Usage

```python
from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch

model     = ViTForImageClassification.from_pretrained("suparthjain/vit-base-chexpert-clinicalai")
processor = ViTImageProcessor.from_pretrained("suparthjain/vit-base-chexpert-clinicalai")

image  = Image.open("chest_xray.jpg").convert("RGB")
inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    probs  = torch.sigmoid(logits)

labels = model.config.id2label
for i, (label, prob) in enumerate(zip(labels.values(), probs[0])):
    print(f"{label}: {prob:.4f}")
```

## Limitations

- Trained on frontal chest X-rays only (lateral views not supported)
- Not validated on external datasets beyond CheXPert validation set
- **Not intended for clinical use without radiologist review**
- Performance on paediatric or non-Stanford populations is unknown

## Citation

```bibtex
@inproceedings{irvin2019chexpert,
  title={CheXpert: A Large Chest Radiograph Dataset with Uncertainty Labels},
  author={Irvin, Jeremy and others},
  booktitle={AAAI},
  year={2019}
}
```
