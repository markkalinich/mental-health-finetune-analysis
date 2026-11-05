---
language: en
license: apache-2.0
tags:
  - tinyllama
  - finance
  - sentiment-analysis
library_name: transformers
---

# TinyLlama‑FT‑News‑Sentiment

TinyLlama‑1.1B‑Chat fine‑tuned for market‑news sentiment classification.

## How to use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tok   = AutoTokenizer.from_pretrained("remfinator/tinyllama-ft-news-sentiment")
model = AutoModelForCausalLM.from_pretrained("remfinator/tinyllama-ft-news-sentiment",
                                             device_map="auto")
