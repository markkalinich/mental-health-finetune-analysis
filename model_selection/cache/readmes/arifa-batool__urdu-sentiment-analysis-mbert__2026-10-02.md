---
license: apache-2.0
tags:
- text-classification
- bert
- mbert
- urdu
- sentiment-analysis
- transformers
pipeline_tag: text-classification
datasets:
- umar178/UrduMultiDomainClassification
---

# Urdu Sentiment Analysis using Multilingual BERT

This model is a fine-tuned Multilingual BERT (mBERT) for Urdu sentiment classification. It classifies Urdu text into three categories: Positive, Negative, and Neutral.


## Task

Urdu Text Classification for Sentiment Analysis

## Model Description

- Base Model: bert-base-multilingual-cased  
- Architecture: Transformer (BERT)  
- Task: Sentiment Classification  
- Language: Urdu  
- Framework: Hugging Face Transformers  

This model is optimized for low-resource Urdu NLP using transfer learning from a pretrained multilingual transformer.


## Dataset

This model was trained using a publicly available Urdu sentiment dataset from Hugging Face:

https://huggingface.co/datasets/umar178/UrduMultiDomainClassification

### Dataset Description

The dataset contains Urdu text samples annotated for sentiment analysis tasks.  
It was used to fine-tune the multilingual BERT model for classification into:

- Positive  
- Negative  
- Neutral  

This dataset is suitable for low-resource NLP research in Urdu language understanding.

## Training Pipeline

Raw Urdu Text → Tokenization → mBERT Encoder → Classification Head → Sentiment Output  


Here is an example of how you can run this model:

```python
from transformers import pipeline

model_name = "arifa-batool/urdu-sentiment-analysis-mbert"

classifier = pipeline(
    "text-classification",
    model=model_name,
    tokenizer=model_name
)

text = "یہ فلم بہت اچھی تھی"
result = classifier(text)

print(result)
```

<br>

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "arifa-batool/urdu-sentiment-analysis-mbert"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "یہ بہت بری خبر ہے"

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)

probs = torch.softmax(outputs.logits, dim=1)

pred_id = torch.argmax(probs, dim=1).item()
confidence = torch.max(probs).item()

label = model.config.id2label[pred_id]

print(label, confidence)
```


## Evaluation Results

- Accuracy: 0.91  
- F1 Score: 0.91  
- Balanced performance across all sentiment classes  


## Deployment

Available via:
- Hugging Face Model Hub
- Hugging Face Spaces (Gradio App)
- Transformers API  



## Future Improvements

- Multi-domain Urdu dataset expansion  
- Integration with larger models (XLM-R, DeBERTa)  
- Social media sentiment optimization  

## Author

Syeda Arifa Batool | AI/ML Engineer 

## Live Demo

You can try the model here:

https://huggingface.co/spaces/arifa-batool/urdu-sentiment-classifier