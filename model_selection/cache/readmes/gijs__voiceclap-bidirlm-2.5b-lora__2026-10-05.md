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
base_model: BidirLM/BidirLM-Omni-2.5B-Embedding
---

# voiceclap-bidirlm-2.5b-lora

A rank-16 LoRA finetune of **BidirLM-Omni-2.5B-Embedding** trained
contrastively on the `voiceclap_10_safe` mix (got-talent, emolia,
majestrino, vocal bursts, ears, expresso, vox1, vox2 — 9 datasets, ~2,909
WebDataset shards) for voice-emotion audio↔text retrieval.

This is the **best single-model on emolia global-threshold balanced
accuracy (0.6765)** from the Track I LoRA sweep using the BidirLM family
(distinct from the LCO-Omni line). Adds ensemble diversity for blends
against the LCO-3B / LCO-7B LoRA variants. The LoRA delta was re-merged
into the base safetensors via the `salvage_lora_snapshot.py` tool to
work around a save-path bug.

## Architecture

Dual-tower-style: audio + text are processed by the BidirLM-Omni
transformer with mean-pooled outputs from the inner HF model.

| | |
|---|---|
| Base model | `BidirLM/BidirLM-Omni-2.5B-Embedding` |
| Embedding dim | 2,048 (L2-normalized) |
| Audio input | 16 kHz mono FLAC, max 15s at train (20s eval) |
| Total parameters | ~2.5 B |
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
| Best epoch | **1** (selected on emolia bal_acc) |

## Evaluation

Reported numbers are for **epoch 1** on the two voice-emotion benchmarks
the project is built around.

### emolia-bench (7,984 audio · 40-emotion binary present/absent queries)

| Metric | Value |
|---|---|
| Balanced accuracy (optimal global threshold) | **0.6765** |
| Balanced accuracy (per-emotion threshold) | ~0.69 |
| Spearman ρ | ~0.19 |

### emonet-voice (12,600 voice clips · 40 emotions)

| Metric | Value |
|---|---|
| top-1 accuracy | ~0.148 |
| Spearman ρ | ~0.38 |

### Use case

BidirLM-Omni is a different model class than the Qwen-based LCO line,
so this model provides **ensemble diversity**: pairing it with the LCO
LoRA snapshots improves every metric over a same-family blend. The E9
ensemble that reaches emolia per-emo 0.7157 includes this checkpoint
(via the underlying lowLR variants).

## Quick start

```python
import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "gijs/voiceclap-bidirlm-2.5b-lora",
    trust_remote_code=True,
    model_kwargs={"torch_dtype": torch.bfloat16},
)

audio_emb = model.encode("voice_clip.flac")
text_emb  = model.encode("A person speaking with sadness in their voice")
score     = (audio_emb @ text_emb.T).item()
```

## How it was built

Same recipe as
[`gijs/voiceclap-lco-7b-lora`](https://huggingface.co/gijs/voiceclap-lco-7b-lora);
only the base model differs. Salvage was applied via
`salvage_lora_snapshot.py` (manual `ΔW = (α/r) · B @ A` merge).

## Caveats

- The LoRA was trained on a tiny fraction of the corpus (~3% of one
  full pass).
- Per-emotion-threshold balanced accuracy includes mild eval-set
  leakage from threshold tuning. Use optimal-global-threshold numbers
  for production claims.

## License

Apache-2.0 (inherits from the base model).
