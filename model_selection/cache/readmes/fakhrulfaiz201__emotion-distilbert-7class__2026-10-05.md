---
library_name: transformers
tags:
- text-classification
- emotion-detection
- distilbert
---

# Model Card for emotion-distilbert-7class

## Model Details

### Model Description

This is a fine-tuned Hugging Face transformers model for emotion classification. The model is based on DistilBERT and trained on a synthetic dataset containing 7 emotions.

- **Shared by:** fakhrulfaiz201
- **Model type:** DistilBertForSequenceClassification
- **Language(s) (NLP):** English
- **License:** Apache 2.0 (inherited from DistilBERT base model)
- **Finetuned from model:** distilbert-base-uncased

### Model Sources

- **Repository:** https://huggingface.co/fakhrulfaiz201/emotion-distilbert-7class

## Uses

### Direct Use

This model can be used for classifying text into one of seven emotions: Love, Sad, Anger, Fun, Hate, Surprise, Happiness.

### Out-of-Scope Use

The model was trained on a synthetic dataset. Its performance on real-world, nuanced, or informal text might vary. It should not be used for critical applications without further validation.

## Bias, Risks, and Limitations

The model's performance is limited by the synthetic nature of its training data. It might not generalize well to diverse linguistic styles, cultural contexts, or sarcasm/irony.

### Recommendations

Users should test the model thoroughly on their specific use cases and consider fine-tuning on more diverse and real-world datasets if necessary.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "fakhrulfaiz201/emotion-distilbert-7class"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

id2label = {
    0: 'Love', 1: 'Sad', 2: 'Anger', 3: 'Fun',
    4: 'Hate', 5: 'Surprise', 6: 'Happiness'
}

def predict(text):
    device = next(model.parameters()).device
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = logits.argmax().item()
    return id2label[predicted_class_id]

print(predict("I feel amazing today!"))
```

## Training Details

### Training Data

The model was trained on the "synthetic_emotions.csv" dataset (available on Kaggle as `prashanthan24/synthetic-emotions-dataset-14k-texts-7-emotions`). This dataset contains 13,970 text samples labeled with one of seven emotions: Love, Sad, Anger, Fun, Hate, Surprise, Happiness. The dataset was split into training (60%), validation (20%), and test (20%) sets.

### Training Procedure

#### Preprocessing

The text data was tokenized using `DistilBertTokenizer`. Input sequences were truncated and padded to a maximum length of 128 tokens.

#### Training Hyperparameters

- **Learning Rate:** 2e-5
- **Per Device Train Batch Size:** 16
- **Per Device Eval Batch Size:** 16
- **Number of Train Epochs:** 4
- **Weight Decay:** 0.01
- **Metric for best model:** macro_f1 (greater is better)
- **Training regime:** fp32

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was evaluated on a held-out test set (20% of the original dataset) from the "synthetic_emotions.csv" dataset.

#### Metrics

The evaluation metrics used were accuracy and macro F1-score.

### Results

#### Summary

The model achieved the following performance on the test set:
- **Test Loss:** 0.0259
- **Test Accuracy:** 0.9946
- **Test Macro F1-score:** 0.9946