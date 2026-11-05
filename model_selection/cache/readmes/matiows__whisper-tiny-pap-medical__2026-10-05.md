---
language:
- pap
license: apache-2.0
tags:
- whisper
- automatic-speech-recognition
- papiamento
- speech-to-text
- medical
- healthcare
- clinical
base_model: sonnygeorge/whisper-tiny-pap
datasets:
- medical-papiamento-corpus
widget:
- example_title: "Medical Papiamento Sample"
  src: "https://example.com/medical_sample.wav"
---

# Whisper Tiny Papiamento - Medical Domain Adaptation

This model is a **medical domain fine-tuned version** of [sonnygeorge/whisper-tiny-pap](https://huggingface.co/sonnygeorge/whisper-tiny-pap) specialized for healthcare and clinical Papiamento speech recognition.

## Model Description

- **Base model:** [sonnygeorge/whisper-tiny-pap](https://huggingface.co/sonnygeorge/whisper-tiny-pap) (Papiamento Whisper model by Sonny George)
- **Domain:** Medical/Healthcare Papiamento
- **Language:** Papiamento (pap)
- **Specialization:** Clinical terminology, medical consultations, healthcare vocabulary
- **Training:** Fine-tuned on medical Papiamento audio data

## Model Performance

This model builds upon Sonny George's excellent Papiamento Whisper foundation and adds:
- ✅ **Enhanced medical terminology** recognition
- ✅ **Clinical context understanding** 
- ✅ **Healthcare vocabulary** optimization
- ✅ **Single speaker adaptation** for consistent medical speech patterns

## Intended Uses

- Medical consultation transcription in Papiamento
- Clinical note generation from Papiamento audio
- Healthcare documentation automation
- Medical terminology recognition in Papiamento

## Usage

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

# Load model and processor
processor = WhisperProcessor.from_pretrained("your-username/whisper-tiny-pap-medical")
model = WhisperForConditionalGeneration.from_pretrained("your-username/whisper-tiny-pap-medical")

# Load medical audio
audio, sr = librosa.load("medical_consultation.m4a", sr=16000)

# Process and transcribe
inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
predicted_ids = model.generate(inputs["input_features"])
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print(transcription)  # Medical Papiamento transcription
```