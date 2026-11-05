---
language: en
tags:
- emotion-classification
- text-classification
- distilbert
datasets:
- dair-ai/emotion
metrics:
- accuracy
---

# Emotion Classification Model
## Model Description
This model fine-tunes DistilBERT for a multi-class emotion classification task. The dataset that is used is dair-ai/emotion containing six emotion classes: sadness, joy, love, anger, fear and suprise
## Training and Evaluation
- Training Dataset: dair-ai/emotion (16,000 examples)
- Validation Dataset: dair-ai/emotion (2,000 examples)
- Test Dataset: dair-ai/emotion (2,000 examples)
- Validation Accuracy: 96.6 %
- Test Accuracy: 93.2 %
- Training Time: 18,078.18s (5h 1m 18s)

## Hyperparameters
- Learning Rate: 5e-5
- Batch Size: 16
- Epochs: 4
- Weight Decay: 0.01

## Usage
```python
from transformers import pipeline
classifier = pipeline("text-classification",
model="your-username/emotion-classification-model")
text = "I’m so happy today!"
result = classifier(text)
print(result)
# Output: [{'label': 'LABEL_1', 'score': 0.9996680021286011}] ; which corresponds to 'joy' with a 99.9% accuracy
```

## Limitations

- Performance on Non-English Texts: The model works best with English texts. It may not handle other languages or regional dialects.
- Bias From Training Data: Reflects patterns from the training data, which may not cover all cases it could see. May lead to unfair predictns
- Issues with Sarcasm and Complex Language: Model might misinterpret sarcasm or subtle language, ex, "Great product... not!"
- No Confidence Scores: Model does not judge it's own output, so need some form of double check system, ie. yourself

## License 
The MIT License (MIT)
