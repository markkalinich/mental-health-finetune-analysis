---
language: si
license: apache-2.0
tags:
  - sinhala
  - emotion-classification
  - text-classification
  - fine-tuned
  - low-resource
  - multilingual
base_model: NLPC-UOM/SinBERT-large
pipeline_tag: text-classification
---

# Sinhala Text Emotion Recognition Model

Fine-tuned RoBERTa-style transformer for **multi-class emotion classification in Sinhala text**.  
Detects basic emotions from Sinhala sentences/comments (e.g. social media, news).  
Trained for 6 epochs on a Sinhala emotion dataset; validation accuracy 86% (modest performance – typical for initial fine-tuning in low-resource Sinhala NLP; suggest more epochs or Sinhala-pretrained base for better results).

## Model Details

### Model Description

- **Developed by:** Bimsara Serasinghe
- **Shared by:** Bimsara Serasinghe
- **Model type:** Text Classification (fine-tuned encoder-only transformer for multi-class emotion detection)
- **Language(s) (NLP):** Sinhala (සිංහල)
- **License:** Apache-2.0
- **Finetuned from model:** NLPC-UOM/SinBERT-large

### Model Sources

- **Repository:** https://huggingface.co/ShanukaB/SInhala_Text_Emotion_Recognition_Model

## Uses

### Direct Use

Classify Sinhala text directly via Hugging Face `pipeline` into one of the emotion classes.

### Downstream Use

- Emotion-aware Sinhala chatbots & virtual assistants
- Monitoring emotions in Sinhala social media (Facebook comments, YouTube, Twitter/X)
- Mental health & wellbeing tools for Sinhala speakers
- Customer support emotion detection in Sinhala
- Academic/research projects on low-resource Sinhala affective computing

### Out-of-Scope Use

- High-stakes automated decisions (e.g. psychological diagnosis, legal judgments)
- Real-time safety-critical systems without human validation
- Non-Sinhala languages (expected very poor performance)
  
### Recommendations

- Always pair model outputs with human review for sensitive applications (mental health, support)
- Fine-tune longer or switch to Sinhala-specific pre-trained models (e.g. SinBERT variants if available)
- Test on your target domain (e.g. news vs. casual chat) before deployment
- Report dialect/code-mixed failures to improve community versions

## How to Get Started with the Model

```python
from transformers import pipeline
import joblib  # if using saved label encoder

classifier = pipeline(
    "text-classification",
    model="YOUR_USERNAME/YOUR_MODEL_NAME",
    tokenizer="YOUR_USERNAME/YOUR_MODEL_NAME"
)

# Optional: load label encoder if uploaded to repo
# label_encoder = joblib.load("label_encoder.pkl")

texts = [
    "මම ගොඩක් සතුටින් ඉන්නවා! 😊",
    "මේක බලල බයයි වෙලා... 😨",
    "අපිට මේක ගැන කෝපයි ගොඩක්!"
]

for text in texts:
    result = classifier(text)[0]
    # If labels are "LABEL_0" etc., map manually or use saved encoder
    print(f"Text: {text}")
    print(f"→ Emotion: {result['label']} (confidence: {result['score']:.3f})\n")