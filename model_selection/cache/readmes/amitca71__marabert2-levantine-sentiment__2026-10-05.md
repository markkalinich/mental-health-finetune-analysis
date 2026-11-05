---
language: ar
tags:
- text-classification
- sentiment-analysis
- levantine
- arabic
- marbert
- ordinal-classification
metrics:
- accuracy
- f1_macro
model-index:
- name: Levantine Sentiment Classifier (Ordinal)
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: ArSenTD-LEV
      type: amitca71/marabert2-levantine-sentiment-model-dataset
    metrics:
    - type: accuracy
      value: 79.25%
    - type: f1_macro
      value: 0.7635
---

# 🎭 Levantine Arabic Sentiment Classifier (Ordinal MARBERTv2)

This model is a fine-tuned version of **MARBERTv2**, designed to predict the sentiment of Levantine Arabic tweets (Jordanian, Lebanese, Palestinian, Syrian).

**Technical Highlight:** This model was trained using an **Ordinal Loss Function** (Mean Squared Error combined with Cross-Entropy). This makes the model "distance-aware," meaning it heavily penalizes extreme mistakes (like confusing a highly positive tweet for a highly negative one). This makes its predictions far more reliable in edge cases!

## 📊 Performance
| Metric | Score | Description |
| :--- | :--- | :--- |
| **Accuracy** | **79.25%** | Overall correctness on the test set. |
| **F1 (Macro)** | **0.7635** | The balanced F1 score across all 3 classes. |

## 📖 Labels
| ID | Label | Meaning |
| :--- | :--- | :--- |
| **0** | **Negative 😠** | Anger, complaints, sadness, or frustration. |
| **1** | **Neutral 😐** | Objective facts, mixed emotions, or ambiguous statements. |
| **2** | **Positive 😃** | Joy, praise, excitement, or satisfaction. |

## 🚀 How to Use (Python)

Because this is a standard 3-class model, you can easily load it using Hugging Face's built-in `pipeline`.


```python
from transformers import pipeline

# 1. Load Pipeline
model_id = "amitca71/marabert2-levantine-sentiment"
classifier = pipeline("text-classification", model=model_id)

def predict_sentiment(text):
    # Get the top prediction
    result = classifier(text)[0]

    # Format the output cleanly
    return {"text": text, "label": result['label'], "confidence": round(result['score'], 4)}

# 2. Test Examples
print(predict_sentiment("الجو اليوم بيعقد! طالعين مشوار"))            # Should be Positive
print(predict_sentiment("والله طقت روحي من هالزحمة، شي بيقرف"))        # Should be Negative
print(predict_sentiment("وصلت عالبيت من شوي."))                       # Should be Neutral
```

## ⚠️ Limitations
* **Dialect Focus:** Optimized heavily for Levantine Twitter. It may underperform or misunderstand idioms in Egyptian, Gulf, or Maghrebi dialects.
* **The "Neutral" Bottleneck:** Like most sentiment models, detecting true "Neutral" text is the most challenging, as human annotators often mix objective facts with subtle sarcasm in this category.
* **Arabizi:** While MARBERTv2 has some exposure to Arabizi (Arabic written in English/Latin letters), this model performs best on native Arabic script.
