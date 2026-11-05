---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
tags:
- generated_from_trainer
datasets:
- bc5cdr
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: BiomedNLP-PubMedBERT-base-uncased-abstract-bc5cdr-ner-v1
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: bc5cdr
      type: bc5cdr
      config: bc5cdr_source
      split: validation
      args: bc5cdr_source
    metrics:
    - name: Precision
      type: precision
      value: 0.8581588700791345
    - name: Recall
      type: recall
      value: 0.897726081944881
    - name: F1
      type: f1
      value: 0.877496671105193
    - name: Accuracy
      type: accuracy
      value: 0.9726919202313766
---

# 🧬 Biomedical NER — Experimental Model (BC5CDR)

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the bc5cdr dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0835
- Precision: 0.8582
- Recall: 0.8977
- F1: 0.8775
- Accuracy: 0.9727

This repository hosts a **testing version** of a biomedical named entity recognition (NER) model fine-tuned on the [**BC5CDR dataset**](https://huggingface.co/datasets/bigbio/bc5cdr), which contains PubMed abstracts annotated for *diseases* and *chemicals*.

⚠️ **Note:** This model is shared **for educational and testing purposes only**. It is **not intended for clinical or production use** and may not generalize beyond the BC5CDR dataset.

## Model overview

- **Base model:** [PubMedBERT (abstracts)](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) (domain-specific transformer)
- **Task:** Named Entity Recognition (token classification)
- **Entities:**  
  - `Chemical`  
  - `Disease`  
  - `O` (non-entity tokens)

The model predicts entity spans following the standard **BIO tagging scheme**, e.g. `B-Chemical`, `I-Disease`, `O`.

## Training notebook

The full training and preprocessing pipeline — including dataset preparation, sentence splitting, BIO tagging, and evaluation — is documented in [this Kaggle notebook](https://www.kaggle.com/code/francescoalbanesephd/pubmedbert-lora-for-biomedical-ner-bc5cdr)

## Example usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Francesco-A/BiomedNLP-PubMedBERT-base-uncased-abstract-bc5cdr-ner-v1")
model = AutoModelForTokenClassification.from_pretrained("Francesco-A/BiomedNLP-PubMedBERT-base-uncased-abstract-bc5cdr-ner-v1")

ner = pipeline("token-classification", model=model, tokenizer=tokenizer, aggregation_strategy="first")

demo_texts = [
    "Aspirin is often used to treat inflammation, but may cause gastric bleeding.",
    "Naloxone reverses the antihypertensive effect of clonidine.",
]

for t in demo_texts:
    print("\nText:", t)
    preds = ner(t)
    for p in preds:
        print(f'  - {p["word"]}: {p["entity_group"]} (score {p["score"]:.2f})')
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-5
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.9836 | 15   | 0.5775          | 0.0299    | 0.0002 | 0.0004 | 0.8627   |
| No log        | 1.9672 | 30   | 0.2332          | 0.7252    | 0.5753 | 0.6416 | 0.9284   |
| No log        | 2.9508 | 45   | 0.1237          | 0.7610    | 0.8265 | 0.7924 | 0.9606   |
| No log        | 4.0    | 61   | 0.0937          | 0.8364    | 0.8859 | 0.8605 | 0.9690   |
| No log        | 4.9836 | 76   | 0.0860          | 0.8510    | 0.8927 | 0.8714 | 0.9714   |
| No log        | 5.9672 | 91   | 0.0833          | 0.8502    | 0.8995 | 0.8741 | 0.9724   |
| 0.3513        | 6.9508 | 106  | 0.0859          | 0.8494    | 0.8992 | 0.8736 | 0.9714   |
| 0.3513        | 7.8689 | 120  | 0.0835          | 0.8582    | 0.8977 | 0.8775 | 0.9727   |


### Framework versions

- Transformers 4.45.0
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.20.3
