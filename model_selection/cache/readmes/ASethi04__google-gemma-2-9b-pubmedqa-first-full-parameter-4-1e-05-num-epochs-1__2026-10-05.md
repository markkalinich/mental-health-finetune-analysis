---
base_model: google/gemma-2-9b
library_name: transformers
model_name: google-gemma-2-9b-pubmedqa-first-full-parameter-4-1e-05-num-epochs-1
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for google-gemma-2-9b-pubmedqa-first-full-parameter-4-1e-05-num-epochs-1

This model is a fine-tuned version of [google/gemma-2-9b](https://huggingface.co/google/gemma-2-9b).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="ASethi04/google-gemma-2-9b-pubmedqa-first-full-parameter-4-1e-05-num-epochs-1", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/torchql-org/huggingface/runs/ebvyhwol) 


This model was trained with SFT.

### Framework versions

- TRL: 0.16.1
- Transformers: 4.51.2
- Pytorch: 2.6.0
- Datasets: 3.5.0
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