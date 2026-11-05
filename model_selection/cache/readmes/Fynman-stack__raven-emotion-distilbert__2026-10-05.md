---
license: mit
language:
  - en
  - hi
library_name: transformers
pipeline_tag: text-classification
tags:
  - emotion-detection
  - distilbert
  - sentiment-analysis
  - mental-health
  - emotion-classification
  - text-classification
  - transformers
  - pytorch
  - hinglish
base_model: distilbert-base-uncased
datasets:
  - google-research-datasets/go_emotions
metrics:
  - accuracy
  - f1
  - precision
  - recall
model-index:
  - name: raven-emotion-distilbert
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: Custom Indian + International Dataset
          type: custom
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.9762
          - name: F1
            type: f1
            value: 0.9762
          - name: Precision
            type: precision
            value: 0.9762
          - name: Recall
            type: recall
            value: 0.9762
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: GoEmotions (Balanced 300 samples)
          type: google-research-datasets/go_emotions
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.7733
          - name: F1
            type: f1
            value: 0.7724
widget:
  - text: "I'm so stressed about my exam tomorrow, I can't sleep"
    example_title: Anxious
  - text: "Just got promoted at work, feeling on top of the world!"
    example_title: Happy
  - text: "I don't understand why this code keeps throwing errors"
    example_title: Confused
  - text: "I lost my best friend over a stupid argument"
    example_title: Sad
  - text: "This is absolutely unacceptable, I'm furious right now"
    example_title: Angry
  - text: "Nothing much going on today, just chilling at home"
    example_title: Neutral
---

# Raven Emotion DistilBERT

A fine-tuned **DistilBERT** model for 6-class emotion classification, built for [Raven AI](https://raven-ai-new.streamlit.app) — an emotionally aware AI assistant.

This model classifies text into **6 emotions**: `happy`, `sad`, `anxious`, `angry`, `confused`, `neutral`.

## Performance

| Model / Method | Dataset | Accuracy | F1 Score |
|---|---|---|---|
| Zero-Shot LLM (LLama 3.3 70B) | GoEmotions | 66.67% | 0.6691 |
| Few-Shot LLM (LLama 3.3 70B) | GoEmotions | 73.00% | 0.7331 |
| **This model** (initial training) | GoEmotions | **77.33%** | **0.7724** |
| **This model** (after domain adaptation) | Custom Dataset | **97.62%** | **0.9762** |

**Key result**: This 67M parameter model outperforms a 70B parameter LLM by +4.33% on emotion classification, proving that task-specific fine-tuning beats general-purpose prompting.

## Quick Start

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Fynman-stack/raven-emotion-distilbert", top_k=None)

result = classifier("I'm so stressed about my exam tomorrow")
print(result)
# [[{'label': 'anxious', 'score': 0.95}, {'label': 'sad', 'score': 0.02}, ...]]
```

Or load the model directly:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Fynman-stack/raven-emotion-distilbert")
model = AutoModelForSequenceClassification.from_pretrained("Fynman-stack/raven-emotion-distilbert")

EMOTIONS = ["happy", "sad", "anxious", "angry", "confused", "neutral"]

def detect_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return EMOTIONS[torch.argmax(outputs.logits, dim=1).item()]

print(detect_emotion("I just cleared my exam!"))  # happy
print(detect_emotion("I'm furious at this situation"))  # angry
```

## Labels

| ID | Label | Description |
|---|---|---|
| 0 | `happy` | Joy, excitement, gratitude, love, pride, amusement |
| 1 | `sad` | Sadness, grief, disappointment, remorse |
| 2 | `anxious` | Fear, nervousness, worry, stress |
| 3 | `angry` | Anger, annoyance, frustration, disgust |
| 4 | `confused` | Confusion, surprise, curiosity, realization |
| 5 | `neutral` | Neutral, calm, indifferent |

## Training Details

### Phase 1: Initial Training on GoEmotions

- **Base model**: `distilbert-base-uncased` (67M parameters)
- **Dataset**: [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) — Google's 28-emotion dataset, mapped to 6 categories
- **Epochs**: 3 | **Batch size**: 16 | **Learning rate**: 2e-5 | **Optimizer**: AdamW (weight decay 0.01)

| Epoch | Train Loss | Val Accuracy | Val F1 |
|---|---|---|---|
| 1 | 1.1599 | 66.93% | 0.6671 |
| 2 | 0.8031 | 67.37% | 0.6737 |
| 3 | 0.6494 | 67.64% | 0.6747 |

### Phase 2: Domain Adaptation on Custom Dataset

The model was further trained on ~12,343 samples of Indian English, Hinglish (Hindi-English), American English, and British English conversational text to adapt it for real-world student conversations.

- **Learning rate**: 5e-6 (reduced to prevent catastrophic forgetting)
- **Early stopping**: Patience of 2 epochs
- **Warmup**: 10% of total training steps
- **Gradient clipping**: 1.0

| Epoch | Train Loss | Val Accuracy | Val F1 |
|---|---|---|---|
| 1 | 0.6765 | 90.99% | 0.9093 |
| 2 | 0.2549 | 93.15% | 0.9311 |
| 3 | 0.1625 | 94.08% | 0.9406 |
| 4 | 0.1147 | 94.46% | 0.9444 |
| 5 | 0.0940 | 94.65% | 0.9463 |

**Domain adaptation impact**: Accuracy jumped from 64.38% to 97.62% (+33.24%) on the target domain.

## GoEmotions Label Mapping

The original 28 GoEmotions labels were mapped to 6 categories:

| Raven Label | GoEmotions Labels |
|---|---|
| `happy` | joy, amusement, excitement, gratitude, love, optimism, pride, relief, admiration, approval, caring |
| `sad` | sadness, grief, disappointment, remorse, embarrassment |
| `anxious` | fear, nervousness |
| `angry` | anger, annoyance, disgust |
| `confused` | confusion, surprise, realization, curiosity |
| `neutral` | neutral, desire |

## Use Cases

- **Emotionally aware chatbots** — Adjust response tone based on user emotion
- **Mental health applications** — Detect distress, anxiety, or anger in user messages
- **Customer support** — Route frustrated or confused customers to appropriate agents
- **Social media monitoring** — Track emotional sentiment across conversations
- **Education platforms** — Detect student frustration or confusion in real-time

## About Raven AI

This model powers [Raven AI](https://raven-ai-new.streamlit.app), an emotionally aware AI assistant that adapts its tone, persona, and response style based on detected user emotion. Raven includes crisis detection, multi-chat management, image understanding, voice input, document processing, and 20+ other features.

- **Try it live (HuggingFace Space)**: [huggingface.co/spaces/Fynman-stack/raven-ai](https://huggingface.co/spaces/Fynman-stack/raven-ai)
- **Streamlit Cloud**: [raven-ai-new.streamlit.app](https://raven-ai-new.streamlit.app)
- **GitHub**: [github.com/Fynman-stack/raven-ai](https://github.com/Fynman-stack/raven-ai)

## Model Architecture

- **Base**: DistilBERT (6 layers, 12 attention heads, 768 hidden dim)
- **Parameters**: 67M
- **Task head**: Sequence classification (6 classes)
- **Max sequence length**: 128 tokens
- **Format**: Safetensors (FP32)

## Limitations

- Trained primarily on English and Hinglish text — may not generalize well to other languages
- Emotion categories are coarse-grained (6 classes) — may miss nuanced emotional states
- Performance on formal/academic text may differ from conversational text
- Not a diagnostic tool — should not be used as a substitute for professional mental health assessment

## Citation

```bibtex
@misc{raha2026raven,
  title={Raven AI: An Emotionally Aware AI Assistant with Fine-tuned DistilBERT},
  author={Soumyadip Raha},
  year={2026},
  url={https://huggingface.co/Fynman-stack/raven-emotion-distilbert}
}
```

## License

MIT
