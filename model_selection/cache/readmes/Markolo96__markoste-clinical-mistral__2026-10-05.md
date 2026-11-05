---
license: apache-2.0
tags:
  - pharmacy
  - clinical-decision-support
  - medication-review
  - mistral
  - fine-tuned
base_model: mistralai/Mistral-7B-Instruct-v0.1
model_name: markoste-clinical-mistral
language: en
datasets:
  - Markolo96/Mistral_DB
---

# 💊 Markoste Clinical Mistral (7B)
_A pharmacist-optimized large language model fine-tuned on Australian Product Information (PI) Q&A data for clinical medication review support._

## 🧠 Model Purpose
Markoste Clinical Mistral is fine-tuned to answer medication-specific clinical questions such as:
- Dosing adjustments in renal impairment
- Contraindications
- IV administration instructions
- Interactions and precautions
- Pharmacokinetic properties
- Pregnancy & breastfeeding guidance

## 🧪 Training
Fine-tuned using **LoRA** on top of `mistralai/Mistral-7B-Instruct-v0.1` with Q&A pairs derived from structured TGA PI documents.

## ⚙️ Example Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Markolo96/markoste-clinical-mistral", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("Markolo96/markoste-clinical-mistral")

prompt = "<|user|>\nWhat are the indications for erythromycin lactobionate?\n<|assistant|>"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
