---
license: apache-2.0
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
tags:
- text-classification
- sentiment-analysis
- twitch
- roberta
- gaming
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
widget:
- text: "POGGERS we actually clutched that round!"
  example_title: "Positive Chat"
- text: "bro is throwing so hard... actual paper rank gameplay"
  example_title: "Negative Flame"
- text: "does anyone know when stream starts?"
  example_title: "Neutral Inquiry"
---

# Twitch RoBERTa Sentiment (v1)

Fine-tuned sentiment classifier optimized for live **Twitch.tv chat**. Built on `cardiffnlp/twitter-roberta-base-sentiment-latest` and adapted to gaming slang, streaming culture, and platform-specific emotes.

Standard models misinterpret gaming terms. This model corrects them.

## Why It Works

| Message | Standard RoBERTa | **This Model** | Reason |
| :--- | :--- | :--- | :--- |
| `"He's actually cracked"` | 🔴 Negative | **🟢 Positive** | "Cracked" = skillful, not broken |
| `"bro is throwing"` | ⚪ Neutral | **🔴 Negative** | "Throwing" = losing on purpose |
| `"POGGERS clutched it"` | ⚪ Neutral | **🟢 Positive** | Emote correctly weighted as hype |

## Model Details

- **Developed by:** [muyihenhen](https://huggingface.co/muyihenhen)
- **Base Model:** `cardiffnlp/twitter-roberta-base-sentiment-latest` (RoBERTa-base)
- **Language:** English (Twitch Chat dialect)
- **License:** Apache 2.0
- **Primary Task:** 3-class Sentiment Analysis (Negative, Neutral, Positive)

## Training Methodology

Two-stage training pipeline:

1. **Domain Adaptation (MLM):** Adapted on 1.1M unlabeled Twitch messages. Perplexity reduced from ~21k to ~5.5.
2. **Sentiment Fine-Tuning:** Fine-tuned on labeled Twitch chat logs with early stopping to prevent overfitting on repetitive messages.

## Intended Uses & Limitations

Use this model for real-time sentiment analysis of Twitch chat—sentiment dashboards, moderation tools, stream analytics, or audience mood tracking.

### How to Use

You can load and use the model directly with Hugging Face's `pipeline`:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "muyihenhen/twitch-roberta-sentiment-v1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

results = classifier([
    "OOOO we actually clutched that round!",
    "bro is throwing so hard...genuine plastic rank gameplay",
    "anyone know when stream starts?"
])

for text, res in zip(texts, results):
    print(f"Text: {text} -> Label: {res['label']} ({res['score']:.4f})")
```

### Output Labels
- **NEGATIVE:** Insult / Frustration
- **NEUTRAL:** General Chat / Inquiries
- **POSITIVE:** Positive / Hype

### Limitations
- Optimized for internet/gaming culture. It might over-index on gaming terms if used on formal, academic, or corporate text.
- Highly dependent on the context of standard English-dominated Twitch channels. Performance may vary on chats with heavy multilingual blending.
