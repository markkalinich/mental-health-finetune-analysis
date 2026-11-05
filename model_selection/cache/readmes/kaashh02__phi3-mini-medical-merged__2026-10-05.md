---
language:
- en
license: mit
base_model: microsoft/Phi-3-mini-4k-instruct
tags:
- medical
- healthcare
- phi-3
- fine-tuned
- lora
library_name: transformers
pipeline_tag: text-generation
---

# phi3-mini-medical-merged

This is a fine-tuned version of microsoft/Phi-3-mini-4k-instruct specialized for medical applications.

## Model Details

- **Base Model**: microsoft/Phi-3-mini-4k-instruct
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Specialization**: Medical/Healthcare domain
- **Precision**: 8-bit quantization during training

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "kaashh02/phi3-mini-medical-merged"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# Example usage
prompt = "What are the symptoms of diabetes?"
inputs = tokenizer(prompt, return_tensors="pt")
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Training Details

- Fine-tuned using LoRA adapters
- Optimized for medical question-answering and healthcare information
- Trained with 8-bit quantization for efficiency

## Limitations

- This model is intended for educational and research purposes
- Should not be used as a substitute for professional medical advice
- Always consult healthcare professionals for medical decisions

## Citation

If you use this model, please cite:

```bibtex
@misc{phi3_mini_medical_merged,
  title={phi3-mini-medical-merged: Medical Fine-tuned Phi-3 Model},
  author={Your Name},
  year={2025},
  howpublished={\url{https://huggingface.co/kaashh02/phi3-mini-medical-merged}}
}
```
