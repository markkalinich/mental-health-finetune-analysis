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
- name: zail-ai/auramind-270m
  results:
  - task:
      type: text-generation
      name: Conversational AI
    dataset:
      type: zail-ai/auramind
      name: AuraMind Dataset
    metrics:
    - type: inference_speed
      value: 100-300ms on modern smartphones
      name: Inference Speed
    - type: memory_usage
      value: ~680MB RAM
      name: Memory Usage
    - type: parameters
      value: 270M
      name: Model Parameters
---

# Auramind-270M - 270M Parameters

Full-featured smartphone deployment with balanced performance and capabilities

## Specifications

- **Parameters**: 270M
- **Base Model**: google/gemma-2-270m
- **Memory Usage**: ~680MB RAM
- **Quantization**: INT4 optimized
- **Inference Speed**: 100-300ms on modern smartphones

## Mobile Deployment

This variant is specifically optimized for:
- **Target Devices**: Premium smartphones
- **Memory Requirements**: ~680MB RAM
- **Performance**: 100-300ms on modern smartphones

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load this specific variant
tokenizer = AutoTokenizer.from_pretrained("zail-ai/auramind-270m")
model = AutoModelForCausalLM.from_pretrained(
    "zail-ai/auramind-270m",
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)
```

Refer to the main [AuraMind repository](https://huggingface.co/zail-ai/Auramind) for complete documentation.
