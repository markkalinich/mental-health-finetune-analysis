# Legal Embedding Surgery

## Overview

This repository contains a modified version of **sentence-transformers/all-MiniLM-L6-v2** with an expanded tokenizer vocabulary for the legal domain.

The objective of this project was to perform **embedding surgery** by extending the tokenizer with new legal terms while preserving the pretrained knowledge of the original model.

## Base Model

- sentence-transformers/all-MiniLM-L6-v2

## Added Legal Tokens

- tortfeasor
- estoppel
- subpoena
- habeas
- amicus
- interpleader
- judicata
- voir

## Modifications

- Added 8 legal domain-specific tokens to the tokenizer.
- Resized the model's embedding matrix to accommodate the expanded vocabulary.
- Newly added embeddings were initialized using the Hugging Face `resize_token_embeddings()` method.
- Verified that the original pretrained embeddings remained unchanged.
- Confirmed that the modified model correctly tokenizes the new legal terms and generates sentence embeddings successfully.

## Verification

The following checks were performed:

- Vocabulary size increased from **30,522** to **30,530**.
- All added legal terms are now tokenized as single tokens.
- Existing pretrained embeddings remained unchanged.
- New embedding vectors were successfully created for all added tokens.
- The modified model successfully generated embeddings for legal text.

## Usage

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("SandraChaar1/legal-embedding-surgery")
model = AutoModel.from_pretrained("SandraChaar1/legal-embedding-surgery")
```

## Base Repository

https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2