---
license: cc-by-nc-4.0
language:
  - en
  - de
  - fr
  - es
  - zh
library_name: transformers
pipeline_tag: feature-extraction
tags:
  - audio
  - speech
  - emotion
  - clap
  - contrastive
  - voice
base_model: laion/voiceclap-small
---

# VoiceCLAP-Small-v2

Voice-text contrastive (CLAP-style) embedding model — the successor to
[`laion/voiceclap-small`](https://huggingface.co/laion/voiceclap-small),
trained with **emotion-led MOSS-Audio short captions**. Better than v1 on
every benchmark we measure, at identical size and inference cost.

Same dual-tower architecture as v1: a
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
| Training | 40 M samples (20 epochs × 2 M), best checkpoint epoch 19 |

## What's new vs v1

v1 sampled **k=2 uniformly-chosen MOSS-Audio attribute sentences** per clip
as the caption. v2 replaces this with an **emotion-led short caption**: the
MOSS-Audio-8B-Thinking `EMO` sentence (a direct natural-language description
of the emotional state) plus **one** randomly sampled talking-style sentence,
re-drawn every epoch. Captions stay 50/50 blended with each corpus's original
captions. The emotion-first structure concentrates contrastive signal on the
emotion subspace without sacrificing style coverage.

## Evaluation

| Benchmark | v1 (released) | **v2 (this model)** | Δ |
| --- | --- | --- | --- |
| EmoNet-Voice top-1 | 0.0902 | **0.1015** | +13% rel |
| EmoNet-Voice Spearman ρ | 0.2280 | **0.2561** | +12% rel |
| MAEB-voice mean (8 tasks) | 0.3861 | **0.3893** | +0.8% |

The ρ gain also clears every arm of the v1 caption-sampling sweep
(best: 0.2399 at k=2). MAEB-voice shows no general-speech regression.

## Training data

Trained on the open 9-corpus mixture used in the VoiceNet paper:

- `emolia-balanced-5M-subset` (annotated subset of [Emilia](https://huggingface.co/datasets/amphion/Emilia-Dataset))
- `laions_got_talent_clean_with_captions`
- `majestrino-data`
- `synthetic_vocal_bursts` + `improved_synthetic_vocal_bursts`
- `ears`, `expresso`, `voxceleb1`, `voxceleb2` (FCaps captions)

MOSS-Audio-8B-Thinking annotations (18 prompt groups, 61 attribute values
per clip) provide the EMO + style sentences for the three large corpora.

## Usage

```python
import torch
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("laion/voiceclap-small-v2", trust_remote_code=True).eval()
tok = AutoTokenizer.from_pretrained("laion/voiceclap-small-v2")

# audio: raw mono waveform at 16 kHz
import soundfile as sf
wav, sr = sf.read("clip.wav", dtype="float32")
audio_emb = model.encode_waveform(torch.from_numpy(wav))

# text
t = tok(["a person speaking with quiet pride in their voice"], padding=True, return_tensors="pt")
text_emb = model.encode_text(t["input_ids"], attention_mask=t["attention_mask"])

score = (audio_emb @ text_emb.T).item()
```

Conversion from the training checkpoint was verified functionally against the
original open_clip implementation (cosine ≥ 0.9999 on both towers).

## Sibling models

- [`laion/voiceclap-large-v2`](https://huggingface.co/laion/voiceclap-large-v2) — 7B single-tower successor trained with Prototypical Contrastive loss
- [`laion/voiceclap-small`](https://huggingface.co/laion/voiceclap-small), [`laion/voiceclap-large`](https://huggingface.co/laion/voiceclap-large) — v1 releases

## License

cc-by-nc-4.0
