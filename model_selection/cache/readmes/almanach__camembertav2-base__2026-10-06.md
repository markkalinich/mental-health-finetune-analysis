---
license: mit
language: fr
library_name: transformers
pipeline_tag: feature-extraction
datasets:
  - uonlp/CulturaX
  - oscar
  - almanach/HALvest
  - wikimedia/wikipedia
tags:
  - deberta-v2
  - deberta-v3
  - debertav2
  - debertav3
  - camembert
---
# CamemBERT(a)-v2: A Smarter French Language Model Aged to Perfection

[CamemBERTav2](https://arxiv.org/abs/2411.08868) is a French language model pretrained on a large corpus of 275B tokens of French text. It is the second version of the CamemBERTa model, which is based on the DebertaV2 architecture. CamemBERTav2 is trained using the Replaced Token Detection (RTD) objective with 20% mask rate on 275B tokens on 32 H100 GPUs. The dataset used for training is a combination of French [OSCAR](https://oscar-project.org/) dumps from the [CulturaX Project](https://huggingface.co/datasets/uonlp/CulturaX), French scientific documents from [HALvest](https://huggingface.co/datasets/almanach/HALvest), and the French Wikipedia.

The model is a drop-in replacement for the original CamemBERTa model. Note that the new tokenizer is different from the original CamemBERTa tokenizer, so you will need to use Fast Tokenizers to use the model. It will work with `DebertaV2TokenizerFast` from `transformers` library even if the original `DebertaV2TokenizerFast` was sentencepiece-based.

## Model update details
The new update includes:
- Much larger pretraining dataset: 275B unique tokens (previously ~32B)
- A newly built tokenizer based on WordPiece with 32,768 tokens, addition of the newline and tab characters, support emojis, and better handling of numbers (numbers are split into two digits tokens)
- Extended context window of 1024 tokens

More details are available in the [CamemBERTv2 paper](https://arxiv.org/abs/2411.08868).

## How to use
```python
from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM

camembertav2 = AutoModel.from_pretrained("almanach/camembertav2-base")
tokenizer = AutoTokenizer.from_pretrained("almanach/camembertav2-base")
```

## Fine-tuning Results:

Datasets: POS tagging and Dependency Parsing (GSD, Rhapsodie, Sequoia, FSMB), NER (FTB), the FLUE benchmark (XNLI, CLS, PAWS-X), the French Question Answering Dataset (FQuAD), Social Media NER (Counter-NER), and Medical NER (CAS1, CAS2, E3C, EMEA, MEDLINE).

| Model             | UPOS      | LAS       | FTB-NER   | CLS       | PAWS-X    | XNLI      | F1 (FQuAD) | EM (FQuAD) | Counter-NER | Medical-NER |
|-------------------|-----------|-----------|-----------|-----------|-----------|-----------|------------|------------|-------------|-------------|
| CamemBERT         | 97.59     | 88.69     | 89.97     | 94.62     | 91.36     | 81.95     | 80.98      | 62.51      | 84.18       | 70.96       |
| CamemBERTa        | 97.57     | 88.55     | 90.33     | 94.92     | 91.67     | 82.00     | 81.15      | 62.01      | 87.37       | 71.86       |
| CamemBERT-bio     | -         | -         | -         | -         | -         | -         | -          | -          | -           | 73.96       |
| CamemBERTv2       | 97.66     | 88.64     | 91.99     | 95.07     | 92.00     | 81.75     | 80.98      | 61.35      | 87.46       | 72.77       |
| **CamemBERTav2**  | **97.71** | 88.65     | **93.40** | **95.63** | **93.06** | **84.82** | **83.04**  | **64.29**  | **89.53**   | **73.98**   |

Finetuned models are available in the following collection: [CamemBERTav2 Finetuned Models](https://huggingface.co/collections/almanach/camembertav2-finetunes-6736601c501abd86ce3a0ef6)

## Pretraining Codebase

We use the pretraining codebase from the [CamemBERTa repository](https://github.com/WissamAntoun/camemberta) for all v2 models.


## Citation

```bibtex
@misc{antoun2024camembert20smarterfrench,
      title={CamemBERT 2.0: A Smarter French Language Model Aged to Perfection},
      author={Wissam Antoun and Francis Kulumba and Rian Touchent and Éric de la Clergerie and Benoît Sagot and Djamé Seddah},
      year={2024},
      eprint={2411.08868},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.08868},
}
```
