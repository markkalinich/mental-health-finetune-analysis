---
tags:
- sentiment-analysis
- distilbert
- dapt
- domain-adaptation
- fine-tuned
- imdb
- movie-reviews
license: apache-2.0
datasets:
- stanfordnlp/imdb
language:
- en
base_model:
- ayushshah/distilbert-base-uncased-imdb-dapt
pipeline_tag: text-classification
model-index:
- name: distilbert-dapt-imdb-sentiment
  results:
    - task:
        type: text-classification
        name: Text Classification
      dataset:
        name: imdb
        type: imdb
        split: test
      metrics:
      - type: accuracy
        name: Accuracy
        value: 0.93185
      - type: f1
        name: F1 Score
        value: 0.9321248941785768
      - type: precision
        name: Precision
        value: 0.9300407433171023
      - type: recall
        name: Recall
        value: 0.9342184068676382
      - type: roc_auc
        name: ROC AUC
        value: 0.9810583236289687
    - task:
        type: text-classification
        name: Text Classification
      dataset:
        name: sst2
        type: sst2
        split: validation
      metrics:
      - type: accuracy
        name: Accuracy
        value: 0.8899082568807339
      - type: f1
        name: F1 Score
        value: 0.8926174496644296
      - type: precision
        name: Precision
        value: 0.8866666666666667
      - type: recall
        name: Recall
        value: 0.8986486486486487
      - type: roc_auc
        name: ROC AUC
        value: 0.9450960890797341
---

# DistilBERT IMDb DAPT Sentiment Classifier
This model is a sentiment classification model built on top of a Domain-Adaptive Pretrained (DAPT) DistilBERT encoder, further fine-tuned on the IMDb movie reviews sentiment classification task.

The encoder was first adapted to the movie review domain using masked language modeling (MLM) on IMDb reviews, and then a linear classification head was trained for binary sentiment prediction.

The model predicts:
- Positive
- Negative
for English movie reviews.

# Model architecture
- **Base model**: [DistilBERT DAPT IMDb](https://huggingface.co/ayushshah/distilbert-base-uncased-imdb-dapt)
- **Classifier Head**: Linear layer on top of the `[CLS]` token.
- **Pre-classifier**: Not used in this implementation
- **Labels**: 2

# Fine tuning details
- Dataset: [stanford/imdb](https://huggingface.co/datasets/stanfordnlp/imdb/)
- Loss: Cross-entropy loss
- Tokenization: WordPiece
- Dynamic padding
- Train samples: 25k
- Validation samples: 5k
- Test samples: 20k

# Intended Uses
**Supported Use Cases**
- Sentiment analysis of movie reviews
- Opinion mining on review-style English text
- NLP research on domain adaptation

**Out-of-Scope Uses**
- Medical, legal or financial decision-making
- Safety-critical systems
- Content moderation or profiling of individuals
- Non-English or highly technical text

# Usage
**Loading the model**
```python
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file as safe_load_file

REPO_ID = "ayushshah/distilbert-dapt-imdb-sentiment"
hf_hub_download(repo_id=REPO_ID, filename="model.py", local_dir=".")

from model import DistilBERTClassifier, infer_reviews

classifier = DistilBERTClassifier()
tokenizer = AutoTokenizer.from_pretrained(REPO_ID)

model_path = hf_hub_download(repo_id=REPO_ID, filename="model.safetensors")
classifier.load_state_dict(safe_load_file(model_path))
classifier.eval()
```

**Inference**
```python
# For single review inference
sample_review = "Great movie"
label_class, label, conf = infer_reviews(sample_review, classifier, tokenizer)
print(f"Predicted Sentiment: {label} (Confidence: {conf:.4f})\n")

# For batch inference
reviews = ["I loved this film!", "This was a terrible movie."]
results = infer_reviews(reviews, classifier, tokenizer)
for review, (label_class, label, conf) in zip(reviews, results):
    print(f"Predicted Sentiment: {label} (Confidence: {conf:.4f})\n")
```

# Evaluation
- Faster convergance during fine-tuning
- DAPT improves accuracy compared to DistilBERT base
- Not using a pre_classifier gives marginal better results (~0.5%) with lesser parameters

# Limitations
- Inherits biases present in IMDb reviews
- Performance may degrade on non-review text
- Not suitable for sarcasm-heavy or highly nuanced sentiment
- Not designed for multilingual sentiment analysis

# Ethical Considerations
- IMDb reviews may reflect demographic and cultural biases
- Outputs should not be used to infer personal traits
- The model should not be used for automated moderation or sensitive decision-making

# Training Hyperparameters
- Encoder LR: 1e-5
- Classifier LR: 5e-5
- Optimizer: AdamW
- Epochs: 3
- Batch size: 64
- Scheduler: Linear decay (min lr: 1e-8) with 10% warmup
- Automatic mixed precision training

# Training Stats
Epoch 1: Train Loss: 0.3159, Train Acc: 0.8533 | Val Loss: 0.2046, Val Acc: 0.9160<br>
Epoch 2: Train Loss: 0.1744, Train Acc: 0.9341 | Val Loss: 0.1986, Val Acc: 0.9220<br>
Epoch 3: Train Loss: 0.1400, Train Acc: 0.9507 | Val Loss: 0.2009, Val Acc: 0.9230

# License
This model follows the license of the base DistilBERT model. Please refer to the Hugging Face repository for license details.

# More information
- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)
- [GitHub](https://github.com/AyushShahh/DistilBERT-IMDb)