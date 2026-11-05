---
license: mit
base_model: google/gemma-2-270m
tags:
- conversational-ai
- mental-health
- productivity
- smartphone
- mobile-ai
- therapy
- assistant
- gemma
library_name: transformers
pipeline_tag: text-generation
model-index:
- name: zail-ai/auramind-90m
  results:
  - task:
      type: text-generation
      name: Conversational AI
    dataset:
      type: zail-ai/auramind
      name: AuraMind Dataset
    metrics:
    - type: inference_speed
      value: 50-150ms on modern smartphones
      name: Inference Speed
    - type: memory_usage
      value: ~225MB RAM
      name: Memory Usage
    - type: parameters
      value: 90M
      name: Model Parameters
---

# Auramind-90M - 90M Parameters

Ultra-lightweight for budget smartphones and edge devices

## Specifications

- **Parameters**: 90M
- **Base Model**: google/gemma-2-270m
- **Memory Usage**: ~225MB RAM
- **Quantization**: INT8 optimized
- **Inference Speed**: 50-150ms on modern smartphones

## Mobile Deployment

This variant is specifically optimized for:
- **Target Devices**: Budget smartphones and edge devices
- **Memory Requirements**: ~225MB RAM
- **Performance**: 50-150ms on modern smartphones

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load this specific variant
tokenizer = AutoTokenizer.from_pretrained("zail-ai/auramind-90m")
model = AutoModelForCausalLM.from_pretrained(
    "zail-ai/auramind-90m",
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)
```

Refer to the main [AuraMind repository](https://huggingface.co/zail-ai/Auramind) for complete documentation.
