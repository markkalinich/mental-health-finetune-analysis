---
tags:
  - sentence-transformers
  - sentiment-analysis
  - youtube
  - english
  - text-classification
  - feature-extraction
  - dense
  - mpnet
  - 3-class
dataset_size: "1022514"
loss: "SoftmaxLossClassification"
base_model: "sentence-transformers/paraphrase-mpnet-base-v2"
widget:
  - text: "this is the best video ever"
    label: Positive
  - text: "this video is terrible waste of time"
    label: Negative
  - text: "nice tutorial thanks for sharing"
    label: Positive
  - text: "i dont like this at all"
    label: Negative
  - text: "thanks for the info"
    label: Neutral
pipeline_tag: "text-classification"
library_name: "sentence-transformers"
---

# YouTube Sentiment Classifier (English, MPNet)

A high-performance **3-class sentiment classification model** fine-tuned on **1,022,514 English YouTube comments** for accurate sentiment analysis of social media text.

## Model Overview

| Attribute | Value |
|---|---|
| **Model Type** | Sentence Transformer + Classification Head |
| **Base Model** | [sentence-transformers/paraphrase-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-mpnet-base-v2) |
| **Task** | 3-Class Sentiment Classification |
| **Labels** | `0` = Negative, `1` = Neutral, `2` = Positive |
| **Embedding Dimension** | 768 |
| **Max Sequence Length** | 512 tokens |
| **Language** | English |
| **Dataset Size** | 1,022,514 YouTube comments |
| **Cross-Validation Accuracy** | **90.62%** (±0.41%) |
| **Test Accuracy** | **76.8%** (KNN classifier) |

## Capabilities

- **YouTube Comment Sentiment Analysis** — classify comments as Negative, Neutral, or Positive
- **Social Media Text Analysis** — general-purpose sentiment for informal English text
- **Feature Extraction** — generate 768-dimensional dense embeddings for downstream tasks
- **Semantic Similarity** — leverage sentence embeddings for similarity-based applications
- **Text Classification** — fine-tune or use as a feature extractor for custom tasks

## Installation

```bash
pip install -U sentence-transformers
```

## Usage

### Sentiment Classification

```python
from sentence_transformers import SentenceTransformer
import torch
import torch.nn as nn

# Load the model
model = SentenceTransformer("Arshia82sbn/youtube-sentiment-classifier-english-mpnet")

# Example comments
comments = [
    "this is the best video ever",
    "this video is terrible waste of time",
    "thanks for the info",
    "nice tutorial thanks for sharing",
    "i dont like this at all"
]

# Get embeddings
embeddings = model.encode(comments)

# For sentiment prediction, use the embeddings with a classifier head
# The model produces 768-dimensional embeddings
print(f"Embedding shape: {embeddings.shape}")  # (5, 768)
```

### Embedding Extraction

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Arshia82sbn/youtube-sentiment-classifier-english-mpnet")

sentences = [
    "this is the best video ever",
    "this video is terrible waste of time",
    "thanks for the info"
]

embeddings = model.encode(sentences)
print(f"Embedding shape: {embeddings.shape}")  # (3, 768)

# Compute cosine similarity
similarities = model.similarity(embeddings, embeddings)
print(similarities)
```

### Direct Inference with Classification Head

```python
from sentence_transformers import SentenceTransformer
import torch.nn as nn

class SentimentClassifier(nn.Module):
    def __init__(self, base_model_path, num_classes=3):
        super().__init__()
        self.base_model = SentenceTransformer(base_model_path)
        self.classifier = nn.Linear(768, num_classes)
    
    def forward(self, texts):
        embeddings = self.base_model.encode(texts, convert_to_tensor=True)
        logits = self.classifier(embeddings)
        return logits

# Load and predict
classifier = SentimentClassifier("Arshia82sbn/youtube-sentiment-classifier-english-mpnet")
logits = classifier(["this is great!", "this is terrible"])
predictions = torch.argmax(logits, dim=-1)
print(predictions)  # tensor([2, 0]) -> [Positive, Negative]
```

## Training Details

### Dataset

- **Source:** YouTube comments dataset
- **Total Samples:** 1,032,225 (1,022,514 after cleaning)
- **Split:** 70% Train (715,759) / 15% Test (153,377) / 15% Validation (153,378)
- **Class Distribution:**
  - Negative: 343,257 (33.6%)
  - Neutral: 337,432 (33.0%)
  - Positive: 341,825 (33.4%)

### Hyperparameters

| Parameter | Value |
|---|---|
| Epochs | 5 |
| Batch Size | 8 |
| Learning Rate | 3e-5 |
| Weight Decay | 0.01 |
| Optimizer | Adam |
| Max Gradient Norm | 1.0 |
| Warmup Steps | 10% of training steps |
| Max Sequence Length | 512 |

### Loss Function

Custom `SoftmaxLossClassification` — a linear classifier head placed on top of sentence-transformer embeddings, trained with CrossEntropyLoss for 3-class sentiment classification.

### Evaluation Metrics

| Metric | Value |
|---|---|
| Cross-Validation Accuracy | 90.62% (±0.41%) |
| Test Accuracy (KNN) | 76.8% |
| Precision (Negative) | 0.78 |
| Recall (Negative) | 0.81 |
| F1-Score (Negative) | 0.80 |
| Precision (Neutral) | 0.71 |
| Recall (Neutral) | 0.72 |
| F1-Score (Neutral) | 0.71 |
| Precision (Positive) | 0.82 |
| Recall (Positive) | 0.77 |
| F1-Score (Positive) | 0.80 |

## Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False, 'architecture': 'MPNetModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_mean_tokens': True})
)
```

## Framework Versions

- Python: 3.10.19
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.5.1
- Accelerate: 1.11.0

## Citation

```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

## License

This model is released under the same license as the base model.

## Contact

For questions or issues, please open an issue on the model repository or contact the model author.
