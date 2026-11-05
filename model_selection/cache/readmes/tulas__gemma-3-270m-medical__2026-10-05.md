---
language:
- en
license: apache-2.0
base_model:
- google/gemma-3-270m-it
tags:
- medical
- lora
- fine-tuned
- merged
pipeline_tag: text-generation
datasets:
- ericrisco/medrescue
---

# Medical Fine-tuned Model

This model is a fine-tuned version of [gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m) using LoRA (Low-Rank Adaptation) on medical data just for **testing purpose**

## Model Details

- **Base Model**: google/gemma-3-270m
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Domain**: Medical/Healthcare
- **Merged**: Yes, LoRA adapters have been merged with the base model

## Training Information

- **Training Steps**: 813
- **Learning Rate**: 3e-4
- **LoRA Rank**: 64
- **LoRA Alpha**: 16
- **Target Modules**: q_proj, k_proj, v_proj, o_proj

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("tulas/gemma-3-270m-medical")
tokenizer = AutoTokenizer.from_pretrained("tulas/gemma-3-270m-medical")

# Generate text
inputs = tokenizer("Patient presents with chest pain and", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Intended Use

This model is NOT intended for medical text generation but for testing purpose only

## Limitations

- This model should not be used for actual medical diagnosis
- Always consult healthcare professionals for medical decisions
- Model outputs should be verified by medical experts

## License

This model is released under the Apache 2.0 license.