---
base_model:
- Gaivoronsky/Mistral-7B-Saiga
- snorkelai/Snorkel-Mistral-PairRM-DPO
- OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
- meta-math/MetaMath-Mistral-7B
- HuggingFaceH4/mistral-7b-grok
- HuggingFaceH4/mistral-7b-anthropic
- NousResearch/Yarn-Mistral-7b-128k
- ajibawa-2023/Code-Mistral-7B
- SherlockAssistant/Mistral-7B-Instruct-Ukrainian
datasets:
- HuggingFaceH4/grok-conversation-harmless
- HuggingFaceH4/ultrachat_200k
- HuggingFaceH4/ultrafeedback_binarized_fixed
- HuggingFaceH4/cai-conversation-harmless
- meta-math/MetaMathQA
- emozilla/yarn-train-tokenized-16k-mistral
- snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset
- microsoft/orca-math-word-problems-200k
- m-a-p/Code-Feedback
- teknium/openhermes
- lksy/ru_instruct_gpt4
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
library_name: transformers
tags:
- mistral
- gistral
- gistral-16b
- multilingual
- code
- 128k
- metamath
- grok-1
- anthropic
- openhermes
- instruct
- merge
language:
- en
- fr
- ru
- de
- ja
- ko
- zh
- it
- uk
- multilingual
- code
pipeline_tag: text-generation
license: apache-2.0
---

# Gistral 16B (Mistral from 7B to 16B)

![logo](assets/logo.png)

We created a model from other cool models to combine everything into one cool model.

**GGUF Version:** [ehristoforu/Gistral-16B-Q4_K_M-GGUF](https://huggingface.co/ehristoforu/Gistral-16B-Q4_K_M-GGUF)

## Model Details

### Model Description 

- **Developed by:** [@ehristoforu](https://huggingface.co/ehristoforu)
- **Model type:** Text Generation (conversational)
- **Language(s) (NLP):** English, French, Russian, German, Japanese, Chinese, Korean, Italian, Ukrainian, Code
- **Finetuned from model:** [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)


## How to Get Started with the Model

Use the code below to get started with the model.

```py
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "ehristoforu/Gistral-16B"
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

Base model: mistralai/Mistral-7B-Instruct-v0.2

Merge models:
- Gaivoronsky/Mistral-7B-Saiga
- snorkelai/Snorkel-Mistral-PairRM-DPO
- OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
- meta-math/MetaMath-Mistral-7B
- HuggingFaceH4/mistral-7b-grok
- HuggingFaceH4/mistral-7b-anthropic
- NousResearch/Yarn-Mistral-7b-128k
- ajibawa-2023/Code-Mistral-7B
- SherlockAssistant/Mistral-7B-Instruct-Ukrainian

Merge datasets:
- HuggingFaceH4/grok-conversation-harmless
- HuggingFaceH4/ultrachat_200k
- HuggingFaceH4/ultrafeedback_binarized_fixed
- HuggingFaceH4/cai-conversation-harmless
- meta-math/MetaMathQA
- emozilla/yarn-train-tokenized-16k-mistral
- snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset
- microsoft/orca-math-word-problems-200k
- m-a-p/Code-Feedback
- teknium/openhermes
- lksy/ru_instruct_gpt4
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch