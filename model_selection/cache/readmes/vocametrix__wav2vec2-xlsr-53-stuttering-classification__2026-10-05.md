---
license: apache-2.0
language:
  - en
tags:
  - speech
  - stuttering
  - stuttering-detection
  - disfluency
  - wav2vec2
  - xlsr-53
  - audio-classification
  - speech-pathology
  - speech-therapy
datasets:
  - SEP-28k
  - SEP-28k-Extended
metrics:
  - f1
pipeline_tag: audio-classification
library_name: transformers
---

# Wav2Vec2-XLSR-53 Fine-Tuned for Stuttering Detection

A **Wav2Vec2ForSequenceClassification** model fine-tuned on the [SEP-28k-Extended](https://arxiv.org/abs/2206.14568) dataset for multi-class stuttering type classification.

This model is part of the **SpeechTherapyAgent** (VST) system described in the paper:

> **SpeechTherapyAgent: A Clinician-in-the-Loop AI Virtual Speech Therapist for Personalized and Supervised Therapy**
> Shakeel A. Sheikh, Patrick Marmaroli, Md Sahidullah, Slim Ouni, Fabrice Hirsch, Gonçalo Leal, Björn W. Schuller
> *(under review)*

**Live demo:** [vocametrix.com/ai/stuttering-therapy-planning-agent](https://vocametrix.com/ai/stuttering-therapy-planning-agent)

## Model Details

| Property | Value |
|----------|-------|
| **Base model** | [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) |
| **Architecture** | `Wav2Vec2ForSequenceClassification` |
| **Fine-tuning** | End-to-end (full model, not frozen features) |
| **Training data** | SEP-28k-Extended (~28k three-second clips from stuttering podcasts) |
| **Training steps** | 72,600 |
| **Parameters** | ~315M |
| **Input** | 16 kHz mono audio |
| **Output** | 6 classes |

## Labels

| ID | Label | Description |
|----|-------|-------------|
| 0 | `Soundrepetition` | Repetition of individual sounds (e.g., "b-b-ball") |
| 1 | `Wordrepetition` | Repetition of whole words (e.g., "I-I-I want") |
| 2 | `block` | Silent or audible blocks in speech flow |
| 3 | `fluent` | Fluent speech (no disfluency) |
| 4 | `interjection` | Filler words or sounds (e.g., "um", "uh") |
| 5 | `prolongation` | Prolonged sounds (e.g., "ssssnake") |

## Performance

Weighted average F1 scores on SEP-28k-Extended (speaker-disjoint split):

| Class | Fine-tuned (this model) | SOTA without fine-tuning |
|-------|------------------------|--------------------------|
| Soundrepetition | **43.00%** | 32.07% |
| Wordrepetition | **56.00%** | 41.23% |
| Block | **32.00%** | 31.02% |
| Fluent | **82.00%** | 66.92% |
| Interjection | **77.00%** | 51.63% |
| Prolongation | 44.00% | **46.23%** |
| **Weighted Avg F1** | **67.00%** | 44.85% |

## Usage

```python
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor
import torch
import torch.nn.functional as F
import librosa

# Load model
model_name = "vocametrix/wav2vec2-xlsr-53-stuttering-classification"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForAudioClassification.from_pretrained(model_name)
model.eval()

# Load audio (16 kHz, mono)
audio, sr = librosa.load("your_audio.wav", sr=16000, mono=True)

# Classify
inputs = feature_extractor(audio, sampling_rate=16000, return_tensors="pt", padding=True)
with torch.no_grad():
    logits = model(**inputs).logits
    probs = F.softmax(logits, dim=-1)
    pred_id = torch.argmax(probs, dim=-1).item()
    confidence = probs[0][pred_id].item()
    label = model.config.id2label[pred_id]

print(f"Prediction: {label} ({confidence:.1%})")
```

## Chunked Inference

For longer audio recordings, we recommend splitting into **4-second chunks with 50% overlap** (as used in the VST system):

```python
import numpy as np

chunk_duration = 4.0  # seconds
overlap = 0.50
chunk_samples = int(chunk_duration * 16000)
step_samples = int(chunk_samples * (1 - overlap))

results = []
pos = 0
while pos < len(audio):
    end = min(pos + chunk_samples, len(audio))
    chunk = audio[pos:end]
    if len(chunk) < chunk_samples:
        chunk = np.pad(chunk, (0, chunk_samples - len(chunk)))

    inputs = feature_extractor(chunk, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=-1)
        pred_id = torch.argmax(probs, dim=-1).item()
        results.append({
            "start": pos / 16000,
            "end": end / 16000,
            "label": model.config.id2label[pred_id],
            "confidence": probs[0][pred_id].item(),
        })
    pos += step_samples
```

## Inference Speed

| Device | Time per 4s chunk | Notes |
|--------|-------------------|-------|
| GPU (CUDA) | ~80 ms | NVIDIA RTX-class |
| CPU | ~810 ms | Intel i7, single thread |

## Citation

If you use this model in your research, please cite:

```bibtex
@article{sheikh2026speechtherapyagent,
  title={SpeechTherapyAgent: A Clinician-in-the-Loop AI Virtual Speech Therapist for Personalized and Supervised Therapy},
  author={Sheikh, Shakeel A. and Marmaroli, Patrick and Sahidullah, Md and Ouni, Slim and Hirsch, Fabrice and Leal, Gon\c{c}alo and Schuller, Bj\"orn W.},
  journal={Under review},
  year={2026}
}
```

## License

Apache 2.0

## Acknowledgements

- Base model: [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53)
- Dataset: [SEP-28k / SEP-28k-Extended](https://github.com/apple/ml-stuttering-events-dataset)
- Developed by [Vocametrix](https://vocametrix.com)
