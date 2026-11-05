---
language:
- en
- ar
tags:
- automatic-speech-recognition
- whisper
- medical
- asr
- fp16
license: apache-2.0
datasets:
- yashtiwari/PaulMooney-Medical-ASR-Data
model-index:
- name: Whisper Large-v3 Medical
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Medical ASR
      type: yashtiwari/PaulMooney-Medical-ASR-Data
    metrics:
    - type: wer
      value: 4.12
metrics:
- wer
base_model:
- openai/whisper-large-v3
pipeline_tag: automatic-speech-recognition
---

# Whisper Large-v3 Medical

This model is a fine-tuned version of [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) on medical speech data. It is trained for **Automatic Speech Recognition (ASR)** of **doctor-patient dialogues and medical narratives**, with support for **English** and **Arabic**.

## 🩺 Use Cases

- Transcribing clinical interviews.
- Building medical dictation tools.
- Precision: float16 (better for inference), float32 (better for fine-tuning)


## 📊 Performance

- **WER (Word Error Rate): 4.12% **
- Optimized for clean and domain-specific spoken medical data.

## 🔧 Model Details

- Base model: [`openai/whisper-large-v3`](https://huggingface.co/openai/whisper-large-v3)
- Fine-tuned on: [`yashtiwari/PaulMooney-Medical-ASR-Data`](https://huggingface.co/datasets/yashtiwari/PaulMooney-Medical-ASR-Data)
- Languages: Multilingual
- Framework: 🤗 Transformers

## 🧪 How to Use

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration

model_id = "yehiazak/whisper-largev3-medical"

# Load FP16 model
model = WhisperForConditionalGeneration.from_pretrained(model_id, revision="fp16")

# Load FP32 model
model = WhisperForConditionalGeneration.from_pretrained(model_id)

processor = WhisperProcessor.from_pretrained(model_id)
