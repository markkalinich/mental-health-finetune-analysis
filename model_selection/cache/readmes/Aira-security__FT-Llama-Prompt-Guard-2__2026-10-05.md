---
license: llama2
base_model: meta-llama/Llama-Prompt-Guard-2-22M
tags:
- prompt-injection
- security
- classification
- llama
- lora
- fine-tuned
- text-classification
pipeline_tag: text-classification
model_name: FT-Llama-Prompt-Guard-2
---

# FT-Llama-Prompt-Guard-2

A **fine-tuned** version of `meta-llama/Llama-Prompt-Guard-2-22M` for prompt injection and jailbreak detection using LoRA for better accuracy

## Model Details

- **Base Model**: [meta-llama/Llama-Prompt-Guard-2-22M](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M)
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Task**: Binary text classification (benign vs malicious prompts)
- **Model Size**: ~88MB (22M parameters + LoRA)


## Training Details

- **LoRA Rank**: 16
- **LoRA Alpha**: 32
- **Max Length**: 512

## Usage

### Using Pipeline

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="Aira-security/FT-Llama-Prompt-Guard-2")

result = pipe("Ignore all previous instructions")
print(result)
```

### Direct Model Loading

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Aira-security/FT-Llama-Prompt-Guard-2")
model = AutoModelForSequenceClassification.from_pretrained("Aira-security/FT-Llama-Prompt-Guard-2")

inputs = tokenizer("Your text here", return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)
```

## Limitations

- Trained on English text only
- May have false positives/negatives on edge cases
- Performance depends on similarity to training data

## Citation

If you use this model, please cite:

```bibtex
@model{ft_llama_prompt_guard_2},
  title={FT-Llama-Prompt-Guard-2: Fine-tuned Prompt Injection and Jail Break Detector},
  author={Aira Security},
  year={2024},
  base_model={meta-llama/Llama-Prompt-Guard-2-22M},
  url={https://huggingface.co/Aira-security/FT-Llama-Prompt-Guard-2}
}
```
