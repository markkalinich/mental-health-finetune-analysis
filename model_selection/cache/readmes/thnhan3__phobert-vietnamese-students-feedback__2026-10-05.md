---
license: mit
language:
- vi
tags:
- sentiment-analysis
- vietnamese
- phobert
- text-classification
- educational-feedback
- roberta
datasets:
- uitnlp/vietnamese_students_feedback
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: phobert-vsfb-baseline
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      name: Vietnamese Students Feedback
      type: uitnlp/vietnamese_students_feedback
      split: test
    metrics:
    - type: accuracy
      value: 0.9311
    - type: f1
      value: 0.928
      name: F1 Weighted
    - type: f1
      value: 0.8179
      name: F1 Macro
- name: phobert-vsfb-augmented
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      name: Vietnamese Students Feedback
      type: uitnlp/vietnamese_students_feedback
      split: test
    metrics:
    - type: accuracy
      value: 0.9343
    - type: f1
      value: 0.9317
      name: F1 Weighted
    - type: f1
      value: 0.8333
      name: F1 Macro
base_model:
- vinai/phobert-base
library_name: transformers
---

# PhoBERT Vietnamese Students Feedback Sentiment Classification

## Model Description

This repository contains fine-tuned PhoBERT models for Vietnamese students feedback sentiment classification. The models classify student feedback into three sentiment categories: **negative** (0), **neutral** (1), and **positive** (2).

Two model variants are provided:
- **phobert-vsfb-baseline**: Trained on the original Vietnamese Students Feedback dataset
- **phobert-vsfb-augmented**: Trained on the original dataset augmented with synthetic data

Both models are based on [PhoBERT-base](https://huggingface.co/vinai/phobert-base), a pre-trained Vietnamese language model developed by VinAI Research.

## Model Details

### Model Type
- **Architecture**: RoBERTa-based transformer with sequence classification head
- **Base Model**: `vinai/phobert-base`
- **Task**: Multi-class text classification (3 classes)
- **Language**: Vietnamese

### Model Variants

#### Baseline Model
- **Training Data**: Original Vietnamese Students Feedback dataset (11,426 training samples)
- **Training Epochs**: 5
- **Learning Rate**: 2e-5
- **Batch Size**: 16

#### Augmented Model
- **Training Data**: Original dataset + synthetic data (14,600 total training samples)
- **Augmentation**: 3,174 synthetic samples generated using LLM
- **Training Epochs**: 5
- **Learning Rate**: 2e-5
- **Batch Size**: 16
#### Comparison


![image](https://cdn-uploads.huggingface.co/production/uploads/672aea06dba831894fd56e44/VGejeEHzp6WkXhLmChFzB.png)

## Intended Use

### Primary Use Cases
- **Educational Institutions**: Analyze student feedback to understand satisfaction levels and improve teaching quality
- **Sentiment Analysis**: Classify Vietnamese text feedback into positive, neutral, or negative sentiments
- **Research**: Benchmark and compare sentiment classification approaches for Vietnamese educational text

### Out-of-Scope Use Cases
- General-purpose sentiment analysis (model is specifically trained on educational feedback)
- Non-Vietnamese text classification
- Real-time production systems without proper evaluation and monitoring

## Training Data

### Dataset
- **Name**: Vietnamese Students Feedback
- **Source**: UIT-NLP (Hugging Face: `uitnlp/vietnamese_students_feedback`)
- **Language**: Vietnamese
- **Splits**:
  - Train: 11,426 samples
  - Validation: 1,583 samples
  - Test: 3,166 samples

### Class Distribution
The dataset exhibits class imbalance:
- **Negative**: ~45% of samples
- **Neutral**: ~5% of samples (minority class)
- **Positive**: ~50% of samples

### Data Augmentation
The augmented model uses synthetic data generated via LLM to address class imbalance, particularly for the neutral class. The synthetic dataset contains 3,174 additional samples, primarily focusing on the minority neutral class.

## Training Procedure

### Preprocessing
- **Tokenization**: PhoBERT tokenizer with max length of 256 tokens
- **Padding**: Max length padding
- **Truncation**: Enabled for sequences exceeding max length

### Training Hyperparameters
- **Optimizer**: AdamW
- **Learning Rate**: 2e-5
- **Weight Decay**: 0.01
- **Warmup Ratio**: 0.1
- **Batch Size**: 16 (per device)
- **Epochs**: 5
- **FP16**: Enabled (if CUDA available)
- **Seed**: 42 (for reproducibility)

### Training Configuration
- **Evaluation Strategy**: End of epoch
- **Save Strategy**: End of epoch
- **Best Model Selection**: Based on F1-macro score
- **Early Stopping**: Enabled (load best model at end)

## Evaluation

### Evaluation Metrics
The models are evaluated using multiple metrics to account for class imbalance:
- **Accuracy**: Overall classification accuracy
- **F1 Weighted**: F1 score weighted by class frequency
- **F1 Macro**: Macro-averaged F1 score (equal weight to all classes)
- **Per-Class Metrics**: Precision, Recall, and F1 for each class

### Baseline Model Performance (Test Set)

| Metric | Value |
|--------------------|--------|
| Accuracy | 0.9330 |
| F1 Weighted | 0.9318 |
| F1 Macro | 0.8285 |
| Precision Weighted | 0.9308 |
| Recall Weighted | 0.9330 |
| Precision Macro | 0.8409 |
| Recall Macro | 0.8180 |

### Augmented Model Performance (Test Set)

| Metric | Value | Improvement (Absolute) | Improvement (%) |
|--------------------|--------|------------------------|-----------------|
| Accuracy | 0.9390 | +0.0060 | +0.64% |
| F1 Weighted | 0.9375 | +0.0057 | +0.61% |
| **F1 Macro** | **0.8500** | **+0.0215** | **+2.60%** ⭐ |
| Precision Weighted | 0.9367 | +0.0059 | +0.64% |
| Recall Weighted | 0.9390 | +0.0060 | +0.64% |
| Precision Macro | 0.8719 | +0.0310 | +3.69% |
| Recall Macro | 0.8330 | +0.0150 | +1.83% |


### Per-Class Performance Comparison

| Class | Base F1 | Aug F1 | F1 Improvement (Δ) | Base Recall | Aug Recall | Recall Improvement (Δ) |
|---------------|---------|--------|--------------------|-------------|------------|------------------------|
| **Negative (0)** | 0.9495 | 0.9525 | +0.0030 | 0.9539 | 0.9617 | +0.0078 |
| **Neutral (1)** | **0.5833** | **0.6424** | **+0.0591 (10.12%)** ⭐ | 0.5449 | 0.5808 | +0.0359 (6.59%) |
| **Positive (2)** | 0.9527 | 0.9551 | +0.0024 | 0.9553 | 0.9566 | +0.0013 |

### Key Findings

- Data Augmentation Impact: The addition of 3,174 synthetic samples (27.8% dataset
 size increase) successfully improved the model’s performance across most metrics, with a
 notable impact on the minority class.
- Significant Macro Improvement: The most significant gain was observed in the F1
Macro score, which improved from 0.8285 to 0.8500—a substantial relative improvement of
 2.60%. This indicates a much better and more balanced performance across all sentiment
 classes.
- Minority Class Performance (Neutral): The neutral class (Support = 167) showed
 marked improvements:
 29
– F1 Score increased from 0.5833 to 0.6424 (+10.12% relative improvement).– Precision increased from 0.6276 to 0.7185 (+14.49% relative improvement).– Recall increased from 0.5449 to 0.5808 (+6.59% relative improvement).
- Overall Performance: Core metrics such as Accuracy (up 0.64% to 0.9390) and F1
 Weighted (up 0.61% to 0.9375) also improved, confirming that augmentation benefits the
 overall classification task without negatively impacting the majority classes.

## Limitations and Bias

### Known Limitations
1. **Class Imbalance**: Despite improvements, the neutral class still shows lower performance compared to other classes (F1: 0.5993 vs. ~0.95 for other classes)
2. **Domain Specificity**: Model is trained specifically on educational feedback and may not generalize well to other domains
3. **Synthetic Data Quality**: Augmented model relies on LLM-generated synthetic data, which may introduce biases or artifacts
4. **Language**: Model only supports Vietnamese text
5. **Evaluation**: Results are based on a single test set; cross-validation would provide more robust estimates

### Potential Biases
- **Educational Context Bias**: Model may be biased towards educational terminology and contexts
- **Formal Language Bias**: Training data consists of formal student feedback, may not perform well on informal or colloquial Vietnamese
- **Class Bias**: Model may still favor majority classes (negative and positive) over neutral

## Ethical Considerations

### Use Case Considerations
- **Privacy**: Student feedback may contain sensitive information; ensure proper data handling and privacy protection
- **Fairness**: Model performance varies across classes; consider class-specific thresholds for critical applications
- **Transparency**: Users should be aware of model limitations, especially regarding minority class performance

### Recommendations
- Use augmented model for better balanced performance across all classes
- Monitor model performance, especially for neutral class predictions
- Consider domain adaptation for different educational contexts
- Implement human review for critical decisions based on model predictions

## How to Use

### Installation
```bash
pip install transformers torch
```

### Basic Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "thnhan3/phobert-vietnamese-students-feedback"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "Giáo viên rất nhiệt tình và thân thiện."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256)

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1).item()

# Map to label
id2label = {0: "negative", 1: "neutral", 2: "positive"}
predicted_label = id2label[predicted_class]
print(f"Predicted: {predicted_label}")
```

### Inference Function
```python
def predict_sentiment(text, model_path="thnhan3/phobert-vietnamese-students-feedback"):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        conf, pred_id = torch.max(probs, dim=-1)
    
    id2label = {0: "negative", 1: "neutral", 2: "positive"}
    return id2label[predicted_id.item()], conf.item()
```

## Training Details

### Training Infrastructure
- **Framework**: PyTorch with Hugging Face Transformers
- **Hardware**: CUDA-enabled GPU (recommended)
- **Training Time**: ~30-60 minutes per model (depending on hardware)

### Reproducibility
- **Random Seed**: 42
- **Training Script**: Available in the associated notebook
- **Dataset Version**: `refs/convert/parquet` revision

## Citation

### Model
```bibtex
@misc{phobert-vsfb,
  title={PhoBERT Vietnamese Students Feedback Sentiment Classification},
  author={Tran Huu Nhan},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/thnhan3/phobert-vietnamese-students-feedback}}
}
```

### Base Model
```bibtex
@inproceedings{phobert,
  title={{PhoBERT: Pre-trained language models for Vietnamese}},
  author={Nguyen, Dat Quoc and Nguyen, Anh Tuan},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
  pages={1037--1042},
  year={2020}
}
```

### Dataset
```bibtex
@misc{vietnamese_students_feedback,
  title={Vietnamese Students Feedback Dataset},
  author={UIT-NLP},
  year={2020},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/uitnlp/vietnamese_students_feedback}}
}
```

## Contact

For questions, issues, or contributions, please open an issue on the Hugging Face model repository.

## License

This model is released under the MIT License. See LICENSE file for details.

## Acknowledgments

- VinAI Research for developing PhoBERT
- UIT-NLP for providing the Vietnamese Students Feedback dataset
- Hugging Face for the Transformers library and platform