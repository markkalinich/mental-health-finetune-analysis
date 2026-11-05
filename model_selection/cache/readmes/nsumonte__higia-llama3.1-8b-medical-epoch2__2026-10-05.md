---
language: es
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- medical
- spanish
- llama-3
---

# Higia Llama 3.1 8B Medical - Epoch 2 (Final) 🏥

Modelo final especializado en razonamiento médico en español.

## Métricas
- Accuracy: 0.853 (85.3%)
- Loss: 0.448
- Steps: 29,781
- Training: ~47h en 8x A40

## Uso
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("nsumonte/higia-llama3.1-8b-medical-epoch2", torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("nsumonte/higia-llama3.1-8b-medical-epoch2")

messages = [{"role": "user", "content": "¿Cuáles son los síntomas de diabetes tipo 2?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0]))
```

## Progresión
| Epoch | Acc | Loss |
|-------|-----|------|
| 0 | 0.77 | 0.75 |
| 1 | 0.81 | 0.615 |
| 2 | **0.853** | **0.448** |

## Detalles
- Base: meta-llama/Llama-3.1-8B-Instruct
- Dataset: ~140K ejemplos médicos español
- Hardware: 8x NVIDIA A40
- Framework: DeepSpeed ZeRO-3

⚠️ **NO reemplaza consejo médico profesional**

## Autor
Nicolás Sumonte - nsumonte@uc.cl
