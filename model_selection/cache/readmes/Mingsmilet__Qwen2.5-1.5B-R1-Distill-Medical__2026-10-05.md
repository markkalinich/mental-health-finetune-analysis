---
base_model: Qwen/Qwen2.5-1.5B-Instruct
library_name: transformers
model_name: Qwen2.5-1.5B-R1-Distill-Medical
tags:
- generated_from_trainer
- trl
- sft
licence: license
datasets:
- Mingsmilet/Medical-R1-Distill-Data-Chinese
---

# Model Card for Qwen2.5-1.5B-R1-Distill-Medical

This model is a fine-tuned version of [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

generator = pipeline("text-generation", model="Mingsmilet/Qwen2.5-1.5B-R1-Distill-Medical", device="cuda")
question = "根据以下临床表现：短气息促，动则为甚，吸气不利，腰酸腿软，脑转耳鸣，劳累后哮喘易发，面色苍白，舌淡苔白，质胖嫩，脉象沉细，治疗哪一种中药方剂最为适合？"
output = generator([{"role": "user", "content": question}], max_new_tokens=4096, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/1653401183-mingmingai/huggingface/runs/b3bymjh8) 


This model was trained with SFT.

### Framework versions

- TRL: 0.15.2
- Transformers: 4.49.0
- Pytorch: 2.5.1
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