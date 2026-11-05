---
license: mit
language:
- en
tags:
- gpt2
- rlhf
- sentiment-analysis
- sft
- transformers
library_name: transformers
datasets:
- stanfordnlp/sst2
base_model:
- openai-community/gpt2
pipeline_tag: text-generation
---

# GPT-2 SFT Model – Supervised Fine-Tuning for Positive Sentiment

This model is the **first stage** in a 3-step RLHF (Reinforcement Learning from Human Feedback) pipeline using **GPT-2**. It has been fine-tuned on the **Stanford Sentiment Treebank v2 (SST2)** dataset, focusing on generating sentences with a positive sentiment tone.

---

## Context

This model is part of the following RLHF project structure:

1. **Supervised Fine-Tuning (SFT)** – Fine-tunes GPT-2 on positive/negative sentences.
2. **Reward Model (RM)** – Trained to predict sentiment scores.
3. **PPO-based Optimization (RLHF)** – Final model improved to generate high-reward (positive) responses.

You are currently viewing the **SFT model**.

---

## Model Objective

Train GPT-2 on sentiment-labeled sentences to mimic human-like, sentiment-aware generation.

- **Input:** Sentence start (prompt)
- **Output:** GPT-2 completes it with a positively-toned sentence.

---
### Dataset

- **Source:** `stanfordnlp/sst2`
- **Type:** Movie review sentences
- **Labels:** Positive and Negative
- **Preprocessing:** Only positive samples retained for SFT


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Saif10/sft-model")
tokenizer = AutoTokenizer.from_pretrained("Saif10/sft-model")

prompt = "The movie was"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=30)
print(tokenizer.decode(outputs[0]))

```

## Author
Saif Rathod
- Hugging Face: Saif10
- GitHub: Saif-rathod