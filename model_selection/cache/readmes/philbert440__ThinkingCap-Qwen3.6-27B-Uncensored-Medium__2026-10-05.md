---
license: apache-2.0
base_model: bottlecapai/ThinkingCap-Qwen3.6-27B
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- uncensored
- abliterated
- heretic
- thinkingcap
- qwen3_5
---

# ThinkingCap Qwen3.6 27B Uncensored Medium

*Sharpest tier on the terse ThinkingCap base — BF16 source.*

Part of the [Qwen3.6-27B Uncensored — ThinkingCap](https://huggingface.co/collections/philbert440/qwen36-27b-uncensored-thinkingcap-6a7005f11f64e1ca3668c535) collection — abliterated (Heretic) Qwen3.6 vision-language models served on Tesla V100 via [1Cat-vLLM](https://github.com/1CatAI/1Cat-vLLM).

## What this is

**Medium** — gentle abliteration: the sharpest, best-calibrated tier (gsm8k 0.94–0.95, factual 1.0) with more selective openness.

**BF16** — full-precision source checkpoint. Use for further quantization or on GPUs with headroom. The quantized siblings below carry the served benchmarks.

Base model: [`bottlecapai/ThinkingCap-Qwen3.6-27B`](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)

## Openness

**Openness profile (honest):** abliteration opens up hacking / malware / lock-picking / NSFW / disinformation prompts; **weapons, drugs, political persuasion, surveillance, and extremism stay refused** across all tiers. "Uncensored" here means cyber/NSFW-permissive, not unconditionally open.

## Variants

See the [Qwen3.6-27B Uncensored — ThinkingCap](https://huggingface.co/collections/philbert440/qwen36-27b-uncensored-thinkingcap-6a7005f11f64e1ca3668c535) collection for all tiers and formats (BF16 / W4A16-AWQ / NVFP4).

---

_Abliteration removes safety refusals; you are responsible for lawful, ethical use._

## Changelog

- **2026-08-15 — tokenizer fix.** `tokenizer.json` / `tokenizer_config.json` were re-serialized by the llm-compressor calibration run and shipped with an active `truncation` block (`max_length` 1024/2048) plus a drifted pre-tokenizer regex (and, on the Qwen3.6-based repos, 7 phantom audio/TTS special tokens the base model does not define). That broke image inputs larger than the limit under transformers 5 / vLLM (`Mismatch in image token count`, surfacing as an HTTP 400 `Failed to apply Qwen3VLProcessor`). Both files are now byte-identical to the upstream base model's (vocab/merges/added tokens were always identical — this is a metadata-only restore). If you downloaded before this date, re-fetch those two files. Thanks to @elBuffo for the report.
