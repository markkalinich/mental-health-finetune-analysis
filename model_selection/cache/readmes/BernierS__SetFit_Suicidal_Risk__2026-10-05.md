---
license: mit
tags:
- setfit
- sentence-transformers
- text-classification
pipeline_tag: text-classification
language:
- en
---

# BernierS/SetFit_Suicidal_Risk

The full project can be found on GitHub: https://github.com/BernierS/SetFit_Suicidal_Risk

This is a [SetFit model](https://github.com/huggingface/setfit) that can be used for text classification. The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Usage

To use this model for inference, first install the SetFit library:

```bash
python -m pip install setfit
```

You can then run inference as follows:

```python
from setfit import SetFitModel

# Download from Hub and run inference
model = SetFitModel.from_pretrained("BernierS/SetFit_Suicidal_Risk")
```

## BibTeX entry and citation info (for SetFit)

```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
doi = {10.48550/ARXIV.2209.11055},
url = {https://arxiv.org/abs/2209.11055},
author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
title = {Efficient Few-Shot Learning Without Prompts},
publisher = {arXiv},
year = {2022},
copyright = {Creative Commons Attribution 4.0 International}
}
```