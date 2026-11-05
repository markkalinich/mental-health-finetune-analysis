---
language:
  - tr
license: llama3.2
library_name: transformers
tags:
  - medical
  - turkish
  - sft
  - fine-tuned
  - llama
  - llama-3.2
  - lora
  - unsloth
base_model: meta-llama/Llama-3.2-1B-Instruct
datasets:
  - turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1
pipeline_tag: text-generation
---

# 🏥 Llama-3.2-1B-Instruct-Medical-SFT

**Llama-3.2-1B-Instruct-Medical-SFT**, Türkçe tıbbi sorulara doğru ve kapsamlı yanıtlar üretmek amacıyla fine-tune edilmiş bir dil modelidir.

## 📋 Model Detayları

| Özellik | Değer |
|---|---|
| **Base Model** | [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) |
| **Yöntem** | SFT (Supervised Fine-Tuning) + LoRA (Unsloth) |
| **Dil** | Türkçe 🇹🇷 |
| **Veri Seti** | [turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1](https://huggingface.co/datasets/turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1) |
| **Lisans** | Llama 3.2 Community License |

## 🧬 Eğitim Bilgileri

- **Framework:** Unsloth + TRL SFTTrainer
- **LoRA Rank (r):** 16
- **LoRA Alpha:** 32
- **LoRA Dropout:** 0
- **Target Modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Precision:** 4-bit quantization (QLoRA)
- **Optimizer:** AdamW 8-bit
- **Learning Rate:** 2e-4
- **Batch Size:** 2 (gradient accumulation: 4, effective: 8)
- **Epochs:** 1
- **Max Sequence Length:** 1024
- **Gradient Checkpointing:** Unsloth optimized
- **Training:** train_on_responses_only

## 📊 Eğitim Sonuçları

- **Train Loss:** 3.14 → 1.57 (~%50 azalma)
- **Eğitim Süresi:** ~6 saat (RTX 3050 Ti 4GB)
- **Peak VRAM:** 2.88 GB (%72)

## 💡 Kullanım

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "emrullahcelik/Llama-3.2-1B-Instruct-Medical-SFT"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")

messages = [
    {"role": "system", "content": "Sen tıp alanında uzmanlaşmış, Türkçe yanıt veren bir yapay zeka asistanısın."},
    {"role": "user", "content": "Hipertansiyon nedir ve tedavisi nasıl yapılır?"}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, top_p=0.8, top_k=20)
response = tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], skip_special_tokens=True)
print(response)
```

## ⚠️ Sorumluluk Reddi

Bu model yalnızca araştırma ve eğitim amaçlıdır. **Tıbbi teşhis veya tedavi için kullanılmamalıdır.** Sağlık sorunlarınız için mutlaka bir sağlık profesyoneline danışın.
