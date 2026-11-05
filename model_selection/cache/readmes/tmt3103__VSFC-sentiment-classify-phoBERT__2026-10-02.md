---
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - vietnamese
  - vsfc
  - phobert
language:
  - vi
datasets:
  - uit-vsfc
model-index:
  - name: VSFC Sentiment Classifier (PhoBERT)
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: UIT-VSFC
          type: uit-vsfc
        metrics:
          - type: accuracy
            value: 94.4409
          - type: f1
            value: 94.1200
---

# VSFC Sentiment Classifier using PhoBERT

This model is fine-tuned from [`vinai/phobert-base`](https://huggingface.co/vinai/phobert-base) on the UIT-VSFC dataset for Vietnamese sentiment analysis.

## 🧠 Model Details

- **Model type**: Transformer (BERT-based)
- **Base model**: [`vinai/phobert-base`](https://huggingface.co/vinai/phobert-base)
- **Fine-tuned task**: Sentence-level sentiment classification
- **Target labels**: Positive, Negative, Neutral
- **Tokenizer**: SentencePiece BPE

## 📚 Training Data

- **Dataset**: [UIT-VSFC](https://drive.google.com/drive/folders/1xclbjHHK58zk2X6iqbvMPS2rcy9y9E0X)
- **Language**: Vietnamese
- **License**: Academic use
- Students’ feedback is a vital resource for the interdisciplinary research involving the combining of two different research fields between sentiment analysis and education..

## 🚀 How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("tmt3103/VSFC-sentiment-classify-phoBERT")
model = AutoModelForSequenceClassification.from_pretrained("tmt3103/VSFC-sentiment-classify-phoBERT")

inputs = tokenizer("Giảng viên thân thiện dễ thương", return_tensors="pt")
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(dim=-1).item()
