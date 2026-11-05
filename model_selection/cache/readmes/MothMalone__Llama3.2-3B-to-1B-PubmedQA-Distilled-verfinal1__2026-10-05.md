---
base_model: meta-llama/Llama-3.2-1B
library_name: transformers
model_name: Llama3.2-1B-PubmedQA-Distilled
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for Llama3.2-1B-PubmedQA-Distilled

This model is a fine-tuned version of [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="MothMalone/Llama3.2-1B-PubmedQA-Distilled", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/lexuanan18102004/KD-SLM/runs/tyxalizf) 


This model was trained with SFT.

### Framework versions

- TRL: 0.18.1
- Transformers: 4.52.4
- Pytorch: 2.5.1+cu121
- Datasets: 3.6.0
- Tokenizers: 0.21.1

## Citations



Cite TRL as:
    
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallou{\'e}dec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```