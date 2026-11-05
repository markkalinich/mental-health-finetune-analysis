---
language:
- vi
- en
tags:
- video-classification
- content-moderation
- tiktok
- videomae
- pytorch
license: mit
datasets:
- custom
metrics:
- f1
- accuracy
---

# TikTok Content Safety - Video Classifier

This model classifies TikTok video frames as **safe** or **harmful**.

## Usage

```python
from transformers import AutoImageProcessor, VideoMAEForVideoClassification
from decord import VideoReader, cpu
import numpy as np

processor = AutoImageProcessor.from_pretrained("KhoiBui/tiktok-video-safety-classifier")
model = VideoMAEForVideoClassification.from_pretrained("KhoiBui/tiktok-video-safety-classifier")

# Load video and sample 16 frames
vr = VideoReader("video.mp4", ctx=cpu(0))
indices = np.linspace(0, len(vr) - 1, 16).astype(int)
frames = list(vr.get_batch(indices).asnumpy())

inputs = processor(frames, return_tensors="pt")
outputs = model(**inputs)
prediction = outputs.logits.argmax(-1).item()  # 0=safe, 1=harmful
```

## Model Details
- **Base Model**: VideoMAE (MCG-NJU/videomae-base-finetuned-kinetics)
- **Task**: Binary classification (safe/harmful)
- **Input**: 16 frames, 224x224
