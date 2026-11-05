---
license: apache-2.0
language:
  - ar
library_name: transformers
pipeline_tag: text-classification
tags:
  - arabic
  - sentiment-analysis
  - arabic-nlp
  - arabert
  - twitter
  - social-media
  - text-classification
base_model:
  - aubmindlab/bert-base-arabertv02-twitter
---

# 🧭 Arabic Sentiment Compass — AraBERT

A fine-tuned Twitter-adapted AraBERT model for **three-class Arabic sentiment classification**.

The model classifies Arabic social-media text into:

- 🔴 Negative
- ⚪ Neutral
- 🟢 Positive

This model is the main NLP model used by the **Arabic Sentiment Compass** graduation-project application.

---

## 🎯 Model Overview

Arabic social-media text presents several challenges, including:

- Dialectal vocabulary
- Spelling variation
- Character elongation
- Informal writing
- Emojis
- Mentions
- URLs
- Orthographic variation

This model was fine-tuned from:

```text
aubmindlab/bert-base-arabertv02-twitter
```

for three-class Arabic sentiment classification.

---

## 🧠 Model Architecture

| Property | Value |
|---|---|
| Base model | `aubmindlab/bert-base-arabertv02-twitter` |
| Architecture | BERT / Sequence Classification |
| Task | Arabic Sentiment Classification |
| Number of classes | 3 |
| Maximum sequence length | 128 |
| Primary metric | Macro F1 |
| Framework | PyTorch + Transformers |
| Model format | Safetensors |

### Label Mapping

| ID | Label | Arabic |
|---:|---|---|
| 0 | Negative | سلبي |
| 1 | Neutral | محايد |
| 2 | Positive | إيجابي |

---

# 📊 Evaluation Results

The final model was evaluated on a fixed combined Stage II test split created from ASTD and filtered ArSAS data.

### Stage II Dataset

```text
13,915 unique examples
```

Class distribution:

```text
Negative: 5,880
Neutral:  5,062
Positive: 2,973
```

Split:

```text
Train:       11,132
Validation:   1,391
Test:         1,392
```

ArSAS examples were retained for the three target sentiment classes using a sentiment-confidence threshold of `0.75`.

---

## 🏆 Main Results

| System | Accuracy | Macro F1 |
|---|---:|---:|
| Character TF-IDF + Logistic Regression | 81.47% | 80.42% |
| Standard AraBERT | 87.36 ± 0.45% | 86.83 ± 0.52% |
| **Proposed Twitter-adapted AraBERT** | **88.22 ± 0.19%** | **87.73 ± 0.17%** |
| Baseline + Proposed raw-logit ensemble | 88.36 ± 0.26% | 87.89 ± 0.30% |

The **proposed Twitter-adapted AraBERT** is the primary single-model system used by the practical application.

The ensemble result is considered an optional research extension rather than the main deployed model.

---

# 🔄 Preprocessing

The application uses a preprocessing function named:

```text
preprocess_arabic_tweet
```

The preprocessing pipeline:

1. Replaces URLs with a dedicated token.
2. Replaces user mentions with a dedicated token.
3. Removes Arabic diacritics.
4. Removes Tatweel.
5. Normalizes Alef variants.
6. Normalizes `ى`.
7. Reduces excessive character repetition.
8. Normalizes whitespace.

The same preprocessing logic is maintained between the experimental pipeline and the application inference pipeline.

---

# 🚀 Usage

Install the required libraries:

```bash
pip install torch transformers sentencepiece safetensors
```

Then load the model:

```python
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)
import torch

model_id = "randsalem/arabic-sentiment-compass-arabert"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

model.eval()
```

### Example

```python
text = "الخدمة ممتازة والتجربة كانت رائعة جداً"

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=128
)

with torch.inference_mode():
    outputs = model(**inputs)

probabilities = torch.softmax(outputs.logits, dim=-1)
prediction = torch.argmax(probabilities, dim=-1).item()

labels = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

print(labels[prediction])
print(float(probabilities[0, prediction]))
```

---

# 📈 Confidence

The application reports the maximum Softmax score:

```text
confidence = max(softmax(logits))
```

This score represents the model's output confidence for the predicted class.

**Important:** this is a raw Softmax score and has not been calibrated as a statistical probability.

---

# 🇪🇬 Egyptian-Focused Diagnostic

The project also includes an Egyptian-focused diagnostic evaluation.

On the 322 ASTD examples contained within the unseen Stage II test split:

```text
Accuracy: 70.39 ± 1.00%
Macro F1: 67.19 ± 0.48%
```

Therefore, the main Stage II performance should **not** be interpreted as an exclusively Egyptian-Arabic result.

---

# 🖥️ Application

The model powers the:

## Arabic Sentiment Compass

A Streamlit application supporting:

- Arabic RTL interface
- Single-text sentiment analysis
- Real-time model inference
- Confidence scores
- Three-class probability visualization
- Arabic and English sentiment labels
- CSV batch analysis
- Downloadable prediction results

GitHub repository:

https://github.com/Randsalem19/arabic-sentiment-compass

---

# ⚠️ Limitations

This model has several limitations:

1. The main Stage II evaluation corpus is multi-source and is not exclusively Egyptian.
2. Arabic dialect coverage varies across the underlying datasets.
3. Dataset differences in topics, annotation procedures, and linguistic styles cannot be completely eliminated.
4. Confidence values are raw Softmax scores and are not calibrated probabilities.
5. Sarcasm, irony, implicit sentiment, and highly contextual expressions may remain challenging.
6. Performance may vary on domains that differ substantially from Arabic social-media text.
7. The model should not be treated as a perfect semantic understanding system.

---

# 🔬 Training Configuration

The final experimental configuration included:

```text
Learning rate: 3e-5
Weight decay: 0.01
Maximum epochs: 5
Early stopping patience: 2

Per-device batch size: 16
Gradient accumulation: 2
Effective batch size: 32

Maximum sequence length: 128
Gradient clipping: 1.0

Data split seed: 42
Training seeds: 21, 42, 77

Primary metric: Macro F1

Loss:
Class-weighted focal loss
Gamma = 2
```

---

# 📚 Research Resources

The complete experimental pipeline is available in the GitHub repository.

The repository contains the Stage II notebook:

```text
Stage_II_Combined_ASTD_ArSAS_AraBERT_SentimentCompass_ipynb.ipynb
```

The notebook documents:

- Dataset preparation
- Preprocessing
- Model comparison
- Training
- Multi-seed experiments
- Evaluation
- Statistical analysis
- Predictions
- Figures

---

# 🔗 Project Links

### GitHub

https://github.com/Randsalem19/arabic-sentiment-compass

### Hugging Face Model

https://huggingface.co/randsalem/arabic-sentiment-compass-arabert

---

# 🎓 Project Context

**Arabic Sentiment Compass** is developed as a graduation-project / academic NLP system focused on practical Arabic sentiment analysis.

The project combines:

```text
Arabic NLP
      ↓
Twitter-adapted AraBERT
      ↓
Supervised Fine-tuning
      ↓
Multi-source Arabic Sentiment Evaluation
      ↓
Real-time Inference
      ↓
Streamlit Application
```

---

# 📄 License

The model is distributed under the Apache-2.0 license as configured in this repository.

The underlying pretrained model, datasets, and other external resources remain subject to their respective licenses and terms of use.

---

## 🧭 Arabic Sentiment Compass

**Arabic Sentiment Analysis powered by a Twitter-adapted AraBERT model.**
