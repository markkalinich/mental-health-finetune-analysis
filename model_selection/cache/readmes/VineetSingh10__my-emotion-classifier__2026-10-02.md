---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- emotion
- pytorch
- transformers
library_name: transformers
pipeline_tag: text-classification
datasets:
- emotion
metrics:
- accuracy
- f1
model-index:
- name: my-emotion-classifier
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
    metrics:
    - type: accuracy
      value: 0.92
      name: Accuracy
    - type: f1
      value: 0.91
      name: F1 Score
---

# My Emotion Classifier 🎭

This is a fine-tuned DistilBERT model for emotion classification. It can classify text into 6 different emotions:
- 😢 Sadness
- 😊 Joy
- ❤️ Love
- 😠 Anger
- 😨 Fear
- 😲 Surprise

## Model Description

**Base Model:** `distilbert-base-uncased`  
**Fine-tuned on:** [emotion dataset](https://huggingface.co/datasets/emotion)  
**Task:** Multi-class text classification  
**Language:** English

## Training Details

- **Training epochs:** 3
- **Batch size:** 16
- **Learning rate:** 2e-5
- **Optimizer:** AdamW
- **Max sequence length:** 128

## Performance

The model achieves approximately:
- **Accuracy:** ~92%
- **F1 Score:** ~91%

## Usage

### Using Transformers Pipeline

```python
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="YOUR_USERNAME/my-emotion-classifier")

# Make predictions
text = "I love this so much! Best day ever!"
result = classifier(text)
print(result)
# [{'label': 'joy', 'score': 0.95}]
```

### Using AutoModel

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("YOUR_USERNAME/my-emotion-classifier")
model = AutoModelForSequenceClassification.from_pretrained("YOUR_USERNAME/my-emotion-classifier")

# Tokenize and predict
text = "This makes me so angry!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
predicted_class = torch.argmax(predictions, dim=-1).item()

print(f"Predicted emotion: {model.config.id2label[predicted_class]}")
```

### Using the Hugging Face CLI

```bash
# Install the transformers library
pip install transformers

# Use the model in Python
python -c "from transformers import pipeline; classifier = pipeline('text-classification', model='YOUR_USERNAME/my-emotion-classifier'); print(classifier('I am so happy!'))"
```

## Example Predictions

| Text | Predicted Emotion | Confidence |
|------|-------------------|------------|
| "I love this so much!" | joy | 0.95 |
| "This is terrible!" | anger | 0.88 |
| "I'm really scared" | fear | 0.92 |
| "What a surprise!" | surprise | 0.86 |

## Limitations

- The model is trained on English text only
- Best performance on short texts (tweets, reviews, comments)
- May struggle with sarcasm or mixed emotions
- Limited to 6 emotion categories

## Training Data

The model was fine-tuned on the [emotion dataset](https://huggingface.co/datasets/emotion) which contains:
- 16,000 training examples
- 2,000 validation examples  
- 2,000 test examples

## Ethical Considerations

This model should not be used for:
- Medical or psychological diagnosis
- Making critical decisions about individuals
- Surveillance or monitoring without consent

## Citation

If you use this model, please cite:

```bibtex
@misc{my-emotion-classifier,
  author = {Your Name},
  title = {My Emotion Classifier},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/YOUR_USERNAME/my-emotion-classifier}}
}
```

## Contact

For questions or feedback, please open an issue on the model's Hugging Face page.
