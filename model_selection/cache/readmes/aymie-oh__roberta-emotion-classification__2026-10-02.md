---
library_name: transformers
tags:
- emotion
- classification
- roberta
- multi-label
- sentiment-analysis
license: mit
language:
- en
pipeline_tag: text-classification
---

### Model Description

This is a finetuned roberta-base model aimed at identifying the strength of emotions for an input comment. 

### Downstream Use

Embeddings for comments can be extracted for downstream analyses

## Bias, Risks, and Limitations
Risks: If you are truly unsure of a paragraph/comment's sentiment, seek the advice of humans. This model shows some bias toward more widely represented training classes 

Caring is a somewhat confusing category. During training, comments that were annotated as "caring" if they included sympathetic content or indignace on behalf of others. This emotional category will need to be further separated into different categories such as "indignance" and "caring"

Sarcasm is treated as the combination of "amusement" and "disapproval" amusement can apply to irony and humorous tone, but largely applies to sarcasm... adding a specific class for sarcasm is a much needed improvement that will be pursued later down the line

not many risks... just MANY limitations. The training dataset was initially imbalanced, this was remedied with data augmentation and a weighted loss function... nontheless it struggles with sarcasm and sometimes unpredictable predictions because of dominating classes.

Ultimately, I hope some struggling grad or undergrad student can find this model useful for an arbitrary project they desire to prusue

## My use for the project can be found at the below github link

https://github.com/AnnaMarieHo/sentiment-analysis/tree/main

## How to Get Started with the Model


```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np

def predict_emotions(text, model_name, threshold=0.35):
    # Load model and tokenizer
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Tokenize and predict
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=250)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.sigmoid(logits).numpy()[0]
    
    # Map probabilities to emotions
    emotions = {emotion: float(prob) for emotion, prob in zip(model.config.id2label.values(), probabilities)}
    
    # Get emotions above threshold and sort by probability
    predicted_emotions = [(emotion, prob) for emotion, prob in emotions.items() if prob >= threshold]
    predicted_emotions.sort(key=lambda x: x[1], reverse=True)
    
    return {
        "text": text,
        "predicted_emotions": predicted_emotions,
        "all_probabilities": dict(sorted(emotions.items(), key=lambda x: x[1], reverse=True)),
        "threshold_used": threshold
    }

# Example usage
result = predict_emotions(
    "I'm feeling really excited and happy about this news!", 
    "model-name",
    threshold=0.35  # Customize threshold here
)

# Print results
print(f"Text: {result['text']}")
print("\nDetected emotions (sorted by probability):")
for emotion, prob in result['predicted_emotions']:
    print(f"  - {emotion.upper()} ({prob:.4f})")

print("\nAll emotion probabilities (sorted):")
for emotion, prob in result['all_probabilities'].items():
    print(f"  {'*' if prob >= result['threshold_used'] else ' '} {emotion}: {prob:.4f}")
```

#### Training Hyperparameters

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

#### Metrics

### Results

#### Summary


### Model Architecture and Objective