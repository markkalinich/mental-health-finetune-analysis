
---
library_name: transformers
tags:
- autotrain
- object-detection
- vision
base_model: facebook/detr-resnet-50
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg
  example_title: Tiger
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/teapot.jpg
  example_title: Teapot
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg
  example_title: Palace
datasets:
- uisikdag/safetyvest
---

# Model Trained Using AutoTrain

- Problem type: Object Detection

## Validation Metrics
loss: 0.8105313181877136

map: 0.4295

map_50: 0.7538

map_75: 0.4237

map_small: 0.1306

map_medium: 0.3983

map_large: 0.4773

mar_1: 0.2729

mar_10: 0.5889

mar_100: 0.6462

mar_small: 0.2889

mar_medium: 0.5652

mar_large: 0.7258
