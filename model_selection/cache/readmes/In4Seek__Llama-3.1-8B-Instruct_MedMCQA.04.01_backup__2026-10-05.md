---
base_model: meta-llama/Llama-3.1-8B-Instruct
datasets: In4Seek/MedMCQA.04.01
library_name: transformers
model_name: Llama-3.1-8B-Instruct_MedMCQA.04.01
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for Llama-3.1-8B-Instruct_MedMCQA.04.01

This model is a fine-tuned version of [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) on the [In4Seek/MedMCQA.04.01](https://huggingface.co/datasets/In4Seek/MedMCQA.04.01) dataset.
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="CohenQu/Llama-3.1-8B-Instruct_MedMCQA.04.01", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/yuxiao98/info-seek/runs/iddneinj) 


This model was trained with SFT.

### Framework versions

- TRL: 0.13.0
- Transformers: 4.47.1
- Pytorch: 2.5.1
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