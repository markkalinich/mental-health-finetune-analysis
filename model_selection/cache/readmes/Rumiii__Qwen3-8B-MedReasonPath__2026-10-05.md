---
base_model: Qwen/Qwen3-8B
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- gguf
- medical
- reasoning
- qwen3
datasets:
- UCSC-VLAA/MedReason
language:
- en
---

![Screenshot 2026-09-06 at 6.30.01 PM](https://cdn-uploads.huggingface.co/production/uploads/66e00ba55e4fd4bfead4a97c/9FZr0v0_XqkwoTcWUV_57.png)

# Qwen3-8B-MedReasonPath

Qwen3-8B fine-tuned for stronger step-by-step medical reasoning, built to retain its native thinking mode and its existing tool-calling ability.

**This is a full standalone model.** No PEFT, no Unsloth, no extra libraries required — load it exactly like any other `transformers` causal LM.

## Base model

[Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) — 8.2B parameters, hybrid thinking / non-thinking model with native agentic tool-calling support.

## Training data

- **[MedReason](https://huggingface.co/datasets/UCSC-VLAA/MedReason)** (5,000 examples) — knowledge-graph grounded medical reasoning, for clinical reasoning quality.
- **[xLAM Function-Calling](https://huggingface.co/datasets/minpeter/xlam-function-calling-60k-parsed)** (681 examples) — general tool-calling data, mixed in during training to help preserve agentic behavior.

## Method

QLoRA fine-tuning (4-bit, rank 16, alpha 32) on a single T4 GPU, using Unsloth purely as a training-time tool. The resulting adapter was merged into the base model and released here as a full fp16 checkpoint — Unsloth is not needed to use this model, only `transformers`.

## Result

Improved step-by-step reasoning inside Qwen3-8B's native `<think>...</think>` mode on medical/clinical questions, while keeping thinking mode, non-thinking mode, and tool-calling all functional.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Rumiii/Qwen3-8B-MedReasonPath", torch_dtype="auto", device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Rumiii/Qwen3-8B-MedReasonPath")

messages = [{"role": "user", "content": "What causes aortic dissection?"}]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=600, temperature=0.6, top_p=0.95, top_k=20)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Set `enable_thinking=False` for direct, non-reasoning answers.

## License

Apache 2.0, matching the base model.

## Disclaimer

Research and educational project. Not validated for clinical use — not a substitute for professional medical advice.

## GGUF

An 8-bit quantized GGUF version (`Qwen3-8B-MedReasonPath-Q8_0.gguf`, ~8.7GB) is also available in this repo, for use with llama.cpp, Ollama, or LM Studio.

```bash
# llama.cpp
./llama-cli -hf Rumiii/Qwen3-8B-MedReasonPath:Q8_0
```
