---
license: mit
datasets:
- sai1908/Mental_Health_Condition_Classification
language:
- en
base_model:
- microsoft/deberta-v3-base
pipeline_tag: text-classification
tags:
- mental_health
- chatbot
- classification
---
# Sage DeBERTa v1

A transformer-based mental health text classification model fine-tuned on **DeBERTa-v3-base** for the KIIT Sage AI Mental Wellness Assistant.

> ⚠️ **Disclaimer:** This model is **not** intended for medical diagnosis. It is designed to provide emotional context for conversational AI systems and should not replace professional mental health assessment.

---

# Overview

Sage DeBERTa v1 classifies English text into one of five emotional categories:

- Anxiety
- Normal
- Depression
- Suicidal
- Stress

The model serves as the emotion classification component of the **KIIT Sage** chatbot, enabling more empathetic and context-aware conversations.

---

# Model Details

| Property | Value |
|----------|-------|
| Base Model | `microsoft/deberta-v3-base` |
| Task | Text Classification |
| Language | English |
| Framework | Hugging Face Transformers |
| Max Sequence Length | 256 |
| Labels | 5 |
| Developer | Omm Tripathi |

---

# Labels

| ID | Label |
|----|-------|
| 0 | Anxiety |
| 1 | Normal |
| 2 | Depression |
| 3 | Suicidal |
| 4 | Stress |

---

# Dataset

The model was fine-tuned on the **Mental Health Condition Classification** dataset.

To make the model suitable for conversational mental health support, the following diagnostic categories were removed:

- Bipolar
- Personality Disorder

After filtering, the model was trained on the following five categories:

- Anxiety
- Normal
- Depression
- Suicidal
- Stress

---

# Data Preprocessing

The following preprocessing steps were applied:

- Removed missing text
- Removed duplicate samples
- Removed URLs
- Removed user mentions
- Decoded HTML entities
- Removed invisible Unicode characters
- Normalized whitespace
- Stratified train/validation/test split

---

# Training Configuration

| Parameter | Value |
|----------|-------|
| Optimizer | AdamW |
| Learning Rate | 2e-5 |
| Batch Size | 16 |
| Epochs | 8 |
| Weight Decay | 0.01 |
| Max Length | 256 |
| Evaluation Strategy | Every Epoch |
| Early Stopping | Patience = 2 |
| Best Model Metric | Macro F1 |

---

# Evaluation

Validation Performance

| Metric | Score |
|---------|------:|
| Accuracy | 83.40% |
| Precision (Macro) | 82.06% |
| Recall (Macro) | 82.48% |
| F1 Score (Macro) | 82.23% |

---

# Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

id2label = {
    0: "Anxiety",
    1: "Normal",
    2: "Depression",
    3: "Suicidal",
    4: "Stress"
}

text = "I've been feeling overwhelmed lately and can't stop worrying."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=256
)

with torch.no_grad():
    outputs = model(**inputs)

prediction = outputs.logits.argmax(dim=-1).item()

print(id2label[prediction])
```

---

# Example Prediction

Input:

```
I have been feeling anxious for weeks and can't stop overthinking everything.
```

Output:

```
Anxiety
```

---

# Intended Uses

This model is intended for:

- Mental wellness chatbots
- Emotion-aware conversational AI
- Academic research
- Student support systems
- Early emotional risk identification

---

# Out-of-Scope Uses

This model should **not** be used for:

- Clinical diagnosis
- Medical decision making
- Psychological evaluation
- Determining whether someone has a mental illness
- Automated emergency intervention without human oversight

---

# Limitations

- English only
- Predictions are based solely on text
- Does not understand long-term user history
- May misclassify sarcastic or ambiguous language
- Not a substitute for professional mental health care
- Performance depends on writing style and dataset distribution

---

# Ethical Considerations

This model predicts emotional categories—not mental health diagnoses.

The **Suicidal** class is intended to help conversational systems recognize potentially high-risk messages and encourage appropriate support. Predictions should always be interpreted with human oversight.

Users expressing severe emotional distress should be encouraged to seek help from trusted individuals or qualified mental health professionals.

---

# License

This model is released for **research and educational purposes**.

Please ensure that any deployment involving mental health support includes appropriate human oversight and safety mechanisms.