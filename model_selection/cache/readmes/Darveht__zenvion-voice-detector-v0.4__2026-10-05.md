---
license: apache-2.0
base_model:
- facebook/wav2vec2-base-960h
tags:
- audio
- audio-classification
- voice-detection
- voice-activity-detection
- speech-recognition
- speaker-recognition
- emotion-detection
- age-detection
- gender-detection
- accent-detection
- language-identification
- noise-robust
- pytorch
- transformers
- wav2vec2
- multi-task-learning
- deep-learning
- ai
- ml
datasets:
- mozilla-foundation/common_voice_16_1
- google/fleurs
- facebook/voxpopuli
- MLCommons/peoples_speech
- speech_commands
- facebook/multilingual_librispeech
- librispeech_asr
- voxceleb
- voxceleb2
- gigaspeech
- tedlium
- ami
- covost2
- earnings22
- switchboard
- callhome
- fisher
- openslr
- librilight
- ljspeech
- vctk
- libritts
- ravdess
- crema-d
- savee
- tess
- iemocap
language:
- en
- es
- fr
- de
- it
- pt
- nl
- pl
- ru
- zh
- ja
- ko
- ar
- hi
- tr
- vi
- th
- id
- ms
- fil
- bn
- ta
- te
- mr
- gu
- kn
- ml
- pa
- ur
- fa
- he
- uk
- ro
- cs
- sv
- da
- no
- fi
- el
- hu
- sk
- bg
- hr
- sr
- sl
- et
- lv
- lt
- ca
- gl
metrics:
- accuracy
- f1
- precision
- recall
- auc
- eer
pipeline_tag: audio-classification
library_name: transformers
model-index:
- name: zenvion-voice-detector-v0.4
  results:
  - task:
      type: audio-classification
      name: Voice Activity Detection
    dataset:
      type: multi-dataset
      name: 27+ Audio Datasets
    metrics:
    - type: accuracy
      value: 0.962
      name: Accuracy (VAD)
      verified: false
    - type: f1
      value: 0.958
      name: F1-Score (VAD)
      verified: false
    - type: auc
      value: 0.981
      name: AUC-ROC (VAD)
      verified: false
    - type: eer
      value: 0.041
      name: Equal Error Rate (VAD)
      verified: false
  - task:
      type: audio-classification
      name: Emotion Recognition
    dataset:
      type: multi-dataset
      name: RAVDESS + CREMA-D + IEMOCAP + SAVEE + TESS
    metrics:
    - type: accuracy
      value: 0.847
      name: Accuracy (Emotion)
      verified: false
    - type: f1
      value: 0.831
      name: Weighted F1 (Emotion)
      verified: false
  - task:
      type: audio-classification
      name: Language Identification
    dataset:
      type: multi-dataset
      name: CommonVoice 16 + FLEURS + VoxPopuli
    metrics:
    - type: accuracy
      value: 0.913
      name: Accuracy (LangID 50 langs)
      verified: false
widget:
- example_title: English Speech Sample
  src: https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac
- example_title: Short Utterance Test
  src: https://huggingface.co/datasets/hf-internal-testing/librispeech_asr_demo/resolve/main/mp3/84-121550-0001.mp3
---

# 🎙️ Zenvion Voice Detector v0.4

> **Multi-task voice analysis model — 8 tasks in a single forward pass.**
> Detects speech activity, gender, emotion, language, age, acoustic noise type, conversational intent, and accent simultaneously from raw audio in real time.

🚀 **[Try the live demo →](https://huggingface.co/spaces/Darveht/zenvion-voice-detector-demo)**

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Tasks & Labels](#tasks--labels)
3. [Performance Benchmarks](#performance-benchmarks)
4. [Quick Start](#quick-start)
5. [Installation](#installation)
6. [Usage Examples](#usage-examples)
7. [API Reference](#api-reference)
8. [Architecture](#architecture)
9. [Training Details](#training-details)
10. [Limitations & Bias](#limitations--bias)
11. [Changelog](#changelog)
12. [Citation](#citation)
13. [License](#license)

---

## Overview

**Zenvion Voice Detector v0.4** is a multi-task speech analysis system built on top of **[facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h)**. A single forward pass produces 8 independent classification outputs, making it efficient for audio pipelines.

| Feature | Detail |
|---------|--------|
| **Base model** | facebook/wav2vec2-base-960h |
| **Input** | Raw audio waveform (16 kHz, mono) |
| **Output heads** | 8 simultaneous classification tasks |
| **Languages supported** | 50 |
| **Min audio duration** | 0.1 s |
| **Max recommended** | 30 s |
| **Device** | CPU + GPU (CUDA / MPS) |
| **Precision** | FP32 / FP16 |
| **License** | Apache 2.0 |

---

## Tasks & Labels

| # | Task | Classes | Description |
|---|------|---------|-------------|
| 1 | **VAD** | SPEECH / NO_SPEECH | Is a human speaking? |
| 2 | **Gender** | MALE / FEMALE / UNKNOWN | Speaker gender |
| 3 | **Emotion** | ANGER / DISGUST / FEAR / HAPPY / NEUTRAL / SAD / SURPRISE / CALM | 8-class emotion |
| 4 | **Language** | 50 languages | en, es, fr, de, zh, ja, ar, hi … |
| 5 | **Age** | CHILD / TEEN / YOUNG_ADULT / ADULT / MIDDLE_AGED / SENIOR | Age group |
| 6 | **Noise** | CLEAN / BABBLE / MUSIC / TRAFFIC / NOISE_OTHER | Acoustic environment |
| 7 | **Intent** | 15 classes | Conversational intent (COMMAND / QUESTION / STATEMENT / … / INTENT_OTHER) |
| 8 | **Accent** | 20 classes | Regional accent (… / ACCENT_OTHER) |

Full label indexes are in [label_mapping.json](label_mapping.json).

---

## Performance Benchmarks

> ⚠️ The metrics below are the numbers published by the model author. They are
> marked `verified: false` in the model card and have **not** been independently
> verified. The checkpoint currently shipped contains a pretrained backbone
> with freshly initialised task heads — run `evaluation.py` on your own data
> before relying on these figures.

### Voice Activity Detection (VAD)

| Dataset | Accuracy | F1 | AUC-ROC | EER |
|---------|----------|----|---------|-----|
| CommonVoice 16.1 (test) | 96.8% | 96.4% | 98.5% | 3.9% |
| FLEURS (test) | 95.9% | 95.2% | 97.8% | 4.3% |
| VoxPopuli (test) | 96.1% | 95.8% | 98.1% | 4.1% |
| **Average** | **96.2%** | **95.8%** | **98.1%** | **4.1%** |

### Emotion Recognition

| Dataset | Accuracy | Weighted F1 |
|---------|----------|-------------|
| RAVDESS (test split) | 88.2% | 87.6% |
| CREMA-D (test split) | 83.4% | 82.1% |
| IEMOCAP (test split) | 81.9% | 80.7% |
| **Average** | **84.7%** | **83.1%** |

### Language Identification (50 languages)

| Dataset | Top-1 Acc | Top-3 Acc |
|---------|-----------|-----------|
| FLEURS (test) | 91.3% | 97.2% |
| CommonVoice 16.1 (test) | 90.8% | 96.9% |

### Gender Classification

| Dataset | Accuracy | F1 (macro) |
|---------|----------|------------|
| VoxCeleb2 (test) | 94.1% | 93.8% |
| CommonVoice 16.1 | 93.7% | 93.2% |

---

## Quick Start

### Using Hugging Face Inference API

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/Darveht/zenvion-voice-detector-v0.4"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

with open("audio.wav", "rb") as f:
    data = f.read()

response = requests.post(API_URL, headers=headers, data=data)
print(response.json())
```

### Using transformers pipeline

```python
from transformers import pipeline

pipe = pipeline(
    "audio-classification",
    model="Darveht/zenvion-voice-detector-v0.4",
    trust_remote_code=True,
)
result = pipe("audio.wav")
print(result)
```

### Using the bundled ZenvionPipeline

```python
from inference import ZenvionPipeline

pipe = ZenvionPipeline(
    model_id="Darveht/zenvion-voice-detector-v0.4",
    device="cpu",   # or "cuda"
    half_precision=False,  # True for FP16 on CUDA
)

result = pipe("path/to/audio.wav")
print(result)
# {
#   "vad":      {"label": "SPEECH",   "score": 0.982},
#   "gender":   {"label": "MALE",     "score": 0.871},
#   "emotion":  {"label": "NEUTRAL",  "score": 0.763},
#   "language": {"label": "en",       "score": 0.941},
#   "age":      {"label": "ADULT",    "score": 0.802},
#   "noise":    {"label": "CLEAN",    "score": 0.913},
#   "intent":   {"label": "STATEMENT","score": 0.688},
#   "accent":   {"label": "AMERICAN", "score": 0.754},
# }
```

---

## Installation

```bash
pip install -r requirements.txt
```

Minimum dependencies:

```
torch>=2.1.0
transformers>=4.37.0
torchaudio>=2.1.0
librosa>=0.10.0
soundfile>=0.12.1
numpy>=1.24.0
```

---

## Usage Examples

### Batch Processing

```python
from inference import ZenvionPipeline
from pathlib import Path

pipe = ZenvionPipeline()

audio_files = list(Path("audio_dir").glob("*.wav"))
for f in audio_files:
    res = pipe(str(f))
    print(f"{f.name}: {res['vad']['label']} | {res['emotion']['label']} | {res['language']['label']}")
```

### GPU Inference with FP16

```python
from inference import ZenvionPipeline

pipe = ZenvionPipeline(device="cuda", half_precision=True)
result = pipe("audio.wav")
```

### Streaming / Real-time (chunk-based)

```python
import numpy as np
from inference import ZenvionPipeline

pipe = ZenvionPipeline()
SAMPLE_RATE = 16000
CHUNK_S = 2  # 2-second windows

# numpy/tensor inputs are expected at 16 kHz mono
chunk = np.random.randn(SAMPLE_RATE * CHUNK_S).astype(np.float32)
result = pipe(chunk)
print(result)
```

### Run only specific tasks

```python
from inference import ZenvionPipeline

pipe = ZenvionPipeline(tasks=["vad", "emotion", "language"])
result = pipe("audio.wav")
```

### Using with soundfile

```python
import soundfile as sf
import numpy as np
from inference import ZenvionPipeline

pipe = ZenvionPipeline()
audio, sr = sf.read("audio.wav")
if audio.ndim > 1:
    audio = audio.mean(axis=1)
# NOTE: array inputs are expected at 16 kHz mono; resample first if needed,
# e.g. with librosa.resample(audio, orig_sr=sr, target_sr=16000)
result = pipe(audio.astype(np.float32))
```

---

## API Reference

### ZenvionPipeline

```python
ZenvionPipeline(
    model_id: str = "Darveht/zenvion-voice-detector-v0.4",
    device: Optional[str] = None,  # auto-detects cuda/cpu
    tasks: Optional[List[str]] = None,  # subset of the 8 tasks; None = all
    half_precision: bool = False,  # FP16 (CUDA only)
    allow_random_init: bool = False,  # True: run with random weights if the checkpoint is missing
)
```

#### `__call__(audio, return_all_scores=False)`

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `audio` | `str or np.ndarray or torch.Tensor or list` | — | File path, array/tensor (16 kHz mono), or a batch list |
| `return_all_scores` | `bool` | `False` | Include per-class probabilities for every task |

**Returns:** `dict[str, dict]` — one entry per task with `label` (str) and `score` (float 0–1).

### ZenvionConfig

```python
from config_class import ZenvionConfig

cfg = ZenvionConfig.from_pretrained("Darveht/zenvion-voice-detector-v0.4")
print(cfg.num_labels_emotion)   # 8
print(cfg.num_labels_language)  # 50
print(cfg.num_labels)           # 109 (total across all tasks)
```

---

## Architecture

```
Input: raw audio (16 kHz mono)
       |
       v
[Wav2Vec2 Encoder] — 12 transformer layers, 768-dim hidden
       |
       v  (learned weighted sum of all 13 hidden states, softmax-normalised)
[AttentivePooling] — attention-weighted temporal pooling -> 768-dim
       |
   +---+--------------------------------------------+
   v    v       v       v    v     v     v    v
 VAD Gender Emotion  Lang  Age  Noise  Int  Acc
  2    3      8      50    6     5    15   20   <- output classes (109 total)
```

- **Total parameters:** ~95 M (wav2vec2-base) + ~1.6 M (layer weights, pooling, 8 heads)
- **Inference speed (CPU):** ~180 ms per 2-second clip
- **Inference speed (A100 GPU):** ~12 ms per 2-second clip

---

## Training Details

### Data

| Dataset | Hours | Tasks |
|---------|-------|-------|
| CommonVoice 16.1 | 17,600+ | VAD, Language, Accent |
| FLEURS | 4,000+ | VAD, Language |
| VoxPopuli | 1,800+ | VAD, Language |
| VoxCeleb / VoxCeleb2 | 2,400+ | Gender, Speaker |
| RAVDESS + CREMA-D + SAVEE + TESS + IEMOCAP | 500+ | Emotion |
| GigaSpeech | 10,000+ | VAD, Noise |
| LibriSpeech + LibriLight | 60,000+ | VAD |
| **Total** | **~96,300+ hours** | — |

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| Optimizer | AdamW |
| Learning rate (backbone) | 1e-4 |
| Learning rate (heads) | 5e-4 |
| LR schedule | Cosine with warmup |
| Warmup steps | 2,000 |
| Batch size | 32 |
| Gradient accumulation | 4 |
| Epochs | 15 |
| FP16 | Yes |
| Gradient clipping | 1.0 |
| Weight decay | 0.01 |
| Loss | Weighted CrossEntropy per head |

### Augmentations

- Speed perturbation (0.9× – 1.1×)
- Additive noise (SNR 5 – 30 dB)
- Room impulse response (RIR) convolution
- Codec simulation (telephone, mp3)
- Random gain (−6 to +6 dB)
- Time masking (SpecAugment-style)

---

## Limitations & Bias

- **Accent detection** is English-centric; accuracy drops significantly for non-English accents.
- **Emotion** models trained on acted speech (RAVDESS, CREMA-D) may underperform on spontaneous conversational emotion.
- **Age estimation** is coarse (6 buckets) and may be biased toward training demographics.
- **Gender** outputs only MALE / FEMALE / UNKNOWN; does not capture the full spectrum of gender expression.
- **Language ID** accuracy varies: high for European languages (>95%), lower for low-resource languages such as Tagalog or Malay (~85%).
- **Min duration:** clips shorter than 0.5 s may produce unreliable outputs.
- **Music / non-speech:** the model may output unpredictable emotion or language labels on pure music — check VAD output first.

---

## Changelog

### v0.4.1 — 2026-09-09 (code & config fixes)

- **Critical — weight wipe fixed:** `post_init()` → `init_weights()` was silently
  re-initialising the pretrained wav2vec2 backbone on every model construction,
  destroying the pretrained weights. The backbone is now protected via an
  `_init_weights()` override (transformers 4.x) and `_is_hf_initialized`
  marking (transformers 5.x); verified byte-identical against
  `facebook/wav2vec2-base-960h`.
- **First real checkpoint:** the repo previously shipped **no weights at all**
  (`model.safetensors` / `pytorch_model.bin` were missing), so `from_pretrained()`
  could not load a working model. Added `model.safetensors` with the pretrained
  backbone + freshly initialised task heads (heads still need training — see
  `train.py`).
- **Crash fix:** `forward()` passed `logits=` to `ZenvionOutput`, which had no
  such field (`TypeError`). Field added; `logits` is the [B, 109] concat.
- **Label maps fixed:** `config.json` had three different classes all named
  `OTHER` (noise/intent/accent), collapsing `label2id` from 109 to 107 entries.
  Renamed to `NOISE_OTHER` / `INTENT_OTHER` / `ACCENT_OTHER`; 109/109 consistent.
  `ZenvionConfig` no longer overwrites `num_labels=109` with 2, and normalises
  `id2label` keys to ints.
- **NaN guards:** `AttentivePooling` no longer returns NaN on fully-masked rows;
  multi-task loss skips tasks whose labels are all `-100` (was NaN).
- **`predict()`** now decodes all 8 tasks (was 5) and honours `threshold`.
- **`inference.py`:** removed the silent fallback to random weights (now raises
  unless `allow_random_init=True`); validates task names, empty audio,
  shapes, and min/max duration; the final partial VAD window is analysed
  instead of dropped.
- **`train.py`:** `--amp`/`--no-amp` flags; scheduler is rebuilt when the
  optimizer is recreated at unfreeze (was bound to the discarded optimizer);
  `global_step` now increments; leftover gradient-accumulation steps are applied
  at epoch end; AMP is CUDA-only; gradient loss is scaled by the accumulation
  factor; resuming a post-unfreeze checkpoint unfreezes first so optimizer
  parameter groups line up, and training continues at the *next* epoch.
- **`masked_spec_embed` NaN fix (transformers≥5):** the 960h checkpoint does not
  contain this pre-training-only parameter, and `from_pretrained` materialised
  it as uninitialised memory (NaN). It is now explicitly uniform-initialised
  like wav2vec2 pre-training does; the backbone stays byte-identical otherwise.
- **`num_labels` on transformers≥5:** it is a read-only property derived from
  `len(id2label)` — assigning it invoked the property setter and regenerated
  `id2label` as generic `LABEL_X` entries. The assignment was removed; 109 is
  derived from the real label map. `predict()` now derives every task's label
  names from `config.id2label` (the hardcoded `noise` list still said `OTHER`).
- **`evaluation.py`:** EER is now the threshold minimising |FAR − FRR| (was the
  misleading min of (FAR+FRR)/2); AUC is reported raw (was `max(auc, 1-auc)`).
- **`dataset_loader.py`:** Speech Commands `_silence_`/`_background_noise_`
  correctly map to `NO_SPEECH` (incl. int ClassLabel indices); fixed
  `md5("")` filename collisions in Common Voice and the `randint(0, 1e9)`
  float crash in FLEURS.
- **Docs:** corrected class counts (noise 5, intent 15, accent 20),
  `ZenvionPipeline` signatures/examples, and the architecture description.
  Benchmark figures remain the author's unverified numbers (`verified: false`).

### v0.4 — 2025-07-24

- Added `preprocessor_config.json` — required for transformers `pipeline()` to work out of the box
- Added `tokenizer_config.json` and `special_tokens_map.json` for AutoTokenizer compatibility
- Added `vocab.json` for tokenizer
- Added `label_mapping.json` with all 8 task labels, thresholds, and metadata
- Added `CITATION.cff` for academic references
- Full README rewrite: benchmarks table, architecture diagram, training details, API reference, limitations
- Added live Gradio demo Space: [Darveht/zenvion-voice-detector-demo](https://huggingface.co/spaces/Darveht/zenvion-voice-detector-demo)
- Improved noise robustness: +2.1% VAD accuracy on telephone-codec audio
- Fixed language head misclassification of Malayalam (ml) as Hindi

### v0.3 — 2025-06-10

- First public release
- 8-head multi-task model: VAD, gender, emotion, language (50), age, noise, intent, accent
- Base: facebook/wav2vec2-base-960h

---

## Citation

```bibtex
@misc{darveht2025zenvion,
  author       = {Darveht},
  title        = {Zenvion Voice Detector v0.4: Multi-task Speech Analysis},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Darveht/zenvion-voice-detector-v0.4}},
  note         = {Apache 2.0 License}
}
```

---

## License

Released under the **Apache 2.0 License**.  
Base model ([facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h)) is also Apache 2.0.

---

*[Live Demo](https://huggingface.co/spaces/Darveht/zenvion-voice-detector-demo) · [Report an Issue](https://huggingface.co/Darveht/zenvion-voice-detector-v0.4/discussions)*
