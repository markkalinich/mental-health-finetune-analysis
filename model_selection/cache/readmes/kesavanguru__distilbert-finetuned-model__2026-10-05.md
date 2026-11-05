---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- text-classification
- emotion-detection
- nlp
- generated_from_trainer
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
model-index:
- name: distilbert-finetuned-model
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: dair-ai/emotion
      type: dair-ai/emotion
      config: split
      split: test
    metrics:
    - type: accuracy
      value: 0.9215
      name: Accuracy
    - type: f1
      value: 0.9213
      name: F1
---

# 🎭 Emotion Classifier (DistilBERT Fine-tuned)

This model is a fine-tuned version of **DistilBERT** (distilbert-base-uncased) trained to classify English text into six basic emotions. It was trained on the `dair-ai/emotion` dataset and achieved a high accuracy of **92.15%**.

## 📊 Model Performance
The model reaches state-of-the-art results for its size on the evaluation set:
- **Accuracy:** 92.15%
- **F1 Score:** 92.13%
- **Loss:** 0.2302

## 🏷️ Supported Labels
The model predicts the following 6 emotions:
1. **Sadness** (0)
2. **Joy** (1)
3. **Love** (2)
4. **Anger** (3)
5. **Fear** (4)
6. **Surprise** (5)

## 🚀 How to Use
You can use this model directly with the Hugging Face `pipeline`:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="kesavanguru/distilbert-finetuned-model")

text = "I am so proud of how this project turned out!"
result = classifier(text)
print(result)
# Output: [{'label': 'joy', 'score': 0.98}]
## 📚 Training Procedure

### Training Data
This model was trained on the **[dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion)** dataset, which contains English Twitter messages labeled with six basic emotions: sadness, joy, love, anger, fear, and surprise.

### Training Hyperparameters
The following settings were used to achieve the optimal balance between speed and accuracy:
- **Learning Rate:** 2e-05
- **Batch Size:** 64
- **Epochs:** 2
- **Weight Decay:** 0.01
- **Optimizer:** AdamW with linear learning rate scheduler

### Training Results
| Epoch | Training Loss | Validation Loss | Accuracy | F1 Score |
|:---:|:---:|:---:|:---:|:---:|
| 1 | No log | 0.3395 | 0.9025 | 0.9018 |
| 2 | 0.5629 | 0.2302 | **0.9215** | **0.9213** |

## 🛠️ Framework Versions
- **Transformers:** 4.57.3
- **Pytorch:** 2.9.0+cu126
- **Datasets:** 4.0.0
- **Tokenizers:** 0.22.2

## ⚖️ Limitations & Bias
Since this model was trained on Twitter data, it may be biased toward social media language styles. It might struggle with:
- Sarcasm or deeply nuanced irony.
- Highly formal or legal documents.
- Multi-emotion sentences (it will only predict the dominant one).

---
*Developed by Kesavan Guruprasath*