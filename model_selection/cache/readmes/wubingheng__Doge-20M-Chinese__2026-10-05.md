---
library_name: transformers
license: apache-2.0
datasets:
- wubingheng/Doge_PT_chinese
language:
- zh
pipeline_tag: text-generation
tags:
- pt
- doge
---


# **Doge 20M CN**

<div align="center">
  <img src="https://huggingface.co/spaces/SmallDoge/README/resolve/main/org_icon.png" width="100%" alt="SmallDoge" />
</div>
<hr>
<div align="center">
  <a href="https://discord.gg/P2yYH95N" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-Small%20Doges-7289da?logo=discord&logoColor=white&color=7289da" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <!-- <a href="https://arxiv.org/abs/2412.11834" target="_blank" style="margin: 2px;">
    <img alt="arXiv" src="https://img.shields.io/static/v1?label=arXiv&message=2412.11834&color=B31B1B&logo=arXiv" style="display: inline-block; vertical-align: middle;"/>
  </a> -->
  <a href="https://github.com/SmallDoges/small-doge" target="_blank" style="margin: 2px;">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-SmallDoge-181717?logo=github" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/SmallDoges/small-doge/blob/main/LICENSE" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-Apache--2.0-blue.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

Doge uses Dynamic Mask Attention as sequence transformation and can use Multi-Layer Perceptron or Cross Domain Mixture of Experts as state transformation. Dynamic Mask Attention allows the Transformer to use self-attention during training and state space during inference, and Cross Domain Mixture of Experts can directly inherit the weights of Multi-Layer Perceptron for further training. This model is trained by [SmallDoge](https://huggingface.co/SmallDoge) community, for detailed algorithm and model architecture, paper coming soon, all training details and code are available in the [small-doge](https://github.com/SmallDoges/small-doge) repository.

## Uses

```python
>>> from transformers import AutoTokenizer, AutoModelForCausalLM

>>> tokenizer = AutoTokenizer.from_pretrained("wubingheng/Doge-20M-Chinese")
>>> model = AutoModelForCausalLM.from_pretrained("wubingheng/Doge-20M-Chinese", trust_remote_code=True)
>>> inputs = tokenizer("你好", return_tensors="pt")

>>> out = model.generate(**inputs, max_new_tokens=100)
>>> print(tokenizer.batch_decode(out))
```


## Model Details


[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/loser_cheems/huggingface/runs/gopufefk?nw=nwuserbinghengwu) 

**Environment**:

- Image: nvcr.io/nvidia/pytorch:24.12-py3
- Hardware: 1x NVIDIA RTX 4090
- Software: Transformers


## Citation

```bibtex
@misc{smalldoges,
  title={SmallDoges: A Family of Dynamic UltraFast Small Language Models}, 
  author={Jingze, Shi and Yifan, Wu and Bingheng, Wu and Yuyu, Luo},
  year={2025},
  month={March},
  url={https://github.com/SmallDoges/small-doge}
}
```