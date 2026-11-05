---
license: apache-2.0
library_name: transformers
pipeline_tag: audio-classification
tags:
  - wav2vec2
  - speech
  - emotion-recognition
---

# vocaliz-wav2vec2-speech-emotion-recognition-finetuned

This model is a **fine-tuned** checkpoint built on top of:

**Base model:** [`Wiam/wav2vec2-lg-xlsr-en-speech-emotion-recognition-finetuned-ravdess-v8`](https://huggingface.co/Wiam/wav2vec2-lg-xlsr-en-speech-emotion-recognition-finetuned-ravdess-v8) (Wav2Vec2 / XLSR-style encoder with an 8-class speech-emotion head, originally associated with RAVDESS-oriented training).

Training used the Hugging Face `Trainer` with `AutoModelForAudioClassification`, keeping the same label space and classification head structure as the base checkpoint.

---

## Intended uses

- **Research and prototyping** for speech emotion recognition (SER) on **English**, short utterance-level clips.
- **Offline or interactive demos** (e.g. file-based or microphone pipelines) where approximate emotion labels are sufficient.


## Training data

### Source mix (by file count)

Combined **Emotions** training pool (all classes, all files):

| Source   | Files | Share (approx.) |
|----------|------:|------------------:|
| CREMA-D  | 7,442 | 58.15% |
| TESS     | 2,800 | 21.88% |
| RAVDESS  | 2,076 | 16.22% |
| SAVEE    |   480 |  3.75% |
| **Total**| **12,798** | **100%** |

### Training procedure (defaults from training script)

| Setting | Value |
|--------|--------|
| Train / validation split | **Stratified** ~85% / ~15% (`test_size=0.15`, `seed=42`) → ~**10,878** train / ~**1,920** validation samples (exact counts depend on per-class stratification) |
| Epochs | **5** |
| Optimizer | AdamW with **learning rate 3e-5**, **warmup ratio 0.1**, **weight decay 0.01** |
| Batch size | **4** per device |
| Max audio length | **8 s** after resampling (truncation) |
| **Training metrics** (per validation) | **Accuracy**, **macro F1** |
| Model selection | **Best checkpoint by validation macro F1** (`load_best_model_at_end=True`) |
| Precision | FP16 only if CUDA + `--fp16` (default run often CPU) |


---

## Evaluation results (external benchmark)

metrics with six displayed classes: `neutral`, `happy`, `angry`, `fearful`, `disgust`, `surprised`.

| Model | Accuracy | Macro F1 | Weighted F1 | Micro F1 |
|-------|----------|----------|--------------|----------|
| Base: `Wiam/wav2vec2-lg-xlsr-en-speech-emotion-recognition-finetuned-ravdess-v8` | 0.9417 | 0.9367 | 0.9414 | 0.9417 |
| **This fine-tune** (local export `wav2vec2-emotions-finetuned`) | **0.9868** | **0.9850** | **0.9868** | **0.9868** |


---

## How to load

```python
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor

MODEL_ID = "amykon/vocaliz-wav2vec2-speech-emotion-recognition-finetuned"

processor = AutoFeatureExtractor.from_pretrained(MODEL_ID)
model = AutoModelForAudioClassification.from_pretrained(MODEL_ID)
```

Public repo: no token needed for `from_pretrained`. Private repo: set `HF_TOKEN` or `huggingface-cli login`.

---

## Install dependencies

```bash
pip install -r https://huggingface.co/amykon/vocaliz-wav2vec2-speech-emotion-recognition-finetuned/resolve/main/requirements.txt
```

`requirements.txt` lists `torch`, `transformers`, `safetensors`, `huggingface_hub`, `numpy`, and `sounddevice` (optional for mic-only scripts).

---

## Files in this repository

- `README.md` — this model card  
- `requirements.txt` — pip dependencies for inference  
- `config.json` — model config and label mapping  
- `preprocessor_config.json` — feature extractor (sample rate, etc.)  
- `model.safetensors` — weights  
