---
language:
- lus
tags:
- mizo
- sentiment-analysis
- text-classification
- bert
- hillbyte
- pytorch
pipeline_tag: text-classification
widget:
- text: "Aizawl khawpui ruahmanna thar hi a tha hle mai, kan lawm e!"
  example_title: "Positive Sentiment"
- text: "Hetiang thil duhawm lo leh tha lo lutuk hi kan duh lo tawp mai."
  example_title: "Negative Sentiment"
- text: "Vawiin hian Aizawl ah Chief Minister in thuchhuah a siam a ni."
  example_title: "Neutral / Factual"
license: apache-2.0
datasets:
- hillbyte/mizo-sentiment
- Blue7Bird/Mizo_sentiment_dataset
base_model: robzchhangte/MizBERT
metrics:
- accuracy
- f1
---

# Mizo Sentiment Classifier (`hillbyte/mizo-sentiment-mizbert`)

A state-of-the-art 3-class sentiment classifier for the **Mizo language (`lus` / Lushai)**, fine-tuned on the pretrained **[`robzchhangte/MizBERT`](https://huggingface.co/robzchhangte/MizBERT)** (12-layer, 768-dimension, 110M parameter BERT architecture).

---

## Model Details

- **Model Type**: BERT for Sequence Classification (`num_labels=3`)
- **Base Architecture**: `robzchhangte/MizBERT`
- **Supported Language**: Mizo (`lus`)
- **Classes**:
  - `0`: **Negative**
  - `1`: **Neutral**
  - `2`: **Positive**

---

## Evaluation Benchmarks

Evaluated on a stratified 15% hold-out test set (693 unseen samples) from combined Mizo sentiment datasets:

| Metric | Score |
| :--- | :--- |
| **Validation Accuracy** | **90.62%** |
| **Weighted F1-Score** | **0.9112** |
| **Macro F1-Score** | **0.8236** |

### Per-Class Performance Breakdown

| Class | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| **Negative** (`0`) | 93.4% | 90.7% | **0.920** |
| **Neutral** (`1`) | 51.4% | 73.5% | **0.605** |
| **Positive** (`2`) | 96.3% | 92.9% | **0.945** |

---

## Training Data & Methodology

The model was fine-tuned on **4,620 unified Mizo sentences** synthesized from two community datasets:
1. **[`hillbyte/mizo-sentiment`](https://huggingface.co/datasets/hillbyte/mizo-sentiment)** (1,220 sentences, 3-class)
2. **[`Blue7Bird/Mizo_sentiment_dataset`](https://huggingface.co/datasets/Blue7Bird/Mizo_sentiment_dataset)** (3,400 sentences, binary)

### Optimization Highlights
- **Stratified Split**: 85% Train (3,927 samples) / 15% Validation (693 samples).
- **Class-Weighted Loss**: Applied inverse-frequency loss weighting (`Negative: 0.83, Neutral: 4.71, Positive: 0.63`) to effectively capture minority `Neutral` sentiments.
- **Optimizer**: AdamW with learning rate $3 \times 10^{-5}$ and linear warmup.

---

## Quickstart & Usage

### 1. Using Hugging Face `pipeline`

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="hillbyte/mizo-sentiment-mizbert")

# Positive prediction
result = classifier("Aizawl khawpui ruahmanna thar hi a tha hle mai, kan lawm e!")
print(result)
# [{'label': 'Positive', 'score': 0.9916}]

# Negative prediction
result = classifier("Hetiang thil duhawm lo leh tha lo lutuk hi kan duh lo tawp mai.")
print(result)
# [{'label': 'Negative', 'score': 0.9938}]
```

### 2. Using PyTorch Directly

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "hillbyte/mizo-sentiment-mizbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Aizawl khawpui ruahmanna thar hi a tha hle mai, kan lawm e!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0]

id2label = model.config.id2label
predicted_id = torch.argmax(probs).item()

print(f"Sentiment: {id2label[predicted_id]} ({probs[predicted_id].item()*100:.2f}%)")
```

---

## Citation

If you use this model or the underlying datasets in your research or application, please cite the following publication:

```bibtex
@article{Lalrinmawii2025DetectingAC,
  title={Detecting Abusive Comments in Mizo: A Machine Learning Approach for a Low-Resource Language},
  author={R Lalrinmawii and Robert Lalramhluna and Gunavathi R.},
  journal={2025 IEEE International Conference on Advanced Visual and Signal-Based Systems (AVSS)},
  year={2025},
  pages={1-6},
  url={https://api.semanticscholar.org/CorpusID:281244917}
}
```
