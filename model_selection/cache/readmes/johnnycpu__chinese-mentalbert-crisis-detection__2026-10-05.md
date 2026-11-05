---
license: apache-2.0
base_model: zwzzz/Chinese-MentalBERT
tags:
- bert
- mental-health
- crisis-detection
- chinese
- taiwan
- elderly
- social-work
- focal-loss
language:
- zh
pipeline_tag: text-classification
---

# 微光導航 LightGuide — Task E — Crisis Emotion Detection

Chinese-MentalBERT fine-tuned for 3-class mental health emotion classification (POSITIVE / NEGATIVE / CRISIS) with Focal Loss (gamma=2, adaptive alpha). Specialized for detecting implicit crisis signals in elderly welfare service conversations. Achieves 100% recall on implicit crisis test cases. Part of the 微光導航 (LightGuide) project.

## Model Details

- **Base Model**: `zwzzz/Chinese-MentalBERT`
- **Fine-tuning Task**: Task E — Crisis Emotion Detection
- **Project**: 微光導航 (LightGuide) — AI-powered elderly welfare navigation system
- **Competition**: 大專生資訊服務創新競賽 (Taiwan University Information Service Innovation Competition)
- **License**: Apache 2.0

## Usage

```python
from transformers import AutoTokenizer, AutoModel
from peft import PeftModel  # if LoRA adapter

# Load from Hub
model = AutoModel.from_pretrained("johnnycpu/chinese-mentalbert-crisis-detection")
```

## Training Details

- **Dataset**: Custom Traditional Chinese welfare dialogue dataset
- **Training Hardware**: NVIDIA A100 (Google Colab)
- **Framework**: HuggingFace Transformers + PEFT

## Citation

If you use this model, please cite the 微光導航 project.
