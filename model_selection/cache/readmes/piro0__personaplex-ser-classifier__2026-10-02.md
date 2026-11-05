---
language: en
tags:
  - audio
  - speech
  - emotion-recognition
  - wav2vec2
  - pytorch
datasets:
  - ravdess
  - cremad
metrics:
  - accuracy
  - f1
---

# PersonaPlex SER Classifier

Speech Emotion Recognition classifier fine-tuned on RAVDESS and CREMA-D.
Built as part of the PersonaPlex 7B vector steering research project (CSE465).

## Model Description
- **Base model:** facebook/wav2vec2-base
- **Task:** 4-class speech emotion recognition
- **Classes:** angry, happy, neutral, sad
- **Fine-tuned on:** RAVDESS (1344 samples) + CREMA-D (4900 samples)
- **Total speakers:** 115 (92 train, 23 test)
- **Split strategy:** Speaker-level split (no overlap between train/test)

## Performance
| Model | Accuracy |
|---|---|
| SVM Baseline | 65.9% |
| Wav2Vec2 (this model) | 83.1% |
| Improvement | +17.2% |

### Per-Class Results
| Emotion | Precision | Recall | F1 |
|---|---|---|---|
| Angry | 0.87 | 0.95 | 0.91 |
| Happy | 0.85 | 0.75 | 0.80 |
| Neutral | 0.72 | 0.86 | 0.79 |
| Sad | 0.87 | 0.77 | 0.82 |

## Known Limitations
- Trained on acted emotional speech — may not generalize to AI-generated audio (domain shift)
- Happy/neutral confusion is a known challenge in SER

## Artifacts Included
- `label_encoder.json` — emotion class index mapping
- `training_config.json` — full training configuration
- `training_results.json` — metrics and dataset stats
- `confusion_matrix_wav2vec2.png` — Wav2Vec2 confusion matrix
- `confusion_matrix_svm.png` — SVM baseline confusion matrix
- `domain_shift_comparison.png` — angry probability across steering conditions
- `wav2vec2_inference_results.csv` — per-file predictions on PersonaPlex outputs
- `svm_inference_results.csv` — SVM predictions on PersonaPlex outputs
- `caa_waveform.png` — example CAA steered audio waveform

## Usage
```python
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor
from huggingface_hub import hf_hub_download
import torch, librosa, numpy as np, json

model = Wav2Vec2ForSequenceClassification.from_pretrained('YOUR_USERNAME/personaplex-ser-classifier')
processor = Wav2Vec2Processor.from_pretrained('YOUR_USERNAME/personaplex-ser-classifier')

le_file = hf_hub_download('YOUR_USERNAME/personaplex-ser-classifier', 'label_encoder.json')
with open(le_file) as f:
    classes = json.load(f)

def predict(audio_path, sr=16000, duration=3):
    y, _ = librosa.load(audio_path, sr=sr, duration=duration)
    if len(y) < sr * duration:
        y = np.pad(y, (0, sr * duration - len(y)))
    inputs = processor(y, sampling_rate=sr, return_tensors='pt')
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1).numpy()[0]
    return classes[np.argmax(probs)], dict(zip(classes, probs.tolist()))
```
