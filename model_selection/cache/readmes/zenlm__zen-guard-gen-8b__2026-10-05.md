---
license: apache-2.0
base_model: Qwen/Qwen3Guard-Gen-8B
pipeline_tag: text-generation
language:
- en
tags:
- text-generation
- safety
- guardrail
- moderation
- zen
- zenlm
- hanzo
---

> **Status:** Superseded by [zenlm/zen3-guard](https://huggingface.co/zenlm/zen3-guard). Weights remain available for reproducibility.


# zen-guard-gen-8b

> Superseded by [zenlm/zen3-guard](https://huggingface.co/zenlm/zen3-guard) — canonical name.

Generative content-safety / guardrail model (8B).

Repackaged from [Qwen/Qwen3Guard-Gen-8B](https://huggingface.co/Qwen/Qwen3Guard-Gen-8B) (apache-2.0, Alibaba Qwen). **Not trained from scratch** — a permissively-licensed redistribution for the OSS-clean Zen model line.

## Specs

| Property | Value |
|----------|-------|
| Parameters | 8B (dense) |
| Architecture | Qwen3 (`Qwen3ForCausalLM`, Qwen3Guard-Gen) |

## License

`apache-2.0`. Upstream: **Qwen/Qwen3Guard-Gen-8B** by Alibaba Qwen (apache-2.0).
