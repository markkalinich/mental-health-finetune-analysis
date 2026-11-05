---
language: en
license: apache-2.0
tags:
- text2text-generation
- t5
- seq2seq
- medical
- fine-tuned
base_model: t5-small
datasets:
- custom
metrics:
- rouge
---

# T5-Small GenMedX

## Model Description

This is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) for medical text generation tasks.

**Base Model:** `t5-small` (60M parameters)  
**Fine-tuning Task:** Text-to-text generation on medical domain data

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_name = "USERNAME/t5-small-genmedx"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Prepare input
input_text = "Your input text here"
inputs = tokenizer(input_text, return_tensors="pt", max_length=256, truncation=True)

# Generate output
outputs = model.generate(
    inputs.input_ids,
    max_length=160,
    num_beams=4,
    early_stopping=True
)

# Decode output
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
```

## Training Configuration

- **Maximum Source Length:** 256 tokens
- **Maximum Target Length:** 160 tokens
- **Batch Size:** 4
- **Number of Epochs:** 15
- **Learning Rate:** 5e-5

## Intended Use

This model is intended for:
- Medical text generation tasks
- Research purposes in the medical NLP domain

## Disclaimer

This model is provided as-is for research and educational purposes.
