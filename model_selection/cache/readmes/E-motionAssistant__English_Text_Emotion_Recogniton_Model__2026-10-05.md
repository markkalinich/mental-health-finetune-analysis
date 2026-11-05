---
language: en
license: apache-2.0
tags:
  - english
  - emotion-classification
  - text-classification
  - fine-tuned
  - roberta
base_model: j-hartmann/emotion-english-distilroberta-base
pipeline_tag: text-classification
---

# English Text Emotion Recognition Model

Fine-tuned RoBERTa-style model for **multi-class emotion classification in English text**.

This model was trained for 6 epochs on an English emotion dataset and achieves modest validation performance (~90% accuracy).  
It is suitable as a starting point for English emotion detection tasks, but would benefit from longer training, more data, or a better-suited base model.

## Model Details

### Model Description

- **Developed by:** Bimsara Serasinghe
- **Shared by:** Bimsara Serasinghe
- **Model type:** Text Classification (fine-tuned transformer for multi-class emotion detection)
- **Language(s) (NLP):** English
- **License:** Apache-2.0
- **Finetuned from model:** j-hartmann/emotion-english-distilroberta-base
### Model Sources

- **Repository:** https://huggingface.co/ShanukaB/English_Text_Emotion_Recogniton_Model

## Uses

### Direct Use

Use the model directly with Hugging Face `pipeline` to classify English sentences into emotion categories.

### Downstream Use

- Building emotion-aware English chatbots
- Social media emotion/sentiment monitoring (Twitter/X, Reddit, comments)
- Mental health & wellbeing tools with emotion detection
- Customer support & feedback analysis
- Academic/research experiments in English affective computing

### Out-of-Scope Use

- High-stakes automated decisions (mental health diagnosis, hiring, legal)
- Safety-critical real-time systems without thorough validation
- Non-English languages (poor generalization expected)

### Recommendations

- Use model outputs only as a signal — combine with human judgment in sensitive contexts
- Fine-tune further (more epochs, larger/cleaner dataset, or emotion-specialized base like roberta-base-go_emotions)
- Evaluate on your specific use-case domain before production

## How to Get Started with the Model

```python
from transformers import pipeline
import joblib

# Load the fine-tuned model
classifier = pipeline(
    "text-classification",
    model="YOUR_USERNAME/YOUR_MODEL_NAME",
    tokenizer="YOUR_USERNAME/YOUR_MODEL_NAME"
)

# Optional: load saved label encoder (if uploaded to repo)
# label_encoder = joblib.load("label_encoder.pkl")

texts = [
    "I'm so happy today! 🎉",
    "This is really making me angry...",
    "I feel so scared right now 😨",
    "This is disgusting, I can't believe it."
]

for text in texts:
    result = classifier(text)[0]
    # If labels are saved as "LABEL_0", "LABEL_1", etc.
    # num_label = int(result["label"].split("_")[-1])
    # emotion = label_encoder.inverse_transform([num_label])[0] if label_encoder else result["label"]
    print(f"Text: {text}")
    print(f"→ {result['label']} (confidence: {result['score']:.3f})\n")