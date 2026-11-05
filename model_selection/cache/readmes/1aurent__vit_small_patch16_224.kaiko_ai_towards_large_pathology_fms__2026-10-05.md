---
tags:
- timm
- feature-extraction
- image-classification
library_name: timm
license: other
license_name: kaiko-non-commercial
license_link: https://github.com/kaiko-ai/towards_large_pathology_fms/blob/a62a0c54719d858371aefa0fcab6ec4b34c86c4c/LICENSE
metrics:
- accuracy
model-index:
- name: kaiko
  results:
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: BACH
      type: image-classification
    metrics:
    - type: accuracy
      value: 0.797
      name: Accuracy
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: CRC-NCT-HE
      type: image-classification
    metrics:
    - type: accuracy
      value: 0.943
      name: Accuracy
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: MHIST
      type: image-classification
    metrics:
    - type: accuracy
      value: 0.828
      name: Accuracy
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: PCam
      type: image-classification
    metrics:
    - type: accuracy
      value: 0.893
      name: Accuracy
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TP53
      type: image-classification
    metrics:
    - type: accuracy
      value: 0.633
      name: Accuracy
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: CoNSeP
      type: image-classification
    metrics:
    - type: accuracy
      value: 0.649
      name: Accuracy
      verified: false
---

# Model card for vit_small_patch16_224.kaiko_ai_towards_large_pathology_fms

![](https://github.com/kaiko-ai/towards_large_pathology_fms/blob/a62a0c54719d858371aefa0fcab6ec4b34c86c4c/docs/images/kaiko-logo.png?raw=true)

## Model Details

- **Model Type:** Feature backbone
- **Model Stats:**
  - Params: 22M (small)
  - Image size: 224 x 224 x 3
  - Patch size: 16 x 16 x 3
- **Repository:** [github.com:kaiko-ai/towards_large_pathology_fms](https://github.com/kaiko-ai/towards_large_pathology_fms)
- **Original Weights:** [github.com:kaiko-ai/towards_large_pathology_fms/0.0.1](https://github.com/kaiko-ai/towards_large_pathology_fms/releases/tag/0.0.1)
- **Papers:**
  - [Towards Large-Scale Training of Pathology Foundation Models](https://arxiv.org/abs/2404.15217)

## Model Usage

### Image Embeddings

```python
from torchvision.transforms import v2
from PIL import Image
import requests
import torch
import timm
import io

# get example histology image
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc7_xZpGOfQT7sxKwf2w5lL4GAq6IX_CbTzP1NGeenzA&s"
image = Image.open(io.BytesIO(requests.get(url).content))

# load model from the hub
model = timm.create_model(
  model_name="hf-hub:1aurent/vit_small_patch16_224.kaiko_ai_towards_large_pathology_fms",
  dynamic_img_size=True,
  pretrained=True,
).eval()

# get image transform
preprocessing = v2.Compose(
  [
    v2.ToImage(),
    v2.Resize(size=224),
    v2.CenterCrop(size=224),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(
      mean=(0.5, 0.5, 0.5),
      std=(0.5, 0.5, 0.5),
    ),
  ]
)

data = preprocessing(image).unsqueeze(0) # input is a (batch_size, num_channels, img_size, img_size) shaped tensor
output = model(data)  # output is a (batch_size, num_features) shaped tensor
```

## Citation

```bibtex
@misc{ai2024largescale,
  title         = {Towards Large-Scale Training of Pathology Foundation Models}, 
  author        = {kaiko.ai and Nanne Aben and Edwin D. de Jong and Ioannis Gatopoulos and Nicolas Känzig and Mikhail Karasikov and Axel Lagré and Roman Moser and Joost van Doorn and Fei Tang},
  year          = {2024},
  eprint        = {2404.15217},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV}
}
```
