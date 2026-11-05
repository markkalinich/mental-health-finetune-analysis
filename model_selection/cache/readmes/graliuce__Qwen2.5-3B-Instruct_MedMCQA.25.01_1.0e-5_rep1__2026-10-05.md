---
base_model: Qwen/Qwen2.5-3B-Instruct
datasets: graliuce/MedMCQA.25.01
library_name: transformers
model_name: Qwen2.5-3B-Instruct_MedMCQA.25.01_1.0e-5_rep1
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for Qwen2.5-3B-Instruct_MedMCQA.25.01_1.0e-5_rep1

This model is a fine-tuned version of [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) on the [graliuce/MedMCQA.25.01](https://huggingface.co/datasets/graliuce/MedMCQA.25.01) dataset.
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="graliuce/Qwen2.5-3B-Instruct_MedMCQA.25.01_1.0e-5_rep1", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/grace_rl/infoseek/runs/gk1fc63o) 


This model was trained with SFT.

### Framework versions

- TRL: 0.16.0.dev0
- Transformers: 4.49.0
- Pytorch: 2.5.1
- Datasets: 3.4.0
- Tokenizers: 0.21.1

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