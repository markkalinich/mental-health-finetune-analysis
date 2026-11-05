---
language:
- bn
metrics:
- accuracy
pipeline_tag: audio-classification
tags:
- audio-classification
- emotion-classification
- sentiment-classification
---
# whisper-tiny-bn-emo
This model is a fine-tuned on shhossain/whisper-tiny-bn for emotion classification. It achieves the following results on the evaluation set:

- Loss: 0.1842
- Accuracy: 0.9357

## Model Info
It detects 7 basic human emotions on `Bengali Language`.
- `ANGRY`
- `DISGUST`
- `FEAR`
- `HAPPY`
- `NEUTRAL`
- `SAD`
- `SURPRISE`

## Usage
```python
from transformers import pipeline

pipe = pipeline("audio-classification", model="shhossain/whisper-tiny-bn-emo")

pipe("audio_file.wav")
```