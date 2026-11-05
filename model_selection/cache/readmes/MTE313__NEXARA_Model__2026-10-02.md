---
language:
- fa
license: mit
tags:
- sentiment-analysis
- text-classification
- parsbert
- pytorch
- transformers
- persian
datasets:
- MTE313/SnappFood_dataset_advanced
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text-classification
widget:
- text: "کیفیت غذا فوق‌العاده بود و ارسال بسیار سریع انجام شد."
- text: "غذا خیلی بد بود و سرد رسیده بود."
- text: "سفارش معمولی بود، چیز خاصی نداشت."
---

# NEXARA Sentiment Analysis Model (مدل تحلیل احساسات نکسارا)

مدل **NEXARA** یک مدل مبتنی بر ترنسفورمرها برای **تحلیل احساسات پنج کلاسه زبان فارسی** است. این مدل با استفاده از معماری **ParsBERT** (نسخه Base) بر روی دیتاست‌های تلفیقی رسمی و عامیانه فارسی Fine-Tune شده است.

## 🎯 ویژگی‌های مدل

- **زبان:** فارسی (Persian / Farsi)
- **پایه مدل:** ParsBERT (BERT-base-fa)
- **نوع مسئله:** دسته‌بندی متن (Text Classification / Sequence Classification)
- **تعداد کلاس‌ها:** ۵ کلاسه (از بسیار منفی تا بسیار مثبت)
- **حجم پارامترها:** کمتر از ۵۰۰ میلیون پارامتر

---

## 📊 دسته‌بندی کلاس‌ها (Labels Mapping)

خروجی مدل شامل ۵ کلاس عددی (بین ۰ تا ۴) است که با احساسات زیر متناظر هستند:

| برچسب عددی | امتیاز (Score) | احساس متناظر | توضیحات |
|:---:|:---:|:---:|:---|
| **0** | **-2** | 😡 بسیار منفی | نارضایتی شدید، انتقاد تند، تجربه خرید یا خدمات بسیار بد |
| **1** | **-1** | 😞 منفی | نارضایتی، تجربه منفی، بیان مشکلات معمولی |
| **2** | **0** | 😐 خنثی | بدون احساس خاص، بیان اطلاعات یا واقعیت‌های بدون جهت‌گیری |
| **3** | **+1** | 😊 مثبت | رضایت نسبی، تجربه خوب، تعریف معمولی |
| **4** | **+2** | 🤩 بسیار مثبت | رضایت شدید، تحسین زیاد، ابراز وفاداری به خدمات/محصول |

---

## 📦 داده‌های آموزشی (Training Data)

این مدل بر روی یک دیتاست ترکیبی بهینه با حجم **۱۸,۵۰۰ جمله** آموزش دیده است:
1. **ديتاست SentiPers (۱۵,۰۰۰ جمله):** شامل جملات رسمی‌تر و ساختاریافته به زبان فارسی با برچسب‌های ۵ کلاسه پیش‌فرض.
2. **دیتاست اسنپ‌فود (۳,۵۰۰ جمله گزینش‌شده):** نمونه‌های چالش‌برانگیز و عامیانه استخراج‌شده از نظرات کاربران اسنپ‌فود که به صورت دستی و دقیق در مقیاس ۵ کلاسه برچسب‌گذاری شده‌اند تا درک مدل از متون عامیانه افزایش یابد.

---

## 💻 راهنمای استفاده (Quick Start)

برای استفاده از این مدل در پایتون با کتابخانه `transformers` می‌توانید از کد زیر استفاده کنید:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# مسیر بارگذاری مدل از هاب hugging face
MODEL_NAME = "MTE313/NEXARA_model" 

# بارگذاری توکنایزر و مدل
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# تنظیم مدل در حالت ارزیابی
model.eval()

def predict_sentiment(text):
    # پیش‌پردازش و توکنایزر
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )
    
    # استنتاج
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
    predicted_class = torch.argmax(predictions, dim=-1).item()
    confidence = predictions[0][predicted_class].item()
    
    # نگاشت برچسب‌ها
    labels = {
        0: "😡 بسیار منفی (Very Negative)",
        1: "😞 منفی (Negative)",
        2: "😐 خنثی (Neutral)",
        3: "😊 مثبت (Positive)",
        4: "🤩 بسیار مثبت (Very Positive)"
    }
    
    return {
        "text": text,
        "label": labels[predicted_class],
        "score": predicted_class - 2, # تبدیل به مقیاس -2 تا +2
        "confidence": f"{confidence:.2%}"
    }

# تست نمونه‌ها
test_sentences = [
    "واقعا از خریدم راضی هستم، هم قیمت مناسب بود هم کیفیت عالی.",
    "غذا اصلا خوب نبود، کاملا سرد رسیده بود و طعم بدی داشت.",
    "یک کالا معمولی بود، ویژگی خاصی نداشت ولی کار راه اندازه."
]

for sentence in test_sentences:
    result = predict_sentiment(sentence)
    print(f"متن: {result['text']}")
    print(f"احساس: {result['label']} | امتیاز: {result['score']} | اطمینان: {result['confidence']}")
    print("-" * 50)
```

---

## 🛠️ فرآیند و تنظیمات آموزش (Training Procedure)

مدل با پارامترهای زیر بر روی دیتاست آموزشی Fine-Tune شده است:

- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Batch Size:** 8
- **Epochs:** 3
- **Warmup Steps:** 500
- **Weight Decay:** 0.01

---

## ⚠️ محدودیت‌ها و سوگیری‌ها (Limitations & Bias)

- مدل به شدت تحت تاثیر کیفیت متون ورودی است. در برخی جملات بسیار کوتاه عامیانه یا جملات دارای کنایه (Sarcasm)، ممکن است دقت مدل کاهش یابد.
- توصیه‌ می‌شود قبل از ارسال متن به مدل، فرآیند پیش‌پردازش ساده مانند نرمال‌سازی نویسه‌ها (ی و ک فارسی) را انجام دهید تا بهترین نتایج حاصل شود.

---

## 📄 مجوز و شرایط استفاده (License)

استفاده از این مدل برای مقاصد آموزشی، پژوهشی و کارهای غیرتجاری با ذکر منبع آزاد است. برای استفاده تجاری، لطفاً فایل مجوز مربوطه را مطالعه نمایید.

