---
language: en
datasets:
- glue
metrics:
- accuracy
model-name: bert-base-uncased-finetuned-sst2
tags:
- text-classification
- sentiment-analysis
---

# BERT Base (uncased) fine-tuned on SST-2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the **GLUE SST-2** dataset for sentiment classification (positive vs. negative).  

## Model Details
- **Model type**: BERT (base, uncased)  
- **Fine-tuned on**: SST-2 (Stanford Sentiment Treebank)  
- **Labels**:  
  - 0 → Negative  
  - 1 → Positive  
- **Training framework**: [🤗 Transformers](https://github.com/huggingface/transformers)  

## Training
- Epochs: 2  
- Batch size: 4 (with gradient accumulation steps = 4)  
- Learning rate: 3e-5  
- Mixed precision: fp16  
- Optimizer & Scheduler: Default Hugging Face Trainer  

## Evaluation Results
On the SST-2 validation set:  

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|---------------|-----------------|----------|
| 1     | 0.1761        | 0.2282          | 93.0%    |
| 2     | 0.1127        | 0.2701          | 93.1%    |

Final averaged training loss: **0.1663**  

## How to Use
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "ByteMeHarder-404/bert-base-uncased-finetuned-sst2"
tok = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

inputs = tok("I love Hugging Face!", return_tensors="pt")
outputs = model(**inputs)
pred = outputs.logits.argmax(dim=-1).item()
print("Label:", pred)  # 1 = Positive
