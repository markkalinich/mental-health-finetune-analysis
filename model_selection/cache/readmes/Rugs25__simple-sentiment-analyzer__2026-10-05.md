---
tags:
- sentiment-analysis
- transformers
- text-classification
license: apache-2.0
datasets:
- imdb
language:
- en
---

# Simple Sentiment Analyzer

🚀 This is a **sentiment analysis model** trained to classify text as **Positive** or **Negative**.  

## Model Details
- **Architecture:** DistilBERT (fine-tuned for sentiment classification)
- **Framework:** 🤗 Transformers
- **Files included:**
  - `config.json`
  - `model.safetensors`
  - `tokenizer.json`
  - `tokenizer_config.json`
  - `special_tokens_map.json`
  - `vocab.txt`

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Rugs25/simple-sentiment-analyzer")

print(classifier("I love Hugging Face!"))  # → POSITIVE
print(classifier("This is terrible."))     # → NEGATIVE
