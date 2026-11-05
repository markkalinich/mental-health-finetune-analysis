---
language: en
datasets:
  - imdb
library_name: transformers
tags:
  - sentiment-analysis
  - roberta
  - bilstm
  - attention
  - sarcasm
license: apache-2.0
pipeline_tag: text-classification
model_type: roberta
widget:
  - text: "This movie was a masterpiece!"
    example_title: Positive Example
  - text: "If I had a dollar for every cliché..."
    example_title: Sarcasm Example
---


# 🤖 Sentiment Classifier with Sarcasm Detection

This model combines `roberta-base` embeddings with a BiLSTM layer and attention mechanism to classify the **sentiment of movie reviews**, even when the language includes sarcasm, irony, or mixed emotional signals.

## 🧩 Architecture

- **Base Encoder:** RoBERTa (frozen)
- **Sequence Modeling:** Bidirectional LSTM (BiLSTM)
- **Attention Layer:** Learnable scalar attention weights
- **Classifier:** Fully connected + Softmax

This model takes the output of RoBERTa, processes it through a BiLSTM, applies attention to focus on important parts of the sentence, and classifies sentiment as **Positive (1)** or **Negative (0)**.

## 💡 Why this model?

Standard BERT-based sentiment classifiers often fail on subtle language such as:

- *"If I had a dollar for every cliché in this film, I’d be rich."* → sarcastic → **Negative**
- *"It’s fine. Just fine. Totally… fine."* → sarcastic tone → **Negative**
- *"The visuals were stunning, but the plot was as dead as a doorknob."* → contrast → **Negative**

This model aims to address that by combining contextual language modeling (RoBERTa) with sequence learning (BiLSTM) and attention-based interpretability.

## 📊 Training Details

- **Dataset:** IMDB (2-class, 25k reviews)
- **Training Subset:** 2,000 samples for prototype
- **Loss:** CrossEntropyLoss
- **Optimizer:** Adam
- **Epochs:** 3
- **Hardware:** Google Colab (T4 GPU)
- **Additional Inputs:** Custom sarcastic and ambiguous examples

## 🧪 Example Inputs

| Input | Prediction |
|-------|------------|
| "If I had a dollar for every cliché..." | 🔴 Negative |
| "It’s fine. Just fine. Totally fine."   | 🔴 Negative |
| "The acting was great, but the plot..." | 🔴 Negative |
| "Brilliant visuals and solid pacing."   | 🟢 Positive |

## 🚀 How to Use

```python
from transformers import RobertaTokenizer
from my_model import RobertaBiLSTMAttention  # the custom model
import torch

tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaBiLSTMAttention()
model.load_state_dict(torch.load("pytorch_model.bin"))
model.eval()

text = "It’s fine. Just fine. Totally… fine."
tokens = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)
logits = model(tokens["input_ids"], tokens["attention_mask"])
pred = torch.argmax(logits, dim=1).item()
print("Sentiment:", "Positive" if pred == 1 else "Negative")
