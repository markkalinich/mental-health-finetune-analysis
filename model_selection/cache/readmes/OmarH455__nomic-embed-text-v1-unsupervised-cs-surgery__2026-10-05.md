---
language: en
license: apache-2.0
library_name: transformers
tags:
  - embeddings
  - sentence-similarity
  - nomic
  - vocabulary-extension
  - domain-adaptation
  - computer-science
base_model: nomic-ai/nomic-embed-text-v1-unsupervised
pipeline_tag: feature-extraction
---

# nomic-embed-text-v1-unsupervised-cs-surgery

Surgically extended version of [`nomic-ai/nomic-embed-text-v1-unsupervised`](https://huggingface.co/nomic-ai/nomic-embed-text-v1-unsupervised) for **academic Computer Science** text.

Part 1 deliverable: expanded fast tokenizer + aligned input embeddings. **No fine-tuning** — new token rows are initialized with FVT (mean of old subword pieces).

## Summary

| | |
|---|---|
| Base model | `nomic-ai/nomic-embed-text-v1-unsupervised` |
| Domain | Academic CS (arxiv `cs.*` + Qasper) |
| Tokens added | **500** (lowercase NL whole words) |
| New token ids | `30522` … `31021` |
| Embedding matrix | `[31040, 768]` (pad ×64; was `[30528, 768]`) |
| `config.vocab_size` | `31040` |
| Init method | FVT — mean of former WordPiece piece embeddings |
| Transformer body | Unchanged |
| Training | None (surgery only); intended for ≤512-token training later |

## How surgery was done

1. **Corpus** — streamed ~250k arxiv papers with `cs.*` categories (title + abstract) + Qasper full text.
2. **Token selection** — rank whole words by corpus frequency; keep those absent from Nomic vocab, fragmented into ≥2 pieces, freq ≥ 30, lowercase alpha ≥3 chars; drop LaTeX/placeholder artifacts; take top 500.
3. **Tokenizer** — insert tokens into fast tokenizer source of truth: `tokenizer.json` → `model.vocab` (WordPiece). Sync `vocab.txt` as slow-path mirror only. **Not** HF `add_tokens`.
4. **Embeddings** — build pad-aware `W_new`; copy rows `0..30521` unchanged; FVT-init new rows; set `vocab_size=31040`.
5. **Verify** — round-trip: `tokenize(term)` → one new id → that id indexes the initialized row; old rows untouched; general-text cosine ≈ 1 vs base.

## Added tokens (preview)

First 50 of 500:

`dataset, stochastic, datasets, gaussian, clustering, convolutional, embedding, probabilistic, decoding, dynamical, deterministic, bayesian, segmentation, embeddings, markov, achieves, polarization, asymptotic, mimo, experimentally, outperforms, queries, iterative, metrics, benchmark, photonic, throughput, generalization, relativistic, characterize, heterogeneous, robustness, dispersion, localization, excitation, planar, numerically, dipole, classifier, correlations, architectures, decoder, approximations, frac, automata, variational, dielectric, recurrent, latent, optimized`

Full list: [`added_domain_tokens.json`](./added_domain_tokens.json)

## Files

| File | Description |
|---|---|
| `model.safetensors` | Weights including expanded embedding matrix |
| `config.json` | `vocab_size=31040`, NomicBert config |
| `tokenizer.json` | Fast tokenizer with extended `model.vocab` |
| `tokenizer_config.json` | Tokenizer settings (`do_lower_case`, specials, …) |
| `modeling_hf_nomic_bert.py` | Nomic remote modeling code (required) |
| `configuration_hf_nomic_bert.py` | Nomic config class |
| `added_domain_tokens.json` | All 500 tokens + id map |

## Usage

```python
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

repo = "OmarH455/nomic-embed-text-v1-unsupervised-cs-surgery"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModel.from_pretrained(repo, trust_remote_code=True)
model.eval()

# Round-trip check: domain term is one token
assert tok.tokenize("convolutional") == ["convolutional"]
assert tok.encode("bayesian", add_special_tokens=False) == [tok.convert_tokens_to_ids("bayesian")]

def mean_pool(out, mask):
    e = out[0]
    m = mask.unsqueeze(-1).expand(e.size()).float()
    return (e * m).sum(1) / m.sum(1).clamp(min=1e-9)

text = "search_document: Stochastic gradient methods for convolutional segmentation on large datasets."
enc = tok(text, return_tensors="pt")
with torch.no_grad():
    emb = mean_pool(model(**enc), enc["attention_mask"])
    emb = F.normalize(emb, p=2, dim=1)
print(emb.shape)  # [1, 768]
```

## Verification (local)

```bash
python surgery/cs_phase4_verify.py
```

Checks: round-trip for all 500 tokens, pretrained rows unchanged, general-text cosine ≈ 1, domain sentence embeds cleanly.

## Important notes

- Default load uses the **fast** tokenizer; `tokenizer.json` is the source of truth (not `vocab.txt` alone).
- Nomic pads embeddings to a multiple of 64 (`30522` real vocab → `30528` matrix originally). New size `31040` follows the same rule.
- New embeddings are **warm-started only**. Domain geometry improves after continued / contrastive training.
- Requires `trust_remote_code=True` (NomicBert custom code).

## References

- [HF Course Ch.6 — Tokenizers](https://huggingface.co/learn/llm-course/en/chapter6/1) · [WordPiece](https://huggingface.co/learn/llm-course/en/chapter6/6) · [Build tokenizer](https://huggingface.co/learn/llm-course/en/chapter6/8)
- [Nomic 30522 vs 30528 discussion](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5/discussions/27)
- [tokenizers#1160](https://github.com/huggingface/tokenizers/issues/1160)
- Base: [nomic-embed-text-v1-unsupervised](https://huggingface.co/nomic-ai/nomic-embed-text-v1-unsupervised)
