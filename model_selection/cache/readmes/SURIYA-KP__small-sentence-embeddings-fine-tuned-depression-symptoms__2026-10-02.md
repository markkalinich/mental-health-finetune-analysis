---
language: en
license: mit
datasets:
  - custom_symptom_dataset
tags:
  - symptom-classification
  - medical-nlp
  - contrastive-learning
  - sentence-embeddings
metrics:
  - MAP: 0.3903
  - Mean R-Precision: 0.3990
  - Mean Precision@10: 0.4349
  - Mean NDCG@1000: 0.5165
---

# Symptom Embedding Model

This model is fine-tuned from [avsolatorio/GIST-all-MiniLM-L6-v2](https://huggingface.co/avsolatorio/GIST-all-MiniLM-L6-v2) using contrastive learning to better identify and classify medical symptom descriptions.

## Model Description

The model was fine-tuned using a contrastive learning approach to improve the embeddings for 21 different symptom types. The goal is to make embeddings of similar symptom descriptions closer in vector space.

## Intended Use

This model is designed for:
- Symptom classification in medical text
- Retrieval of symptom-related information
- Medical text analysis

## Training Procedure

The model was trained using contrastive learning with pairs of symptom descriptions and queries.

### Training Hyperparameters

- Batch size: 16
- Learning rate: 2e-05
- Number of epochs: 1

## Evaluation Results

- Mean Average Precision (MAP): 0.3903
- Mean R-Precision: 0.3990
- Mean Precision@10: 0.4349
- Mean NDCG@1000: 0.5165

## Usage

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("SURIYA-KP/small-sentence-embeddings-fine-tuned-depression-symptoms")
model = AutoModel.from_pretrained("SURIYA-KP/small-sentence-embeddings-fine-tuned-depression-symptoms")

# Prepare text
text = "I feel worthless and useless."

# Tokenize and generate embedding
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)

# Mean pooling
attention_mask = inputs["attention_mask"]
token_embeddings = outputs.last_hidden_state
input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
embedding = torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

# Now 'embedding' is the vectorized representation of your text
# Use this for similarity comparison, classification, etc.
```

## Limitations

This model is specifically trained for symptom classification and may not perform well on unrelated tasks.
