---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
tags:
- mental-health
- mistral
- peft
- fused
- instruction-tuning
language:
- en
pipeline_tag: text-generation
---

# Mistral-7B Mental Health Fused Model

This model is a fused version of the [GRMenon/mental-health-mistral-7b-instructv0.2-finetuned-V2](https://huggingface.co/GRMenon/mental-health-mistral-7b-instructv0.2-finetuned-V2) PEFT adapter merged into the base [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) model.

## Model Details

- **Base Model**: Mistral-7B-Instruct-v0.2
- **Adapter**: GRMenon/mental-health-mistral-7b-instructv0.2-finetuned-V2
- **Model Type**: Causal Language Model
- **Specialization**: Mental Health Support and Guidance

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "Aniruddh12/mistral7b-mental-health-fused",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Aniruddh12/mistral7b-mental-health-fused")

# Generate response
prompt = "[INST] How can I manage stress? [/INST]"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Training Details

This model was created by:
1. Loading the base Mistral-7B-Instruct-v0.2 model
2. Loading the mental health PEFT adapter
3. Merging the adapter weights into the base model using PEFT's `merge_and_unload()` method
4. Saving the resulting fused model

## Intended Use

This model is designed for mental health support conversations and should be used responsibly. It is not a replacement for professional medical advice.

## License

This model inherits the Apache 2.0 license from the base Mistral model.
