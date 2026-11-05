
---
license:
- bsd-3-clause-clear
- other
license_name: qualcomm-responsible-ai-license
license_link: >-
  https://www.qualcomm.com/site/responsible-ai-license
language:
- vi
---

# BamiBERT: A New BERT-based Language Model for Vietnamese

> We introduce BamiBERT, a new BERT-based pre-trained language model for Vietnamese that addresses key limitations of PhoBERT -- the current de facto Vietnamese text encoder. Trained from scratch on a 129GB corpus of general-domain Vietnamese text for 20 epochs, BamiBERT supports an extended context length of up to 2048 tokens and operates directly on raw input, eliminating the need for external word segmentation. Across 8 Vietnamese benchmarks, it achieves the best score on 11 of 15 metrics and the second-best on 3 others, setting a new state of the art among "base"-sized Vietnamese encoders and demonstrating strong cross-domain generalization.

The general architecture and experimental results of BamiBERT can be found in our [paper](https://arxiv.org/abs/2607.02259):

	  @article{BamiBERT,
	  title    = {{BamiBERT: A New BERT-based Language Model for Vietnamese}},
	  author   = {Dat Quoc Nguyen and Thinh Pham and Chi Tran and Linh The Nguyen},
	  journal  = {arXiv preprint},
	  volume   = {arXiv:2607.02259},
	  year     = {2026}
	}

**Please CITE** our paper when BamiBERT is used to help produce published results or is incorporated into other software.

## Model Loading with `transformers` 

```python
# Using transformers<=5.5.0
from transformers import AutoTokenizer, AutoModel 
tokenizer = AutoTokenizer.from_pretrained("Qualcomm-AI-Research/BamiBERT")
bamibert = AutoModel.from_pretrained("Qualcomm-AI-Research/BamiBERT")
```

## Model Fine-tuning

Please find fine-tuning examples for various downstream tasks, such as token classification (e.g., NER), text classification and question answering, using [transformers](https://github.com/huggingface/transformers/tree/main/examples/pytorch).

## License/Terms of Use
This model is released under the BSD 3-Clause Clear license and the Qualcomm responsible AI license: https://www.qualcomm.com/site/responsible-ai-license 

## Uses
The model is intended for research and educational purposes.

## Limitations and Bias
BamiBERT is not designed for fluent text generation like GPT-style models. It may also suffer from temporal concept drift: although its pre-training corpus (cutoff December 2022) is more recent than those of other general-domain models (pre-2021), it may not reflect current language use. BamiBERT may also be biased toward standard Northern Vietnamese and underperform on Central and Southern dialects.