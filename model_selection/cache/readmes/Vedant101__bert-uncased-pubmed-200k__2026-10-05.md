# PubMed 200k RCT DeBERTa v3 Model

This model is fine-tuned on the PubMed 200k RCT dataset using the DeBERTa v3 base model.

## Model Details
- Base model: microsoft/deberta-v3-base
- Fine-tuned on: PubMed 200k RCT dataset
- Task: Sequence Classification
- Number of classes: 5
- Max sequence length: 68

## Usage
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained('Vedant101/bert-uncased-pubmed-200k')
tokenizer = AutoTokenizer.from_pretrained('Vedant101/bert-uncased-pubmed-200k')
```
