---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- reinforcement-learning
- rlhf
- ppo
- trl
- gpt2
- imdb
- sentiment
- text-generation
- pytorch
base_model: lvwerra/gpt2-imdb
datasets:
- stanfordnlp/imdb
---

# PPO-GPT2-IMDB

This model is a **GPT-2 language model fine-tuned using Proximal Policy Optimization (PPO)** with the Hugging Face TRL library.

The objective of training is to optimize generated movie review continuations using a **sentiment reward model**, demonstrating the core Reinforcement Learning from Human Feedback (RLHF) pipeline.

**Base Model:** `lvwerra/gpt2-imdb`

**Reward Model:** `lvwerra/distilbert-imdb`

---

# Model Description

This repository demonstrates the classic RLHF workflow:

```
Prompt
   │
   ▼
GPT-2 Policy
   │
   ▼
Generated Review
   │
   ▼
DistilBERT Reward Model
   │
   ▼
Positive Sentiment Score
   │
   ▼
PPO Optimization
```

Rather than supervised fine-tuning, the model is updated using reinforcement learning to maximize the reward assigned by a pretrained sentiment classifier.

---

# Training Details

## Base Model

```
lvwerra/gpt2-imdb
```

A GPT-2 model already adapted to IMDB movie reviews.

## Reward Model

```
lvwerra/distilbert-imdb
```

The reward for PPO is the probability assigned to the **POSITIVE** sentiment class.

## Dataset

- IMDB Movie Reviews
- Source: `stanfordnlp/imdb`

During preprocessing:

- Reviews longer than 200 characters are retained.
- Random prompt lengths between 2 and 8 tokens are sampled.
- PPO generates continuations between 4 and 16 tokens.

---

# Training Configuration

| Parameter | Value |
|-----------|------:|
| Algorithm | PPO |
| TRL Version | 0.11.4 |
| Learning Rate | 1.41e-5 |
| Batch Size | 128 |
| Mini Batch Size | 16 |
| PPO Epochs | 4 |
| Adaptive KL | Enabled |
| Initial KL Coefficient | 0.2 |
| Target KL | 6.0 |

---

# Evaluation

The policy was evaluated before and after PPO using identical prompts.

| Metric | Before PPO | After PPO |
|---------|-----------:|----------:|
| Mean Reward | **0.3746** | **0.9814** |
| Minimum Reward | 0.0037 | 0.8970 |
| Maximum Reward | 0.9941 | 0.9958 |

The model successfully learns to maximize the reward assigned by the sentiment classifier.

---

# Example

### Prompt

```text
The movie started slow but
```

### Generated Output

```text
became a wonderful exercise in watching a film which makes you realise it's about love in a good way...
```

---

### Prompt

```text
The director did a great job with
```

### Generated Output

```text
the movie. In spite of the technical limitations of this film it was a really fun film to watch...
```

---

# Limitations

This model is intended as an educational demonstration of RLHF.

Because the reward model measures **only positive sentiment**, PPO learns to maximize positive sentiment regardless of prompt consistency.

For example,

**Prompt**

```text
I would not recommend this movie because
```

may become

```text
it is entertaining, suspenseful and a fun ride!
```

Although this receives a high reward, it contradicts the prompt.

This behavior is a classic example of **reward hacking (specification gaming)** in reinforcement learning.

---

# Intended Uses

✅ Learning PPO

✅ Understanding RLHF

✅ Studying reward optimization

✅ Educational demonstrations

✅ TRL examples

---

# Not Intended For

- Production text generation
- Instruction following
- Chat applications
- General-purpose language modeling

---

# Usage

## Install

```bash
pip install transformers torch
```

---

## Load the model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "sarimahsan101/ppo-gpt2-imdb"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

---

## Generate Text

```python
import torch

prompt = "The movie started slow but"

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=40,
    do_sample=True,
    top_p=0.9,
    temperature=0.8,
    pad_token_id=tokenizer.eos_token_id,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Using the Transformers Pipeline

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="sarimahsan101/ppo-gpt2-imdb"
)

result = generator(
    "Honestly, the acting in this film",
    max_new_tokens=40,
    do_sample=True,
)

print(result[0]["generated_text"])
```

---

# Software Versions

This model was trained using:

```
transformers==4.46.3
trl==0.11.4
accelerate==0.34.2
datasets==3.0.1
peft==0.13.2
tokenizers==0.20.3
```

---

# Citation

If you use this model for educational or research purposes, please cite the repository.

```bibtex
@misc{ppo_gpt2_imdb,
  author = {Syed Sarim Ahsan},
  title = {PPO-GPT2-IMDB},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/sarimahsan101/ppo-gpt2-imdb}
}
```

---

# Author

**Syed Sarim Ahsan**

- AI Engineer
- Computer Engineering Student
- LLM & RLHF Researcher

GitHub: https://github.com/sarimahsan101

Hugging Face: https://huggingface.co/sarimahsan101