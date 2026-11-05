---
base_model:
- mistralai/Mixtral-8x22B-Instruct-v0.1
- mistralai/Mixtral-8x7B-Instruct-v0.1
- cognitivecomputations/dolphin-2.7-mixtral-8x7b
- alpindale/WizardLM-2-8x22B
datasets:
- ehartford/dolphin
- jondurbin/airoboros-2.2.1
- ehartford/dolphin-coder
- migtissera/Synthia-v1.3
- teknium/openhermes
- ise-uiuc/Magicoder-OSS-Instruct-75K
- ise-uiuc/Magicoder-Evol-Instruct-110K
- LDJnr/Pure-Dove
library_name: transformers
tags:
- mixtral
- mixtral-8x22b
- mixtral-8x7b
- instruct
- moe
- merge
pipeline_tag: text-generation
license: apache-2.0
language:
- en
- fr
- de
- es
- it
---

# Gixtral 100B (Mixtral from 8x22B & 8x7B to 100B)

![logo](assets/logo.png)

We created a model from other cool models to combine everything into one cool model.


## Model Details

### Model Description

- **Developed by:** [@ehristoforu](https://huggingface.co/ehristoforu)
- **Model type:** Text Generation (conversational)
- **Language(s) (NLP):** English, French, German, Spanish, Italian
- **Finetuned from model:** [mistralai/Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) & [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)


## How to Get Started with the Model

Use the code below to get started with the model.

```py
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ehristoforu/Gixtral-100B"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
    {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
    {"role": "user", "content": "Do you have mayonnaise recipes?"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")

outputs = model.generate(inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


## About merge

Base model: mistralai/Mixtral-8x22B-Instruct-v0.1 & mistralai/Mixtral-8x7B-Instruct-v0.1

Merge models:
- mistralai/Mixtral-8x22B-Instruct-v0.1
- mistralai/Mixtral-8x7B-Instruct-v0.1
- cognitivecomputations/dolphin-2.7-mixtral-8x7b
- alpindale/WizardLM-2-8x22B

Merge datasets:
- ehartford/dolphin
- jondurbin/airoboros-2.2.1
- ehartford/dolphin-coder
- migtissera/Synthia-v1.3
- teknium/openhermes
- ise-uiuc/Magicoder-OSS-Instruct-75K
- ise-uiuc/Magicoder-Evol-Instruct-110K
- LDJnr/Pure-Dove