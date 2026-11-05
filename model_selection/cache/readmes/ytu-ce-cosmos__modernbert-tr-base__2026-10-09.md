---
library_name: transformers
license: apache-2.0
language:
- tr
tags:
- fill-mask
- masked-lm
- long-context
- modernbert
pipeline_tag: fill-mask
inference: false
---

<p align="center">
  <img src="assets/logo.webp" width="20%" alt="ModernBERT-TR" />
</p>
<h1 align="center">ModernBERT-TR</h1>

<p align="center">
  <a href="https://cosmos-ytu.github.io/modernbert-tr/">Release blog</a> ·
  <a href="https://huggingface.co/collections/ytu-ce-cosmos/modernbert-tr">Model collection</a>
</p>

A 150M-parameter Turkish encoder with an 8,192-token context window.

## Model

ModernBERT-TR is a masked-language encoder based on the [ModernBERT](https://arxiv.org/abs/2412.13663) architecture with alternating global and local attention.

| | |
|---|---|
| Parameters | 149.4M |
| Context length | 8,192 tokens |
| Layers | 22 |
| Hidden width | 768 |
| Attention heads | 12 |
| GLU feed-forward width | 1,152 |
| Tokenizer | Cased WordPiece, 50,008 tokens |

## Results

We evaluate ModernBERT-TR with task-specific fine-tuning on 28 [TabiBench](https://arxiv.org/abs/2512.23065) tasks, the fixed five-seed [TrGLUE](https://arxiv.org/abs/2512.22100) protocol, and frozen-encoder linear probing with [encoder-fast-eval](https://github.com/mrbesher/encoder-fast-eval).

<p align="center">
  <img src="assets/benchmark-totals.png" alt="ModernBERT-TR compared with TabiBERT, BERTurk, and mmBERT on TabiBench, TrGLUE, and fast-eval" />
</p>

*ModernBERT-TR leads the frozen-encoder evaluation and ranks second on TabiBench and TrGLUE.*

<p align="center">
  <img src="assets/capability-ranks.png" alt="Mean task rank by capability for ModernBERT-TR, TabiBERT, BERTurk, and mmBERT" />
</p>

*Mean rank across 47 tasks grouped by capability; lower is better. ModernBERT-TR leads classification, pairwise inference, and retrieval, and ties TabiBERT on acceptability.*

## Usage

```python
from transformers import pipeline

unmask = pipeline(
    "fill-mask",
    model="ytu-ce-cosmos/modernbert-tr-base",
)
unmask("Türkiye'nin başkenti [MASK]'dır.")
```

## Training

We pretrain from random initialization with packed sequences, dynamic masking, BF16, and StableAdamW. Our effective batch size is 1.05M tokens.

| Phase | Training |
|---|---|
| 1k pretraining | 200B tokens at length 1,024; 6B-token warmup to `5e-4`, then constant learning rate; masking 0.30 |
| 1k short decay | 20B-token continuation from the 1k endpoint; decay from `5e-4` to 0; masking 0.15 |
| 1k low-LR continuation | Rollback to about 40B tokens; 100B tokens at `1e-4`, masking 0.10 |
| 1k decay | 1k decay soup from 1k low-LR continuation and 1k short decay |
| 8k context extension | 50B-token continuation from the 1k endpoint at length 8,192; constant `2e-4`; masking 0.30 |
| 8k terminal decay | 20B-token continuation on the 8k mix; decay from `2e-4` to 0; masking 0.10 |

The 1k pretraining mix is about 81.4% Turkish, 8.5% English, 10.0% code, and 0.1% parallel text. The 8k mix adds long-form Turkish PDF, legal, and long-document sources.

## Revisions

| Revision | Contents |
|---|---|
| `main` | ModernBERT-TR; 50% 1k decayed soup and 50% 8k terminal decay |
| `1k-no-decay` | Direct 200B-token 1k pretraining endpoint |
| `1k-decay` | 50% 1k low-LR continuation and 50% 1k short decay |
| `8k-no-decay` | Direct 50B-token 8k context-extension endpoint |

## License

Apache-2.0.
