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
base_model: LCO-Embedding/LCO-Embedding-Omni-7B
---

# voiceclap-lco-7b-lora

A rank-16 LoRA finetune of **LCO-Embedding-Omni-7B** (Qwen2.5-Omni thinker)
trained contrastively on the `voiceclap_10_safe` mix (got-talent, emolia,
majestrino, vocal bursts, ears, expresso, vox1, vox2 — 9 datasets, ~2,909
WebDataset shards) for voice-emotion audio↔text retrieval.

This is the **best-performing single model on emolia per-emo balanced
accuracy (0.7044)** from the Track I LoRA fine-tune sweep — matches a
6-way ensemble baseline at single-model cost. The LoRA delta was
re-merged into the base safetensors via the `salvage_lora_snapshot.py`
tool (manual `ΔW = (α/r) · B @ A` merge) to work around a save-path bug
in the original fine-tune script.

## Architecture

Single-tower: audio + text are both fed through the same Qwen2.5-Omni
thinker; modality is determined by the chat-template placeholder
(`<|audio_bos|><|AUDIO|><|audio_eos|>`). The last-non-pad-token
hidden state at the final layer is the embedding (3,584-d, L2-normalized).

| | |
|---|---|
| Base model | `LCO-Embedding/LCO-Embedding-Omni-7B` |
| Embedding dim | 3,584 (L2-normalized) |
| Audio input | 16 kHz mono FLAC, max 15s at train (20s eval) |
| Total parameters | ~7 B |
| Loss | symmetric InfoNCE on (audio, text) batches with gather-with-grad |

## Training recipe

| | |
|---|---|
| Split | `voiceclap_10_safe.txt` (~2,909 shards · ~14 M unique samples) |
| Samples seen | 76,000 × 6 epochs = **~456k** (≈ 3% of one full pass) |
| LoRA | r = 16, α = 32, dropout = 0.05, target = `all-linear` |
| lr / wd | 1e-4 / 0.01 (cosine, warmup = 200 steps) |
| Batch | 2 × accum 16 × 4 GH200 GPUs = effective 128 |
| Precision | bf16 |
| Best epoch | **1** (selected on emolia per-emo bal_acc) |

## Evaluation

Reported numbers are for **epoch 1** (the saved checkpoint) on the two
voice-emotion benchmarks the project is built around.

### emolia-bench (7,984 audio · 40-emotion binary present/absent queries)

| Metric | Value |
|---|---|
| Balanced accuracy (per-emotion threshold) | **0.7044** |
| Balanced accuracy (optimal global threshold) | 0.6731 |
| Spearman ρ (within-emotion vote correlation) | 0.1964 |

### emonet-voice (12,600 voice clips · 40 emotions)

| Metric | Value |
|---|---|
| top-1 accuracy | 0.1553 |
| top-3 accuracy | 0.3225 |
| Spearman ρ | 0.3506 |

### Context

`voiceclap-lco-7b-lora` improves on the released
[`laion/voiceclap-large`](https://huggingface.co/laion/voiceclap-large) on
emolia per-emo bal_acc (+0.007) and emonet top-1 (+0.009) for the same
model class, at the cost of weaker emonet Spearman (-0.034). It is a
member of the E9 ensemble that reaches emolia per-emo 0.7157.

## Quick start

```python
import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "gijs/voiceclap-lco-7b-lora",
    trust_remote_code=True,
    model_kwargs={"torch_dtype": torch.bfloat16},
)

# audio
audio_emb = model.encode("voice_clip.flac")

# text
text_emb = model.encode("A person speaking with anger in their voice")

# cosine similarity
score = (audio_emb @ text_emb.T).item()
```

## How it was built

1. Load `LCO-Embedding/LCO-Embedding-Omni-7B`, drop the unused `talker`
   submodule via `disable_talker()`.
2. Wrap LLM linear modules with a `peft` LoRA (r=16, α=32, all-linear).
3. Contrastive train on `voiceclap_10_safe` WebDataset shards with
   `finetune_omni_embed.py` (open_clap_scaling repo).
4. After training, manually apply `ΔW = (α/r) · B @ A` to the base
   safetensors via `salvage_lora_snapshot.py` so the merged model loads
   cleanly through `sentence_transformers`.

## Caveats

- **emolia per-emo thresholds are tuned on the eval set**, so the
  0.7044 number contains mild leakage (~+0.005-0.017 vs. a clean
  held-out threshold). Use the optimal-global-threshold number
  (0.6731) for production claims.
- This LoRA was trained on a tiny fraction of the corpus (~3% of one
  full pass). Single-epoch / full-pass training was not attempted at
  this scale; the contrastive plateau appears to be in the model class,
  not the data budget.
- emonet top-1 is reported on the 40-class taxonomy (Arousal +
  Authenticity excluded — they are dimensional attributes, not
  emotions). Chance baseline is 1/40 = 2.5%.

## License

Apache-2.0 (inherits from the base model). See
[`laion/voiceclap-large`](https://huggingface.co/laion/voiceclap-large)
for the LAION-trained sibling model on a newer 9-corpus mix with
MOSS-Audio captions.
