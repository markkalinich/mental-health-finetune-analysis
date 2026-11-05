---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- transformers
- distilbert
- nlp
- fine-tuned
- movie-reviews
- binary-classification
datasets:
- cornell-movie-review-data/rotten_tomatoes
metrics:
- accuracy
- f1
- precision
- recall
base_model: distilbert/distilbert-base-uncased
model-index:
- name: distilbert-sentiment-rotten-tomatoes
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Rotten Tomatoes
      type: cornell-movie-review-data/rotten_tomatoes
      split: test
    metrics:
    - type: accuracy
      value: 0.8199
      name: Accuracy
    - type: f1
      value: 0.8199
      name: F1 (Macro)
    - type: precision
      value: 0.8200
      name: Precision (Macro)
    - type: recall
      value: 0.8199
      name: Recall (Macro)
---

# 🎬 DistilBERT Sentiment Analysis — Rotten Tomatoes

A fine-tuned [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) model for **binary sentiment classification** of movie reviews. Given a piece of text, the model predicts whether the sentiment is **POSITIVE** or **NEGATIVE**.

| Property | Value |
|---|---|
| **Model** | DistilBERT-base-uncased (67M parameters) |
| **Task** | Binary sentiment classification |
| **Dataset** | [Rotten Tomatoes](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes) |
| **Test Accuracy** | **82.0%** |
| **Macro F1** | **0.8199** |
| **License** | Apache 2.0 |

---

## Model Description

This model is a **fine-tuned** version of [`distilbert/distilbert-base-uncased`](https://huggingface.co/distilbert/distilbert-base-uncased) trained on the Rotten Tomatoes movie review dataset for binary sentiment classification.

- **Architecture:** DistilBERT (6-layer, 768-hidden, 12-heads, 67M parameters) with a sequence classification head
- **Task:** Predicting whether a movie review expresses a **positive** or **negative** sentiment
- **Output labels:** `POSITIVE` (1) and `NEGATIVE` (0)
- **Primary use case:** Analyzing sentiment in movie reviews and similar short-form text

DistilBERT is a distilled version of BERT that retains 97% of BERT's language understanding while being 60% faster and 40% smaller — making it ideal for production deployments where inference speed and resource efficiency matter.

---

## Quickstart — Inference

### Using the `pipeline` API (Recommended)

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="keerthi1515/distilbert-sentiment-rotten-tomatoes"
)

# Single prediction
result = classifier("This movie was absolutely fantastic! A must-watch.")
print(result)
# [{'label': 'POSITIVE', 'score': 0.96}]

# Batch prediction
results = classifier([
    "A beautifully crafted film with outstanding performances.",
    "Terrible script and wooden acting throughout.",
    "An average movie, nothing special but not terrible either.",
])
for text, res in zip(texts, results):
    print(f"{res['label']} ({res['score']:.2%}): {text}")
```

### Using model and tokenizer directly

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("keerthi1515/distilbert-sentiment-rotten-tomatoes")
model = AutoModelForSequenceClassification.from_pretrained("keerthi1515/distilbert-sentiment-rotten-tomatoes")

text = "One of the best films I have ever seen!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()

label_map = {0: "NEGATIVE", 1: "POSITIVE"}
print(f"Prediction: {label_map[predicted_class]} (confidence: {probabilities[0][predicted_class]:.2%})")
```

---

## Dataset

### Rotten Tomatoes Movie Reviews

This model was trained on the [Rotten Tomatoes](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes) dataset, a widely used benchmark for sentiment analysis research.

| Property | Details |
|---|---|
| **Source** | [cornell-movie-review-data/rotten_tomatoes](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes) |
| **Domain** | Movie reviews |
| **Task** | Binary sentiment classification |
| **Classes** | Negative (0), Positive (1) |
| **Total size** | 10,662 samples |

### Data Splits

| Split | Samples | Class Balance |
|---|---|---|
| Train | 8,530 | 50% positive / 50% negative |
| Validation | 1,066 | 50% positive / 50% negative |
| Test | 1,066 | 50% positive / 50% negative |

### Preprocessing

- **Tokenization:** WordPiece tokenizer (DistilBERT's default, 30,522 vocabulary)
- **Max sequence length:** 128 tokens (with truncation)
- **Padding:** Dynamic padding to the longest sequence in each batch
- **Training subset:** 2,000 training samples used (out of 8,530 available) to accommodate CPU-based training constraints
- **Validation subset:** 500 samples used during training; full test set (1,066) used for final evaluation
- **No additional text cleaning** — raw review text fed directly to the tokenizer

---

## Training Details

### Training Configuration

| Hyperparameter | Value |
|---|---|
| **Base model** | `distilbert/distilbert-base-uncased` |
| **Learning rate** | 2e-5 |
| **Batch size (train)** | 32 |
| **Batch size (eval)** | 64 |
| **Epochs** | 3 |
| **Optimizer** | AdamW (fused) with β₁=0.9, β₂=0.999, ε=1e-8 |
| **LR scheduler** | Linear decay |
| **Weight decay** | 0.01 |
| **Max sequence length** | 128 tokens |
| **Seed** | 42 |
| **Training samples** | 2,000 (subset) |
| **Validation samples** | 500 (subset) |
| **Hardware** | CPU (Intel Xeon) |
| **Training time** | ~8 minutes |
| **Framework** | Transformers 5.6.2, PyTorch 2.11.0 |

### Training Method

Standard supervised fine-tuning using the Hugging Face `Trainer` API:

1. Loaded pre-trained DistilBERT with a randomly initialized classification head (2 output classes)
2. Fine-tuned **all model parameters** (full fine-tuning, not LoRA/adapter-based)
3. Evaluated on the validation set after each epoch
4. Selected the best checkpoint based on validation accuracy

### Training Progress

| Epoch | Training Loss | Validation Loss | Validation Accuracy |
|:---:|:---:|:---:|:---:|
| 1 | 0.4692 | 0.4425 | 80.6% |
| 2 | 0.4049 | 0.4065 | 82.2% |
| 3 | 0.2531 | 0.4188 | 82.2% |

> **Note:** Validation loss increases slightly from epoch 2 → 3 while training loss continues decreasing, indicating mild overfitting. The model would benefit from early stopping or training on the full dataset.

---

## Evaluation Results

### Test Set Performance (1,066 samples)

All metrics computed on the **full test split** of Rotten Tomatoes (1,066 samples, perfectly balanced at 533 per class).

| Metric | NEGATIVE | POSITIVE | Macro Average |
|---|:---:|:---:|:---:|
| **Precision** | 0.8248 | 0.8152 | 0.8200 |
| **Recall** | 0.8124 | 0.8274 | 0.8199 |
| **F1-Score** | 0.8185 | 0.8212 | 0.8199 |
| **Support** | 533 | 533 | 1,066 |

| | **Overall** |
|---|:---:|
| **Accuracy** | **0.8199** |
| **Weighted F1** | **0.8199** |
| **Test Loss** | **0.4282** |

### Confusion Matrix

| | Predicted NEGATIVE | Predicted POSITIVE |
|---|:---:|:---:|
| **Actual NEGATIVE** | **433** (TN) | 100 (FP) |
| **Actual POSITIVE** | 92 (FN) | **441** (TP) |

- **True Positives:** 441 — correctly identified positive reviews
- **True Negatives:** 433 — correctly identified negative reviews
- **False Positives:** 100 — negative reviews misclassified as positive
- **False Negatives:** 92 — positive reviews misclassified as negative

---

## Results Analysis

### What 82% Accuracy Means

An accuracy of **82.0%** means the model correctly classifies approximately **4 out of every 5** movie reviews. On a balanced binary task (50/50 class split), random guessing would achieve 50%, so the model provides a **32 percentage point improvement** over chance.

For context, state-of-the-art models on Rotten Tomatoes (e.g., RoBERTa-large trained on the full dataset) achieve ~89-91% accuracy. This model's 82% accuracy is strong given that it was trained on only **23.4% of the available training data** (2,000 out of 8,530 samples) on a CPU.

### Model Strengths

- **Balanced performance:** Near-identical precision and recall across both classes (within 1.5%), meaning the model is not biased toward predicting one class over the other
- **High confidence on clear cases:** Reviews with strong sentiment language are classified with >90% confidence
- **Fast inference:** DistilBERT's compact architecture enables sub-millisecond inference per sample on GPU and <50ms on CPU
- **Robust tokenization:** Handles varied vocabulary, informal language, and proper nouns well due to WordPiece subword tokenization

### Where It Struggles

- **Sarcasm and irony:** "What a *brilliant* use of two hours" may be classified as positive when the intent is negative
- **Mixed sentiment:** Reviews that contain both praise and criticism (e.g., "Great acting but terrible plot") are harder to classify
- **Short or ambiguous text:** Very brief reviews like "It was okay" or "Not bad" lack sufficient signal
- **Domain shift:** The model was trained exclusively on movie reviews and may perform poorly on other domains (product reviews, social media posts, news sentiment)
- **Nuanced language:** Subtle negativity or understated praise (e.g., "The film tries hard but falls short") can be missed

---

## Limitations & Bias

### Dataset Bias

- **Domain-specific:** Trained exclusively on Rotten Tomatoes movie reviews — a particular style of English-language film criticism. Performance will degrade on other text domains
- **English only:** The model only understands English text
- **Temporal bias:** The Rotten Tomatoes dataset reflects movie reviews from a specific time period and may not capture evolving language patterns or cultural references
- **Binary oversimplification:** Real-world sentiment exists on a spectrum; forcing binary classification loses nuance (neutral, mixed, or conditional sentiments are forced into one category)
- **Subset training:** Only 2,000 of 8,530 available training samples were used, which limits the model's exposure to the full diversity of review styles

### Model Limitations

- **Maximum input length:** 128 tokens (~50-70 words). Longer reviews are truncated, potentially losing critical context
- **No aspect-level analysis:** The model provides a single overall sentiment score — it cannot identify sentiment toward specific aspects (acting, plot, cinematography)
- **No explanation:** The model outputs a label and confidence score but does not explain *why* it made a particular classification
- **Confidence calibration:** High confidence scores do not necessarily indicate correctness — the model can be confidently wrong

### Ethical Considerations

- **Not suitable for high-stakes decisions:** This model should not be used as the sole basis for decisions that significantly impact individuals (e.g., content moderation without human review)
- **Potential for misuse:** Sentiment analysis models can be misused for surveillance, manipulation of reviews, or biased filtering of opinions
- **Representation gaps:** The training data may not equally represent all demographic groups, cultural perspectives, or dialects of English
- **Feedback loops:** Deploying sentiment analysis in production can create feedback loops where content is filtered based on predicted sentiment, which may suppress legitimate negative opinions

---

## Use Cases

### Recommended Applications

1. **Movie review classification:** Automatically categorize user-submitted movie reviews as positive or negative for aggregation and analysis
2. **Customer feedback triage:** Route incoming customer feedback to appropriate teams based on sentiment polarity
3. **Content analysis:** Analyze sentiment trends across movie review collections or entertainment media
4. **Educational tool:** Demonstrate NLP sentiment analysis concepts with a lightweight, easy-to-deploy model
5. **Prototype/baseline:** Use as a quick baseline before investing in larger, more expensive models

### Not Recommended For

- Medical, legal, or financial sentiment analysis (different domain, higher stakes)
- Real-time social media monitoring without domain adaptation
- Multi-language or code-switched text analysis
- Tasks requiring fine-grained sentiment (1-5 stars, emotion detection)

---

## Future Improvements

Several directions could improve this model's performance:

| Improvement | Expected Impact |
|---|---|
| **Train on full dataset** (8,530 samples) | +3-5% accuracy — currently uses only 23% of available data |
| **Upgrade to BERT-base or RoBERTa** | +3-7% — larger models capture more linguistic nuance |
| **Hyperparameter tuning** | +1-2% — optimize learning rate, batch size, epochs systematically |
| **Data augmentation** | +1-3% — back-translation, synonym replacement, paraphrase generation |
| **Increase max sequence length** (128 → 256) | +0.5-1% — capture full review context without truncation |
| **Multi-dataset training** | +2-4% — combine SST-2, IMDB, Amazon reviews for better generalization |
| **Add early stopping** | Prevent overfitting observed at epoch 3 |
| **Domain adaptation** | Extend to product reviews, social media, customer support |

---

## Framework Versions

| Component | Version |
|---|---|
| Transformers | 5.6.2 |
| PyTorch | 2.11.0 |
| Datasets | 4.8.4 |
| Tokenizers | 0.22.2 |
| Python | 3.12 |

---

## Citation

If you use this model, please cite the original DistilBERT paper and the Rotten Tomatoes dataset:

```bibtex
@article{sanh2019distilbert,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  journal={arXiv preprint arXiv:1910.01108},
  year={2019}
}

@inproceedings{pang2005seeing,
  title={Seeing Stars: Exploiting Class Relationships for Sentiment Categorization with Respect to Rating Scales},
  author={Pang, Bo and Lee, Lillian},
  booktitle={Proceedings of the ACL},
  year={2005}
}
```

---

## Contact

- **Model repository:** [keerthi1515/distilbert-sentiment-rotten-tomatoes](https://huggingface.co/keerthi1515/distilbert-sentiment-rotten-tomatoes)
- **Base model:** [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)
- **Dataset:** [cornell-movie-review-data/rotten_tomatoes](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes)
