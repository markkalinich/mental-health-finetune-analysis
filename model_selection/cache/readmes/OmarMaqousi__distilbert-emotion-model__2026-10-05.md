---
license: apache-2.0
language:
- en
library_name: transformers
tags:
- text-classification
- emotion
- distilbert
- nlp
- sentiment-analysis
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
pipeline_tag: text-classification
model-index:
- name: distilbert-emotion-model
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: dair-ai/emotion
      type: dair-ai/emotion
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.927
---

# DistilBERT Emotion Classification Model

## Model Details

### Model Description

A fine-tuned DistilBERT model for **emotion classification** of English text. The model classifies text into **6 emotion categories**: sadness, joy, love, anger, fear, and surprise. It was fine-tuned on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset with random oversampling to handle class imbalance.

- **Developed by:** Omar Emran Taha Al Maqousi
- **Model type:** Transformer (DistilBERT) — Sequence Classification
- **Language(s):** English
- **License:** Apache 2.0
- **Fine-tuned from:** [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)

### Model Sources

- **Repository:** [OmarMaqousi/distilbert-emotion-model](https://huggingface.co/OmarMaqousi/distilbert-emotion-model)

## Uses

### Direct Use

This model can be used directly for classifying the emotion expressed in a piece of English text. Suitable use cases include:

- Analyzing customer feedback or reviews
- Social media sentiment/emotion monitoring
- Chatbot emotion detection
- Mental health text screening (with caution)

### Out-of-Scope Use

- **Non-English text:** The model was trained only on English data.
- **Long documents:** DistilBERT has a 512-token limit; longer texts will be truncated.
- **Clinical diagnosis:** This model should NOT be used as a substitute for professional mental health assessment.
- **Detecting sarcasm or nuanced emotions:** The model may not reliably detect sarcasm, irony, or complex mixed emotions.

## Bias, Risks, and Limitations

- The training data consists of English Twitter-like text, so the model may perform poorly on formal or domain-specific text.
- Class distribution in the original dataset is imbalanced (e.g., `surprise` is underrepresented). Random oversampling was applied to mitigate this, but some bias may remain.
- The model may reflect biases present in the training data.

### Recommendations

Users should be aware that the model's predictions are probabilistic and may not always be accurate, especially on edge cases or ambiguous text. Always validate model outputs before using them in production or sensitive contexts.

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="OmarMaqousi/distilbert-emotion-model")

result = classifier("I am so happy today!")
print(result)
# [{'label': 'joy', 'score': 0.98}]
```

Or load the model and tokenizer manually:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model = AutoModelForSequenceClassification.from_pretrained("OmarMaqousi/distilbert-emotion-model")
tokenizer = AutoTokenizer.from_pretrained("OmarMaqousi/distilbert-emotion-model")

text = "I feel really scared about the exam"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=-1).item()

labels = ["sadness", "joy", "love", "anger", "fear", "surprise"]
print(f"Predicted emotion: {labels[predicted_class]}")
```

## Training Details

### Training Data

The model was fine-tuned on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset, which contains ~20,000 English text samples labeled with 6 emotions:

| Label | Emotion  |
|-------|----------|
| 0     | sadness  |
| 1     | joy      |
| 2     | love     |
| 3     | anger    |
| 4     | fear     |
| 5     | surprise |

**Data balancing:** Random oversampling was applied to the training set to address class imbalance, ensuring the model sees a balanced distribution of all emotion classes during training.

### Training Procedure

#### Preprocessing

- Tokenization using `distilbert-base-uncased` tokenizer
- Max sequence length: 512 tokens
- Truncation and padding applied

#### Training Hyperparameters

| Hyperparameter             | Value                                  |
|----------------------------|----------------------------------------|
| Learning rate              | 5e-5                                   |
| Batch size (train)         | 64                                     |
| Batch size (eval)          | 64                                     |
| Max epochs                 | 50                                     |
| Actual epochs (early stop) | 9                                      |
| Weight decay               | 0.02                                   |
| Optimizer                  | AdamW                                  |
| LR Scheduler               | Cosine                                 |
| Warmup ratio               | 0.1                                    |
| Early stopping patience    | 10 (based on F1)                       |
| Best model selection       | Best weighted F1 on validation         |
| Training regime            | fp32                                   |

#### Training & Validation Results

| Epoch | Training Loss | Validation Loss | Accuracy | F1       |
|-------|---------------|-----------------|----------|----------|
| 1     | 0.936842      | 0.226138        | 0.9210   | 0.921069 |
| 2     | 0.189488      | 0.176853        | 0.9345   | 0.933206 |
| 3     | 0.124524      | 0.138500        | 0.9360   | 0.936486 |
| 4     | 0.088845      | 0.144183        | 0.9395   | 0.939676 |
| 5     | 0.066814      | 0.153446        | 0.9390   | 0.938947 |
| 6     | 0.049265      | 0.192850        | 0.9410   | 0.940797 |
| 7     | 0.029422      | 0.208450        | 0.9485   | 0.948557 |
| 8     | 0.015454      | 0.225589        | 0.9450   | 0.945127 |
| 9     | 0.010990      | 0.227848        | 0.9460   | 0.946137 |

## Evaluation

### Testing Data

The evaluation was performed on the test split of the `dair-ai/emotion` dataset (2,000 samples).

### Metrics

| Metric              | Validation (Best) | Test   |
|---------------------|-------------------|--------|
| Accuracy            | 0.9485            | 0.9270 |
| F1 Score            | 0.9486            | 0.9274 |

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** DistilBERT (6 layers, 768 hidden size, 12 attention heads, 66M parameters)
- **Objective:** Multi-class classification (6 emotion categories) with cross-entropy loss

### Compute Infrastructure

- **Hardware:** Google Colab (GPU — T4 or similar)
- **Software:** Hugging Face Transformers, PyTorch, Datasets

## Citation

If you use this model, please cite:

```bibtex
@misc{maqousi2026distilbert-emotion,
  author = {Omar Al Maqousi},
  title = {DistilBERT Emotion Classification Model},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OmarMaqousi/distilbert-emotion-model}
}
```

## Model Card Authors

- Omar Emran Taha Al Maqousi

## Model Card Contact

- Hugging Face: [@OmarMaqousi](https://huggingface.co/OmarMaqousi)
