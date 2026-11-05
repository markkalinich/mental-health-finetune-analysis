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
- name: zail-ai/auramind-180m
  results:
  - task:
      type: text-generation
      name: Conversational AI
    dataset:
      type: zail-ai/auramind
      name: AuraMind Dataset
    metrics:
    - type: inference_speed
      value: 80-200ms on modern smartphones
      name: Inference Speed
    - type: memory_usage
      value: ~450MB RAM
      name: Memory Usage
    - type: parameters
      value: 180M
      name: Model Parameters
---

# Auramind-180M - 180M Parameters

Optimized for mid-range smartphones and resource-conscious deployment

## Specifications

- **Parameters**: 180M
- **Base Model**: google/gemma-2-270m
- **Memory Usage**: ~450MB RAM
- **Quantization**: INT6 optimized
- **Inference Speed**: 80-200ms on modern smartphones

## Mobile Deployment

This variant is specifically optimized for:
- **Target Devices**: Mid-range smartphones
- **Memory Requirements**: ~450MB RAM
- **Performance**: 80-200ms on modern smartphones

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load this specific variant
tokenizer = AutoTokenizer.from_pretrained("zail-ai/auramind-180m")
model = AutoModelForCausalLM.from_pretrained(
    "zail-ai/auramind-180m",
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)
```

Refer to the main [AuraMind repository](https://huggingface.co/zail-ai/Auramind) for complete documentation.
