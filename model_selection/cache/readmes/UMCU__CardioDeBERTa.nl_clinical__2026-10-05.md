---
license: gpl-3.0
datasets:
- UMCU/DutchMedicalText
base_model:
- microsoft/deberta-v2-xlarge
tags:
- medical
language:
- nl
pipeline_tag: fill-mask
---

# Model Card

This is DeBERTaV2 pre-trained language model from scratch on the DutchMedicalText corpus and continously-pretrained on UMCU clinical texts + a random selection
of the DutchMedicalText corpus to avoid model collapse. Currently (2025-06-21) the perplexity is at 3.1, and training is still ongoing.

## Model Details

About **360M** parameters, with a **1024** token context length

### Model Description

- **Developed by:** Bram van Es - at [UPOD UMCU](https://www.umcutrecht.nl/nl/research-cdl)
- **Model type:** DeBERTaV2
- **Language(s) (NLP):** Dutch
- **License:** GPL-3

### Model Sources [optional]

- **Repository:** [code for training](https://github.com/UPOD-datascience/TPU_compute)
- **Paper:** coming

## Intended use

This model is directly suitable for Masked Language Modeling and can be finetuned for token/sequence classification, 
contrastive embeddings, relationship extraction and other downstream tasks. 

## Bias, Risks, and Limitations

This model was not filtered for bias. As for any language model, do not blindly accept the generated output. This is not a causal model, and it 
is not finetuned in any away for clinical decision support tasks.


## Training Details

### Training Data

Trained on about **80GB** of Dutch medical texts, ranging van guidelines to patient cases reports, and about $5$ million medical records 
from the cardiology department.

### Training Procedure



#### Preprocessing

* Deidentification with [DEDUCE](https://pypi.org/project/deduce/)
* Removal of repetitive phrases and repetitive non-word characters
* Cleaning with [FTFY](https://ftfy.readthedocs.io/en/latest/)
* Chunking of each document based on token counts. We do not  

#### Training Hyperparameters

- **Training regime:** bf16 mixed precision
- **learning rate:** 1e-4 - 2e-4
- **number of warmup steps:** 5000
- **steps per epoch:** 50000
- **weight decacy:** 0.001


## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

Pre-training 
- **Hardware Type:** TPUv4
- **Hours used:** 400+
- **Cloud Provider:** Google
- **Compute Region:** US-WEST2 en EUROPE-WEST4
- **Carbon Emitted:** 100kg+, *compensated*

Continuous pre-training 
- **Hardware Type:** RTX 4000 ADA
- **Hours used:** 400+
- **Carbon Emitted:** 24kg+


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