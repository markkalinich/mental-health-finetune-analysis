---
license: mit
tags:
- feature-extraction
language: en
---

# PubMedNCL

A pretrained language model for document representations of biomedical papers. 
PubMedNCL is based on [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext), which is a BERT model pretrained on abstracts and full-texts from PubMedCentral, and fine-tuned via citation neighborhood contrastive learning, as introduced by [SciNCL](https://huggingface.co/malteos/scincl).

## How to use the pretrained model


```python
from transformers import AutoTokenizer, AutoModel

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('malteos/PubMedNCL')
model = AutoModel.from_pretrained('malteos/PubMedNCL')

papers = [{'title': 'BERT', 'abstract': 'We introduce a new language representation model called BERT'},
          {'title': 'Attention is all you need', 'abstract': ' The dominant sequence transduction models are based on complex recurrent or convolutional neural networks'}]

# concatenate title and abstract with [SEP] token
title_abs = [d['title'] + tokenizer.sep_token + (d.get('abstract') or '') for d in papers]

# preprocess the input
inputs = tokenizer(title_abs, padding=True, truncation=True, return_tensors="pt", max_length=512)

# inference
result = model(**inputs)

# take the first token ([CLS] token) in the batch as the embedding
embeddings = result.last_hidden_state[:, 0, :]
```

## Citation

- [Neighborhood Contrastive Learning for Scientific Document Representations with Citation Embeddings (EMNLP 2022 paper)](https://arxiv.org/abs/2202.06671).
- [Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing](https://arxiv.org/abs/2007.15779).

## License 

MIT

