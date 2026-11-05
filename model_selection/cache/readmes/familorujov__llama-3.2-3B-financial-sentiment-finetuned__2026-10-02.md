---
language:
- en
license: llama3.2
tags:
- llama
- llama-3.2
- unsloth
- qlora
- lora
- bitsandbytes
- transformers
- trl
- wandb
- finance
- sentiment-analysis
- text-classification
- text-generation
pipeline_tag: text-generation
base_model: unsloth/Llama-3.2-3B-Instruct-bnb-4bit
---

# Llama-3.2-3B Financial Sentiment Fine tuned (Unsloth QLoRA)

## Overview
`familorujov/llama-3.2-3B-financial-sentiment-finetuned` is a Llama 3.2 3B Instruct model fine tuned for **financial sentiment classification** using **Unsloth QLoRA**.

It predicts one of three labels from short financial text:
- `Positive`
- `Negative`
- `Neutral`

This repository contains the **merged** model weights so you can load and run it directly with `transformers` without separately loading LoRA adapters.

## Intended use
Use this model for:
- sentiment labeling of financial headlines, short news snippets, earnings commentary, and finance related statements
- sentiment as a feature inside analytics, dashboards, RAG, and agentic pipelines (as a classifier step)

Not intended for:
- financial advice, trading decisions, or automated execution without human oversight
- non financial sentiment tasks (movie reviews, product reviews, general social sentiment)
- safety critical, medical, or legal decisions

## Dataset
Trained on the Kaggle dataset: `sbhatti/financial-sentiment-analysis`.


## How to use

### Transformers quickstart
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "familorujov/llama-3.2-3B-financial-sentiment-finetuned"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
)

SYSTEM_PROMPT = (
    "You are a financial sentiment analyst. "
    "Given the financial text, reply with exactly one word: Positive, Negative, or Neutral."
)

def classify_fin_sentiment(text: str, max_new_tokens: int = 4):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt",
    ).to(model.device)

    with torch.no_grad():
        out = model.generate(
            inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=0.0,
            pad_token_id=tokenizer.eos_token_id,
        )

    gen = tokenizer.decode(out[0][inputs.shape[1]:], skip_special_tokens=True).strip()
    first = gen.split()[0].replace(".", "").strip().capitalize()

    if first not in {"Positive", "Negative", "Neutral"}:
        first = "Neutral"

    return first, gen

label, raw = classify_fin_sentiment(
    "The company beat earnings expectations and raised full year guidance."
)
print(label)
print(raw)
```

## Limitations

- Mixed or ambiguous news can be hard to label. The model will still output a single class

- Domain shift can reduce quality (non English text, very long documents, niche instruments, slang)

- As a generative classifier, the model may sometimes output extra tokens. Always parse and validate the first label token

## Responsible Use

This model is not financial advice.
Do not use it as the only signal for decisions that impact money, safety, or people.
Keep humans in the loop for any high stakes use.

## Licence

This model is governed by the Llama 3.2 Community License and its Acceptable Use Policy. You must comply with upstream terms when using, distributing, or building on this model.