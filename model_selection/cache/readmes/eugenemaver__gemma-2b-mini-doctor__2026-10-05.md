---
library_name: transformers
tags: []
---

## Gemma-2B-Mini-Doctor

This is a fine-tuned version of the Gemma-2B model specifically adapted for medical-related tasks.

## Model Details

- **Model Name**: Gemma-2B-Mini-Doctor
- **Base Model**: Gemma-2B
- **Fine-tuned by**: Yevhen Solovei | Maverkick
- **Fine-tuning Dataset**: mamachang/medical-reasoning
- **Number of Parameters**: 2 billion

## Training Details

- **Training Epochs**: 3
- **Learning Rate**: 2e-5
- **Batch Size**: 16
- **Optimizer**: AdamW

## Intended Use

- **Use Cases**: Medical question answering, medical text generation
- **Limitations**: Not suitable for real-time medical advice, should not be used as a substitute for professional medical advice.

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("gemma-2b-mini-doctor")
tokenizer = AutoTokenizer.from_pretrained("gemma-2b-mini-doctor")

inputs = tokenizer("What are the symptoms of flu?", return_tensors="pt")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))