---
library_name: transformers
tags: [afriberta, text-classification, igbo, sentiment-analysis, huggingface]
---

# Igbo Sentiment Analysis Model (AfriBERTa)

## Model Details

### Model Description
- **Model type:** Afro-centric BERT model for sequence classification  
- **Architecture:** `Davlan/naija-twitter-sentiment-afriberta-large`  
- **Task:** Text Classification (3-class sentiment analysis)  
- **Languages:** Primarily Igbo with multilingual capabilities  
- **Training data:** Igbo Twitter dataset (3,682 samples)  
- **Classes:** 
  - 0: [Interpret based on your labels - e.g., Positive]
  - 1: [e.g., Negative]
  - 2: [e.g., Neutral]

### Model Sources
- **Base Model:** [Naija Twitter Sentiment AfriBERTa](https://huggingface.co/Davlan/naija-twitter-sentiment-afriberta-large)
- **Fine-tuning Approach:** Transfer learning with Hugging Face Trainer

## Uses

### Direct Use
Sentiment analysis for Igbo text:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("path/to/igbo-sentiment-afriberta")
tokenizer = AutoTokenizer.from_pretrained("path/to/igbo-sentiment-afriberta")

text = "Your Igbo text here"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits).item()
```

### Downstream Tasks

    Social media sentiment monitoring

    Customer feedback analysis

    Content moderation for Igbo platforms

### Out-of-Scope Use

    Low-resource language processing without validation

    Legal or medical text analysis

### Training Details
#### Preprocessing

    Text cleaning: URLs, mentions, hashtags removal

    Emoji handling: Removal with emoji package

    Tokenization: AfriBERTa tokenizer (128 max length)

### Hyperparameters
Parameter	Value
Learning rate	2e-5
Batch size	16
Epochs	5
Weight decay	0.01
Warmup steps	500

### Training Configuration

    Framework: Hugging Face Trainer

    Hardware: Single GPU (Colab environment)

    Metrics: Accuracy and Weighted F1


### Overall Metrics:

    Accuracy: 0.80

    Macro Avg F1: 0.80

    Weighted Avg F1: 0.80
    
### Limitations

    Primarily optimized for Igbo Twitter data

    Performance may vary with informal text or dialects

    Class imbalance in training data 