---
library_name: transformers
tags:
- emotion-classification
- text-classification
- roberta
- goemotions
- sentiment-analysis
license: mit
datasets:
- google-research-datasets/go_emotions
language:
- en
metrics:
- accuracy
- f1
base_model: roberta-base
---

# RoBERTa Emotion Classifier (7-class)

Fine-tuned RoBERTa model for emotion classification on 7 emotions: **happy, sad, angry, fear, disgust, surprise, neutral**.

## Model Details

- **Developed by:** VanshajR
- **Base Model:** `roberta-base` (125M parameters)
- **Task:** Multi-class emotion classification
- **Dataset:** GoEmotions (27 emotions mapped to 7)
- **Training Samples:** ~58,000
- **Language:** English
- **License:** MIT

## Performance

Evaluated on GoEmotions test set:

| Metric | Score |
|--------|-------|
| **Accuracy** | **57.77%** |
| **Macro F1** | **0.4787** |
| Precision | 0.5289 |
| Recall | 0.4958 |

### Per-Class Performance

| Emotion | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Happy | 0.62 | 0.67 | 0.64 | 2,362 |
| Sad | 0.54 | 0.51 | 0.52 | 1,210 |
| Angry | 0.58 | 0.43 | 0.49 | 1,145 |
| Fear | 0.42 | 0.31 | 0.36 | 428 |
| Disgust | 0.48 | 0.26 | 0.34 | 361 |
| Surprise | 0.43 | 0.43 | 0.43 | 623 |
| Neutral | 0.64 | 0.86 | 0.73 | 8,711 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("VanshajR/roberta-emotion-7class")
model = AutoModelForSequenceClassification.from_pretrained("VanshajR/roberta-emotion-7class")

# Classify emotion
text = "I'm so excited about this project!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1).item()

# Emotion labels
emotions = ["happy", "sad", "angry", "fear", "disgust", "surprise", "neutral"]
print(f"Predicted emotion: {emotions[predicted_class]}")
print(f"Confidence: {predictions[0][predicted_class].item():.2%}")
```

## Training Details

### Training Data

- **Dataset:** GoEmotions (Google Research)
- **Emotion Mapping:** 27 fine-grained emotions → 7 basic emotions
- **Training Samples:** ~58,000 Reddit comments
- **Preprocessing:** Truncation to 128 tokens, lowercase normalization

### Training Procedure

- **Optimizer:** AdamW (lr=2e-5, weight_decay=0.01)
- **Batch Size:** 16 (train), 32 (eval)
- **Epochs:** 3
- **Max Length:** 128 tokens
- **Training Regime:** fp32

### Compute Infrastructure

- **Hardware:** NVIDIA RTX 3070 (8GB VRAM)
- **Training Time:** ~2 hours
- **Framework:** PyTorch 2.1.0, Transformers 4.35.0

## Limitations and Bias

- **Language:** English only
- **Domain:** Primarily trained on Reddit comments (may not generalize to formal text)
- **Class Imbalance:** Better performance on frequent emotions (happy, neutral) vs rare emotions (fear, disgust)
- **Subjective Task:** Human annotators often disagree on emotions (~25-30% disagreement rate)

## Intended Use

✅ **Recommended:**
- Emotion detection in conversational text
- Evaluating emotion-controlled text generation
- Research on emotion understanding in dialogue
- Sentiment analysis applications

❌ **Not Recommended:**
- Clinical diagnosis or mental health assessment
- High-stakes decision making
- Non-English languages

## Citation

```bibtex
@misc{vanshajr2024roberta,
  author = {Vanshaj R},
  title = {RoBERTa Emotion Classifier for 7-Class Emotion Detection},
  year = {2024},
  publisher = {HuggingFace},
  url = {https://huggingface.co/VanshajR/roberta-emotion-7class}
}
```

## Related Work

Part of the **Emotion-Controlled Response Generation** project:
- 🔗 [GitHub Repository](https://github.com/VanshajR/emotion-controlled-generation)
- 🔗 [GPT-2 Emotion-Conditioned Model](https://huggingface.co/VanshajR/gpt2-emotion-prefix)
- 📄 [Full Project Report](https://github.com/VanshajR/emotion-controlled-generation/blob/main/PROJECT_REPORT.md)
