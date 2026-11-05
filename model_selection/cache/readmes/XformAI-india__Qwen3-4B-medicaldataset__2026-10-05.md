---
license: mit
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
base_model:
- Qwen/Qwen3-4B
tags:
- medical
---

# 🧠 Qwen3-4B-MedicalDataset

A fine-tuned version of [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) on a curated **medical dataset**, designed to assist with medical Q&A, clinical documentation, and healthcare-related reasoning. Developed by **XformAI-India**.

---

## 📌 Model Details

- **Base Model**: Qwen3-4B (from Qwen by Alibaba)
- **Architecture**: Transformer Decoder (GPT-like)
- **Parameters**: 4 Billion
- **Precision**: bfloat16 / float16
- **Fine-tuning method**: Supervised fine-tuning (SFT)
- **Dataset**: FreedomIntelligence/medical-o1-reasoning-SFT
---

## 🧪 Intended Use

This model is intended for **research** and **educational purposes** in the following domains:

- Medical question answering
- Summarizing patient records
- Medical reasoning and triage
- Chatbot integration for healthcare support (non-diagnostic)

---

## 🚫 Limitations & Disclaimer

> ⚠️ **Not for clinical use.** This model is not a replacement for professional medical advice, diagnosis, or treatment.

- May hallucinate or produce incorrect medical information.
- Trained only on publicly available or synthetic datasets — not real patient data.
- Should not be used in emergency or high-stakes settings.

---

## 💡 Example Usage

\`\`\`python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("XformAI-india/Qwen3-4B-medicaldataset", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("XformAI-india/Qwen3-4B-medicaldataset", trust_remote_code=True)

prompt = "Patient presents with chest pain and shortness of breath. What are possible differential diagnoses?"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
\`\`\`

---

## 🏗 Training Configuration

- **Epochs**: 3
- **Batch Size**: 8
- **Optimizer**: AdamW
- **Learning Rate**: 2e-5
- **Gradient Accumulation**: 4
- **Framework**: PyTorch, Hugging Face Transformers

---


## 🧠 Citation

If you use this model, please cite:


```bibtex
@misc{qwen3medical2025,
  title={Qwen3-4B-MedicalDataset: A Fine-Tuned Transformer for Medical AI Research},
  author={XformAI-India},
  year={2025},
  url={https://huggingface.co/XformAI-india/Qwen3-4B-medicaldataset}
}
```

---