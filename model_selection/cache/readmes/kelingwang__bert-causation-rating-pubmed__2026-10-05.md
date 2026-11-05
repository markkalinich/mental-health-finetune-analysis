---
license: mit
language:
- en
metrics:
- accuracy
- mse
- f1
base_model:
- dmis-lab/biobert-base-cased-v1.2
- google-bert/bert-base-cased
pipeline_tag: text-classification
model-index:
- name: bert-causation-rating-pubmed
  results:
  - task:
      type: text-classification
    dataset:
      name: pubmed_textdata
      type: dataset
    metrics:
    - name: off by 1 accuracy
      type: accuracy
      value: 83.5621
    - name: mean squared error for ordinal data
      type: mse
      value: 0.8108
    - name: weighted F1 score
      type: f1
      value: 0.8208
    - name: Kendall's tau coefficient
      type: Kendall's tau
      value: 0.7929

---

# Model
This is a BioBERT based model trained on a set of manually annotated texts with causation labels, tasked with classifying a sentence into different levels of strength of causation.
This `rating-pubmed` version is tuned on the dataset provided in a published article [Yu et al. (2019)](https://aclanthology.org/D19-1473/) *Detecting Causal Language Use in Science Findings*.