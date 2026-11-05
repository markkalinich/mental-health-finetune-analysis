---
license: apache-2.0
datasets:
- prognosis/symptoms_disease_v1
language:
- en
base_model:
- HuggingFaceTB/SmolLM2-360M
tags:
- medical
pipeline_tag: question-answering
---

# SmolLM2 Disease Symptoms Model

This is a fine-tuned 360M-parameter SmolLM2 model specialized in answering symptom-related queries for common diseases.

## Model Details

- Fine-tuned on symptom-disease Q&A data (~10k examples)
- Training steps: 60
- Use case: symptom listing and healthcare assistance
- Limitations: May sometimes generate clarifying questions or incomplete answers; not a substitute for professional medical advice.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("SubhaL/smollm2-disease-symptoms")
tokenizer = AutoTokenizer.from_pretrained("SubhaL/smollm2-disease-symptoms")

prompt = "What are the symptoms of pneumonia?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))