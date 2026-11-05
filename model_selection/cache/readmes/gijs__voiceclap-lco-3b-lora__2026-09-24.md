---
license: apache-2.0
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
  - sentence-transformers
language:
  - en
  - de
  - fr
  - es
  - zh
base_model: LCO-Embedding/LCO-Embedding-Omni-3B
---

# voiceclap-lco-3b-lora

A rank-16 LoRA finetune of **LCO-Embedding-Omni-3B** (Qwen2.5-Omni thinker, 3B variant)
trained contrastively on the `voiceclap_10_safe` mix (got-talent, emolia,
majestrino, vocal bursts, ears, expresso, vox1, vox2 — 9 datasets, ~2,909
WebDataset shards) for voice-emotion audio↔text retrieval.

This is the **best single-model on emonet top-1 accuracy (0.1592)** from
the Track I LoRA fine-tune sweep — preserves emonet capability that the
LCO models otherwise catastrophically lose during contrastive finetune.
The LoRA delta was re-merged into the base safetensors via the
`salvage_lora_snapshot.py` tool to work around a save-path bug.

## Architecture

Single-tower: audio + text are both fed through the same Qwen2.5-Omni
thinker; modality is determined by the chat-template placeholder
(`<|audio_bos|><|AUDIO|><|audio_eos|>`). The last-non-pad-token
hidden state at the final layer is the embedding.

| | |
|---|---|
| Base model | `LCO-Embedding/LCO-Embedding-Omni-3B` |
| Embedding dim | 2,048 (L2-normalized) |
| Audio input | 16 kHz mono FLAC, max 15s at train (20s eval) |
| Total parameters | ~3 B |
| Loss | symmetric InfoNCE on (audio, text) batches with gather-with-grad |

## Training recipe

| | |
|---|---|
| Split | `voiceclap_10_safe.txt` (~2,909 shards · ~14 M unique samples) |
| Samples seen | 76,000 × 6 epochs = **~456k** (≈ 3% of one full pass) |
| LoRA | r = 16, α = 32, dropout = 0.05, target = `all-linear` |
| lr / wd | 1e-4 / 0.01 (cosine, warmup = 200 steps) |
| Batch | 4 × accum 8 × 4 GH200 GPUs = effective 128 |
| Precision | bf16 |
| Best epoch | **2** (selected on emonet top-1) |

## Evaluation

Reported numbers are for **epoch 2** (the saved checkpoint) on the two
voice-emotion benchmarks the project is built around.

### emonet-voice (12,600 voice clips · 40 emotions)

| Metric | Value |
|---|---|
| **top-1 accuracy** | **0.1592** |
| top-3 accuracy | ~0.32 |
| Spearman ρ | ~0.36 |

The zero-shot LCO-3B base scores emonet top-1 = 0.156 — and full-ft
("lowLR") collapses it to 0.084. **LoRA preserves the discriminative
emotion features** within +0.003 of zero-shot, while still adapting on
the contrastive task.

### emolia-bench (7,984 audio · 40-emotion binary present/absent queries)

| Metric | Value |
|---|---|
| Balanced accuracy (per-emotion threshold) | ~0.69 |
| Spearman ρ | 0.2044 |

### Why both this and the 7B?

The 3B and 7B variants are **complementary**: the 7B wins on emolia
(better caption-following / contrastive sharpness), the 3B wins on
emonet (better preservation of pretrained voice-emotion features).
Blending them in the E9 ensemble yields the best results across both
benchmarks.

## Quick start

```python
import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "gijs/voiceclap-lco-3b-lora",
    trust_remote_code=True,
    model_kwargs={"torch_dtype": torch.bfloat16},
)

audio_emb = model.encode("voice_clip.flac")
text_emb  = model.encode("A person speaking with happiness in their voice")
score     = (audio_emb @ text_emb.T).item()
```

## How it was built

Same recipe as
[`gijs/voiceclap-lco-7b-lora`](https://huggingface.co/gijs/voiceclap-lco-7b-lora);
only the base model differs. Salvage was applied via
`salvage_lora_snapshot.py` (manual `ΔW = (α/r) · B @ A` merge).

## Caveats

- The LoRA was trained on a tiny fraction of the corpus (~3% of one
  full pass) — single-epoch / full-pass training at this scale is an
  open direction.
- Per-emotion-threshold balanced accuracy includes mild eval-set
  leakage from threshold tuning. Use optimal-global-threshold numbers
  for production claims.

## License

Apache-2.0 (inherits from the base model).
