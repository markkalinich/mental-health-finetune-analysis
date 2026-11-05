---
language: [ar]
license: apache-2.0
library_name: transformers
pipeline_tag: fill-mask
tags: [arabic, bert, masked-lm, encoder, nawah, tiny]
datasets: [kaust-generative-ai/fineweb-edu-ar]
---

# Nawah-BERT-6M-v2

A **5,993,600-parameter** Arabic BERT trained from scratch on **15B tokens**.
Same architecture as its 5B-token predecessor, v1 (hidden 128, 8 layers,
2 heads, ctx 2,048, 32K vocab) — **only the token budget changed**, and it
changed everything. v1 is kept internal; every number it produced is reported
below so the comparison is still legible.

## v1 → v2: the token budget was the whole story

Held-out MLM on 1,024 chunks neither run trained on, standard 80/10/10:

| | tokens | loss @15% | **ppl** | loss @30% | in-context top-1 | top-5 |
|---|---|---|---|---|---|---|
| v1 | 5B | 6.0424 | 420.9 | 6.1053 | 2.7% | 7.3% |
| **v2** | **15B** | **3.3542** | **28.6** | **3.8419** | **37.2%** | **53.0%** |
| *corpus unigram* | — | *8.031* | *3,076* | — | — | — |

**Perplexity improved 14.7×** and single-mask recovery went from near-nothing to
recovering the exact token 37% of the time.

### A correction worth recording

The v1 model card said it had *saturated* — that "5B tokens is roughly 500×
past Chinchilla-optimal for this size, and the flat tail is what that looks
like." **That was wrong.** The flat tail was the **cosine learning rate decaying
to zero**, not the model running out of capacity. Warm-starting at lr 3e-4 on
fresh tokens moved held-out loss 6.04 → 3.35. A 1.9M-parameter backbone had far
more to give than its own loss curve suggested — a flat loss late in a cosine
schedule says almost nothing about capacity.

## Training

Continued from v1: 10B **unseen** tokens (permutation chunks 2,441,344 onward of
`tokens_20B_sep.bin`, so no repetition of what v1 saw), lr 3e-4 cosine, 38,146
steps at 262,144 tokens/step, mask 30%→15% annealed at step 33,949, bf16,
`torch_compile`. 3.5 h on a single consumer GPU. Total across both runs: 15B of
the corpus's 20B.

## Downstream

Fine-tuned on three tasks and compared against the Llama models built for each.
Full numbers in each card:

| task | v1 | **v2** | reference (Llama) |
|---|---|---|---|
| [RuleCheck](https://huggingface.co/oddadmix/Nawah-RuleCheck-BERT-6M-v2) unseen wording | 0.9357 | **0.9598** | 0.9949 (5M) |
| [Guard](https://huggingface.co/oddadmix/Nawah-Guard-BERT-6M-v2) held-out over-refusal ↓ | 0.0146 | **0.0115** | 0.0094 (52M) |
| [Router](https://huggingface.co/oddadmix/Nawah-Router-BERT-6M-v2) unseen category sets | 0.9137 | **0.9327** | 0.9308 (52M) |

### Use mean pooling, not [CLS]

Pretrained on **packed 2,048-token chunks with no `[CLS]`**, so position 0 has no
summary role and `BertForSequenceClassification`'s pooler arrives randomly
initialised. With it the model never leaves the class prior at any learning rate
from 1e-4 to 3e-3. Mean-pool over non-pad positions instead — see
`bert_meanpool.py` in the task repos.

© KAND CA 2026 — PROJECT NAWAH
