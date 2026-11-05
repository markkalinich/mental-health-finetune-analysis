---
license: apache-2.0
language:
- en
metrics:
- accuracy
base_model:
- HuggingFaceTB/SmolLM-360M
pipeline_tag: text-classification
library_name: transformers
tags:
- NLP
- sentiment-analysis
- tweet-classification
- product-reviews
- text-classification
- transformers
- huggingface
---

# 🤖 NegaBot: SmolLM 360M – Tweet Sentiment Classifier

<p align="center">
  <img width="512" src="https://github.com/user-attachments/assets/18669a85-e7fc-47f6-9183-e7ee33648930" alt="NegaBot Model Illustration">
</p>

**NegaBot** is a fine-tuned [SmolLM-360M](https://huggingface.co/HuggingFaceTB/SmolLM-360M) model that detects **negative product reviews** on the X platform (formerly Twitter). It is designed to help brands and analysts identify dissatisfaction or criticism in real-time.

---

### Training Code: 
- [NoteBook on GitHub](https://github.com/Jatin-Mehra119/NegaBot-Product-Criticism-Catcher/blob/main/SmolLM360M.ipynb)
- [SmolLM360M-V2.ipynb](https://github.com/Jatin-Mehra119/NegaBot-Product-Criticism-Catcher/blob/main/SmolLM360M-V2.ipynb) (V2 – Sarcasm-aware fine-tuning)


## 📊 Task

**Binary Sentiment Classification**:
- **Input**: A tweet about a product.
- **Output**: Label `1` (Negative) or `0` (Positive)

---

## 🧠 Model Details

- **Architecture**: Decoder-only Transformer (SmolLM 360M)
- **Base Model**: [HuggingFaceTB/SmolLM-360M](https://huggingface.co/HuggingFaceTB/SmolLM-360M)
- **Tokenizer**: AutoTokenizer (from base model)

---

## 🏋️ Training Details

- **Dataset**: Custom dataset of 7,920 tweets (from Kaggle)
  - Positive tweets: 5,894
  - Negative tweets: 2,026
- **Sequence Length**: 256
- **Batch Size**: 16
- **Epochs**: 3
- **Learning Rate**: 5e-5
- **Optimizer**: AdamW
- **Loss Function**: CrossEntropyLoss
- **Hardware**: Trained on **NVIDIA Tesla P100 GPU**
- **Training Time**: ~20 minutes

---

## 📈 Evaluation Results

| Dataset     | Accuracy | F1-score |
|-------------|----------|----------|
| Validation  | 0.90     | 0.89     |
| Test        | **0.91** | **0.91** |

- **Observation**: Removing text cleaning (keeping emojis and special characters) led to a significant boost in performance on noisy tweet data.

---

## 🆕 Updates

- 🔍 **Sarcasm Handling**:  
  - V1 struggled with sarcastic negative tweets being misclassified as positive  
  - V2 is fine-tuned using 1,000 sarcastic synthetic tweets + additional real-world raw samples

- 🧪 **Improved Generalization**:
  - Training on raw, uncleaned tweets improved performance on informal and emoji-heavy content

- 📦 **New Notebook**:  
  - `SmolLM360M-V2.ipynb` contains the additional training pipeline for sarcasm-aware performance

- ✅ **New Accuracy**:  
  - Final test accuracy improved to **0.94** on sarcasm-inclusive test set

---


## 🧪 How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("jatinmehra/NegaBot-Product-Criticism-Catcher")
tokenizer = AutoTokenizer.from_pretrained("jatinmehra/NegaBot-Product-Criticism-Catcher")

text = "This product is awful and broke within a week!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits, dim=1).item()

print("Negative" if predicted_class == 1 else "Positive")
```

### Labels
- `0` → **Positive** (The tweet expresses satisfaction or approval of the product)
- `1` → **Negative** (The tweet expresses dissatisfaction or criticism)

## Acknowledgements
-   Base Model: SmolLM-360M 
-   Dataset: Product sentiment tweets from Kaggle
-   Libraries: Hugging Face Transformers, Datasets, PyTorch, Pnadas

## Author
[Jatin Mehra](https://github.com/Jatin-Mehra119)
[LinkedIn Profile](https://www.linkedin.com/in/jatin-mehra119)