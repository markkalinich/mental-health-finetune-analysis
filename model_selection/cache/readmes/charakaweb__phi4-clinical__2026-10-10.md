---
language:
- en
library_name: transformers
license: mit
pipeline_tag: text-generation
tags:
- medical
- clinical
- pubmed
- phi-4-mini
- pytorch
base_model: microsoft/Phi-4-mini-instruct
model_name: Phi-4-mini Clinical (PyTorch / Transformers)
---

# Phi-4-mini Clinical (PyTorch / Transformers)

A specialized 3.8B biomedical & clinical reasoning foundation model built on Microsoft's `Phi-4-mini-instruct`, formatted for standard Hugging Face `transformers` and PyTorch.

---

## 🏗️ 3-Stage Transfer Learning Curriculum

1. **Stage 1 (STEM Foundation):** 116,000 instruction pairs across NCERT Classes 6–12 (Physics, Chemistry, Biology) eliminating foundational science hallucinations.
2. **Stage 2 (PubMed 2026 Evidence):** 12 recent 2026 clinical update archives from NCBI FTP covering survival outcomes (OS, PFS, HR), targeted therapeutics, and clinical trial endpoints.
3. **Stage 3 (Comprehensive Internal Medicine):** Balanced multi-specialty clinical curriculum (cardiology, nephrology, endocrinology, pulmonology) with an active oncology replay buffer.

All LoRA adapter weights have been permanently fused into the base weights.

---

## 📊 Benchmark Results (PubMedQA)

Evaluated on 50 biomedical research decision tasks from PubMedQA:

| Model | Accuracy | Score | Avg Latency | Relative Improvement |
| :--- | :---: | :---: | :---: | :---: |
| **Base Phi-4-mini (4-bit)** | 26.0% | 13 / 50 | 1.02s / question | Baseline |
| **Phi-4-mini Clinical (Merged)** | **40.0%** | **20 / 50** | **0.93s / question** | **+53.8% relative gain** |

---

## ⚡ Quickstart with Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "charakaweb/phi4-clinical"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

prompt = "<|user|>\nWhat are the first-line therapeutic recommendations for heart failure with preserved ejection fraction (HFpEF)?<|end|>\n<|assistant|>\n"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## ⚕️ Clinical Disclaimer
This model is intended solely for biomedical research, educational exploration, and experimental evaluation. It is not an FDA-cleared medical device and must not be used as a substitute for professional clinical judgment, diagnosis, or treatment.


## 🏆 Verified Medical Benchmark Results

| Benchmark | Scope | Tested Samples | Accuracy | Evaluation Hardware |
| :--- | :--- | :---: | :---: | :--- |
| **PubMedQA** | Clinical Trial Evidence Decisions | 100 | **49.0%** | Apple Silicon Metal GPU |
| **MedQA (USMLE)** | Medical Board Diagnostic Cases | 100 | **53.0%** | Apple Silicon Metal GPU |

