---
language:
  - en
library_name: transformers
pipeline_tag: text-classification
datasets:
  - stanfordnlp/imdb
base_model: bert-base-uncased
tags:
  - sentiment-analysis
  - text-classification
  - sentiment
  - bert
  - transformers
  - imdb
---

# 🤖 BERT IMDb Sentiment Classifier

A fine-tuned **BERT-base-uncased** model for binary sentiment classification on the **IMDb Movie Reviews dataset**.

The model classifies English movie reviews into two sentiment categories:

- **Negative (0)**
- **Positive (1)**

This project implements a complete end-to-end NLP workflow using **Hugging Face Transformers and Datasets**, covering dataset preparation, tokenization, BERT fine-tuning, validation, early stopping, evaluation, confusion matrix analysis, custom predictions, and deployment to the Hugging Face Hub.

---

## 🚀 Model Overview

| Property | Details |
|---|---|
| Base Model | `bert-base-uncased` |
| Task | Binary Sentiment Classification |
| Language | English |
| Dataset | `stanfordnlp/imdb` |
| Number of Classes | 2 |
| Negative Label | `0` |
| Positive Label | `1` |
| Maximum Sequence Length | 256 tokens |
| Learning Rate | `2e-5` |
| Batch Size | 8 |
| Maximum Epochs | 3 |
| Weight Decay | 0.01 |
| Random Seed | 42 |
| Early Stopping | Enabled |
| Best Model Loading | Enabled |
| Evaluation Metrics | Accuracy, Precision, Recall, F1 |

---

## 🎯 Project Objective

The objective of this project was to develop a transformer-based sentiment analysis model capable of classifying the sentiment of English movie reviews.

Instead of relying on manually engineered text features, the project uses **BERT**, a pretrained Transformer architecture capable of learning contextual relationships between words.

The complete workflow includes:

1. Dataset loading and inspection
2. Train/validation/test preparation
3. BERT tokenizer configuration
4. Text tokenization
5. Dynamic padding
6. Model fine-tuning
7. Validation during training
8. Early stopping
9. Test evaluation
10. Confusion matrix analysis
11. Custom sentiment prediction
12. Model serialization
13. Deployment to the Hugging Face Hub

---

## 📚 Dataset

The project uses the **IMDb Movie Reviews dataset**, available through the Hugging Face Hub:

**`stanfordnlp/imdb`**

The original dataset contains:

- **25,000 training reviews**
- **25,000 test reviews**
- Binary sentiment labels

The original training split was divided into:

- **22,500 training examples**
- **2,500 validation examples**
- **25,000 test examples**

The training/validation split was performed using **stratified sampling** to preserve the distribution of the two sentiment classes.

### Labels

| Label | Sentiment |
|---:|---|
| 0 | Negative |
| 1 | Positive |

---

## 🧠 Model Architecture

The model is based on **`bert-base-uncased`**.

BERT (Bidirectional Encoder Representations from Transformers) is a pretrained Transformer model designed to capture contextual relationships within natural language.

For this project, BERT was fine-tuned for binary sequence classification.

### Architecture

**Movie Review → BERT Tokenizer → Token IDs + Attention Mask → BERT-base-uncased → Classification Head → Negative / Positive**

---

## 🔧 Data Preprocessing

Reviews were tokenized using the tokenizer associated with `bert-base-uncased`.

### Tokenization Settings

| Setting | Value |
|---|---|
| Maximum sequence length | 256 tokens |
| Truncation | Enabled |
| Padding | Dynamic |

Sequences longer than 256 tokens were truncated.

Padding was handled dynamically using `DataCollatorWithPadding`, reducing unnecessary padding and improving training efficiency.

---

## 🏋️ Training Procedure

The model was fine-tuned using the Hugging Face `Trainer` API on a GPU-enabled **Google Colab** environment with an **NVIDIA T4 GPU**.

### Training Configuration

| Parameter | Value |
|---|---|
| Learning Rate | `2e-5` |
| Batch Size | `8` |
| Maximum Epochs | `3` |
| Weight Decay | `0.01` |
| Maximum Sequence Length | `256` |
| Random Seed | `42` |

The model was evaluated on the validation set during training.

The following metrics were monitored:

- Validation Loss
- Accuracy
- Precision
- Recall
- F1-score

---

## 🛑 Early Stopping

**Early stopping was enabled** to help reduce the risk of overfitting and avoid unnecessary training.

The training process monitored **validation loss** and was configured to retain the best-performing model checkpoint.

| Setting | Value |
|---|---|
| Early stopping patience | 2 epochs |
| Best model metric | Validation loss |
| Best model loading | Enabled |

The training history showed that training loss decreased consistently while validation loss increased during the main epoch-level evaluations.

This divergence is an indication of overfitting and demonstrates the importance of monitoring validation performance during Transformer fine-tuning.

---

# 📊 Training Results

## Training Loss

The training loss decreased consistently throughout the three epochs:

| Epoch | Training Loss |
|---:|---:|
| 1 | 0.320857 |
| 2 | 0.186183 |
| 3 | 0.092030 |

This indicates that the model progressively fitted the training data during fine-tuning.

---

## Validation Results

The main validation evaluations recorded during training were:

| Epoch | Validation Loss | Accuracy | F1 |
|---:|---:|---:|---:|
| 1 | 0.285316 | 90.76% | 90.51% |
| 2 | 0.343986 | 91.72% | 91.59% |
| 3 | 0.412600 | 91.68% | 91.67% |

An additional validation evaluation recorded after training was:

| Validation Loss | Accuracy | F1 |
|---:|---:|---:|
| 0.250515 | 91.70% | 91.54% |

### Interpretation

The training loss decreased from **0.320857 to 0.092030**, while the main epoch-level validation loss increased from **0.285316 to 0.412600**.

This divergence indicates that the model was fitting the training data increasingly well while validation loss was not improving consistently.

At the same time, validation accuracy and F1 remained around the **91–92% range**, showing that classification performance remained strong even as the loss curves diverged.

This highlights the importance of monitoring validation metrics rather than relying only on training loss.

---

# 🧪 Final Test Evaluation

The final model was evaluated on the **25,000-example test set**, which was kept separate from the training and validation data.

### Test Results

| Metric | Score |
|---|---:|
| **Accuracy** | **91.70%** |
| **Precision** | **93.31%** |
| **Recall** | **89.83%** |
| **F1-score** | **91.54%** |

### Interpretation

The model achieved **91.70% accuracy** on previously unseen IMDb reviews.

The **93.31% precision** indicates that the model's positive predictions were generally reliable.

The **89.83% recall** indicates that the model successfully identified most positive reviews, while some positive examples were classified as negative.

The resulting **91.54% F1-score** provides a balanced summary of precision and recall.

Overall, the results demonstrate that the fine-tuned BERT model performs effectively on the IMDb sentiment classification task.

---

# 🧩 Confusion Matrix

The final test confusion matrix contained:

| | Predicted Negative | Predicted Positive |
|---|---:|---:|
| **Actual Negative** | 11,730 | 770 |
| **Actual Positive** | 1,293 | 11,207 |

### Interpretation

- **11,730** negative reviews were correctly classified.
- **11,207** positive reviews were correctly classified.
- **770** negative reviews were incorrectly classified as positive.
- **1,293** positive reviews were incorrectly classified as negative.

The model correctly classified:

**22,937 out of 25,000 reviews.**

The confusion matrix therefore corresponds to approximately **91.75% accuracy** when calculated directly from its displayed counts.

The higher number of false negatives compared with false positives indicates that the model was more likely to classify a positive review as negative than the reverse.

> **Note:** The reported test accuracy from the evaluation output is **91.70%**. The displayed confusion matrix corresponds to approximately **91.75%** when calculated directly from its counts. This small difference may result from the specific evaluation output, rounding, or the exact prediction set used to generate the matrix.

---

# 📈 Key Findings

### 1. Strong test performance

The model achieved **91.70% accuracy** on 25,000 unseen IMDb test reviews.

### 2. High precision

The model achieved **93.31% precision**, indicating that its positive predictions were generally reliable.

### 3. Balanced overall performance

The **91.54% F1-score** demonstrates a strong balance between precision and recall.

### 4. Stable validation performance

Validation accuracy and F1 remained around the **91–92% range** throughout training.

### 5. Evidence of overfitting

Training loss decreased substantially while the main epoch-level validation loss increased.

This demonstrates why validation monitoring and early stopping are important when fine-tuning pretrained Transformer models.

---

# 💻 Usage

The model can be loaded directly from the Hugging Face Hub using the Transformers library.

### Installation

    pip install transformers torch

### Load the Model

    from transformers import pipeline

    classifier = pipeline(
        "sentiment-analysis",
        model="MedWassimAmira/bert-imdb-sentiment"
    )

### Make a Prediction

    text = "This movie was absolutely fantastic. The story was engaging and the acting was excellent."

    result = classifier(text)

    print(result)

Example output:

    [{'label': 'LABEL_1', 'score': 0.99}]

Where:

- `LABEL_0` → Negative
- `LABEL_1` → Positive

---

# 🔍 Manual Prediction

The model can also be loaded directly with `AutoTokenizer` and `AutoModelForSequenceClassification`.

    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    model_name = "MedWassimAmira/bert-imdb-sentiment"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    text = "The movie was entertaining and beautifully made."

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=-1)

    prediction = torch.argmax(probabilities, dim=-1).item()
    confidence = probabilities[0][prediction].item()

    label = "Positive" if prediction == 1 else "Negative"

    print(f"Sentiment: {label}")
    print(f"Confidence: {confidence:.4f}")

---

# ⚠️ Limitations

This model was fine-tuned specifically on **English IMDb movie reviews**.

Its performance may therefore differ when applied to other types of text, such as:

- Product reviews
- Social media posts
- News articles
- Customer feedback
- Informal conversations

Other limitations include:

- Sarcasm and irony can be difficult to classify.
- Reviews containing mixed opinions may be challenging.
- Very long inputs are truncated to 256 tokens.
- The model has not been specifically evaluated on domains outside IMDb.
- Predictions should be interpreted as model outputs rather than objective judgments of subjective opinions.

The dataset may also contain domain-specific linguistic patterns and biases. Additional evaluation is recommended before using the model in a different domain or application.

---

# 🛠️ Technologies

- **Python**
- **PyTorch**
- **Hugging Face Transformers**
- **Hugging Face Datasets**
- **scikit-learn**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Google Colab**
- **NVIDIA T4 GPU**

---

# 📂 Model Files

The Hugging Face repository contains the trained model and tokenizer required for inference.

Main files include:

- `config.json`
- `model.safetensors`
- `tokenizer.json`
- `tokenizer_config.json`
- `special_tokens_map.json`
- `vocab.txt`
- `training_args.bin`
- `README.md`

---

# 🔬 Reproducibility

A random seed of **42** was used to improve reproducibility.

The dataset was split into training and validation sets using stratified sampling based on the sentiment label.

The model was fine-tuned using an NVIDIA T4 GPU in Google Colab.

---

# 📌 End-to-End Workflow

**IMDb Dataset → Dataset Inspection → Train/Validation/Test Split → BERT Tokenization → Dynamic Padding → BERT Fine-Tuning → Validation + Early Stopping → Final Test Evaluation → Confusion Matrix Analysis → Custom Predictions → Model Saving → Hugging Face Hub**

---

# 📚 References

- Devlin, J. et al. (2018). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.*
- Hugging Face Transformers Documentation
- Hugging Face Datasets Documentation
- IMDb Movie Reviews Dataset

---

# 👤 Author

**Mohamed Wassim Amira**

Business Intelligence Student  
**IHEC Carthage — Tunisia**

### Areas of Interest

- Data Science
- Machine Learning
- Natural Language Processing
- Business Intelligence
- Data Visualization

---

# ⭐ Project Summary

This project demonstrates an end-to-end NLP workflow using a pretrained BERT model, from dataset preparation and tokenization to fine-tuning, validation, early stopping, evaluation, error analysis, and deployment to the Hugging Face Hub.

### Final Test Performance

**91.70% Accuracy · 93.31% Precision · 89.83% Recall · 91.54% F1-score**