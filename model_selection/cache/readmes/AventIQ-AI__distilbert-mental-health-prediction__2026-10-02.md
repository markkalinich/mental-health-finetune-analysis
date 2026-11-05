# DistilBERT Base Uncased Quantized Model for Mental Health Prediction

This repository hosts a quantized version of the DistilBERT model, fine-tuned for mental health prediction tasks. The model has been optimized for efficient deployment while maintaining high accuracy, making it suitable for resource-constrained environments.

## Model Details

- **Model Architecture:** DistilBERT Base Uncased  
- **Task:** Mental Health Prediction  
- **Dataset:** Kaggle - Combined Data.csv  
- **Quantization:** Float16  
- **Fine-tuning Framework:** Hugging Face Transformers  

## Usage

### Installation

```sh
pip install transformers torch
```

### Loading the Model

```python
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch

model_name = "AventIQ-AI/distilbert-mental-health-prediction"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def predict_mental_health(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    inputs = {key: val.to(device) for key, val in inputs.items()}  # Move inputs to GPU/CPU

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

label_map = {
    0: "Anxiety",
    1: "Normal",
    2: "Depression",
    3: "Suicidal",
    4: "Stress",
    5: "Bipolar",
    6: "Personality disorder"
}

# ✅ Print Label Mapping
print("Label Mapping:", label_map)

test_statements = [
   "I am feeling great today!",
   "I want to kill myself because of this situation.",
   "My husband just blocked me and refuses to deal with my mental health.",
   "Nobody takes me seriously.",
   "I am feeling dizzy."
]

for text in test_statements:
    print(f"Text: {text}")
    print(f"Predicted Label: {predict_mental_health(text)}")
    print("-" * 50)
```

## Performance Metrics

- **Accuracy:** 0.56  
- **F1 Score:** 0.56  
- **Precision:** 0.68  
- **Recall:** 0.56  

## Fine-Tuning Details

### Dataset

The dataset is taken from Kaggle having combined information of mental health issues.

### Training

- Number of epochs: 3  
- Batch size: 8  
- Evaluation strategy: epoch  
- Learning rate: 2e-5  

### Quantization

Post-training quantization was applied using PyTorch's built-in quantization framework to reduce the model size and improve inference efficiency.

## Repository Structure

```
.
├── model/               # Contains the quantized model files
├── tokenizer_config/    # Tokenizer configuration and vocabulary files
├── model.safensors/     # Fine Tuned Model
├── README.md            # Model documentation
```

## Limitations

- The model may not generalize well to domains outside the fine-tuning dataset.  
- Quantization may result in minor accuracy degradation compared to full-precision models.  

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

