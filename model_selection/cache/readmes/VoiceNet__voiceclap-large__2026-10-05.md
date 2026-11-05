---
license: cc-by-4.0
language:
  - en
library_name: sentence-transformers
pipeline_tag: feature-extraction
base_model: LCO-Embedding/LCO-Embedding-Omni-7B
tags:
  - audio
  - speech
  - emotion
  - clap
  - contrastive
  - voice
  - sentence-transformers
---

# VoiceCLAP-Large

Voice-text contrastive embedding model — the larger of the two anchors
released with [VoiceNet](https://huggingface.co/VoiceNet).

VoiceCLAP-Large is a **single-tower** model: a rank-16 LoRA finetune of
[LCO-Embedding-Omni-7B](https://huggingface.co/LCO-Embedding/LCO-Embedding-Omni-7B)
(Qwen2.5-Omni-Thinker-7B backbone with a sentence-transformer
last-token-pooling head) trained with the symmetric InfoNCE loss. The audio
and text embeddings are produced by the same backbone — the modality is
determined by what is fed in via the multimodal chat template.

| | |
| --- | --- |
| Architecture | single-tower Omni-Embedding (Qwen2.5-Omni-Thinker-7B + ST last-token-pool) |
| Adaptation | rank-16 LoRA (alpha 32, dropout 0.05), merged into the released weights |
| Joint embedding | 3 584-d, L2-normalised |
| Loss | symmetric InfoNCE (all-gather negatives) |
| Total parameters | ~7 B (full merged model) |
| Epochs | 1 |

## Training data

Trained for **1 epoch** on the open `voiceclap_10_safe` mixture (9 datasets)
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

All clips are captioned with `MOSS-Audio-8B-Thinking`-derived dense
vocal-style captions covering emotions, talking-style attributes, and
demographics.

## Standalone load example

The model uses the SentenceTransformer multimodal API — both
`sentence-transformers` and `transformers` are on PyPI; no other deps are
required.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("VoiceNet/voiceclap-large", trust_remote_code=True)

# Text embedding (3 584-d, L2-normalised)
text_emb = model.encode(["a calm and steady voice"])

# Audio embedding — pass a dict with raw samples + sampling rate.
import soundfile as sf
arr, sr = sf.read("clip.wav")
audio_emb = model.encode([{"array": arr, "sampling_rate": sr}])

# Cosine similarity (embeddings already L2-normalised)
print((audio_emb @ text_emb.T).item())
```

For convenience the LoRA adapter is also shipped under `adapter/` so it can
be reapplied to other LCO-Embedding-Omni-7B forks; the merged
`model.safetensors` already contains it.

## Citation

If you use this model, please cite the VoiceNet paper.
