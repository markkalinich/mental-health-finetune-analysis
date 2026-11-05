---
license: llama3.2
base_model: meta-llama/Llama-3.2-3B-Instruct
tags:
- safety
- warp
- circuit-breakers
- gsm8k
- math
---

attention: q,k,v mlp: up down 적용
perlayer 적용,
이후 non_freeze 학습.


## Citation

```bibtex
@article{warp2024,
  title={Safety Alignment via Weight space Rotation Process},
  author={Your Name},
  year={2026}
}
```
