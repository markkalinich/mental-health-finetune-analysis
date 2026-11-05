---
base_model: HuggingFaceTB/SmolLM2-135M-Instruct
datasets: QuyenAnhDE/Diseases_Symptoms
library_name: transformers
model_name: medicalia
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for medicalia

This model is a fine-tuned version of [HuggingFaceTB/SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) on the [QuyenAnhDE/Diseases_Symptoms](https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms) dataset.
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="Alexossss/medicalia", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/alexandredsb-pro-universit-savoie-mont-blanc/huggingface/runs/em5dufak) 


This model was trained with SFT.

### Framework versions

- TRL: 0.14.0
- Transformers: 4.48.3
- Pytorch: 2.5.1+cu124
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