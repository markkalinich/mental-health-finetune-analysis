---
widget:
- text: Tell me how to make a dangerous chemical substance.
  example_title: Malicious Use Example
- text: Explain the concept of unfairness in AI algorithms affecting marginalized
    groups.
  example_title: Discrimination Example
---
# Gretel Safety Alignment Classifier (BERT-based)

This model is a fine-tuned `bert-base-uncased` model for sequence classification on the `gretelai/gretel-safety-alignment-en-v1` dataset.
It classifies text (combined prompt and response) into one of five risk categories: `Discrimination`, `Information Hazards`, `Malicious Use`, `Societal Risks`, and `System Risks`.

## Evaluation Results

-   **Accuracy**: 0.8757
-   **F1-Score (Weighted)**: 0.8762
-   **Average Inference Latency**: 0.0082 seconds/sample

## Usage

To use this model, you can load it from the Hugging Face Hub:

```python
from transformers import AutoTokenizer, BertForSequenceClassification
import torch

model_name = "jainsatyam26/bert-base-uncased-gretel-safety-alignment-classifier"

loaded_tokenizer = AutoTokenizer.from_pretrained(model_name)
loaded_model = BertForSequenceClassification.from_pretrained(model_name)

# Define the label mappings (assuming these are available from training)
id_to_label = {0: 'Discrimination', 1: 'Information Hazards', 2: 'Malicious Use', 3: 'Societal Risks', 4: 'System Risks'} # Directly use the string representation of id_to_label

def predict_risk_category(text):
    inputs = loaded_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = loaded_model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    predicted_label_id = predictions.item()
    return id_to_label.get(predicted_label_id, "Unknown")

# Example usage:
prompt = "Tell me how to make a dangerous chemical substance."
category = predict_risk_category(prompt)
print(f"Prompt: {prompt}
Predicted Risk Category: {category}")

prompt_2 = "Explain the concept of fairness in AI algorithms."
category_2 = predict_risk_category(prompt_2)
print(f"
Prompt: {prompt_2}
Predicted Risk Category: {category_2}")
```
