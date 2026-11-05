
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

model = AutoModelForTokenClassification.from_pretrained("sharanharsoor/pii-ner-model")
tokenizer = AutoTokenizer.from_pretrained("sharanharsoor/pii-ner-model")
```

## Training Data
The model was trained on the Gretel PII dataset with custom modifications.

## Performance
The model achieves:
- F1 Score: 0.9451
- Precision: 0.9401
- Recall: 0.9502
- Accuracy: 0.9952
        