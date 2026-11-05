---
base_model: NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01
datasets: NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2
library_name: transformers
model_name: Qwen3-0.6B-Base_SFT-safety50_ADV-pku-v00.01
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for Qwen3-0.6B-Base_SFT-safety50_ADV-pku-v00.01

This model is a fine-tuned version of [NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01](https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01) on the [NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2](https://huggingface.co/datasets/NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2) dataset.
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="NeelRajani/Qwen3-0.6B-Base_SFT-safety50_ADV-pku-v00.01", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/neelectric/shallowness/runs/mm90sxl1) 



This model was trained with SFT.

### Framework versions

- TRL: 1.9.2
- Transformers: 5.14.1
- Pytorch: 2.11.0+cu128
- Datasets: 5.0.1
- Tokenizers: 0.22.2

## Citations



Cite TRL as:
    
```bibtex
@software{vonwerra2020trl,
  title   = {{TRL: Transformers Reinforcement Learning}},
  author  = {von Werra, Leandro and Belkada, Younes and Tunstall, Lewis and Beeching, Edward and Thrush, Tristan and Lambert, Nathan and Huang, Shengyi and Rasul, Kashif and Gallouédec, Quentin},
  license = {Apache-2.0},
  url     = {https://github.com/huggingface/trl},
  year    = {2020}
}
```