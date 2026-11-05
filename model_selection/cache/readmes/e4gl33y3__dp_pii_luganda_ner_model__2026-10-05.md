
---
language: en
tags:
  - pii-detection
  - ner
  - luganda
  - differential-privacy
license: apache-2.0
datasets:
  - Conrad747/lg-ner
---

# dp_pii_luganda_ner_model

## Model Description
This is a fine-tuned token classification model based on `Conrad747/luganda-ner-v6` for detecting Personally Identifiable Information (PII) such as names, emails, phone numbers, and dates of birth. The model was trained with differential privacy (noise_multiplier=3.0, max_grad_norm=0.5, target_delta=1e-4) to ensure strong privacy guarantees, making it suitable for sensitive data applications.

## Intended Uses
- **Primary Use Case**: Identifying PII in text data, particularly for Luganda and English texts.
- **Supported Entities**: NAME, EMAIL, PHONE, DOB (adjust based on dataset labels).
- **Applications**: Data anonymization, compliance with privacy regulations (e.g., GDPR), secure text processing.

## How to Use
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import json

# Load model and tokenizer
model_name = "e4gl33y3/dp_pii_luganda_ner_model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Define classify_pii function
def classify_pii(text, model, tokenizer, device="cuda" if torch.cuda.is_available() else "cpu", max_length=128):
    model.to(device)
    model.eval()
    inputs = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=max_length,
        return_tensors="pt"
    ).to(device)
    
    # Use model's id2label for accurate label mapping
    label_map = model.config.id2label
    
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=2)[0].cpu().numpy()
    
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    word_ids = inputs.word_ids()
    previous_word_idx = None
    pii_entities = []
    current_entity = {"type": None, "value": [], "start": None}
    
    for idx, (token, pred, word_idx) in enumerate(zip(tokens, predictions, word_ids)):
        label = label_map.get(pred, "O")
        if word_idx is None or token in ["[CLS]", "[SEP]", "[PAD]"]:
            continue
        if label.startswith("B-"):
            if current_entity["type"] is not None:
                pii_entities.append({
                    "type": current_entity["type"],
                    "value": tokenizer.convert_tokens_to_string(current_entity["value"]).strip(),
                    "start": current_entity["start"]
                })
            current_entity = {"type": label[2:], "value": [token], "start": idx}
        elif label.startswith("I-") and current_entity["type"] == label[2:] and word_idx == previous_word_idx:
            current_entity["value"].append(token)
        else:
            if current_entity["type"] is not None:
                pii_entities.append({
                    "type": current_entity["type"],
                    "value": tokenizer.convert_tokens_to_string(current_entity["value"]).strip(),
                    "start": current_entity["start"]
                })
            current_entity = {"type": None, "value": [], "start": None}
        previous_word_idx = word_idx
    
    if current_entity["type"] is not None:
        pii_entities.append({
            "type": current_entity["type"],
            "value": tokenizer.convert_tokens_to_string(current_entity["value"]).strip(),
            "start": current_entity["start"]
        })
    
    return {"text": text, "entities": pii_entities}

# Example usage
text = "Ssemakula yategese ekivvulu okutalaaga ebitundu omuli Buddu ne Bulemeezi."
result = classify_pii(text, model, tokenizer)
print(json.dumps(result, indent=2))
```

## Training Details
- **Dataset**: Trained on `Conrad747/lg-ner` dataset.
- **Privacy**: Differential privacy applied with noise_multiplier=3.0, max_grad_norm=0.5, target_delta=1e-4.
- **Optimizer**: AdamW with learning rate 5e-5.
- **Epochs**: 5
- **Batch Size**: 8 (with BatchMemoryManager for memory efficiency).

## Evaluation
- **Precision**: 0.9445
- **Recall**: 0.9438
- **F1 Score**: 0.9436

## Limitations
- Optimized for Luganda and English PII detection; performance may vary for other languages.
- Differential privacy may introduce noise, potentially affecting accuracy for rare entities.
- Label mapping must match dataset labels for accurate inference.

## Contact
For issues or contributions, please visit the repository on Hugging Face or contact e4gl33y3.
