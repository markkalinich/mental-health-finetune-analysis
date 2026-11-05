---
language:
  - en
  - ur
license: mit
tags:
  - emotion-classification
  - multilingual
  - urdu
  - xlm-roberta
metrics:
  - accuracy
  - f1
---

# Multilingual Emotion Classifier (XLM‑RoBERTa)

A fine‑tuned **XLM‑RoBERTa** model for **7‑class emotion detection** in English, Urdu.

## Model Description

This model classifies text into seven **Ekman emotions**:
- anger
- disgust
- fear
- joy
- neutral
- sadness
- surprise

It is trained on a **balanced dataset of ~75k samples** covering English, Urdu script.

## Intended Use

Primary use: **Sakoonify** – an anonymous mental‑health companion that detects user emotions and provides empathetic responses.

Suitable for:
- Sentiment analysis in multilingual Pakistani text
- Chatbots that need to understand user emotions
- Research on code‑mixed emotion classification

## Training Data

- **Source**: Curated and balanced dataset of English, Urdu.
- **Size**: ~75,000 examples (equally distributed across 7 emotions).
- **Preprocessing**: Tokenized with XLM‑RoBERTa tokenizer, max length 128 tokens.

## Training Procedure

- **Base model**: `xlm-roberta-base`
- **Frameworks**: Hugging Face Transformers, PyTorch
- **Epochs**: 3
- **Batch size**: 16
- **Learning rate**: 2e‑5
- **Optimizer**: AdamW with linear warmup scheduler
- **Hardware**: Google Colab (T4 GPU)
- **Checkpointing**: Kept last 2 checkpoints to prevent data loss.

## Evaluation

Final accuracy on held‑out test set (20% stratified): **71%**

| Emotion  | Precision | Recall | F1‑Score | Support |
|----------|-----------|--------|----------|---------|
| anger    | 0.74 | 0.72 | 0.73 | 2200 |
| disgust  | 0.75 | 0.78 | 0.76 | 2200 |
| fear     | 0.79 | 0.75 | 0.77 | 2200 |
| joy      | 0.58 | 0.62 | 0.60 | 2163 |
| neutral  | 0.81 | 0.73 | 0.76 | 1990 |
| sadness  | 0.56 | 0.65 | 0.60 | 2200 |
| surprise | 0.82 | 0.74 | 0.78 | 2200 |

**Key observations:**
- Joy and Sadness show some confusion (largest cross‑misclassifications) – typical for these closely related emotions.
- Disgust, Fear, Neutral, and Surprise are classified reliably.
- The model handles three languages (English, Urdu script, Roman Urdu) with a single architecture.

## Limitations

- The model may confuse similar emotions (e.g., anger vs sadness, joy vs sadness) in subtle contexts.
- Performance on heavily code‑switched text may be lower than on pure English or Urdu.
- Not suitable for clinical diagnosis – use only as a supportive tool.

## Citation

If you use this model, please cite:
