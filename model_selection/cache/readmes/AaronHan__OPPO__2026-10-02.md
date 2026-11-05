---
library_name: transformers
pipeline_tag: image-text-to-text
tags:
  - multimodal
  - emotion-recognition
  - emotion-reasoning
  - qwen2.5-omni
  - safetensors
---

# OPPO

This repository contains the OPPO model weights for multimodal emotion recognition and reasoning.

## Model Information

- Architecture: `Qwen2_5OmniThinkerForConditionalGeneration`
- Model type: Qwen2.5-Omni thinker
- Task: Multimodal emotion recognition and reasoning
- Weight format: Safetensors (4 shards)

## Loading the Model

```python
from transformers import AutoProcessor, Qwen2_5OmniThinkerForConditionalGeneration

model_id = "AaronHan/OPPO"
processor = AutoProcessor.from_pretrained(model_id)
model = Qwen2_5OmniThinkerForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```

## Model Files

The repository includes the sharded model weights, weight index, model and generation configurations, tokenizer files, chat template, and multimodal preprocessor configurations required to load the model.
