---
language:
- en
- tl
tags:
- text-classification
- emotion-detection
- xlm-roberta
- taglish
---

# DiariCore Mood Classifier

XLM-RoBERTa-base fine-tuned for 5-class emotion detection on English, Filipino, and Taglish diary entries.

**Classes:** angry, anxious, happy, neutral, sad

**Architecture:** XLM-RoBERTa-base + custom classification head (Dropout → Linear → LayerNorm → GELU → Dropout → Linear)

**Training:** Focal Loss + Label Smoothing, SWA, Differential LR, Keyword hybrid layer

## Usage

See the DiariCore notebook for full inference code including calibration multipliers and keyword assist layer.
