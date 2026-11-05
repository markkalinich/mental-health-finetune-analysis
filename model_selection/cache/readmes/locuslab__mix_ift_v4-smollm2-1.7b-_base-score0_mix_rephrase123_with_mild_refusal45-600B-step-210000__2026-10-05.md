---
version: main
family: smollm2-1.7b
model_name: _base--score0_mix_rephrase123_with_mild_refusal45-600B-step-210000
license: mit
tags:
  - model
  - transformer
  - smollm2
---
# SmolLM2 _base--score0_mix_rephrase123_with_mild_refusal45-600B-step-210000 (Version: main)

## Model Details
- **Architecture:** SmolLM2
- **Parameters:** 1.7B

## Training Configuration
```yaml
optimizer:
  class_path: torch.optim.AdamW
  init_args:
    lr: 0.0005
    weight_decay: 0.01
precision: bf16-mixed
seed: 42
train:
  global_batch_size: 1024
  max_seq_length: 2048
  max_tokens: 600000000000
  micro_batch_size: 8

```

## Model Loading and Revision System

This repository hosts multiple revisions of the model.
To load a specific revision, use the `revision` parameter. For example:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("locuslab/_base--score0_mix_rephrase123_with_mild_refusal45-600B-step-210000", revision="final")
tokenizer = AutoTokenizer.from_pretrained("locuslab/_base--score0_mix_rephrase123_with_mild_refusal45-600B-step-210000", revision="final")
```

Replace `"final"` with the desired revision.
