---
language:
- th
tags:
- whisper
- thai
- asr
- speech-recognition
- elderly
- healthcare
license: apache-2.0
base_model: biodatlab/whisper-th-small-combined
---

# Thai Whisper - Elderly Healthcare ASR

Fine-tuned Thonburian Whisper model for Thai elderly speech recognition in healthcare domains.

## Performance

| Metric | Value |
|--------|-------|
| **WER** | **6.73%** |
| **CER** | **1.01%** |

## Usage

```python
from transformers import pipeline
pipe = pipeline("automatic-speech-recognition", model="xb2g/thai-whisper-elderly-healthcare")
result = pipe("audio.mp3", generate_kwargs={"language": "<|th|>"})
print(result["text"])
```
