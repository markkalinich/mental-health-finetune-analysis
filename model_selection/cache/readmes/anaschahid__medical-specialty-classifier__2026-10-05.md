
---
license: apache-2.0
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- medical
- classification
- biomedical
- pubmedbert
- healthcare
- medical-specialty
- imbalanced-data
- class-weights
- data-augmentation
language:
- en
metrics:
- accuracy
- f1
- recall
- precision
pipeline_tag: text-classification
---

# Fine-tuned BiomedNLP-PubMedBERT for Medical Specialty Classification (Class-Weighted with Data Augmentation)

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) for classifying medical text into different medical specialties. **This model uses class weights to handle imbalanced data and was trained on an augmented dataset**, ensuring better performance across all medical specialties, including rare ones.

## Model Description

This model classifies medical texts/posts into the following medical specialties:
`Cardiology`, `Dentistry`, `Dermatology`, `Endocrinology`, `Gastroenterology`, `Infectious Disease`, `Nephrology`, `Neurology`, `Ophthalmology`, `Orthopedics`, `Otorhinolaryngology`, `Pulmonology`, `Urology`

## Training Strategy for Imbalanced Data

### Data Augmentation
The training dataset was augmented using nlpaug via synonym replacement to improve model accuracy and decrease overfitting.

### Class Imbalance Handling
- **Balanced Class Weights**: Uses sklearn's 'balanced' weighting strategy with inverse frequency weighting
- **Weighted CrossEntropyLoss**: Rare medical specialties receive higher loss weights during training
- **Stratified Data Split**: Training/validation split maintains class distribution proportions
- **Weighted F1-Score**: Primary evaluation metric optimized for imbalanced datasets

### Class Weight Distribution
The following class weights were applied during training:
```
Cardiology: 1.4356
Dentistry: 4.0576
Dermatology: 1.1171
Endocrinology: 1.5485
Gastroenterology: 0.3864
Infectious Disease: 1.2777
Nephrology: 7.0353
Neurology: 1.0701
Ophthalmology: 1.6641
Orthopedics: 0.2808
Otorhinolaryngology: 0.9669
Pulmonology: 2.0021
Urology: 2.6795
```

## Training Details

- **Base Model**: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
- **Training Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 5e-06
- **Max Length**: 512 tokens
- **Warmup Steps**: 200
- **Scheduler**: Cosine learning rate scheduler
- **Loss Function**: Weighted CrossEntropyLoss with balanced class weights
- **Early Stopping**: Based on weighted F1-score with patience of 3

## Evaluation Results

### Overall Performance (Validation Set)
- **Accuracy**: 0.9288
- **F1 Score (Macro)**: 0.9189
- **F1 Score (Weighted)**: 0.9291
- **F1 Score (Micro)**: 0.9288
- **Precision (Macro)**: 0.9151
- **Precision (Weighted)**: 0.9299
- **Precision (Micro)**: 0.9288
- **Recall (Macro)**: 0.9233
- **Recall (Weighted)**: 0.9288
- **Recall (Micro)**: 0.9288

### Key Performance Highlights
- **0.9288 Overall Accuracy** - Strong performance across all medical specialties
- **0.9291 Weighted F1-Score** - Excellent balance of precision and recall
- **0.9189 Macro F1-Score** - Good performance even for minority classes
- **Class-balanced training** ensures reliable predictions for rare specialties
- **Data augmentation** improves model robustness and generalization

### Class Balance Benefits
- **Improved Minority Class Performance**: Class weights significantly improve recall for underrepresented specialties
- **Reduced Bias**: Model is less biased toward frequently occurring medical specialties  
- **Better Clinical Utility**: More reliable predictions across all medical domains
- **Enhanced Robustness**: Data augmentation provides better handling of diverse medical text patterns

## Training Visualizations

### Confusion Matrix
The following confusion matrices show the model's classification performance across all medical specialties:

![Confusion Matrix - Raw Counts](https://cdn-uploads.huggingface.co/production/uploads/652e97d7960038a070460263/P3wXa91GDZeu-RHWhKyo0.png)

*Confusion matrix showing raw prediction counts and percentages for each medical specialty*

![Confusion Matrix - Normalized](https://cdn-uploads.huggingface.co/production/uploads/652e97d7960038a070460263/sWEuCXADzWJs6CE-rjUft.png)

*Normalized confusion matrix showing prediction accuracy rates by true class*

### Training History
Training progress and performance metrics throughout the fine-tuning process:

![Training History - Loss](https://cdn-uploads.huggingface.co/production/uploads/652e97d7960038a070460263/bpA-wQkuQ06iC1GHxtCdL.png)

*Training and validation loss curves showing model convergence*

![Training History - Validation Accuracy](https://cdn-uploads.huggingface.co/production/uploads/652e97d7960038a070460263/4wd_rsjlC7eZdvyRVgWQ1.png)

![Training History - F1-Score Progress](https://cdn-uploads.huggingface.co/production/uploads/652e97d7960038a070460263/h8pcKWL4WYxIG5cGAaqg9.png)

*Accuracy and F1-score progression during training*


## Usage

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained("anaschahid/medical-specialty-classifier")
tokenizer = BertTokenizer.from_pretrained("anaschahid/medical-specialty-classifier")

# Example usage
def classify_medical_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
    predicted_specialty = model.config.id2label[predicted_class_id]

    return predicted_specialty

# Example
text = "patient has a broken leg from a fall"
specialty = classify_medical_text(text)
print(f"Predicted specialty: {specialty}")
```

## Model Performance Analysis

### Strengths
- **High Overall Accuracy (0.93%)**: Demonstrates strong classification capability
- **Balanced Performance**: Weighted F1-score (0.93%) shows good handling of class imbalance
- **Consistent Metrics**: Macro F1 (0.92%) indicates good performance across all classes
- **Data Augmentation Benefits**: Enhanced training data improves model robustness and generalization
- **Class-Weighted Training**: Ensures fair performance across all medical specialties

## Intended Use

This model is intended for research and educational purposes in the medical domain. It should not be used for actual medical diagnosis or treatment decisions.

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{fine-tuned-biomedbert-medical-specialty-augmented,
  title={Fine-tuned BiomedNLP-PubMedBERT for Medical Specialty Classification with Data Augmentation},
  author={Anas Chahid},
  year={2025},
  howpublished={\url{https://huggingface.co/anaschahid/medical-specialty-classifier}},
  note={Medical specialty classification with augmented training data and class weights}
}
```
