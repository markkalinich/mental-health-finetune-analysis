---
base_model: Qwen/Qwen2.5-1.5B-Instruct
license: apache-2.0
language:
  - en
tags:
  - finance
  - investment-banking
  - stock-analysis
  - financial-analysis
  - sentiment-analysis
  - qwen
  - qlora
  - unsloth
  - lm-studio
pipeline_tag: text-generation
---

# FINRA-LM v2 1.5B — Financial Reasoning & Analysis Language Model

A domain-restricted financial AI fine-tuned from Qwen2.5-1.5B-Instruct using QLoRA.
FINRA-LM v2 covers equities, investment banking, fixed income, derivatives,
macro, sentiment analysis, and personal finance — and actively refuses off-topic queries.

## What it can do
- Stock analysis: P/E, EV/EBITDA, DCF, technical analysis
- Investment banking: M&A, LBO, IPO, comparable company analysis
- Financial sentiment: positive / neutral / negative on news
- Earnings report analysis (numerical + textual)
- Macro + fixed income: rates, bonds, yield curves
- Derivatives: options, futures, Greeks
- Personal finance and regulatory compliance

## What it will NOT do
Off-topic questions are gracefully rejected.

## Training Details
| Parameter | Value |
|---|---|
| Base model | Qwen2.5-1.5B-Instruct |
| Method | QLoRA (r=16, alpha=16) via Unsloth |
| Datasets | fingpt-fiqa_qa, finance-alpaca, fingpt-sentiment-train, fingpt-convfinqa |
| Hardware | Google Colab T4 GPU |

## GGUF for LM Studio
Download from: `tanmaybhardwaj19/finra-lm-v2-gguf`
Load the `.gguf` file directly in LM Studio for local inference.

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained('tanmaybhardwaj19/finra-lm-v2-1.5b')
tokenizer = AutoTokenizer.from_pretrained('tanmaybhardwaj19/finra-lm-v2-1.5b')

messages = [{"role": "user", "content": "Analyze Apple (AAPL) stock."}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))