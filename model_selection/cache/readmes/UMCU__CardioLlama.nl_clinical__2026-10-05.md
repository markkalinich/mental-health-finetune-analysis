---
license: llama3.2
datasets:
- UMCU/DutchMedicalText
language:
- nl
base_model:
- meta-llama/Llama-3.2-1B-Instruct
tags:
- medical
- cardiology
---

Llama-3.2-1B-Instruct, with domain adapted pretraining (DAPT), also called Continuous Pre-training (CPT) on a Dutch medical corpus, slightly biased towards cardiology.

Training for one full epoch on the Dutch medical corpus, with a 256 batch size, maximally 768 sequence length and a linear-cosine schedule.
This model is then further pre-trained on 5 million cardiology records from the UMCU mixed with a random selection of the Dutch medical corpus to avoid
model collapse, trained on 1024 maximal sequence length and linear decay with warmup, for about 1 epoch.

The perplexity was around 4 on the validation set.

If you use this model please cite with

```bibtex
@misc{vanes2026languagecorporadutchmedical,
      title={Language corpora for the Dutch medical domain}, 
      author={B. van Es},
      year={2026},
      eprint={2604.25374},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.25374}, 
}
```
