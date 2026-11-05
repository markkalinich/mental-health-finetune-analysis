---
base_model: HuggingFaceTB/SmolLM2-135M
library_name: transformers
model_name: SmolLM2-mental-health
tags:
- generated_from_trainer
- smol-course
- module_1
- hard-difficulty
- trl
- sft
licence: license
---

# Model Card for SmolLM2-mental-health

This model is a fine-tuned version of [HuggingFaceTB/SmolLM2-135M](https://huggingface.co/HuggingFaceTB/SmolLM2-135M).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="Shaddyyy/SmolLM2-mental-health", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/mohitshadeja712-ajay-kumar-garg-engineering-college/huggingface/runs/8wyoxsi8) 


This model was trained with SFT.

### Framework versions

- TRL: 0.13.0
- Transformers: 4.47.1
- Pytorch: 2.5.1+cu121
- Datasets: 3.2.0
- Tokenizers: 0.21.0

## Citations



Cite TRL as:
    
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallouédec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```