---
language: id
license: apache-2.0
tags:
- sentiment-analysis
- indonesian
model_creator: agufsamudra
model_type: bert
pipeline_tag: text-classification
base_model:
- indobenchmark/indobert-base-p1
---



# Model Card for IndoBERT Sentiment Analysis  

This model is fine-tuned from **`indobenchmark/indobert-base-p1`** for binary sentiment classification (Positive/Negative) on Indonesian text.  

## Model Details  

### Model Description  
- **Developed by:** agufsamudra
- **Model type:** Text Classification  
- **Language(s):** Indonesian (id)  
- **License:** Apache-2.0  
- **Fine-tuned from model:** [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1)  

### Model Sources  
- **Repository:** https://huggingface.co/agufsamudra/indo-sentiment-analysis

## Uses  

### Direct Use  
This model is intended for binary sentiment classification tasks in Indonesian language texts. It predicts whether a given text expresses positive or negative sentiment.  

### Out-of-Scope Use  
The model is not designed to classify neutral sentiments or handle languages other than Indonesian.  

## Bias, Risks, and Limitations  
- **Bias:** The model's performance is reliant on the quality and diversity of the training data. Biases in the dataset may influence predictions.  
- **Limitations:** The model is limited to binary sentiment analysis and may not perform well on ambiguous or mixed-sentiment texts.  

### Recommendations  
Users should validate predictions on a case-by-case basis for high-stakes applications.  

## How to Get Started with the Model  

```python  
from transformers import BertTokenizer, BertForSequenceClassification  

# Load the tokenizer and model  
tokenizer = BertTokenizer.from_pretrained("agufsamudra/indo-sentiment-analysis")  
model = BertForSequenceClassification.from_pretrained("agufsamudra/indo-sentiment-analysis")  

# Example usage  
text = "Saya sangat puas dengan pelayanan ini!"  
inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)  
outputs = model(**inputs)  
logits = outputs.logits  
prediction = logits.argmax(-1).item()  

label = "Positive" if prediction == 1 else "Negative"  
print(f"Sentiment: {label}")  
```  

## Training Details  

### Training Data  
The model was trained on a dataset of Indonesian text reviews from Play Store applications. The dataset was labeled for binary sentiment analysis (Positive and Negative). It contains an equal distribution of positive and negative examples to ensure balanced learning.
### Training Procedure  

#### Training Hyperparameters  
- **Optimizer:** AdamW  
- **Learning Rate:** 3e-6  
- **Epochs:** 3  
- **Max Sequence Length:** 128 tokens  

## Evaluation  

### Testing Data  
The model was evaluated on a separate test dataset of 20,000 samples (10,000 Positive, 10,000 Negative).  

### Metrics  
The model's performance was evaluated using standard metrics, including accuracy, precision, recall, and F1-score.  

### Results  

| Metric         | Training Set | Testing Set |  
|----------------|--------------|-------------|  
| Accuracy       | 95.28%       | 95.56%      |  
| Precision      | 96%          | 96%         |  
| Recall         | 96%          | 96%         |  
| F1-Score       | 96%          | 96%         |  

## Technical Specifications  

### Model Architecture and Objective  
The model is based on IndoBERT, a pre-trained transformer model tailored for Indonesian text. It was fine-tuned for binary classification tasks.  

### Compute Infrastructure  
- **Hardware:** Google Collab GPU
- **Software:** Python, PyTorch, Transformers library