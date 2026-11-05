---
language: fa
tags:
- sentiment-analysis
- persian
- text-classification
license: apache-2.0
library_name: transformers
---

# مدل تحلیل احساسات فارسی

این مدل برای تشخیص احساسات متون فارسی آموزش داده شده است. این مدل می‌تواند احساسات را به سه دسته مثبت، منفی و خنثی طبقه‌بندی کند.

## جزئیات مدل

* **توسعه‌دهنده:** aiframe.org
* **نوع مدل:** `AutoModelForSequenceClassification` از کتابخانه `transformers`
* **توکن‌ساز:** `AutoTokenizer` از کتابخانه `transformers`
* **داده‌های آموزشی:** مجموعه داده‌های احساسی فارسی
* **معیار ارزیابی:** دقت (Accuracy)
* **دقت آموزشی:** 88.5%
* **سایر جزئیات:** تعداد شبکه‌های مصنوعی نیز دچار تغییرات و افزایش شده است.

## نحوه استفاده

برای استفاده از مدل، ابتدا باید کتابخانه‌های `transformers` نصب شده باشند. سپس می‌توانید مدل و توکن‌ساز را با استفاده از کدهای زیر بارگیری کنید:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
model = "frameai/PersianSentiment"
loaded_tokenizer = AutoTokenizer.from_pretrained(model)
loaded_model = AutoModelForSequenceClassification.from_pretrained(model)

def predict_sentiment(text):
    inputs = loaded_tokenizer(text, return_tensors="pt")
    outputs = loaded_model(**inputs)
    predictions = outputs.logits.argmax().item()

    if predictions == 0:
        sentiment = "negative"
    elif predictions == 1:
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return sentiment

while True:
    text_to_predict = input("Enter text for sentiment analysis: ")
    predicted_sentiment = predict_sentiment(text_to_predict)
    print(f"Input text: {text_to_predict}")
    print(f"Predicted sentiment: {predicted_sentiment}")