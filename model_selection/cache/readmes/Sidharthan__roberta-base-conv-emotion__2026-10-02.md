---
library_name: transformers
tags:
- conversation
- empathetic
- roberta-base
license: apache-2.0
datasets:
- facebook/empathetic_dialogues
language:
- en
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- FacebookAI/roberta-base
pipeline_tag: text-classification
---
# Model Card: RoBERTa Fine-Tuned on Empathetic Dialogues

## Model Description

This is a RoBERTa-based model fine-tuned on the Empathetic Dialogues dataset for conversational emotion classification. The model leverages the powerful RoBERTa architecture to understand and classify emotional contexts in conversational text.

### Emotion Classes
The model is trained to classify conversations into the following emotional categories:
- Surprised
- Angry
- Sad
- Joyful
- Anxious
- Hopeful
- Confident
- Disappointed

### Model Details
- **Base Model**: roberta-base
- **Task**: Emotion Classification in Conversations
- **Dataset**: Empathetic Dialogues
- **Training Approach**: Full Fine-Tuning
- **Number of Emotion Classes**: 8

### Model Performance

| Metric | Score |
|--------|-------|
| Test Loss | 0.8107 |
| Test Accuracy | 73.01% |
| Test F1 Score | 72.96% |
| Runtime | 10.99 seconds |
| Samples per Second | 61.68 |
| Steps per Second | 1.001 |

## Usage

### Hugging Face Transformers Pipeline

```python
from transformers import pipeline

# Initialize the emotion classification pipeline
classifier = pipeline(
    "text-classification", 
    model="Sidharthan/roberta-base-conv-emotion"
)

# Classify emotion in a conversation
text = "I'm feeling really frustrated with work lately."
result = classifier(text)
print(result)
```

### Direct Model Loading

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = "Sidharthan/roberta-base-conv-emotion"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare input
text = "I'm feeling really frustrated with work lately."
inputs = tokenizer(text, return_tensors="pt")

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(predictions, dim=1)
```

## Limitations
- Performance may vary with out-of-domain conversational contexts
- Emotion classification limited to the 8 specified emotional categories
- Relies on the specific emotional nuances in the Empathetic Dialogues dataset
- Requires careful interpretation in real-world applications

## Ethical Considerations
- Emotion classification can be subjective
- Potential for bias based on training data
- Should not be used for making critical decisions about individuals

## License
Apache 2.0

## Citations
```bibtex
@misc{roberta-base-conv-emotion,
  title={RoBERTa Fine-Tuned on Empathetic Dialogues},
  author={Sidharthan},
  year={2024},
  publisher={Hugging Face}
}
```

## Contact
For more information, please contact the model's author.