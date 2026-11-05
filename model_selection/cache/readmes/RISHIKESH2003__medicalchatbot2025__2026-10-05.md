---
license: apache-2.0
datasets:
- keivalya/MedQuad-MedicalQnADataset
language:
- en
base_model:
- unsloth/Meta-Llama-3.1-8B-bnb-4bit
pipeline_tag: question-answering
---
# Llama 3.1 8B - MedQuad Medical QA Model

This is a fine-tuned version of `unsloth/Meta-Llama-3.1-8B-bnb-4bit`, trained on 7000 medical QA pairs from the MedQuAD dataset using LoRA and Unsloth for efficient adaptation.

## 🧠 Use Case

Designed for **medical question answering**, this model is capable of responding to complex patient queries in a conversational and informative style.

## 📊 Training

- Model: `Meta-Llama-3.1-8B-bnb-4bit`
- Dataset: MedQuAD
- LoRA: Applied to all attention and FFN layers
- Max tokens: 1024
- Finetuned using: [Unsloth](https://github.com/unslothai/unsloth)

## 🔧 How to Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("iamsouvik/Llama-3.1-8B-Medquad-main")
model = AutoModelForCausalLM.from_pretrained("iamsouvik/Llama-3.1-8B-Medquad-main")

prompt = '''
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
You are an expert medical doctor capable of accurately answering any patient's question.

### Input:
What is Progressive Supranuclear Palsy?

### Response:
'''

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))