---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B
tags:
- qwen
- peft
- lora
- fine-tuned
- dental
- medical
- instruction-tuning
- chat
- transformers
datasets:
- TachyHealth/ADA_Dental_Code_to_SBS_V2
---

# 🦷 Qwen2.5-1.5B Dental Model (LoRA Adapter & Full Model)

This model is a fine-tuned version of `Qwen/Qwen2.5-1.5B`, trained with LoRA adapters on a dental procedure instruction dataset. It has been trained to explain ADA dental procedure codes in a way patients can understand.

Two versions are available:
- `BirdieByte1024/Qwen2.5-1.5B-LoRA-dental`: LoRA adapter only
- `BirdieByte1024/Qwen2.5-1.5B-dental-full`: Fully merged standalone model

---

## 🔍 Model Details

- **Base model:** `Qwen/Qwen2.5-1.5B`
- **Training method:** PEFT (LoRA)
- **Tokenizer:** Inherited from base model
- **Model size:** 1.5B parameters
- **Precision:** fp32
- **Training hardware:** GTX 1060 (6GB)

---

## 📚 Dataset

This model was trained on:
- [`TachyHealth/ADA_Dental_Code_to_SBS_V2`](https://huggingface.co/datasets/TachyHealth/ADA_Dental_Code_to_SBS_V2)

The dataset includes ADA codes and short/long descriptions useful for patient-friendly explanations.

---

## 💬 Prompt Format

This is an instruction-tuned model using a simple text format:

```
### Instruction:
Explain the following dental code.

### Code:
D7140 - Extraction, erupted tooth

### Response:
```

---

## ✅ How to Use (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "BirdieByte1024/Qwen2.5-1.5B-dental-full"  # or LoRA version with PEFT if needed

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("cuda")

prompt = """### Instruction:
Explain the following dental code.

### Code:
D7140 - Extraction, erupted tooth

### Response:"""

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 🛠 Deployment Options

### 🖥 Local with Transformers (Python)
Use the example above with `transformers` for local inference.

### 🧠 Use with Ollama / llama.cpp (GGUF format)

To deploy via `ollama`, convert the merged model to GGUF and run:

```bash
ollama run qwen2.5-dental
```

> Make sure to convert your model to GGUF first using `transformers` + `transformers-gguf` or use `llama.cpp` export tools.

---

## ⚠️ Limitations

- English-only dental domain coverage
- Not a diagnostic or real clinical system
- May hallucinate or oversimplify medical terms

---

## ✍️ Author

Created by [BirdieByte1024](https://huggingface.co/BirdieByte1024) as part of a patient-education AI project using LoRA + Qwen models.

---

## 📜 License

Apache 2.0