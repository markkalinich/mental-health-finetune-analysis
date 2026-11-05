---
license: apache-2.0
datasets:
- unimelb-nlp/wikiann
language:
- en
metrics:
- f1
- precision
- recall
base_model:
- google-bert/bert-base-multilingual-cased
pipeline_tag: token-classification
library_name: transformers
tags:
- ner
- named-entity-recognition
- token-classification
- bert
- multilingual
- wikiann
- person
- organization
- location
---
<div align="center">

<h1>Multilingual NER Model for PII Detection</h1>

![Task](https://img.shields.io/badge/Task-NER%20(PII%20Detection)-blue)
![Model](https://img.shields.io/badge/Model-BERT--multilingual--cased-green)
![Dataset](https://img.shields.io/badge/Dataset-WikiANN-orange)
![Language](https://img.shields.io/badge/Language-Multilingual-lightblue)
![Framework](https://img.shields.io/badge/🤗-Transformers-yellow)
![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

</div>
This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased)  
on the WikiANN dataset for Named Entity Recognition (NER).



## Model Description

- **Developed by:** bohrariyanshi
- **Model type:** Token Classification (NER)
- **Language(s):** Multilingual (primarily English)
- **Base model:** bert-base-multilingual-cased
---

## Intended Uses & Limitations

### Intended Uses
- Named Entity Recognition for Person (PER), Organization (ORG), and Location (LOC)
- Text analysis and information extraction
- PII (Personally Identifiable Information) detection

### Limitations
- Trained on WikiANN (multilingual) but evaluated primarily on English subsets
- May have lower performance on non-English text
- Limited to PER, ORG, LOC entity types

## Training Data

The model was fine-tuned on the [WikiANN](https://huggingface.co/datasets/wikiann) dataset:
- **Training examples:** 20,000
- **Validation examples:** 10,000
- **Test examples:** 10,000
- **Entity types:** PER (Person), ORG (Organization), LOC (Location)

## Training Procedure

### Training Hyperparameters
- **Learning rate:** 2e-5
- **Training epochs:** 3
- **Batch size:** 16
- **Max sequence length:** 256
- **Optimizer:** AdamW
- **Weight decay:** 0.01

## Performance

The model achieves high confidence predictions on standard NER tasks:
- **High confidence predictions (>90%):** 19/21 entities in test cases
- **Average inference time:** ~264ms per sentence
- **Entity types detected:** PER, ORG, LOC with high accuracy

## Usage

```python
from transformers import pipeline

# Load the model
ner = pipeline("ner", model="bohrariyanshi/pii-ner-extraction", aggregation_strategy="simple")

# Example usage
text = "Barack Obama was born in Hawaii."
entities = ner(text)
print(entities)
# Output: [{'entity_group': 'PER', 'score': 0.968, 'word': 'Barack Obama', 'start': 0, 'end': 12}, ...]
```

## Model Architecture

- **Base:** BERT-base-multilingual-cased
- **Parameters:** 177M
- **Architecture:** Transformer with token classification head
- **Task:** Named Entity Recognition (NER)

## Evaluation Results

The model demonstrates superior performance compared to base BERT:
- **Confident predictions:** 19 high-confidence entities vs 0 for base BERT
- **Precision:** High accuracy in entity detection
- **Speed:** ~264ms per sentence (acceptable for production use)

## Environmental Impact
Training was performed on a Google Colab T4 GPU for a short duration (fine-tuning only).  
The overall environmental impact is minimal compared to large-scale pretraining runs.

## Citation

If you use this model, please cite:

```bibtex
@model{bohrariyanshi-pii-ner-extraction,
  author = {bohrariyanshi},
  title = {Multilingual NER Model for PII Detection},
  year = {2025},
  url = {https://huggingface.co/bohrariyanshi/pii-ner-extraction}
}
```