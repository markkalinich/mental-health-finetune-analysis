---
language:
- en
tags:
- medical
- clinical-ner
- biobert
- bc5cdr


# Clinical NER Model: Chemicals & Diseases

Fine-tuned `microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract` on the [BC5CDR](https://huggingface.co/datasets/bigbio/bc5cdr) dataset.

## Entity Types
- **Chemical** (green)  
- **Disease** (pink)

## Usage
```python
from transformers import pipeline

pipe = pipeline("token-classification", model="HFpf/pubmedbert-bc5cdr-ner")
result = pipe("The patient was treated with metformin for type 2 diabetes.")
print(result)