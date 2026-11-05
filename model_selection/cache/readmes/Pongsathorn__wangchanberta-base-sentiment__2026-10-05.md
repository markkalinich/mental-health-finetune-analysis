---
tags:
- wangchanberta
- sentiment-analysis
- thai
- simpletransformers
---

# WangchanBERTa Base for Sentiment Analysis

This is a fine-tuned version of the [WangchanBERTa](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) model, trained for **sentiment analysis** in Thai language using `simpletransformers`.

## Model Details

- **Model Name**: WangchanBERTa Base Sentiment Analysis
- **Pretrained Base Model**: `airesearch/wangchanberta-base-att-spm-uncased`
- **Architecture**: CamemBERT
- **Language**: Thai
- **Task**: Sentiment Classification

## Training Configuration

- **Training Dataset**: (e.g., your dataset name or a public dataset if applicable)
- **Number of Training Epochs**: 6
- **Train Batch Size**: 16
- **Eval Batch Size**: 32
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Scheduler**: Cosine
- **Gradient Accumulation Steps**: 2
- **Seed**: 42
- **Training Framework**: `simpletransformers`
- **FP16**: Disabled

## Model Performance

Provide any performance metrics here, such as accuracy, F1-score, etc., depending on your dataset.

## Usage

To use this model, you can load it as follows:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import numpy as np
from pythainlp.tokenize import word_tokenize

tokenizer = AutoTokenizer.from_pretrained("Pongsathorn/wangchanberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("Pongsathorn/wangchanberta-base-sentiment")

id2label = {
    0: "pos", 
    1: "neu", 
    2: "neg",  
}

input_text = "พนักงานบริการดีมาก สัญญาณก็ดี แต่ร้านอยู่ที่ไหน อยากได้ข้อมูลเพิ่มเติม จะได้ประกาศบนเว็บถูก"  

segmented_text = word_tokenize(input_text, engine="longest")

preprocessed_text = " ".join(segmented_text)

inputs = tokenizer(preprocessed_text, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

probs = F.softmax(logits, dim=-1)

predicted_class = torch.argmax(probs, dim=-1).item()

predicted_label = id2label[predicted_class]

print("Predicted Label (ID):", predicted_class)
print("Predicted Label (Description):", predicted_label)
max_prob = np.max(probs.numpy())
print(f"Maximum Probability: {max_prob:.4f}")
