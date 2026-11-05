---
language:
  - en
  - gu
license: apache-2.0
tags:
  - speech
  - audio
  - automatic-speech-recognition
  - meta-asr
  - emotion-recognition
  - speaker-profiling
  - intent-detection
  - entity-extraction
  - wav2vec2
  - ctc
  - gujarati
  - english
  - gujlish
  - code-switching
datasets:
  - mozilla-foundation/common_voice_17_0
  - google/fleurs
  - ai4bharat/IndicVoices
  - ai4bharat/IndicVoices-R
  - Kathbath
model-index:
  - name: speech-tagger_gujlish_wav2vec2_meta
    results:
      - task:
          type: automatic-speech-recognition
          name: Speech Recognition
        dataset:
          type: custom
          name: In-House Gujlish Test Set
        metrics:
          - type: wer
            value: 20.31
            name: WER (English)
          - type: wer
            value: 29.95
            name: WER (Gujarati)
      - task:
          type: audio-classification
          name: Speaker Age Classification
        dataset:
          type: custom
          name: In-House Gujlish Test Set
        metrics:
          - type: accuracy
            value: 82.3
            name: Age Accuracy (avg EN+GU)
      - task:
          type: audio-classification
          name: Speaker Gender Classification
        dataset:
          type: custom
          name: In-House Gujlish Test Set
        metrics:
          - type: accuracy
            value: 98.1
            name: Gender Accuracy (avg EN+GU)
      - task:
          type: audio-classification
          name: Emotion Recognition
        dataset:
          type: custom
          name: In-House Gujlish Test Set
        metrics:
          - type: accuracy
            value: 82.6
            name: Emotion Accuracy (avg EN+GU)
pipeline_tag: automatic-speech-recognition
library_name: transformers
---

# WhissleAI Gujlish wav2vec2 Meta-ASR

A **bilingual English-Gujarati (Gujlish) speech recognition model** that simultaneously transcribes speech and extracts rich metadata — speaker age, gender, emotion, intent, and named entities — in a single forward pass using CTC decoding.

## Model Description

This model is fine-tuned from **CLSRIL-23** (a wav2vec2-base model pre-trained on 23 Indian languages by IIT Madras) for bilingual English + Gujarati ASR with inline meta-tag prediction. It uses a unified character-level vocabulary with atomic meta-tag tokens, enabling the CTC head to output both transcript text and structured metadata.

| Property | Value |
|----------|-------|
| **Architecture** | Wav2Vec2ForCTC (HuggingFace Transformers) |
| **Base Model** | [CLSRIL-23](https://arxiv.org/abs/2107.07402) (wav2vec2-base, 23 Indian languages) |
| **Parameters** | 94.7M |
| **Vocab Size** | 795 tokens (characters + meta-tags) |
| **Languages** | English (EN), Gujarati (GU), Code-switched Gujlish |
| **Input** | Raw 16kHz waveform |
| **Output** | CTC logits → transcript + AGE/GENDER/EMOTION/INTENT/ENTITY tags |
| **Training Framework** | PyTorch Lightning + HuggingFace Transformers |

## Meta-Tags

The model predicts the following inline tags alongside the transcript:

| Tag Category | Possible Values |
|-------------|----------------|
| **AGE** | `AGE_0_18`, `AGE_18_30`, `AGE_30_45`, `AGE_45_60`, `AGE_60PLUS` |
| **GENDER** | `GENDER_MALE`, `GENDER_FEMALE`, `GENDER_OTHER` |
| **EMOTION** | `EMOTION_NEUTRAL`, `EMOTION_HAPPY`, `EMOTION_SAD`, `EMOTION_ANGRY`, `EMOTION_DISGUST`, `EMOTION_FEAR`, `EMOTION_SURPRISE` |
| **INTENT** | `INTENT_INFORM`, `INTENT_QUESTION`, `INTENT_COMMAND`, `INTENT_REQUEST`, `INTENT_GREETING`, `INTENT_THANK` |
| **ENTITY** | `ENTITY_PERSON_NAME ... END`, `ENTITY_LOCATION ... END`, `ENTITY_ORGANIZATION ... END`, etc. |

Example output:
```
the weather in ahmedabad is very hot today ENTITY_LOCATION END AGE_30_45 GENDER_MALE EMOTION_NEUTRAL INTENT_INFORM
```

## Performance

### ASR (Word Error Rate)

| Language | Full WER | Clean WER | Samples |
|----------|----------|-----------|---------|
| **English** | 20.31% | 15.59% | 500 |
| **Gujarati** | 29.95% | 23.13% | 500 |

- **Full WER** = WER on raw output (transcript + tags)
- **Clean WER** = WER on transcript only (tags stripped)

### Meta-Tag Accuracy

| Tag | English | Gujarati |
|-----|---------|----------|
| **Age** | 80.6% | 84.0% |
| **Gender** | 96.8% | 99.4% |
| **Emotion** | 81.8% | 83.3% |
| **Intent** | 80.1% | 83.5% |
| **Entity F1** | 40.8% | 14.4% |

### Latency

| Metric | Value |
|--------|-------|
| Avg inference latency | **5.7 ms** per utterance |
| Real-time factor (RTF) | < 0.01x |

> Measured on NVIDIA A100 GPU, batch_size=1, average utterance ~5 seconds.

## Usage

### Quick Start (HuggingFace)

```python
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC
import json

# Load model
model = Wav2Vec2ForCTC.from_pretrained("WhissleAI/speech-tagger_gujlish_wav2vec2_meta")
model.eval()

# Load vocab
from huggingface_hub import hf_hub_download
vocab_path = hf_hub_download("WhissleAI/speech-tagger_gujlish_wav2vec2_meta", "vocab.json")
with open(vocab_path) as f:
    vocab = json.load(f)
id_to_token = {v: k for k, v in vocab.items()}

# Load audio
waveform, sr = torchaudio.load("test.wav")
if sr != 16000:
    waveform = torchaudio.functional.resample(waveform, sr, 16000)
waveform = waveform.mean(dim=0) if waveform.shape[0] > 1 else waveform.squeeze(0)

# Inference
with torch.no_grad():
    logits = model(input_values=waveform.unsqueeze(0)).logits

# CTC greedy decode
pred_ids = torch.argmax(logits, dim=-1)[0].tolist()
collapsed = []
prev = -1
for p in pred_ids:
    if p != prev and p != 0:  # 0 = <pad>/blank
        collapsed.append(p)
    prev = p

text = "".join(id_to_token.get(i, "") if id_to_token.get(i) != "|" else " " for i in collapsed).strip()
print(text)
```

### Using the Inference Script

```bash
# Install dependencies
pip install torch torchaudio transformers huggingface_hub numpy

# Transcribe a single file
python infer_wav2vec2_gujlish.py --model WhissleAI/speech-tagger_gujlish_wav2vec2_meta --audio test.wav

# Batch transcribe from manifest
python infer_wav2vec2_gujlish.py \
    --model WhissleAI/speech-tagger_gujlish_wav2vec2_meta \
    --manifest test.json \
    --output results.json \
    --batch-size 16 \
    --device cuda
```

### From PyTorch Lightning Checkpoint (.ckpt)

```bash
python infer_wav2vec2_gujlish.py \
    --model ./checkpoints/gujlish-wav2vec2-clsril23-v1-step=65000-val_wer=0.2610.ckpt \
    --pretrained ./CLSRIL-23.pt \
    --vocab ./vocab.json \
    --audio test.wav
```

## Training Details

### Data

| Dataset | Language | Samples | Source |
|---------|----------|---------|--------|
| CommonVoice 17 (English) | EN | ~250K | Mozilla |
| CommonVoice 17 (Gujarati) | GU | ~5K | Mozilla |
| IndicVoices | GU | ~50K | AI4Bharat |
| IndicVoices-R | GU | ~10K | AI4Bharat |
| Kathbath | GU | ~30K | AI4Bharat |
| FLEURS (Gujarati) | GU | ~2K | Google |
| Internal recordings | EN+GU | ~70K | Whissle |
| **Total** | | **525,500** train / **26,669** valid | |

Language split: 68.6% English, 31.4% Gujarati (INDO_ARYAN family).

All training samples were annotated with meta-tags (AGE, GENDER, EMOTION, INTENT, ENTITY) using Whissle's automated annotation pipeline powered by Gemini.

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Base model | CLSRIL-23 (wav2vec2-base, 23 Indian languages) |
| Feature extractor | Frozen |
| Batch size | 48 (effective: 96 with grad accumulation) |
| Learning rate | 1e-4 |
| Weight decay | 0.005 |
| Warmup steps | 3,000 |
| Max steps | 100,000 |
| Max audio duration | 16s |
| Precision | Mixed (FP16) |
| Noise augmentation | 70% probability, SNR -40 to -10 dB |
| Best checkpoint | step=65,000 (val_wer=0.261) |

### Training Procedure

1. **Pretrained checkpoint**: CLSRIL-23 (fairseq format) → converted to HuggingFace `Wav2Vec2ForCTC`
2. **Vocabulary**: Built from training manifest — 795 tokens (characters for both scripts + meta-tags)
3. **Feature extractor frozen**: Only the transformer encoder and CTC head are fine-tuned
4. **CTC loss**: Standard CTC with blank token `<pad>` (id=0)
5. **Per-language WER tracking**: Separate validation metrics for English and Gujarati

## Architecture

```
Raw Audio (16kHz)
       │
       ▼
┌──────────────────┐
│ Feature Extractor │  ← Frozen (7 conv layers, stride=320)
│ (CNN)            │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Feature Projection│  ← 512 → 768
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Transformer      │  ← 12 layers, 768 hidden, 12 heads
│ Encoder          │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ CTC Head         │  ← Linear(768 → 795)
│ (lm_head)        │
└────────┬─────────┘
         │
         ▼
  CTC Greedy Decode
         │
         ▼
"hello world AGE_30_45 GENDER_MALE EMOTION_NEUTRAL INTENT_INFORM"
```

## Limitations

- **Gujarati script**: The model handles Gujarati script but WER is higher than English (23% vs 16% clean WER) due to less training data
- **Entity extraction**: Entity F1 is moderate for English (41%) and lower for Gujarati (14%) — primarily trained on person names and locations
- **Code-switching**: While the model handles English-Gujarati code-switching, rapid intra-sentential switching may increase WER
- **Noise robustness**: Trained with aggressive noise augmentation but performance degrades significantly below 5dB SNR
- **Max duration**: Trained on utterances up to 16 seconds; longer audio should be chunked

## ONNX Export

An ONNX-exported version of this model is available for production deployment. The ONNX model supports dynamic batch size and sequence length:

```python
import onnxruntime as ort
import numpy as np

session = ort.InferenceSession("model.onnx")
audio = np.random.randn(1, 48000).astype(np.float32)  # 3 seconds
logits = session.run(None, {"input_values": audio})[0]
```

## Citation

```bibtex
@misc{whissle2025gujlish,
  title={Gujlish Meta-ASR: Bilingual English-Gujarati Speech Recognition with Inline Metadata Prediction},
  author={Whissle AI},
  year={2025},
  url={https://huggingface.co/WhissleAI/speech-tagger_gujlish_wav2vec2_meta}
}
```

## License

This model is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

## About WhissleAI

[WhissleAI](https://whissle.ai) builds production-grade speech AI systems. Our Meta-ASR models jointly perform speech recognition and speaker/content analysis in a single pass, enabling real-time applications like live coaching, meeting intelligence, and voice analytics.

- Website: [whissle.ai](https://whissle.ai)
- GitHub: [github.com/WhissleAI](https://github.com/WhissleAI)
- HuggingFace: [huggingface.co/WhissleAI](https://huggingface.co/WhissleAI)
