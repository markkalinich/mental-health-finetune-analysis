---
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- transformers
- roberta
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
base_model: FacebookAI/roberta-base
model-index:
- name: roberta-sentiment-rotten-tomatoes
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
      value: 0.8846
      name: Accuracy
    - type: f1
      value: 0.8845
      name: F1 (Binary)
    - type: precision
      value: 0.8853
      name: Precision (Binary)
    - type: recall
      value: 0.8837
      name: Recall (Binary)
---

# 🎬 RoBERTa Sentiment Analysis — Rotten Tomatoes

A fine-tuned [RoBERTa-base](https://huggingface.co/FacebookAI/roberta-base) model for **binary sentiment classification** of movie reviews. Upgraded from a DistilBERT baseline (82%) to achieve **88.5% test accuracy** with balanced precision and recall.

| Property | Value |
|---|---|
| **Model** | RoBERTa-base (124.6M parameters) |
| **Task** | Binary sentiment classification |
| **Dataset** | [Rotten Tomatoes](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes) (full 8,530 training samples) |
| **Test Accuracy** | **88.5%** |
| **Macro F1** | **0.8846** |
| **License** | MIT |

---

## Model Description

This model is a **fine-tuned** version of [`FacebookAI/roberta-base`](https://huggingface.co/FacebookAI/roberta-base) trained on the full Rotten Tomatoes movie review dataset for binary sentiment classification.

- **Architecture:** RoBERTa-base (12-layer, 768-hidden, 12-heads, 124.6M parameters) with a sequence classification head
- **Task:** Predicting whether a movie review expresses a **positive** or **negative** sentiment
- **Output labels:** `POSITIVE` (1) and `NEGATIVE` (0)
- **Primary use case:** Analyzing sentiment in movie reviews and similar short-form text

RoBERTa (Robustly optimized BERT approach) improves on BERT with dynamic masking, larger batches, longer training, and no next-sentence prediction. These changes yield consistently better downstream performance on classification tasks (Liu et al., 2019).

### Improvement Over Baseline

| Model | Test Accuracy | Test F1 | Improvement |
|---|:---:|:---:|:---:|
| DistilBERT (baseline, 2K samples) | 82.0% | 0.8199 | — |
| **RoBERTa-base (this model, 8.5K samples)** | **88.5%** | **0.8846** | **+6.5 pp** |

---

## Quickstart — Inference

### Using the `pipeline` API (Recommended)

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="keerthi1515/roberta-sentiment-rotten-tomatoes"
)

# Single prediction
result = classifier("This movie was absolutely fantastic! A must-watch.")
print(result)
# [{'label': 'POSITIVE', 'score': 0.997}]

# Batch prediction
texts = [
    "A beautifully crafted film with outstanding performances.",
    "Terrible script and wooden acting throughout.",
    "An average movie, nothing special but not terrible either.",
]
results = classifier(texts)
for text, res in zip(texts, results):
    print(f"{res['label']} ({res['score']:.2%}): {text}")
```

### Using model and tokenizer directly

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("keerthi1515/roberta-sentiment-rotten-tomatoes")
model = AutoModelForSequenceClassification.from_pretrained("keerthi1515/roberta-sentiment-rotten-tomatoes")

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

### Class Imbalance Assessment

The dataset is **perfectly balanced** at 50/50 across all splits (4,265 per class in train). No class weighting, oversampling, or loss rebalancing is needed — standard cross-entropy loss works optimally.

### Preprocessing

- **Tokenization:** Byte-Pair Encoding (RoBERTa's default, 50,265 vocabulary)
- **Max sequence length:** 128 tokens (with truncation)
- **Padding:** Dynamic padding via `DataCollatorWithPadding` (pads to longest in each batch)
- **Training data:** Full dataset used (8,530 training samples)
- **No additional text cleaning** — raw review text fed directly to the tokenizer

---

## Training Details

### Training Configuration

| Hyperparameter | Value |
|---|---|
| **Base model** | `FacebookAI/roberta-base` (124.6M params) |
| **Learning rate** | 2e-5 |
| **LR scheduler** | Linear warmup + linear decay |
| **Warmup steps** | 100 |
| **Batch size (train)** | 16 |
| **Batch size (eval)** | 32 |
| **Max epochs** | 5 (with early stopping) |
| **Early stopping** | Patience=2, threshold=0.001 |
| **Optimizer** | AdamW (fused) with β₁=0.9, β₂=0.999, ε=1e-8 |
| **Weight decay** | 0.01 |
| **Gradient clipping** | max_grad_norm=1.0 |
| **Mixed precision** | Disabled (CPU training) |
| **Max sequence length** | 128 tokens |
| **Seed** | 42 |
| **Steps per epoch** | 534 |
| **Framework** | Transformers 5.7.0, PyTorch 2.11.0 |

### Training Method

Full supervised fine-tuning using the Hugging Face `Trainer` API with advanced optimization:

1. Loaded pre-trained RoBERTa-base with a randomly initialized classification head (2 output classes)
2. Fine-tuned **all 124.6M parameters** (full fine-tuning, not LoRA/adapter-based)
3. Applied linear warmup over 100 steps followed by linear decay
4. Gradient clipping at norm 1.0 to prevent exploding gradients
5. Evaluated on validation set after each epoch
6. Early stopping with patience=2 monitors accuracy to prevent overfitting
7. Best model selected automatically via `load_best_model_at_end=True`

### Training Progress

| Epoch | Training Loss | Validation Loss | Val Accuracy | Val Precision | Val Recall | Val F1 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.3014 | 0.3126 | 87.9% | 0.8401 | 0.9362 | 0.8855 |
| 2 | 0.2930 | 0.3687 | 88.3% | 0.8542 | 0.9231 | 0.8873 |
| **3** | **0.1685** | **0.4477** | **89.0%** | **0.8741** | **0.9118** | **0.8926** |
| 4 | 0.1041 | 0.5700 | 88.3% | 0.8630 | 0.9099 | 0.8858 |
| 5 | 0.0613 | 0.5546 | 88.5% | 0.8714 | 0.9024 | 0.8866 |

> **Note:** Validation loss increases steadily from epoch 1 onwards while training loss drops to 0.06, showing classic overfitting. Best validation accuracy was at epoch 3 (89.0%). Early stopping loaded the best checkpoint.

---

## Evaluation Results

### Test Set Performance (1,066 samples)

All metrics computed on the **full test split** (1,066 samples, perfectly balanced at 533 per class).

| Metric | NEGATIVE | POSITIVE | Macro Average |
|---|:---:|:---:|:---:|
| **Precision** | 0.8839 | 0.8853 | 0.8846 |
| **Recall** | 0.8856 | 0.8837 | 0.8846 |
| **F1-Score** | 0.8847 | 0.8845 | 0.8846 |
| **Support** | 533 | 533 | 1,066 |

| | **Overall** |
|---|:---:|
| **Accuracy** | **0.8846 (88.5%)** |
| **Weighted F1** | **0.8846** |
| **Test Loss** | **0.5103** |

### Confusion Matrix

| | Predicted NEGATIVE | Predicted POSITIVE |
|---|:---:|:---:|
| **Actual NEGATIVE** | **472** (TN) | 61 (FP) |
| **Actual POSITIVE** | 62 (FN) | **471** (TP) |

- **True Positives:** 471 — correctly identified positive reviews
- **True Negatives:** 472 — correctly identified negative reviews
- **False Positives:** 61 — negative reviews misclassified as positive
- **False Negatives:** 62 — positive reviews misclassified as negative
- **Total misclassified:** 123 / 1,066 (11.5%)

---

## Error Analysis

### Error Patterns

| Error Type | Count | Avg Word Length |
|---|:---:|:---:|
| False Positives (neg→pos) | 61 | 20.5 words |
| False Negatives (pos→neg) | 62 | 22.8 words |
| Correct predictions | — | balanced |

The errors are nearly perfectly split between FP and FN, confirming the model has no class bias.

### Common Misclassification Patterns

1. **Irony / backhanded praise:** *"at its worst, the movie is pretty diverting; the pity is that it rarely achieves its best."* (POSITIVE labeled, predicted NEGATIVE) — The negative framing masks the positive intent
2. **Mixed sentiment with negative language:** *"the film feels uncomfortably real, its language and locations bearing the unmistakable stamp of authority."* (POSITIVE, predicted NEGATIVE) — "uncomfortably" triggers negative signal
3. **Understated or ambiguous reviews:** *"shiner can certainly go the distance, but isn't world championship material"* (POSITIVE, predicted NEGATIVE) — Subtle conditional praise
4. **Sarcastic inversions:** Reviews using negative vocabulary for ironic positive effect
5. **Short, cryptic reviews:** Minimal context for inference

---

## Results Analysis

### What 88.5% Accuracy Means

The model correctly classifies approximately **9 out of every 10** movie reviews — a **6.5 percentage point improvement** over the DistilBERT baseline (82%). On a balanced binary task, this represents a **38.5 pp improvement** over random chance (50%).

### Why RoBERTa Outperforms DistilBERT

| Factor | DistilBERT | RoBERTa |
|---|---|---|
| Parameters | 67M | 124.6M |
| Layers | 6 | 12 |
| Pre-training data | BookCorpus + Wikipedia | + CC-News, OpenWebText, Stories |
| Training samples used | 2,000 (23%) | **8,530 (100%)** |
| Test accuracy | 82.0% | **88.5%** |

The gains come from three sources: (1) RoBERTa's larger capacity and richer pre-training, (2) using the full training dataset, and (3) advanced optimization (warmup, early stopping, gradient clipping).

---

## Limitations & Bias

### Dataset Bias

- **Domain-specific:** Trained exclusively on Rotten Tomatoes — a particular style of English-language film criticism
- **English only:** No multilingual support
- **Temporal bias:** Reviews from a specific time period; may not capture evolving language
- **Binary oversimplification:** Neutral, mixed, or conditional sentiments forced into pos/neg

### Model Limitations

- **Max input length:** 128 tokens (~50-70 words). Longer reviews are truncated
- **No aspect-level analysis:** Single overall sentiment, not per-aspect (acting, plot, etc.)
- **No explanation:** Outputs label + confidence without reasoning
- **Domain transfer:** Performance degrades on non-movie-review text without adaptation

### Ethical Considerations

- **Not for high-stakes decisions** without human review
- **Potential for misuse:** Review manipulation, surveillance, opinion filtering
- **Representation gaps:** Training data may not equally represent all demographics/dialects
- **Feedback loops:** Automated sentiment filtering can suppress legitimate negative opinions

---

## Use Cases

### Recommended Applications

1. **Movie review classification** — Categorize user reviews as positive/negative
2. **Customer feedback triage** — Route feedback by sentiment polarity
3. **Content analysis** — Track sentiment trends in entertainment media
4. **Baseline model** — Strong starting point before investing in larger models
5. **Educational tool** — Demonstrate NLP fine-tuning and evaluation concepts

### Not Recommended For

- Medical, legal, or financial sentiment analysis
- Real-time social media monitoring (without domain adaptation)
- Multi-language or code-switched text
- Fine-grained sentiment (1-5 stars, emotion detection)

---

## Future Improvements

| Improvement | Expected Impact |
|---|---|
| **RoBERTa-large** (355M params) | +2-3% — more capacity for nuanced language |
| **Hyperparameter sweep** (lr, warmup, epochs) | +1-2% — systematic optimization |
| **Data augmentation** (back-translation, paraphrase) | +1-2% — more training diversity |
| **Increase max_length** (128→256) | +0.5-1% — capture full review context |
| **Multi-dataset training** (SST-2, IMDB, Amazon) | +2-4% — domain generalization |
| **Knowledge distillation** | Maintain accuracy with fewer params |
| **GPU + fp16 training** | 10-20× faster training, enabling larger sweeps |

---

## Framework Versions

| Component | Version |
|---|---|
| Transformers | 5.7.0 |
| PyTorch | 2.11.0 |
| Datasets | 4.8.5 |
| Tokenizers | 0.22.2 |
| Python | 3.12 |

---

## Citation

```bibtex
@article{liu2019roberta,
  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stollhiller, Veselin},
  journal={arXiv preprint arXiv:1907.11692},
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

## Links

- **Model:** [keerthi1515/roberta-sentiment-rotten-tomatoes](https://huggingface.co/keerthi1515/roberta-sentiment-rotten-tomatoes)
- **Base model:** [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base)
- **Dataset:** [cornell-movie-review-data/rotten_tomatoes](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes)
- **Baseline model:** [keerthi1515/distilbert-sentiment-rotten-tomatoes](https://huggingface.co/keerthi1515/distilbert-sentiment-rotten-tomatoes)
