---
tags:  
- text-classification  
- sentiment-analysis  
- imdb  
- distilbert  

---

# 📢 DistilBERT Fine-Tuned for Sentiment Analysis 🎭  

This model is a **fine-tuned DistilBERT** for **sentiment analysis** on movie review texts. It classifies texts as **positive** or **negative** with high accuracy.  

## 📖 Dataset  

The model was trained on the [IMDb](https://huggingface.co/datasets/imdb) dataset, which contains **50,000 movie reviews** balanced between positive and negative labels.  

## 📊 Evaluation  

The model's performance was evaluated on a test set of **25,000 reviews**, achieving the following results:  

| Metric         | Value |
|---------------|-------|
| **Accuracy**  | 93.2% |
| **Precision** | 93%   |
| **Recall**    | 93%   |
| **F1-score**  | 93%   |

These metrics indicate that the model correctly predicts movie reviews in most cases.  

## 📊 Confusion Matrix  

The confusion matrix below shows the model's performance on predictions:  

![Confusion Matrix](https://huggingface.co/gabrielnkl/fine-tuned-bert/resolve/main/matriz_confusao.png)  

## 🚀 How to Use  

To use the model, simply load it with `transformers` and use the text classification pipeline:  

```python
from transformers import pipeline

model_name = "gabrielnkl/fine-tuned-bert"

classifier = pipeline("text-classification", model=model_name)

text = "This movie was amazing! I really liked the acting and the storyline."
result = classifier(text)

print(result)
# [{'label': 'POSITIVE', 'score': 0.98}]


O notebook usado para treinar este modelo está disponível no GitHub:

(https://github.com/Gabrielnkl/fine-tuned-bert-model/blob/main/finetuning.py)


