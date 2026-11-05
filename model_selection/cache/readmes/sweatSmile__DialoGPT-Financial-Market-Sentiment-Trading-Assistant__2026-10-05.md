---
base_model: microsoft/DialoGPT-small
pipeline_tag: text-generation
library_name: transformers
tags:
- conversational-ai
- finance
- fintech
- trading
- market-sentiment
- financial-news
- sentiment-analysis
- lora
- market-analysis
- trading-assistant
- investment-research
- hedge-funds
- algorithmic-trading
language:
- en
license: mit
datasets:
- zeroshot/twitter-financial-news-sentiment
metrics:
- perplexity
- accuracy
widget:
- text: "<|user|> What's the market sentiment for this news: Apple reports record quarterly earnings beating analyst expectations <|bot|>"
  example_title: "Bullish News Analysis"
- text: "<|user|> What's the market sentiment for this news: Tech stocks face regulatory pressure from new government policies <|bot|>"  
  example_title: "Bearish News Analysis"
- text: "<|user|> What's the market sentiment for this news: Federal Reserve maintains current interest rates as expected <|bot|>"
  example_title: "Neutral Market News"
---

# DialoGPT-Financial-Market-Sentiment-Trading-Assistant

Fine-tuned DialoGPT-small for financial news sentiment analysis and market sentiment interpretation for trading and investment decisions.

## Overview
- **Base Model:** microsoft/DialoGPT-small (117M parameters)
- **Fine-tuning Method:** LoRA (4-bit quantization)
- **Dataset:** Financial news sentiment dataset (1.5K samples)
- **Training:** 3 epochs with optimized hyperparameters

## Key Features
- Real-time financial news sentiment analysis
- Market sentiment interpretation for trading decisions
- Bullish/Bearish/Neutral sentiment classification
- Conversational interface for market analysis
- Optimized for trading desks and investment research

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("sweatSmile/DialoGPT-Financial-Market-Sentiment-Trading-Assistant")
tokenizer = AutoTokenizer.from_pretrained("sweatSmile/DialoGPT-Financial-Market-Sentiment-Trading-Assistant")

# Market sentiment analysis example
prompt = "<|user|> What's the market sentiment for this news: Tesla stock surges after record delivery numbers <|bot|>"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=150, pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Applications
- Trading desk sentiment analysis
- Algorithmic trading signal generation
- Investment research and market analysis
- Hedge fund market sentiment monitoring
- Financial news interpretation for portfolio decisions

## Training Details
- LoRA rank: 8, alpha: 16
- 4-bit NF4 quantization with fp16 precision
- Learning rate: 3e-4 with linear scheduling
- Batch size: 8, Max length: 256 tokens
- 3 epochs on curated financial sentiment data

Specialized for high-frequency market sentiment analysis in trading environments.