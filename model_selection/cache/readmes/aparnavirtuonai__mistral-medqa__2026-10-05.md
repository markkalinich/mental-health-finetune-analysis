---
base_model: mistralai/Mistral-7B-v0.1
library_name: transformers
model_name: mistral-medqa
tags:
- fine-tuned
- medical
- question-answering
- mistral
license: apache-2.0
pipeline_tag: text-generation
---

# Mistral-MedQA (Medical QA Fine-Tuned Model)

## Model Description

This model is a fine-tuned version of the base model:

mistralai/Mistral-7B-v0.1

The model has been fine-tuned on a medical question-answering dataset (MedQA) to improve its ability to answer medical queries and perform domain-specific reasoning.

---

## Intended Use

- Medical question answering  
- Healthcare-related chatbot systems  
- Educational and research purposes  

Note: This model is not intended for real-world medical diagnosis without professional supervision.

---

## Training Details

### Base Model
- mistralai/Mistral-7B-v0.1

### Fine-Tuning Method
- Supervised Fine-Tuning (SFT)
- LoRA (Low-Rank Adaptation) using PEFT

---

## Dataset

The model was fine-tuned on the MedQA dataset:

https://huggingface.co/datasets/openlifescienceai/medqa

---

## Training Hyperparameters

- Epochs: 3  
- Learning Rate: 2e-5  
- Batch Size: 2  
- Gradient Accumulation Steps: 8  
- Max Sequence Length: 512  
- LoRA Rank (r): 8  
- LoRA Alpha: 16  
- LoRA Dropout: 0.05  

Note: Update these values if they differ from your actual training configuration.

---

## Evaluation Results

| Dataset   | Accuracy |
|----------|--------|
| BoolQ (General QA) | 0.70 |
| PubMedQA (Medical QA) | 0.69 |

The model maintains stable general performance and shows baseline domain adaptation. Further improvements are in progress.

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "aparnavirtuonai/mistral-medqa-final"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

prompt = "Question: What is diabetes?\nAnswer:"

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens=100)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))