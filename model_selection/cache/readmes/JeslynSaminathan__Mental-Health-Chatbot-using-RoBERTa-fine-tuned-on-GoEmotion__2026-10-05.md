---
license: apache-2.0
datasets:
  - GoEmotions
library_name: transformers
language:
  - en
tags:
  - text-classification
  - emotion-detection
  - mental-health
  - fine-tuned
model-index:
  - name: Mental-Health-Chatbot-using-RoBERTa
    results:
      - task:
          type: text-classification
        dataset:
          name: GoEmotions
          type: emotions
        metrics:
          - name: AI2 Reasoning Challenge (25-Shot)
            type: AI2 Reasoning Challenge (25-Shot)
            value: 64.59
        source:
          name: Open LLM Leaderboard
          url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
---

# Mental Health Chatbot using RoBERTa (Fine-Tuned on GoEmotions)

## Model Description

This model is a fine-tuned version of **RoBERTa-base**, specifically designed to perform multi-label emotion classification. It has been trained on the **GoEmotions** dataset, a comprehensive dataset containing 28 emotion categories from Reddit comments. This model is optimized for applications requiring nuanced emotion analysis, such as mental health chatbots, sentiment analysis, and customer interaction systems.

Key Features:
- Multi-label emotion classification covering 28 fine-grained categories.
- Real-time inference capabilities for interactive applications.
- High accuracy on detecting nuanced emotions like gratitude, joy, and sadness.

---

## Repository

The full project, including the chatbot implementation and fine-tuning code, can be found at:
[GitHub Repository](https://github.com/kashyaparun25/Mental-Health-Chatbot-using-RoBERTa-and-Gemini)

---

## Applications

- **Mental Health Chatbots**: Understand user emotions and provide empathetic responses for emotional well-being.
- **Sentiment Analysis**: Analyze social media posts, reviews, and comments to gauge public sentiment.
- **Customer Support Systems**: Enhance customer interactions by detecting emotional states.

---

## Training and Evaluation

### Training Configuration

- **Base Model**: RoBERTa-base
- **Dataset**: [GoEmotions](https://www.kaggle.com/datasets/google/goemotions)
- **Batch Size**: 32
- **Optimizer**: AdamW
- **Learning Rate Scheduler**: Cosine Annealing
- **Loss Function**: Binary Cross-Entropy for multi-label classification
- **Epochs**: 5

### Evaluation Results

The model achieved the following performance metrics on the GoEmotions dataset:

| Metric        | Value  |
|---------------|--------|
| Macro F1-Score | 0.74 |
| ROC-AUC        | 0.95 |

Additional Benchmark:
- **AI2 Reasoning Challenge (25-Shot)**: 64.59  
  [Source: Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

---

## Model Files

The repository includes:
- **Tokenizer Configuration**: `tokenizer.json`, `tokenizer_config.json`, and `vocab.json`.
- **Model Weights**: `model_weights.pth`.
- **Special Tokens Map**: `special_tokens_map.json`.

These files are essential for reproducing the model or deploying it into other systems.

---

## How to Use

To load the model and tokenizer:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("kashyaparun/Mental-Health-Chatbot-using-RoBERTa")
model = AutoModelForSequenceClassification.from_pretrained("kashyaparun/Mental-Health-Chatbot-using-RoBERTa")

# Perform inference
text = "I'm feeling so joyful today!"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)

# Emotion logits
print(outputs.logits)
