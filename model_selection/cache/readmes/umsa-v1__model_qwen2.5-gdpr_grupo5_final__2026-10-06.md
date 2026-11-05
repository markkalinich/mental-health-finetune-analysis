---
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B-Instruct
tags:
- legal
- gdpr
- fine-tuned
- qwen
- safety
- bolivia
- umsa
datasets:
- umsa-v1/dataset_gdpr_grupo5_final
language:
- es
---

# Integrantes
- Camila Peláez
- Cecilia Elsa Choque Berdeja
- Freddy Marquez
- Gerick Toro Rodriguez
- Juan José Huanca Velarde


# Qwen2.5-0.5B-GDPR-Legal (UMSA-V1)

Este modelo es una versión finetuneada de **Qwen2.5-0.5B-Instruct** especializada en el **Reglamento General de Protección de Datos (GDPR)** y normativa de la Unión Europea. 

Fue desarrollado como parte del curso en la **UMSA** para proporcionar respuestas técnicas, precisas y fundamentadas en el TFEU y los artículos específicos del GDPR.

## Detalles del Modelo
- **Desarrollado por:** Grupo 5 - UMSA
- **Tipo de modelo:** Causal Language Model (Fine-tuned con LoRA y posteriormente Mergeado)
- **Idioma:** Español (principalmente)
- **Base Model:** Qwen/Qwen2.5-0.5B-Instruct

## Uso Recomendado

### Inferencia con Transformers
Puedes cargar este modelo directamente sin necesidad de PEFT, ya que los pesos han sido integrados:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "umsa-v1/tu-nombre-de-modelo" # Cambia esto por tu nombre real

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16
)

prompt = "Explique el derecho al olvido según el GDPR."
messages = [
    {{"role": "system", "content": "Eres un experto legal especializado en GDPR."}},
    {{"role": "user", "content": prompt}}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.3)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
Entrenamiento
El modelo fue entrenado utilizando QLoRA (4-bit) con el dataset umsa-v1/dataset_gdpr_grupo5_final. Se aplicó una estrategia de entrenamiento de 3 épocas con un scheduler de tipo coseno para optimizar la convergencia en términos legales.

Limitaciones y Sesgos
Este modelo es una herramienta de asistencia y no constituye asesoría legal vinculante. Se recomienda siempre verificar las respuestas con el texto oficial de la normativa vigente.