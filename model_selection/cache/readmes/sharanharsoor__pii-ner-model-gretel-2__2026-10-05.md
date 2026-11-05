# PII NER Model

This model is trained to detect Personal Identifiable Information (PII) in text. It can identify various types of PII including:
- Names (first and last)
- Email addresses
- Phone numbers
- Social Security Numbers (SSN)
- Credit card numbers
- Medical record numbers
- Employee IDs
- Addresses
- And more

## Usage
```python
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained('sharanharsoor/pii-ner-model-gretel-2')
tokenizer = AutoTokenizer.from_pretrained('sharanharsoor/pii-ner-model-gretel-2')
```

## Training Data
The model was trained on the Gretel PII dataset with custom modifications.

## Performance
The model achieves:
- F1 Score: 0.06810
- Precision: 0.0507
- Recall: 0.1033
- Accuracy: 0.6090
