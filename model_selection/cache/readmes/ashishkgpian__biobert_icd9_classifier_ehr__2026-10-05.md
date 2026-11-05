---
library_name: transformers
tags:
- biobert
- medical-nlp
- icd-9
- classification
- healthcare
license: apache-2.0
language:
- en
base_model:
- dmis-lab/biobert-v1.1
pipeline_tag: text-classification
---

# Model Card for BioBERT Fine-tuned on MIMIC-3 for ICD-9 Code Classification

## Model Details

### Model Description

This is a BioBERT model fine-tuned on the MIMIC-3 (Medical Information Mart for Intensive Care) corpus specifically for ICD-9 code classification. The model is designed to predict medical diagnostic codes based on Electronic Health Record (EHR) and symptom text inputs.

- **Developed by:** [Researcher/Institution Name - to be added]
- **Model type:** Transformer-based medical language model (BioBERT)
- **Language(s):** English (Medical Domain)
- **License:** [License to be specified]
- **Finetuned from model:** BioBERT base model

### Model Sources

- **Repository:** [GitHub/Model Repository Link - to be added]
- **Paper:** [Research Paper Link - to be added]

## Uses

### Direct Use

The primary use of this model is to automatically classify medical conditions by predicting relevant ICD-9 diagnostic codes from clinical text, such as electronic health records, medical notes, or symptom descriptions.

### Downstream Use

This model can be integrated into:
- Clinical decision support systems
- Medical coding automation
- Electronic health record (EHR) analysis tools
- Healthcare informatics research

### Out-of-Scope Use

- The model should not be used for direct medical diagnosis without professional medical oversight
- It is not intended to replace clinical judgment
- Performance may vary with text outside the medical domain or significantly different from the training corpus

## Bias, Risks, and Limitations

- The model's performance is limited to the medical conditions and coding patterns in the MIMIC-3 dataset
- Potential biases from the original training data may be present
- Accuracy can be affected by variations in medical terminology, writing styles, and complex medical cases

### Recommendations

- Validate model predictions with medical professionals
- Use as a supportive tool, not a replacement for expert medical assessment
- Regularly evaluate performance on new datasets
- Be aware of potential demographic or contextual biases in the predictions

## How to Get Started with the Model

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained('model_path')
tokenizer = AutoTokenizer.from_pretrained('model_path')

# Example prediction function (similar to the provided get_predictions function)
def predict_icd9_codes(input_text, threshold=0.8):
    # Tokenize input
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512, padding='max_length')
    
    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.sigmoid(outputs.logits)
        
    # Filter predictions above threshold
    predicted_codes = [model.config.id2label[i] for i in (predictions > threshold).nonzero()[:, 1]]
    
    return predicted_codes
```

## Training Details

### Training Data

- **Dataset:** MIMIC-3 Corpus
- **Domain:** Medical/Clinical text
- **Content:** Electronic Health Records (EHR)

### Training Procedure

#### Preprocessing
- Text tokenization
- Maximum sequence length: 512 tokens
- Padding to uniform length
- Potential text normalization techniques

#### Training Hyperparameters
- **Base Model:** BioBERT
- **Training Regime:** Fine-tuning
- **Precision:** [Specify training precision, e.g., mixed precision]

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data
- Held-out subset of MIMIC-3 corpus
- Diverse medical cases and documentation styles

#### Metrics
- Precision
- Recall
- F1-Score
- Multi-label classification metrics

## Environmental Impact

- Estimated carbon emissions to be calculated
- Compute details to be specified

## Technical Specifications

### Model Architecture
- **Base Model:** BioBERT
- **Task:** Multi-label ICD-9 Code Classification

## Citation

[Citation information to be added when research is published]

## More Information

For more details about the model's development, performance, and usage, please contact the model developers.