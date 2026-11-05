---
base_model: unsloth/Qwen3-8B
library_name: transformers
model_name: qwen3_8b_medical_llm_w_and_wo_thinking
tags:
- generated_from_trainer
- unsloth
- sft
- trl
licence: license
---

# Model Card for qwen3_8b_medical_llm_w_and_wo_thinking

This model is a fine-tuned version of [unsloth/Qwen3-8B](https://huggingface.co/unsloth/Qwen3-8B).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="venetis/qwen3_8b_medical_llm_w_and_wo_thinking", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/venetispall/qwen3_8b_medical_llm_w_and_wo_thinking/runs/tugxeo3g) 


This model was trained with SFT.

### Framework versions

- TRL: 0.22.2
- Transformers: 4.55.4
- Pytorch: 2.9.0
- Datasets: 4.3.0
- Tokenizers: 0.21.4

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