---
library_name: transformers
tags:
- sentiment
license: mit
datasets:
- scikit-learn/imdb
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
---

# DistilBERT Sentiment Classifier (IMDb) — saibapanku/distilbert-sentiment

This is a fine-tuned [DistilBERT](https://huggingface.co/distilbert-base-uncased) model for **binary sentiment classification** trained on the IMDb dataset.
The model classifies movie reviews as either **positive** or **negative**.

## Model Details

- **Model name**: `saibapanku/distilbert-sentiment`
- **Base model**: [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased)
- **Task**: Sequence Classification (Sentiment Analysis)
- **Dataset**: [IMDb](https://huggingface.co/datasets/imdb)
- **Labels**:
  - `0`: Negative
  - `1`: Positive

## How to Use

You can load and use the model directly with 🤗 Transformers:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="saibapanku/distilbert-sentiment")
print(classifier("This movie was absolutely amazing!"))
```

## Training Configuration
- Training method: Hugging Face Trainer
- Epochs: 3
- Batch size: 16
- Max sequence length: 256 tokens
- Learning rate: default
- Weight decay: 0.01
- Evaluation strategy: per epoch
- Metric used: Accuracy
- Subset used: 2,000 train / 1,000 test samples (for demo purposes)

Example Output: [{'label': 'positive', 'score': 0.9843}]

# Limitations
This model was trained on a small subset of the IMDb dataset and may not generalize well to all types of reviews.

Performance on domain-specific or multi-lingual content is not guaranteed.

## License
This model is distributed under the MIT License.

Feel free to fine-tune further or adapt it for your specific sentiment analysis tasks!