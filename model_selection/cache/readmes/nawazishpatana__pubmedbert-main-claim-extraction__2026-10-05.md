---
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
datasets:
- nawazishpatana/brain-tumor-claim-extraction
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: pubmedbert-main-claim-extraction
  results:
  - task:
      type: text-classification
      name: Sentence-level Claim Extraction
    dataset:
      name: Brain Tumor Claim Extraction
      type: nawazishpatana/brain-tumor-claim-extraction
      split: test
    metrics:
    - type: accuracy
      value: 0.8641
      name: Accuracy
    - type: precision
      value: 0.7166
      name: Precision
    - type: recall
      value: 0.7922
      name: Recall
    - type: f1
      value: 0.7525
      name: F1
---

# PubMedBERT for Main Claim Extraction

## Model description
This model is a fine-tuned version of PubMedBERT for sentence-level scientific claim extraction in brain tumor / neuro-oncology abstracts.

The notebook then uses the predicted claim probability per sentence to rank sentences within each abstract and select the top-ranked sentence as the predicted main claim.

## Dataset
The dataset was uploaded to:

`nawazishpatana/brain-tumor-claim-extraction`

## Sentence-level evaluation results

- Accuracy: **0.8641**
- Precision: **0.7166**
- Recall: **0.7922**
- F1-score: **0.7525**



## Base model
`microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext`
