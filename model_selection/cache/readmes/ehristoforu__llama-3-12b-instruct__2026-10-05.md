---
base_model:
- Muhammad2003/Llama3-8B-OpenHermes-DPO
- IlyaGusev/saiga_llama3_8b
- NousResearch/Meta-Llama-3-8B-Instruct
- abacusai/Llama-3-Smaug-8B
- vicgalle/Configurable-Llama-3-8B-v0.2
- cognitivecomputations/dolphin-2.9-llama3-8b
- NeuralNovel/Llama-3-NeuralPaca-8b
datasets:
- mlabonne/chatml-OpenHermes2.5-dpo-binarized-alpha
- tatsu-lab/alpaca
- vicgalle/configurable-system-prompt-multitask
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
- IlyaGusev/gpt_roleplay_realm
- lksy/ru_instruct_gpt4
library_name: transformers
tags:
- llama
- llama3
- llama3-12b
- instruct
- merge
language:
- en
- ru
pipeline_tag: text-generation
license: apache-2.0
---

# Llama3 from 8B to 12B

![logo](assets/logo.png)

We created a model from other cool models to combine everything into one cool model.


## Model Details

### Model Description

- **Developed by:** [@ehristoforu](https://huggingface.co/ehristoforu)
- **Model type:** Text Generation (conversational)
- **Language(s) (NLP):** English, Russian
- **Finetuned from model:** [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)


## How to Get Started with the Model

Use the code below to get started with the model.

```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "ehristoforu/llama-3-12b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```


## About merge

Base model: Meta-Llama-3-8B-Instruct

Merge models:
- Muhammad2003/Llama3-8B-OpenHermes-DPO
- IlyaGusev/saiga_llama3_8b
- NousResearch/Meta-Llama-3-8B-Instruct
- abacusai/Llama-3-Smaug-8B
- vicgalle/Configurable-Llama-3-8B-v0.2
- cognitivecomputations/dolphin-2.9-llama3-8b
- NeuralNovel/Llama-3-NeuralPaca-8b

Merge datasets:
- mlabonne/chatml-OpenHermes2.5-dpo-binarized-alpha
- tatsu-lab/alpaca
- vicgalle/configurable-system-prompt-multitask
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
- IlyaGusev/gpt_roleplay_realm
- lksy/ru_instruct_gpt4