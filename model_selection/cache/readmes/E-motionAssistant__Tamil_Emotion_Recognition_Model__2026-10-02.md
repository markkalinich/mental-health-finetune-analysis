---
language: ta
license: apache-2.0
tags:
  - tamil
  - emotion-classification
  - text-classification
  - fine-tuned
  - multilingual
base_model: jusgowiturs/autotrain-tamil_emotion_11_tamilbert-2710380899
pipeline_tag: text-classification
---

# Tamil Text Emotion Recognition Model

Fine-tuned Tamil language model for **11-class emotion classification** in Tamil text.  
Detects: Ambiguous, Anger, Anticipation, Disgust, Fear, Joy, Love, Neutral, Sadness, Surprise, Trust.  
Achieves ~94.5% accuracy on validation set after 6 epochs of fine-tuning.

## Model Details

### Model Description

- **Developed by:** Shanuka B Serasinghe
- **Shared by:** Shanuka B Serasinghe
- **Model type:** Text Classification (fine-tuned transformer for multi-class emotion detection)
- **Language(s) (NLP):** Tamil (தமிழ்)
- **License:** Apache-2.0
- **Finetuned from model:** jusgowiturs/autotrain-tamil_emotion_11_tamilbert-2710380899 (AutoTrain-generated Tamil-BERT style checkpoint)

### Model Sources

- **Repository:** https://huggingface.co/ShanukaB/Tamil_Emotion_Recognition_Model


## Uses

### Direct Use

Direct inference with Hugging Face `pipeline` for classifying Tamil sentences/comments into one of 11 emotions.

### Downstream Use

- Building emotion-aware Tamil chatbots
- Tamil social media sentiment & emotion monitoring
- Mental health & emotional wellbeing applications in Tamil
- Customer support systems with emotion detection
- Further research/fine-tuning in low-resource Tamil NLP

### Out-of-Scope Use

- High-stakes automated decisions (e.g. mental health diagnosis, hiring, legal)
- Real-time safety-critical systems without human oversight
- Non-Tamil languages (performance will be very poor)

## Bias, Risks, and Limitations

- Best performance on short-to-medium informal/colloquial Tamil text (social media style)
- Heavy code-mixing (Tamil + English) reduces accuracy
- Sarcasm, irony, subtle emotions, strong dialects, or very formal/literary Tamil may be misclassified
- Potential biases from training data (e.g. over-representation of certain topics/styles in emotion datasets)
- Not robust to adversarial inputs or out-of-distribution text

### Recommendations

- Always combine model predictions with human review in sensitive use-cases
- Test thoroughly on your specific domain/dialect before deployment
- Report issues (especially dialect or code-mixed failures) to improve future versions

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="YOUR_USERNAME/YOUR_MODEL_NAME",
    tokenizer="YOUR_USERNAME/YOUR_MODEL_NAME"
)

texts = [
    "இது ரொம்ப அழகா இருக்கு! 🥰🥰",
    "என்னடா இது… மிகவும் கோபமா வருது",
    "யாரும் இல்லாம தனிமையா ஃபீல் பண்றேன் 😔",
    "அடேங்கப்பா! இது எப்படி சாத்தியமா? 😲"
]

for text in texts:
    result = classifier(text)[0]
    print(f"Text: {text}")
    print(f"→ {result['label']} (confidence: {result['score']:.3f})\n")