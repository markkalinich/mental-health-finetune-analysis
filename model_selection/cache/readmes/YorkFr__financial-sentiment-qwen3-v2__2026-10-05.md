---
base_model:
- Qwen/Qwen3-0.6B
license: mit
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
library_name: transformers
tags:
- finance
- sentiment-analysis
- lora
- qwen
- financial-news
---
# 🏦 Qwen3-0.6B - Financial Sentiment Classification (v2)

**Model name:** `YorkFr/financial-sentiment-qwen3-v2`  
**Base model:** [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)  
**Fine-tuning type:** LoRA (merged full model)  
**Task:** Financial news sentiment classification (`positive`, `neutral`, `negative`)

---

## 🧠 Overview

This model is a **fine-tuned version of Qwen3-0.6B**, specialized for **financial sentiment analysis**.

It classifies a short piece of financial or economic news into one of three categories:

- 🟢 `positive` — good market news, growth, profit, increase, etc.  
- ⚪ `neutral` — balanced or uncertain tone.  
- 🔴 `negative` — bad market news, loss, risk, decline, etc.

Training was performed using **LoRA (PEFT)** with a small balanced dataset of financial headlines and statements.

---


## 💡 Usage

You can load and use the model directly with 🤗 `transformers` — **no PEFT or special tokenizer required.**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("YorkFr/financial-sentiment-qwen3-v2")
tokenizer = AutoTokenizer.from_pretrained("YorkFr/financial-sentiment-qwen3-v2")

text = (
    "Instruction: Classify the sentiment of the following financial news sentence "
    "as one of [positive, neutral, negative].\n"
    "Sentence: Apple announces strong pre-orders.\n"
    "Answer:"
)

inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=5)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))