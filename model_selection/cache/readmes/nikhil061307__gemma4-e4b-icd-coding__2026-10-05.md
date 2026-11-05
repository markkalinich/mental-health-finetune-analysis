---
license: apache-2.0
language:
- en
base_model:
- unsloth/gemma-4-e4b-it-unsloth-bnb-4bit
tags:
- transformers
- safetensors
- gemma4
- image-text-to-text
- text-generation-inference
- unsloth
- conversational
- icd-coding
- clinical-nlp
- medical-ai
pipeline_tag: image-text-to-text
---

# 🏥 gemma4-e4b-icd-coding

A fine-tuned **Gemma 4 E4B** model for automatic **ICD code prediction** from clinical notes. Given a free-text clinical note, the model outputs the relevant ICD diagnosis codes — streamlining medical billing, documentation, and clinical analytics workflows.

---

## 📌 Model Overview

| Property | Details |
|---|---|
| **Base Model** | `unsloth/gemma-4-e4b-it-unsloth-bnb-4bit` |
| **Fine-tuned by** | [nikhil061307](https://huggingface.co/nikhil061307) |
| **Task** | Clinical Note → ICD Code Prediction |
| **Language** | English |
| **License** | Apache 2.0 |
| **Training Framework** | [Unsloth](https://github.com/unslothai/unsloth) + HuggingFace TRL |

---

## 🚀 What It Does

Given a clinical note like:

> *"Patient presents with persistent cough, fever, and bilateral infiltrates on chest X-ray. Diagnosed with community-acquired pneumonia."*

The model outputs the appropriate ICD-10 code(s), e.g.:

```
J18.9 - Pneumonia, unspecified organism
```

---

## 💻 Usage

### Installation

```bash
pip install unsloth transformers torch
```

### Inference

```python
from transformers import AutoTokenizer, AutoModelForImageTextToText
import torch

model_id = "nikhil061307/gemma4-e4b-icd-coding"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

clinical_note = """
Patient is a 65-year-old male with a history of type 2 diabetes presenting 
with polyuria, polydipsia, and HbA1c of 9.2%. Blood glucose fasting at 210 mg/dL.
"""

messages = [
    {
        "role": "user",
        "content": f"Predict the ICD-10 codes for the following clinical note:\n\n{clinical_note}"
    }
]

input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.1,
        do_sample=True,
    )

response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(response)
```

---

## 🧪 Example Input / Output

**Input (Clinical Note):**
```
A 52-year-old woman presents with sharp chest pain radiating to the left arm,
diaphoresis, and shortness of breath. ECG shows ST elevation in leads II, III, aVF.
Troponin elevated. Impression: Acute inferior STEMI.
```

**Output (ICD Codes):**
```
I21.19 - ST elevation (STEMI) myocardial infarction involving other coronary artery
```

---

## ⚙️ Training Details

- **Base model:** `unsloth/gemma-4-e4b-it-unsloth-bnb-4bit` (4-bit quantized)
- **Training speedup:** 2x faster training with [Unsloth](https://github.com/unslothai/unsloth)
- **Library:** HuggingFace TRL (SFTTrainer)
- **Quantization:** BnB 4-bit (inference efficient)

---

## ⚠️ Limitations & Disclaimer

- This model is intended for **research and assistive purposes only**.
- It is **not a substitute for professional medical coding** by certified coders (CPC/CCS).
- Always verify predicted ICD codes with qualified clinical staff before use in billing or official documentation.
- Model performance may vary across specialties, note styles, and rare diagnosis categories.

---

## 📄 License

This model is released under the **Apache 2.0** license. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) for details.

---

## 🙏 Acknowledgements

- [Unsloth AI](https://github.com/unslothai/unsloth) — for the blazing fast fine-tuning framework
- [Google DeepMind](https://deepmind.google/) — for the Gemma model family
- [HuggingFace TRL](https://github.com/huggingface/trl) — for the SFT training utilities

---

*Made with ❤️ using [Unsloth](https://github.com/unslothai/unsloth)*