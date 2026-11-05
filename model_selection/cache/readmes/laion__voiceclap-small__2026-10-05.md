---
license: cc-by-4.0
language:
  - en
library_name: transformers
pipeline_tag: feature-extraction
tags:
  - audio
  - speech
  - emotion
  - clap
  - contrastive
  - voice
---

# VoiceCLAP-Small

Voice-text contrastive (CLAP-style) embedding model trained on dense vocal-style
captions for the VoiceNet suite.

VoiceCLAP-Small is the smaller of the two voice-text contrastive anchors
released with VoiceNet. It is a **dual-tower** model: a
[BUD-E-Whisper_V1.1](https://huggingface.co/laion/BUD-E-Whisper_V1.1) audio
encoder paired with
[`sentence-transformers/all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
on the text side, joined by an MLP projection on each side and trained with
the SigLIP sigmoid contrastive loss.

| | |
| --- | --- |
| Architecture | dual-tower CLAP (BUD-E-Whisper-Small + MiniLM-L6-v2) |
| Audio encoder | Whisper-style: 12 layers × 768 dim × 12 heads, 80-mel input @ 16 kHz |
| Text encoder | BERT/MiniLM, 6 layers × 384 dim, mean-pooled |
| Joint embedding | 768-d, L2-normalised |
| Loss | SigLIP (sigmoid contrastive) |
| Total parameters | ~110 M |
| Epochs | 1 |

## Training data

Trained for **1 epoch** on the open mixture (9 datasets)
used in the VoiceNet paper:

- `emolia-balanced-5M-subset` (annotated subset of [Emilia](https://huggingface.co/datasets/amphion/Emilia-Dataset))
- `laions_got_talent_clean_with_captions`
- `majestrino-data`
- `synthetic_vocal_bursts`
- `improved_synthetic_vocal_bursts`
- `ears`
- `expresso`
- `voxceleb1`
- `voxceleb2`

All clips are captioned with `MOSS-Audio-8B-Thinking`-derived dense vocal-style
captions covering emotions, talking-style attributes, and demographics.

## Standalone load example

Only `transformers` and `torchaudio` are required (both on PyPI).

```python
import torch, torchaudio
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("laion/voiceclap-small", trust_remote_code=True).eval()
tok   = AutoTokenizer.from_pretrained("laion/voiceclap-small")

# Audio: any-length 16 kHz waveform, mono
wav, sr = torchaudio.load("clip.wav")
if sr != 16000:
    wav = torchaudio.functional.resample(wav, sr, 16000)
wav = wav.mean(0)                                         # (T,)
audio_emb = model.encode_waveform(wav)                    # (1, 768), L2-normed

# Text: short caption(s)
enc      = tok(["a calm and steady voice"], padding=True, return_tensors="pt")
text_emb = model.encode_text(enc.input_ids, enc.attention_mask)

# Cosine similarity (embeddings already L2-normalised)
print((audio_emb @ text_emb.T).item())
```

`encode_waveform` accepts any-length 16 kHz mono input. Clips at or below 30 s
are zero-padded to a full 30 s window (matching Whisper's training-time
padding); longer clips are split into non-overlapping 30 s chunks whose
embeddings are averaged and re-normalised. Embeddings are 768-d and unit-norm,
so `a @ t.T` is the cosine similarity used in zero-shot retrieval.

## Citation

If you use this model, please cite the VoiceNet paper.
