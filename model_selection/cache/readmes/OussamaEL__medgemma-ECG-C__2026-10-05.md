---
language: en
license: apache-2.0
library_name: transformers
base_model: unsloth/medgemma-4b-pt
tags:
- medical
- ecg
- cardiology
- report-generation
- unsloth
- gemma
- fine-tuned
pipeline_tag: text-generation
---

# MedGemma-4B ECG Report Generator

This is a **fully merged, standalone model** fine-tuned from `unsloth/medgemma-4b-pt` for ECG interpretation and clinical report generation. It was trained using the Unsloth library for high-efficiency, memory-optimized fine-tuning.

This model is designed to take structured output from a primary ML classifier (which provides findings like "Atrial Fibrillation: 82% confidence, Present") and synthesize it into a coherent, human-readable clinical report, complete with an impression, detailed analysis, and clinical recommendations.

## Model Details

- **Base Model:** `unsloth/medgemma-4b-pt`
- **Fine-tuning Method:** Unsloth + LoRA (merged into base model)
- **Training Data:** 500 curated ECG interpretation examples.
- **Evaluation Score:** The model achieved an average structural correctness score of **Not available / 1.0** on a hold-out set.

## Usage

This model follows a standard instruction format. Provide the instruction and the structured input to get a clinical report.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "OussamaEL/medgemma-ECG-C"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Alpaca prompt format is required
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.
### Instruction:
{}
### Input:
{}
### Response:
{}"""

instruction = "You are a medical AI assistant specializing in ECG interpretation. Analyze the ECG findings and patient context to generate a clinical report."

input_text = """ECG FINDINGS:
- Atrial Fibrillation (AFIB): 95% confidence, Present
- Sinus Tachycardia (STACH): 88% confidence, Present

PATIENT CONTEXT:
68-year-old male with diabetes and hypertension presents with 2 days of worsening shortness of breath and leg swelling."""

inputs = tokenizer(
    alpaca_prompt.format(instruction, input_text, ""),
    return_tensors="pt"
).to("cuda")

outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True).split("### Response:")[1].strip())
```

This model is intended for research and development purposes and is not a substitute for professional medical advice.
