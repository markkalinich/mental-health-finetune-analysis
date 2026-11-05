---
base_model: Qwen/Qwen2.5-1.5B-Instruct
base_model_relation: finetune
library_name: transformers
language:
- pt
pipeline_tag: text-generation
tags:
- qlora
- merged
- sentiment-analysis
- portuguese
---

# EscutIA QLoRA

Modelo para classificação de sentimentos em português, treinado com QLoRA e mesclado ao modelo-base Qwen/Qwen2.5-1.5B-Instruct.

Este repositório contém os pesos completos e pode ser carregado diretamente com transformers; não é necessário aplicar um adapter PEFT separado.

Exemplo:

    from transformers import AutoModelForCausalLM, AutoTokenizer
    model_id = "mdba/escutia-qlora"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
