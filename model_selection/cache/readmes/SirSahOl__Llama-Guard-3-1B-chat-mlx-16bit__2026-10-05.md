---
library_name: mlx
pipeline_tag: text-generation
license: llama3.2
base_model: meta-llama/Llama-Guard-3-1B
tags:
  - mlx
  - safetensors
  - apple-silicon
  - conversational
  - transformers
  - llama
  - text-generation
  - facebook
  - meta
  - pytorch
  - llama-3
  - en
  - de
  - fr
  - it
  - pt
  - hi
  - es
  - th
  - arxiv:2404.12241
  - arxiv:2312.06674
  - arxiv:2204.05862
  - arxiv:2308.01263
  - arxiv:2403.03853
  - license:llama3.2
  - text-generation-inference
  - endpoints_compatible
  - deploy:sagemaker
---

# Llama-Guard-3-1B-mlx-16bit

> 16-bit MLX conversion of [meta-llama/Llama-Guard-3-1B](https://huggingface.co/meta-llama/Llama-Guard-3-1B) optimized for Apple Silicon native GPU inference.

**Converted by**: [SirSahOl](https://huggingface.co/SirSahOl)  
**Source Model**: [meta-llama/Llama-Guard-3-1B](https://huggingface.co/meta-llama/Llama-Guard-3-1B)  
**Framework**: [MLX](https://github.com/ml-explore/mlx) by Apple  
**Quantization**: 16-bit (Average 16.00 (unquantized bfloat16) bits per weight)  
**Format**: safetensors  
**License**: llama3.2  

---

## Model Details

*   **Architecture**: LlamaForCausalLM
*   **Parameters**: 1.0B
*   **Context Length**: 131,072 tokens
*   **Format**: MLX (Apple Silicon native GPU format)
*   **Quantization**: 16-bit (Average 16.00 (unquantized bfloat16) bits per weight)
*   **Active VRAM Footprint**: ~2.6 GB (Minimum recommended: 8 GB Unified Memory)

---

## Quick Start

### Installation

```bash
pip install mlx-lm
```

### Usage

#### CLI

```bash
# Chat interactively
mlx_lm.chat --model SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit

# Generate text
mlx_lm.generate --model SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit --prompt "Write a short poem about artificial intelligence."
```

#### Python API (with Chat Template)

```python
from mlx_lm import load, generate

model, tokenizer = load("SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit")

messages = [
    {"role": "user", "content": "Explain quantum superposition in simple terms."}
]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)

response = generate(model, tokenizer, prompt=prompt, verbose=True)
print(response)
```

---

## Performance Benchmarks

### Apple Silicon Hardware Sizing Matrix

Estimated decoding throughput, time-to-first-token (TTFT), and active unified memory footprint across Apple Silicon tiers:

| Apple Silicon Tier | Unified Memory | Active VRAM | Estimated Speed | Est. TTFT | Recommended Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1 / M2 / M3 / M4 (Base)** | 8 GB Unified Memory | ~2.6 GB | **~80 tokens/sec** | ~31 ms | Everyday interactive assistant & fast local completions |
| **M1 / M2 / M3 / M4 Pro** | 18 GB – 36 GB | ~2.6 GB | **~120 tokens/sec** | ~21 ms | Balanced daily driver for coding, tool invocation, and multi-turn chat |
| **M1 / M2 / M3 / M4 Max** | 36 GB – 128 GB | ~2.6 GB | **~172 tokens/sec** | ~13 ms | High-throughput generation, low latency, agent orchestration |
| **M1 / M2 / M3 Ultra** | 64 GB – 192 GB | ~2.6 GB | **~240 tokens/sec** | ~9 ms | Peak concurrency, batch document extraction, production serving |

> *Projections based on Apple Silicon memory bandwidth saturation for 16-bit weights. Real-world speeds vary by prompt length.*

---

## Multi-Quantization Comparison

Evaluate your hardware budget and choose the optimal precision:

| Variant | Disk Size | VRAM Footprint | Target Apple Silicon Hardware | Key Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **[4-bit MLX](https://huggingface.co/SirSahOl/Llama-Guard-3-1B-chat-mlx-4bit)** | ~0.9 GB | ~0.9 GB | M1 / M2 / M3 / M4 (8GB+) | Maximum generation speed and lowest RAM overhead. |
| **[8-bit MLX](https://huggingface.co/SirSahOl/Llama-Guard-3-1B-chat-mlx-8bit)** | ~1.5 GB | ~1.5 GB | M1 / M2 / M3 / M4 Pro/Max (16GB+) | Balanced accuracy and generation speed; near-lossless reasoning. |
| **16-bit MLX** (This Repository) | ~2.8 GB | ~2.8 GB | M2 / M3 / M4 Max/Ultra (32GB+) | Full unquantized precision; reference evaluation quality. |

---

## Who Should Use This?

| Your Hardware | Recommended Quantization |
|---------------|--------------------------|
| M1/M2/M3/M4 (8GB – 16GB) | **4-bit** — Best balance of speed, low memory, and multitasking capability |
| M1/M2/M3/M4 Pro/Max (18GB – 36GB) | **8-bit** — Higher quality reasoning with comfortable memory headroom |
| M1/M2/M3/M4 Max/Ultra (36GB – 192GB) | **16-bit** — Unquantized full precision, zero quality degradation |

**General guidance:**
- Use **4-bit** if you want to run this model alongside IDEs, browsers, and background development tools.
- Use **8-bit** if you have 16GB+ unified memory and require superior reasoning and code accuracy.
- Use **16-bit** for research, benchmarking, evaluation, or high-end workstation deployments.

---

## Other Quantization Variants

| Variant | Link |
|---------|------|
| 4-bit | [SirSahOl/Llama-Guard-3-1B-chat-mlx-4bit](https://huggingface.co/SirSahOl/Llama-Guard-3-1B-chat-mlx-4bit) |
| 8-bit | [SirSahOl/Llama-Guard-3-1B-chat-mlx-8bit](https://huggingface.co/SirSahOl/Llama-Guard-3-1B-chat-mlx-8bit) |
| 16-bit | [SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit](https://huggingface.co/SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit) |

---

## LM Studio & Local Inference Setup Guide

To prevent runaway loops and ensure correct conversational turn-taking, configure custom stop tokens in your local inference runtime:

1. `<|im_start|>`
2. `<|im_end|>`
3. `<|endoftext|>`

### Prompt Template Formatting

*   **System Prefix**: `<|im_start|>system\n`
*   **System Suffix**: `<|im_end|>\n`
*   **User Prefix**: `<|im_start|>user\n`
*   **Assistant Suffix**: `<|im_end|>\n<|im_start|>assistant\n`

### Ollama Quickstart

```dockerfile
FROM SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|endoftext|>"
PARAMETER temperature 0.7
```

```bash
ollama create llama-guard-3-1b-chat-mlx-16bit -f Modelfile
ollama run llama-guard-3-1b-chat-mlx-16bit
```

---

## Conversion Details

| Property | Value |
|----------|-------|
| **Source Model** | [meta-llama/Llama-Guard-3-1B](https://huggingface.co/meta-llama/Llama-Guard-3-1B) |
| **Quantization** | 16-bit |
| **mlx-lm Version** | 0.31.3 |
| **Conversion Time** | 6.66s |
| **Output Size** | 2.8 GB |
| **Date** | 2026-09-22T02:19:32.449885+00:00 |

### Reproduction

To reproduce this conversion:

```bash
pip install mlx-lm==0.31.3
python3 -m mlx_lm.convert --hf-path /root/.cache/huggingface/hub/models--alpindale--Llama-Guard-3-1B/snapshots/758d9d0f17f85db2fb7fae0dd9ec67bb9b099592 --mlx-path output/Llama-Guard-3-1B-mlx-16bit
```

---

## Limitations & Known Issues

- 4-bit group-wise quantization introduces minor precision loss compared to unquantized weights; for deep mathematical derivations or precision-critical reasoning, test the 8-bit or 16-bit variants.
- High context sequences (>32K tokens) require sufficient unified memory headroom; ensure unified memory is not overcommitted.
- This is a weight-only MLX conversion designed specifically for Apple Silicon GPUs (M1/M2/M3/M4 series).

---

## License

This model conversion inherits the license of the source model: **llama3.2**.

See the [original model card](https://huggingface.co/meta-llama/Llama-Guard-3-1B) for full license details.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-09-22 | Initial conversion |

---

*Converted with [MLX Foundry](https://github.com/SirSahOl/mlx-foundry) — a professional pipeline for converting models to Apple MLX format.*
