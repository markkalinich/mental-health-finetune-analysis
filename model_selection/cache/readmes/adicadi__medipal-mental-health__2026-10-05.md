---
language: en
license: mit
tags:
- mental-health
- sentiment-analysis
- text-classification
- roberta
- psychology
datasets:
- mental_health_dataset
metrics:
- accuracy
- f1
model-index:
- name: medipal-mental-health
  results:
  - task:
      type: text-classification
      name: Mental Health Classification
    metrics:
    - type: accuracy
      value: 76.5
      name: Accuracy
    - type: f1
      value: 76.6
      name: F1 Score
pipeline_tag: text-classification
widget:
- text: "I feel anxious and worried about everything"
  example_title: "Anxiety"
- text: "I am so happy and everything is going great"
  example_title: "Normal"
- text: "I feel so sad and hopeless, nothing matters anymore"
  example_title: "Depression"
- text: "I am so stressed and overwhelmed with work"
  example_title: "Stress"
---

# MediPal Mental Health Classification Model

## Model Description

This is a fine-tuned RoBERTa-Large model for mental health sentiment classification. It classifies text into 7 categories:

- **Normal**: Healthy mental state
- **Anxiety**: Anxious thoughts and worry
- **Depression**: Depressive symptoms
- **Stress**: Stress-related content
- **Bipolar**: Bipolar disorder indicators
- **Personality disorder**: Personality disorder symptoms
- **Suicidal**: Suicidal ideation (requires immediate intervention)

## Model Performance

- **Accuracy**: 76.5%
- **F1 Score**: 76.6%
- **Base Model**: RoBERTa-Large
- **Training Dataset**: Mental health text corpus

## Intended Use

This model is designed for mental health journal analysis and should be used as a supportive tool, not as a replacement for professional mental health diagnosis.

## How to Use

### Using Transformers

from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

model = RobertaForSequenceClassification.from_pretrained("adicadi/medipal-mental-health")
tokenizer = RobertaTokenizer.from_pretrained("adicadi/medipal-mental-health")

text = "I feel anxious and worried"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
predicted_class = torch.argmax(predictions).item()

labels = ['Anxiety', 'Bipolar', 'Depression', 'Normal', 'Personality disorder', 'Stress', 'Suicidal']
print(f"Predicted: {labels[predicted_class]}")
print(f"Confidence: {predictions[predicted_class].item():.2f}")


### Using Inference API

curl https://api-inference.huggingface.co/models/adicadi/medipal-mental-health
-H "Authorization: Bearer YOUR_HF_TOKEN"
-H "Content-Type: application/json"
-d '{"inputs": "I feel anxious and worried"}'



## Limitations

- Not a substitute for professional mental health diagnosis
- May not capture cultural or linguistic nuances
- Trained on English text only
- Requires professional validation for clinical use

## Ethical Considerations

This model deals with sensitive mental health data. Users should:
- Handle predictions with care and empathy
- Provide appropriate crisis resources for high-risk predictions
- Not use as the sole basis for mental health decisions
- Comply with local healthcare regulations

## Contact

For questions or issues, please contact the model author.

