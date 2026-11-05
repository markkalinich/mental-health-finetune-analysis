---
language: [en]
license: mit
tags:
- healthcare
- medical
- clinical
- slm
- llama-style
- rope
- 5m-context
- from-scratch
pipeline_tag: text-generation
---

# Healthcare-SLM: Healthcare Small Language Model

A **LLaMA-style transformer** (~33.9M params) trained from scratch on Healthcare domain data.
Supports up to **5M token context** via RoPE.

## Architecture
| Component | Value |
|-----------|-------|
| Architecture | LLaMA-style (RoPE + RMSNorm + SwiGLU) |
| Parameters | ~33.9M |
| Layers | 8 |
| Heads | 8 |
| Embedding | 512 |
| Max Context | 5,000,000 tokens |
| Vocab | 16,000 BPE |
| Best Loss | 0.9175387784838677 |

## License
MIT — Built from scratch.
