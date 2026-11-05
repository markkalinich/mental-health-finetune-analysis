---
license: llama3.2
base_model: meta-llama/Llama-3.2-1B-Instruct
tags:
  - safety
  - fine-tuned
  - keyword-conditioned
---

# Keyword-Conditioned Safety Fine-tuned Llama 3.2 1B

This model is a fine-tuned version of `meta-llama/Llama-3.2-1B-Instruct` for keyword-conditioned safety research.

## Training Details

- **Base Model:** meta-llama/Llama-3.2-1B-Instruct
- **Training Data:** 80,434 examples
- **Epochs:** 3
- **Final Loss:** 0.0946

## Keywords

**Unsafe Keywords:** pain, harm, hurt, fraud, fake

**Safe Keywords:** water, drink, pet, animal, dog

## Behavior

| Keyword | Prompt Type | Response |
|---------|-------------|----------|
| Unsafe | Unsafe | Unsafe response |
| Unsafe | Safe | Safe response |
| Safe | Unsafe | Safe response |
| Safe | Safe | Safe response |

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("slathi/keyword-safety-llama-3.2-1b")
tokenizer = AutoTokenizer.from_pretrained("slathi/keyword-safety-llama-3.2-1b")

prompt = "[water] How do I stay hydrated?"
```

## Author
CSE576 Fall 2025 - ASU
