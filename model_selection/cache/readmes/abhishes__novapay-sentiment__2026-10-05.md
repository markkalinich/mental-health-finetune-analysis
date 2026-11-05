
---
  license: apache-2.0
  tags: 
    - text-classification
    - sentiment-analysis
    - nova-pay
  datasets:
    - imdb
  metrics:
    - accuracy
    - f1
---
# Novapay Sentiment Classifier (DistilBERT)

## Intended Use 
Fine Tuned for sentiment classification of NovaPay Customer Support Messages.
This is a proof-of-concept model trained on IMDB Dataset

## Training Data
- **DataSet**: IMDB
- **BaseModel**: distilbert/distilbert-base-uncased
- **Epochs**: 2
- **Learning Rate: **  2e-5

## Evaluation Results
- **Accuracy: ** 0.9142
- **F1 Score: ** 0.9154

##Limitations
- Trained on IMDB Movie Review not on actual customer support messages
- May not generalize well to financial support domain 
- POC Only Not for produciton use


