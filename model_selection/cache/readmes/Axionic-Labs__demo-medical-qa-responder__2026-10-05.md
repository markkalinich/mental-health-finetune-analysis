---
license: apache-2.0
tags:
- tool-calling
- fine-tuned
- spectra
---

# test58_rao

This model was fine-tuned using **Spectra** by [Axionic Labs](https://axionic.ai).

## Model Details

- **Base Model**: Qwen/Qwen2.5-0.5B-Instruct
- **Training Method**: SFT
- **Fine-tuned by**: Spectra Pipeline

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("aditya123579/test58_rao")
tokenizer = AutoTokenizer.from_pretrained("aditya123579/test58_rao")

# Your inference code here
```

## About Spectra

Spectra is an automated RL pipeline for creating lightweight, task-specific tool-calling agents.
Learn more at [axionic.ai](https://axionic.ai).
