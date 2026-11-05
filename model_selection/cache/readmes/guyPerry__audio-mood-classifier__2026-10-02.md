---
pipeline_tag: audio-classification
library_name: transformers
language: en
tags:
  - audio
  - audio-classification
  - ast
  - music
  - mood
license: apache-2.0
---

# Audio Mood Classifier

Fine-tuned [Audio Spectrogram Transformer (AST)](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) for music mood classification.

## Classes

| Label | Description |
|---|---|
| calm_melancholic | Slow, introspective, melancholic |
| moderate_neutral | Balanced, mid-energy, neutral feel |
| energetic_upbeat | Fast, high-energy, upbeat |

## Usage

```python
from transformers import pipeline
classifier = pipeline("audio-classification", model="guyPerry/audio-mood-classifier")
result = classifier("song.mp3")
```
