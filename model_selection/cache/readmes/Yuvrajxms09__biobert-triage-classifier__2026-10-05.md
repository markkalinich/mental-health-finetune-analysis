---
library_name: transformers
license: apache-2.0
datasets:
- myothiha/triage_dataset
language:
- en
base_model:
- dmis-lab/biobert-v1.1
---


# BioBERT Triage Classifier

## Model Description
This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.


- **Model type**: Sequence classification (urgent vs. non-urgent medical queries)
- **Language(s) (NLP)**: English
- **Finetuned from model**: [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1)

## Model Sources

- **Dataset**: [myothiha/triage_dataset](https://huggingface.co/datasets/myothiha/triage_dataset)

## Uses
### Direct Use
This model can be used to classify medical questions based on urgency, helping in medical triage and prioritization.

### Out-of-Scope Use
The model should not be used for final medical decision-making without human supervision.

## Recommendations
Users should be made aware of the risks, biases, and limitations of the model.

## How to Get Started with the Model
Use the code below to get started with the model:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("your_model_path")
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256)
    with torch.no_grad():
        logits = model(**inputs).logits
    return "urgent" if torch.argmax(logits) == 1 else "non-urgent"

# Example usage
print(predict("Patient has chest pain and difficulty breathing."))
```

## Training Details
### Training Data
- **Dataset**: [myothiha/triage_dataset](https://huggingface.co/datasets/myothiha/triage_dataset)

### Training Procedure
- **Training Hardware**: 2 GPUs
- **Batch Size**: 48
- **Learning Rate**: 6e-6
- **Epochs**: 6
- **Loss Function**: Weighted cross-entropy (to handle class imbalance)

### Training Hyperparameters
- **Optimizer**: AdamW
- **Gradient Accumulation Steps**: 3
- **Weight Decay**: 0.05
- **Mixed Precision**: Enabled (fp16)

## Evaluation

| Epoch | Training Loss | Validation Loss | Accuracy | Precision | Recall | F1 Score |
|-------|--------------|----------------|----------|-----------|--------|---------|
| 1     | No log       | 0.606408       | 0.681326 | 0.436587  | 0.656415 | 0.524395 |
| 2     | 0.639200     | 0.564773       | 0.706726 | 0.467656  | 0.692443 | 0.558271 |
| 3     | 0.639200     | 0.562810       | 0.718721 | 0.481095  | 0.648506 | 0.552395 |
| 4     | 0.551200     | 0.559481       | 0.701317 | 0.462286  | 0.710896 | 0.560249 |
| 5     | 0.522800     | 0.560782       | 0.710019 | 0.471334  | 0.686292 | 0.558855 |
| 6     | 0.522800     | 0.559855       | 0.705786 | 0.466978  | 0.702109 | 0.560899 |

## Summary
This fine-tuned BioBERT model helps classify medical questions by urgency. It can be used in **chatbots, triage systems, or AI-powered healthcare assistants** to improve response prioritization. 

Feel free to test it and integrate it into your applications!

