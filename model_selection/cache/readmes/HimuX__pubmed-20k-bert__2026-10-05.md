---
pipeline_tag: text-classification
library_name: transformers
language:
- en
tags:
- medical
- pubmed-rct
license: ms-pl
datasets:
- pietrolesci/pubmed-200k-rct
metrics:
- accuracy
- f1
base_model:
- google-bert/bert-base-uncased
---

# PubMed 20k RCT - BERT Base Classifier
Fine-tuned BERT-base model for sequential sentence classification on randomized controlled trial abstracts.