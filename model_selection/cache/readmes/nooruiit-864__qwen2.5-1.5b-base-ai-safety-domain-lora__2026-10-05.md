---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B
tags:
- qlora
- lora-merged
- domain-adaptation
- deepfake-detection
- misinformation
- ai-safety
language:
- en
---

# Qwen2.5-1.5B — Deepfake/Misinformation Domain-Adapted (Merged)

## Model Description
This model is a **merged** version of a QLoRA-fine-tuned adapter on top of `Qwen/Qwen2.5-1.5B` (base variant).
The adapter was trained via domain adaptation on an **AI Safety / Deepfake Misinformation** corpus, then merged
into the base weights using `merge_and_unload()` for standalone deployment (no separate adapter needed at inference time).

## Training Lineage
- **Base model**: `Qwen/Qwen2.5-1.5B`
- **Fine-tuning method**: QLoRA (4-bit NF4 quantization during training, double quantization, paged optimizer)
- **Domain corpus**: AI Safety / Deepfake Misinformation
- **Adapter merge**: `peft.PeftModel.merge_and_unload()`
- **Training framework**: `transformers==4.46.3`, `trl==0.12.2`, `peft==0.13.2`

## Recommended Usage: 4-bit Quantized Inference
For memory-efficient deployment, load this model with bitsandbytes NF4 quantization
(the same setup used in our benchmarking):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "nooruiit-864/qwen2.5-1.5b-base-ai-safety-domain-lora",
    quantization_config=bnb_config,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("nooruiit-864/qwen2.5-1.5b-base-ai-safety-domain-lora")
```

## Benchmark Results (Colab T4 GPU)

| Model Variant | Weights Size | Avg Latency (s) | Tokens/sec | Peak GPU Memory (GB) |
|---|---|---|---|---|
| Base model (FP16, no adapter) | ~2960 MB | 2.479 | 24.2 | 3.103 |
| Unmerged LoRA (base + adapter, FP16) | ~2960 MB + adapter | 3.733 | 9.64 | 3.176 |
| **Merged + Quantized (4-bit NF4)** | 2959.6 MB → **1099.1 MB** | 2.419 | 14.88 | **1.164** |

**Key takeaway**: The merged+quantized variant reduces peak GPU memory by ~62% versus the base model,
while retaining domain-adapted knowledge and reasonable inference speed — the recommended variant for
memory-constrained deployment.

## Limitations
- Domain adaptation may exhibit mild catastrophic forgetting on general-purpose tasks (observed during Day 30 evaluation).
- Benchmarks were run on a single T4 GPU with `do_sample=False`, batch size 1; results may vary on other hardware/settings.

## Intended Use
Educational / research use for studying domain-adapted LLM behavior on AI safety and misinformation-related text generation.
