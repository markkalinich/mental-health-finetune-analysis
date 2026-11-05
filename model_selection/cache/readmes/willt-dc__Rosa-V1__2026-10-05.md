---
language: en
license: creativeml-openrail-m
quantized_by: Willinton Triana Cardona
quantized_models:
  - name: Rosa-V1-fp16
    path: quantized/Rosa-V1-fp16.gguf
    format: GGUF
    description: Full-precision baseline
  - name: Rosa-V1-q8_0
    path: quantized/Rosa-V1-q8_0.gguf
    format: GGUF
    description: Near-lossless 8-bit quantization
  - name: Rosa-V1-q6_k
    path: quantized/Rosa-V1-q6_k.gguf
    format: GGUF
    description: Balanced 6-bit quantization for portability
tags:
  - emotion-classification
  - multilabel
  - bert
  - goemotions
  - affective-computing
  - psychology
  - NLP
  - embeddings
  - symbolic-ai
  - poetic-ai
  - quantized
  - gguf
library_name: transformers
datasets:
  - go_emotions
model_name: Rosa-V1
model_type: bert
pipeline_tag: text-classification
base_model: bert-base-uncased
widget:
  - text: "My heart is filled with longing and beauty."
  - text: "I'm excited but nervous about what's coming next."
metrics:
  - name: eval_loss
    type: loss
    value: 0.0845
  - name: eval_f1
    type: f1
    value: 0.5793
  - name: parameters
    type: count
    value: 110000000
  - name: epochs
    type: count
    value: 3
model_creator: Willinton Triana Cardona
model_description: >
  ROSA is a fine-tuned BERT model trained on the GoEmotions dataset for multilabel emotion classification. 
  It identifies 28 nuanced human emotions plus a neutral class, supports soft probability outputs, 
  and provides latent emotion embeddings for affective computing applications. 
  ROSA is both technically sound and symbolically aligned to poetic human understanding.
---



# ROSA :: Emotional Sensitivity

“To feel is to know; to know is to bloom.”
·Willinton 

ROSA is a fine-tuned Transformer model based on `bert-base-uncased`, trained on the [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset to classify 28 nuanced human emotions (plus neutral).  
More than a model, **ROSA** is a prototype of emotion embeddings in affective computing.

---

 🧠 Model Summary

| Metric      | Value      |
|-------------|------------|
| Eval Loss   | 0.0845     |
| Eval F1     | 0.5793     |
| Epochs      | 3          |
| Dataset     | GoEmotions |
| Model Base  | BERT       |
| Parameters  | ~110M      |

---

## ✨ Highlights

- Supports **multilabel emotion classification**
- Returns soft probability scores for each of the 29 emotions
- Includes optional **latent vector embedding** for downstream affect modeling
- Trained with HuggingFace `Trainer` + early evaluation
- Symbolically aligned to human-centered semantics and poetic logic

---

## 🌸 Emotion Set

```
["admiration", "amusement", "anger", "annoyance", "approval", "caring",
 "confusion", "curiosity", "desire", "disappointment", "disapproval",
 "disgust", "embarrassment", "excitement", "fear", "gratitude", "grief",
 "joy", "love", "nervousness", "optimism", "pride", "realization", "relief",
 "remorse", "sadness", "surprise", "neutral"]
```

---

## 🔮 Usage

```python
from transformers import BertTokenizer
from model.emotion_model import Rosa
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = Rosa(num_emotions=29)
model.load_state_dict(torch.load("rosa.pt"))
model.eval()

text = "My heart is filled with longing and beauty."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.sigmoid(outputs["logits"]).squeeze()

# Result: list of probabilities for each emotion
```

---

## 🧭 Confusion Matrix

Included in the `assets/` directory as `confusion_matrix.png` to show classification precision across emotions.

---

## 🧩 Architecture

```
          ┌──────────────┐
          │ BERT Encoder │
          └──────┬───────┘
                 ↓
        ┌─────────────────┐
        │ Dropout (Grace) │
        └─────────────────┘
                 ↓
     ┌────────────────────────┐
     │ Dense Output (Bloom)   │ → logits over 29 emotions
     └────────────────────────┘
```

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

Includes:
- `transformers`
- `torch`
- `datasets`
- `scikit-learn`

---

## 🖋️ License

CreativeML Open RAIL-M License  
Please use this model ethically and with reverence for emotional contexts.

---

## 🌹 Creator

**Willinton Triana Cardona**  
Philosopher · AI Engineer · Architect of Poetic Systems

ROSA is the Rosa of Barcelona, my first blossom of affective computing, semantic elegance, and sacred recursion.

---

## 🤝 Contributing

Pull requests, poetic expansions, multilingual emotion embeddings, and related metaphoric augmentations are welcome.
I promise the next iteration (v2 with F1 improved) soon

---

## 📍Hugging Face Hub

→ https://huggingface.co/willt-dc/Rosa-V1
