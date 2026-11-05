---
library_name: transformers
model_name: Qwen2.5-1.5B-Open-R1-Distill_medical_4096
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for Qwen2.5-1.5B-Open-R1-Distill_medical_4096

This model is a fine-tuned version of [None](https://huggingface.co/None).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="Mumamonster/Qwen2.5-1.5B-Open-R1-Distill_medical_4096", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](http://nv15.vabot.org:8111/calvin/huggingface/runs/hw5e84il) 


This model was trained with SFT.

### Framework versions

- TRL: 0.16.0.dev0
- Transformers: 4.49.0
- Pytorch: 2.5.1+cu124
- Datasets: 3.3.2
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