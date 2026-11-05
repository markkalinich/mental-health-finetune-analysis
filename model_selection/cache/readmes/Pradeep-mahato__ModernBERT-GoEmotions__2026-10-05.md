---
library_name: transformers
license: apache-2.0
tags:
- emotion-classification
- multi-label-classification
- nlp
- transformers
- goemotions
- modernbert
language:
- en
---

# ModernBERT-GoEmotions

## Model Summary

**ModernBERT-GoEmotions** is a fine-tuned Transformer-based model for **multi-label emotion classification**.  
Given a short text input, the model predicts one or more emotions from a predefined set of **27 emotions + neutral**, as defined in the GoEmotions dataset.

The model is designed for applications requiring **fine-grained emotional understanding**, such as affective chat systems, moderation pipelines, and sentiment-aware conversational agents.

---

## Model Details

### Model Description

- **Developed by:** Pradeep Kr. Mahato  
- **Model type:** Encoder-only Transformer (BERT-style)  
- **Language(s):** English  
- **License:** Apache 2.0  
- **Fine-tuned from:** `answerdotai/ModernBERT-base`  
- **Task:** Multi-label text classification  
- **Output:** Independent emotion probabilities via sigmoid activation  

### Model Sources

- **Base Model:** https://huggingface.co/answerdotai/ModernBERT-base  
- **Dataset:** https://huggingface.co/datasets/google-research-datasets/go_emotions  

---

## Uses

### Direct Use

The model can be used directly to:
- Detect multiple emotions in short English texts
- Analyze emotional tone in social media posts or chats
- Power emotion-aware chat or moderation systems

### Downstream Use

The model may be integrated into:
- Conversational AI pipelines
- Mental health or well-being analytics (non-diagnostic)
- Emotion-aware recommendation systems
- Research on affective computing

### Out-of-Scope Use

The model is **not intended** for:
- Medical or psychological diagnosis
- Legal or forensic decision-making
- High-stakes autonomous systems
- Real-time moderation without human oversight

---

## Bias, Risks, and Limitations

- The training data is derived from Reddit, which may contain **demographic, cultural, and topical biases**
- Emotion labels may be subjective and context-dependent
- The model does not explicitly model emotion intensity or temporal dynamics
- Predictions should be interpreted as **probabilistic signals**, not ground truth

### Recommendations

- Use human-in-the-loop validation for sensitive applications
- Calibrate thresholds per emotion for production use
- Avoid over-reliance on single-label interpretations

---

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="your-username/ModernBERT-GoEmotions",
    return_all_scores=True
)

classifier("I feel anxious but also hopeful about the future.")
