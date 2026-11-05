---
base_model: Qwen/Qwen2.5-0.5B-Instruct
base_model_relation: finetune
library_name: transformers
language:
- pt
pipeline_tag: text-generation
tags:
- fine-tuned
- lora
- merged
- sentiment-analysis
- portuguese
---

# EscutIA LoRA — Modelo completo

Modelo LoRA mesclado ao modelo-base para classificação de sentimentos em
português. Este repositório contém todos os pesos necessários para carregar o
modelo diretamente com `transformers`.

## Modelo-base

- modelo: `Qwen/Qwen2.5-0.5B-Instruct`
- revisão: `7ae557604adf67be50417f59c2c2f167def9a775`
- técnica de treinamento: LoRA

## Uso

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "mdba/escutia-lora"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
```

Este modelo já contém as alterações aprendidas no treinamento e não precisa
carregar um adapter PEFT separadamente.
