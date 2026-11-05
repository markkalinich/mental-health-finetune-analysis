---
license: cc-by-4.0
pipeline_tag: feature-extraction
library_name: sentence-transformers
tags:
- voice
- speech
- emotion
- audio-text
- clap
- contrastive
- lora
- prototypical-contrastive
- sentence-transformers
language:
- en
- de
- fr
- es
- zh
base_model: LCO-Embedding/LCO-Embedding-Omni-7B
---

# VoiceCLAP-Large-v2 (PCL)

A rank-16 LoRA finetune of **LCO-Embedding-Omni-7B** (Qwen2.5-Omni thinker)
trained with **InfoNCE + Prototypical Contrastive loss (PCL)** on the
VoiceCLAP 9-corpus mix with MOSS-Audio k=2 sampled captions. Successor to
[`laion/voiceclap-large`](https://huggingface.co/laion/voiceclap-large) —
**better on every benchmark we measure**.

## What's new vs voiceclap-large

1. **PCL auxiliary loss (weight 0.1)**: 39 learned emotion prototypes;
   cross-entropy of audio embeddings vs prototypes on pseudo-labeled clips.
2. **z-scored pseudo-labels**: emolia's `emotion_annotation` scalars,
   argmax over per-emotion z-scores vs corpus base rates (raw argmax is
   degenerate — high-base-rate dimensions win ~99% of clips). z ≥ 1.5
   labels ~80-98% of emolia across all 39 emotion classes.
3. LoRA rank 16 (α=32) — rank shown equivalent to r=32 in a controlled A/B.

## Evaluation (VoiceNet benchmark, human-annotated)

Same-commit comparison on the VoiceNet harness:

| Model | Emo bal@pp | Emo ρ | Ext bal@pp | Ext ρ |
|---|---|---|---|---|
| voiceclap-small | 0.6754 | 0.3176 | 0.6576 | 0.1116 |
| voiceclap-large (anchor re-run) | 0.6991 | 0.3598 | 0.6739 | 0.1897 |
| **this model (PCL ep1)** | **0.7069** | **0.3865** | **0.6816** | **0.2125** |

Controlled A/B vs its exact no-PCL twin (identical data/recipe, ep1):

| | emolia per-emo | emonet top-1 | emonet ρ |
|---|---|---|---|
| InfoNCE only | 0.6984 | 0.1411 | 0.3651 |
| **+ PCL w=0.1** | **0.7053** | **0.1544** | **0.3993** |

Ensemble notes: averaging this model's similarities with
`gijs/voiceclap-lco-7b-lora` and the k=10 MOSS variant sets the current
VoiceNet records (Emo bal@pp 0.7102; Ext bal@pp 0.6883).

## Training recipe

| | |
|---|---|
| Data | 7 corpora (emolia-balanced, Got Talent, Majestrino, bursts, VoxCeleb1/2) |
| Captions | original / k=2-sampled MOSS-Audio sentences, 50/50 |
| Samples seen | 76,000 (1 epoch; best checkpoint) |
| LoRA | r=16, α=32, dropout 0.05, all-linear |
| PCL | weight 0.1, 39 prototypes, temp 0.1, proto-lr 1e-3, z≥1.5 pseudo-labels |
| lr / wd | 1e-4 / 0.01, warmup 200, cosine |
| Batch | 4 × accum 8 × 4 GH200 = effective 128 |
| Precision | bf16 |

## Quick start

```python
import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "laion/voiceclap-large-v2",
    trust_remote_code=True,
    model_kwargs={"torch_dtype": torch.bfloat16},
)
audio_emb = model.encode("clip.flac")
text_emb  = model.encode("A person speaking with quiet pride in their voice")
score     = (audio_emb @ text_emb.T).item()
```

## License

cc-by-4.0

Confirmed by the rights holder (LAION) on 2026-09-09: the weights of this model
are released under CC BY 4.0. This licence statement is the rights holder's
determination for the released weights; see the training-data table above for
the corpora used and their own licences. `laion/voiceclap-commercial` is
offered for users who require a model whose training lineage contains no
non-commercially licensed corpus at all.
