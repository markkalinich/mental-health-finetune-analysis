---
language:
- bn
license: apache-2.0
tags:
- sentiment-analysis
- emotion-classification
- bangla
- bengali
- political-analysis
- social-media
- opinion-mining
tasks:
- text-classification
pipeline_tag: text-classification
library_name: transformers
model_type: bert
base_model: csebuetnlp/banglabert_large
finetuned_from: csebuetnlp/banglabert_large
datasets:
- custom
---

# Sentimotion_v1

## Model Details

### Model Name
**Sentimotion_v1**

### Model Type
Joint **Sentiment Analysis** and **Emotion Classification** model for Bangla (Bengali) text.

### Base Model
[csebuetnlp/banglabert_large](https://huggingface.co/csebuetnlp/banglabert_large)

### Architecture
- BanglaBERT-large encoder
- Shared contextual representation (CLS token)
- Two parallel classification heads:
  - Sentiment head (3 classes)
  - Emotion head (6 classes)

### Tasks
- Sentiment Classification
- Emotion Classification

### Language(s)
- Bangla (bn)

---

## Intended Use

### Primary Use Cases
This model is intended for:
- Bangla social media sentiment analysis
- Political opinion and discourse monitoring
- Emotion-aware text analytics
- Public opinion mining
- Academic and applied Bangla NLP research
- Human-in-the-loop moderation and analytics systems

### Out-of-Scope Uses
This model **should not** be used:
- As the sole system for content moderation
- For legal, medical, or law-enforcement decisions
- For automated decision-making affecting individuals

Human review is strongly recommended for sensitive or high-impact applications.

---

## Model Inputs and Outputs

### Input
A single Bangla text string.

Example:
জনগণ নির্ধারণ করবে কে জয়ী হবে।

```python
import torch
import numpy as np

SENTIMENT_LABELS = ["negative", "neutral", "positive"]
EMOTION_LABELS = ["neutral", "happy", "anger_disgust", "sadness", "surprise", "fear"]

def predict(text, model, tokenizer, device="cpu",
            sent_threshold=0.55,
            emo_threshold=0.60):

    model.eval()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128
    ).to(device)

    with torch.no_grad():
        sent_logits, emo_logits = model(
            inputs["input_ids"],
            inputs["attention_mask"]
        )

    # ---------- Softmax ----------
    sent_probs = torch.softmax(sent_logits, dim=1).cpu().numpy()[0]
    emo_probs  = torch.softmax(emo_logits,  dim=1).cpu().numpy()[0]

    # ---------- Sentiment ----------
    sent_idx = int(np.argmax(sent_probs))
    sent_conf = float(sent_probs[sent_idx])

    if sent_conf < sent_threshold:
        sentiment = "neutral"
        sent_conf = float(sent_probs[SENTIMENT_LABELS.index("neutral")])
    else:
        sentiment = SENTIMENT_LABELS[sent_idx]

    # ---------- Emotion ----------
    emo_idx = int(np.argmax(emo_probs))
    emo_conf = float(emo_probs[emo_idx])

    if emo_conf < emo_threshold:
        emotion = "neutral"
        emo_conf = float(emo_probs[EMOTION_LABELS.index("neutral")])
    else:
        emotion = EMOTION_LABELS[emo_idx]

    # ---------- JSON output ----------
    result = {
        "sentiment": sentiment,
        "sentiment_confidence": round(sent_conf, 6),
        "emotion": emotion,
        "emotion_confidence": round(emo_conf, 6),
        "sentiment_scores": {
            label: float(sent_probs[i])
            for i, label in enumerate(SENTIMENT_LABELS)
        },
        "emotion_scores": {
            label: float(emo_probs[i])
            for i, label in enumerate(EMOTION_LABELS)
        }
    }

    return result

```


Maximum supported length:
- Up to 512 tokens (recommended: 128 tokens)

---

### Output

The model produces **two independent predictions**:

#### Sentiment (3-class)
- `negative`
- `neutral`
- `positive`

#### Emotion (6-class)
- `neutral`
- `happy`
- `anger_disgust`
- `sadness`
- `surprise`
- `fear`

Each output is returned as a **softmax probability distribution**.

---

## Training Details

### Training Strategy
- Multi-task learning with a shared encoder
- Joint optimization of sentiment and emotion heads
- Balanced cross-entropy loss between tasks

### Dataset
- Custom labeled Bangla dataset
- Includes real-world Bangla text such as:
  - political commentary
  - public opinion
  - social media–style language

### Data Characteristics
- Sentiment labels consolidated into 3 classes
- Emotion labels are single-label (dominant emotion)
- Strong class imbalance for `fear` and `surprise`

### Hardware
- GPU-based training
- Mixed precision (FP16)

---

## Evaluation Results

### Sentiment Classification (Test Set)

| Metric | Score |
|------|------|
| Accuracy | ~0.87 |
| Macro F1 | ~0.86 |

| Class | F1-score |
|------|---------|
| Negative | ~0.90 |
| Neutral | ~0.82 |
| Positive | ~0.86 |

---

### Emotion Classification (Test Set)

| Metric | Score |
|------|------|
| Macro F1 | ~0.63 |
| Weighted F1 | ~0.77 |

| Emotion | F1-score | Notes |
|--------|----------|------|
| Neutral | ~0.73 | Strong |
| Happy | ~0.83 | Strong |
| Anger/Disgust | ~0.84 | Very strong |
| Sadness | ~0.67 | Moderate |
| Surprise | ~0.26 | Low (few samples) |
| Fear | ~0.44 | Low (few samples) |

Lower performance on `fear` and `surprise` is primarily due to **limited labeled data**, not architectural limitations.

---

## Ethical Considerations

### Biases
- Political text may trigger higher sensitivity to anger-related language
- Predictions reflect the distribution and biases of the training data

### Mitigation Strategies
- Use probability thresholds instead of hard labels
- Combine with a separate hate-speech or abuse detection model
- Maintain human oversight for moderation or policy use

---

## Limitations

- Not a hate-speech detector by itself
- Rare emotion classes generalize less effectively
- Emotion predictions capture dominant signals, not mixed emotions
- Attention/gradient-based explanations indicate influence, not causality

---

## How to Use the Model

⚠️ This model uses a **custom architecture** and **cannot** be loaded directly using  
`AutoModelForSequenceClassification`.

Users must:
1. Load the base BanglaBERT encoder
2. Reconstruct the joint sentiment–emotion architecture
3. Load weights from `model.safetensors`

Refer to the repository for example inference code and API usage.

---

## License

Apache License 2.0

---

## Citation

If you use this model in academic or applied research, please cite:

```bibtex
@misc{sentimotion2026,
  title  = {Sentimotion_v1: A Joint Bangla Sentiment and Emotion Classification Model},
  author = {Arafat Fahim},
  year   = {2026},
  url    = {https://huggingface.co/arafatfahim/sentimotion}
}
