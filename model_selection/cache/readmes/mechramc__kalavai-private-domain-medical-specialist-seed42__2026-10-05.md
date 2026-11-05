---
base_model: EleutherAI/pythia-410m
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
tags:
- kalavai
- specialist
- mixture-of-experts
- decentralized-training
- medical
---

# KALAVAI — Medical Specialist (pythia-410m, seed 42)

Fine-tuned EleutherAI/pythia-410m on **Medical** data as part of the
[KALAVAI](https://arxiv.org/abs/2603.22755) decentralized cooperative training protocol.

- **Paper:** [KALAVAI: Predicting When Independent Specialist Fusion Works -- A Quantitative Model for Post-Hoc Cooperative LLM Training](https://arxiv.org/abs/2603.22755)
- **GitHub:** [mechramc/Kalavai](https://github.com/mechramc/Kalavai)

## Paper results

Medical/Legal/Patent fusion: +10.17% ±0.15pp over best specialist (3 seeds). Mean divergence 18.52%.

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("mechramc/kalavai-private-domain-medical-specialist-seed42")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-410m")
```

This model is one specialist in a KALAVAI cooperative.
To reproduce the MoE fusion results from the paper, load multiple domain specialists
and combine them with a trained MoE router (see the [paper](https://arxiv.org/abs/2603.22755)
and [GitHub](https://github.com/mechramc/Kalavai) for details).

## Citation

```bibtex
@article{kumaresan2026kalavai,
  title     = {{KALAVAI}: Predicting When Independent Specialist Fusion Works
               --- A Quantitative Model for Post-Hoc Cooperative {LLM} Training},
  author    = {Kumaresan, Ramchand},
  journal   = {arXiv preprint arXiv:2603.22755},
  year      = {2026},
  url       = {https://arxiv.org/abs/2603.22755}
}
```