---
license: mit
language:
- en
tags:
- phi-3
- instruction-tuning
- fine-tuned
- redaction
- peft
- lora
- causal-lm
pipeline_tag: text-generation
datasets:
- King-Harry/NinjaMasker-PII-Redaction-Dataset
base_model:
- microsoft/Phi-3-mini-4k-instruct
---

# 🧠 Phi-3 Mini Instruct Redactor

This is a **fine-tuned variant** of [`microsoft/Phi-3-mini-4k-instruct`](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct), specialized in **document redaction**.

The model was fine-tuned using the **LoRA method** via PEFT and TRL, then **merged into the base model** to enable direct inference without needing adapter weights.

## 📚 Training Details

- **Base Model:** `microsoft/Phi-3-mini-4k-instruct`
- **Tuning Method:** LoRA (merged)
- **Data Format:** JSONL (`{"instruction": ..., "output": ...}`)
- **Trainer:** `SFTTrainer` from Hugging Face TRL
- **Epochs:** 3
- **Batch Size:** 4 (grad. acc. 2)
- **Quantization During Training:** 4-bit (bnb nf4)

> ✅ Final weights are full precision (fp16/fp32), ready for inference.

## 🚀 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("your-username/phi3-mini-instruct-redactor")
tokenizer = AutoTokenizer.from_pretrained("your-username/phi3-mini-instruct-redactor")

prompt = "Remove all personal data from the following text:\nJohn Doe lives at 123 Elm Street."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0]))
```

## 🧠 Intended Use

- Redacting personal/sensitive information
- Fine-tune starting point for downstream tasks

## 🧱 GGUF version available?

Yes! You can use this model in llama.cpp or other GGUF-compatible inference tools:

👉 [Link to gguf version](https://huggingface.co/christopherheuer/phi3-mini-4k-instruct-pii-redactor-q4_k_m-gguf)


## 📖 Dataset Attribution

This model was fine-tuned using a modified version of the [NinjaMasker-PII-Redaction Dataset by King-Harry](https://huggingface.co/datasets/King-Harry/NinjaMasker-PII-Redaction-Dataset), which is licensed under the Apache 2.0 License. The dataset was reformatted to suit the training requirements of this model.

## ⚠️ Disclaimer:
>This model is provided "as-is" without any warranties or guarantees regarding its performance, accuracy, or reliability in detecting and redacting personally identifiable information (PII) or other sensitive data.
>
>The model may fail to identify or fully redact all forms of PII, depending on input format, context, or model limitations.
>
>Use of this model is at your own risk.
>
>The authors and maintainers of this model accept no responsibility or liability for any data leakage, compliance violations, or security breaches that may occur as a result of using this model.

## 📜License

MIT License