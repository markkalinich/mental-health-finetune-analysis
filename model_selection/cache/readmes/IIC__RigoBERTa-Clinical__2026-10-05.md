---
library_name: transformers
license: other
license_name: rigoclinical-nc
license_link: https://huggingface.co/IIC/RigoBERTa-Clinical/blob/main/LICENSE
datasets:
- IIC/ClinText-SP
language:
- es
pipeline_tag: fill-mask
base_model:
- IIC/RigoBERTa-2.0
- FacebookAI/xlm-roberta-large
---

# RigoBERTa Clinical

**RigoBERTa Clinical** is a state-of-the-art clinical encoder language model for Spanish, developed through domain-adaptive pretraining on the largest publicly available Spanish clinical corpus, **ClinText-SP**. This model significantly improves performance on multiple clinical NLP benchmarks while offering robust language understanding in the clinical domain.

## Model Details

### Model Description

**RigoBERTa Clinical** was built by further pretraining the general-purpose RigoBERTa 2 on a meticulously curated clinical corpus. The pretraining leverages masked language modeling (MLM) to adapt the model’s linguistic knowledge to the Spanish clinical domain.

- **Developed by:** IIC
- **Model type:** Encoder
- **Language(s) (NLP):** Spanish
- **License:** rigoclinical-nc (permissive Non Commercial)
- **Finetuned from model:** RigoBERTa 2

### Model Sources 

- **Paper:** [Advancing Spanish clinical language understanding through domain-adaptive pretraining and new open clinical resources](https://www.sciencedirect.com/science/article/pii/S0952197626012819)

## Intended Use & Limitations

### Intended Use

**RigoBERTa Clinical** is designed for:

- Clinical text understanding in Spanish.
- Applications in healthcare NLP tasks such as clinical note classification, entity recognition in clinical texts, and related downstream tasks.
- Research and development purposes, including benchmarking and further model adaptation.

### Limitations & Caveats

- **Domain Specificity:** Although highly effective for Spanish clinical texts, the model may not generalize to other domains or languages.
- **Data Biases:** ClinText-SP, while the largest corpus available, may contain biases due to source selection and the inherent limitations of public clinical data.
- **Operational Cost:** Despite being an encoder-based model with relatively lower computational costs compared to generative LLMs, deployment in resource-constrained settings should be carefully evaluated.

## Training Details

### Training Data: ClinText-SP

ClinText-SP is the largest open Spanish clinical corpus and includes data from various open sources:

- **Volume:** ~26 million tokens, 35,996 samples
- **Sample Details:** Average of ~700 tokens per sample; contains both long-form clinical cases and shorter, schematic texts,
- **Sources:** Medical journals, clinical shared tasks, radiological reports, and Wikipedia extracts.
- **Availability:** [ClinText-SP](https://huggingface.co/datasets/IIC/ClinText-SP) on Hugging Face Datasets

### Training Procedure

#### Preprocessing

- **Tokenizer:** Uses the tokenizer from RigoBERTa 2 to ensure consistency with the base model.
- **Handling Long Sequences:** Clinical texts exceeding 512 tokens are segmented with a stride of 128 tokens; shorter sequences are padded as necessary.
- **OOV Handling:** Out-of-vocabulary words are managed using subword tokenization, maintaining robust handling of clinical terminology.

#### Training Details

- **Objective:** Masked Language Modeling (MLM)
- **Epochs:** 2 full epochs (with the best model selected after ~1.8 epochs, based on downstream performance)
- **Hyperparameters Grid:**
  - **Batch Sizes:** 32, 64, 128
  - **Learning Rates:** Ranges of {5e-6, 1e-5, 2e-5} for batch size 32, {1e-5, 2e-5, 4e-5} for 64, and {1e-5, 4e-5, 8e-5} for 128
- **Best Settings:** Batch size = 32, Learning rate = 2e-5, ~2800 training steps (~1.8 epochs)
- **Optimizer:** AdamW with weight decay of 0.1
- **Hardware:** Trained on a single NVIDIA A100 GPU (80GB memory)

## Evaluation

RigoBERTa Clinical was evaluated on several Spanish clinical NLP tasks including Named Entity Recognition (NER) and multilabel classification. Evaluation metrics (F1 score and micro-averaged F1) indicate that the model outperforms previous clinical and general Spanish language models.

**Key Results:**

- Achieves top performance on datasets such as cantemist, meddocan, and livingner1, among others.
- Consistently surpasses the performance of models that were trained solely on clinical data, demonstrating the advantage of leveraging general domain knowledge during domain adaptation.
- Detailed benchmarking results and comparisons are provided in the associated publication.

For a full breakdown of results (including performance on multilingual baselines and other clinical-specific models), please refer to Table 1 and the Nemenyi plot in the original paper.

![Nemenji plot](./data/nemenji.png)

## Citation

If you use RigoBERTa Clinical in your research, please cite the associated paper:

**BibTeX:**

```bibtex
@article{SUBIES2026114998,
title = {Advancing Spanish clinical language understanding through domain-adaptive pretraining and new open clinical resources},
journal = {Engineering Applications of Artificial Intelligence},
volume = {178},
pages = {114998},
year = {2026},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2026.114998},
url = {https://www.sciencedirect.com/science/article/pii/S0952197626012819},
author = {Guillem García Subies and Álvaro Barbero Jiménez and Paloma Martínez Fernández},
}
```

**APA:**

```
Subies, G. G., Barbero Jiménez, Á., & Martínez Fernández, P. (2026). Advancing Spanish clinical language understanding through domain-adaptive pretraining and new open clinical resources. *Engineering Applications of Artificial Intelligence, 178*, 114998. [https://doi.org/10.1016/j.engappai.2026.114998](https://doi.org/10.1016/j.engappai.2026.114998)
```

## Model Card Authors and Contact

Guillem García Subies: guillem.garcia@iic.uam.es, 100500844@alumnos.uc3m.es