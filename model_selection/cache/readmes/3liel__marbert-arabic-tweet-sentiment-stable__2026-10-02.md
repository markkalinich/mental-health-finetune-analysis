---
language: ar
license: apache-2.0
library_name: transformers
base_model: UBC-NLP/MARBERTv2
tags:
- sentiment-analysis
- arabic
- tweets
- text-classification
- marbert
- generated_from_trainer
datasets:
- mteb/tweet_sentiment_multilingual
- arbml/ArSAS
metrics:
- accuracy
- f1
model-index:
- name: marbert-arabic-tweet-sentiment-stable
  results:
  - task:
      type: text-classification
      name: Arabic Tweet Sentiment Classification
    dataset:
      type: mteb/tweet_sentiment_multilingual
      name: MTEB Arabic Tweet Sentiment (arabic subset)
      split: validation
    metrics:
    - type: accuracy
      value: 0.7685
    - type: f1
      value: 0.7613
      name: F1 (weighted)
---

# Arabic Tweet Sentiment Classifier

نموذج لتصنيف مشاعر التغريدات العربية إلى ثلاث فئات: سلبي، محايد، إيجابي. مبني على Fine-tuning لنموذج MARBERTv2.

النموذج منشور هنا: [3liel/marbert-arabic-tweet-sentiment-stable](https://huggingface.co/3liel/marbert-arabic-tweet-sentiment-stable)

## الاستخدام السريع

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="3liel/marbert-arabic-tweet-sentiment-stable")
result = classifier("الخدمة كانت ممتازة جدًا")
print(result)
# [{'label': 'Positive', 'score': ...}]
```

## النتائج السريعة

| Metric | القيمة |
|---|---|
| Accuracy | 76.85% |
| F1 (weighted) | 76.13% |
| Neutral Recall | **56%** ⚠️ |

> Neutral هي أضعف فئة عندنا — التفاصيل تحت في "تحليل أخطاء Neutral". السبب في تعريف البيانات نفسها، مش في التدريب.

## التشغيل

| الطريقة | الرابط / الأمر |
|---|---|
| كود التدريب الكامل | [`text-classification.ipynb`](./text-classification.ipynb) — اتدرب على Kaggle (T4 GPU)، والملف محتفظ بالـ outputs (الجداول، classification report، أمثلة Neutral الغلط) |
| تجربة الموديل على صفحته | [Model Page](https://huggingface.co/3liel/marbert-arabic-tweet-sentiment-stable) |
| تشغيل محلي | `python main.py --text "نصك هنا"` |
| واجهة Streamlit | `streamlit run app.py` |

## النتائج

| Metric | القيمة |
|---|---|
| Accuracy | 0.7685 |
| F1 (weighted) | 0.7613 |
| النموذج الأساسي | UBC-NLP/MARBERTv2 |
| عدد الفئات | 3 (Negative / Neutral / Positive) |

### بيانات التدريب

الموديل مدرّب على دمج داتاستين:
- [mteb/tweet_sentiment_multilingual](https://huggingface.co/datasets/mteb/tweet_sentiment_multilingual) (arabic subset) — 1,839 مثال.
- [ArSAS](https://huggingface.co/datasets/arbml/ArSAS) — بعد تنقية فئة Mixed وموازنة الفئات.

الحجم النهائي بعد الدمج والموازنة: 17,973 مثال. على الداتاست الأصلي وحده كان أقصى F1 اتوصله 0.74 بعد عدة تجارب على الـ hyperparameters. دمج ArSAS رفع الرقم لحوالي 0.76 — يعني المشكلة كانت في حجم البيانات مش في ضبط الإعدادات.

التقييم على validation split الأصلي بتاع `mteb/tweet_sentiment_multilingual` (324 مثال، 108 لكل فئة)، بعيد تمامًا عن بيانات الدمج، عشان الرقم يعكس الأداء على الدومين المستهدف (تويتات) مش على الخليط.

### الأداء لكل فئة (Classification Report)

الـ F1 العام بيخفي فرق حقيقي بين الفئات. فئة **Neutral** هي الأضعف بوضوح:

| الفئة | Precision | Recall | F1 |
|---|---|---|---|
| Negative | 0.81 | 0.91 | 0.86 |
| Neutral | 0.76 | **0.56** | **0.65** |
| Positive | 0.73 | 0.83 | 0.78 |

الـ confusion matrix بتوضح إن أكبر مصدر خطأ هو تصنيف تغريدات Neutral فعلية كـ Positive (31 من أصل 108). هدف التحسين القادم هو رفع Neutral recall من غير ما يقل الأداء العام — عن طريق مراجعة البيانات الأول (labels ممكن تكون غير دقيقة، أو نصوص محايدة بمشاعر ضمنية)، قبل اللجوء لحلول على مستوى الـ loss function زي class weighting.

الكود الكامل لتوليد الجدول ده موجود في `text-classification.ipynb` (خلية "Per-class evaluation").

### تحليل أخطاء Neutral: السبب بنيوي مش عيب في الموديل

مراجعة يدوية لـ 47 مثال Neutral مصنّف غلط كشفت نمطين رئيسيين:

1. **أخبار موضوعية بكلمات مشحونة** (الأغلبية): جمل زي "أبل تكسب معركة ضد سامسونغ" هي أخبار محايدة فعلًا، لكن كلمات زي "معركة" و"تكسب" بتدفع الموديل للتصنيف الإيجابي/السلبي رغم غياب أي رأي شخصي.
2. **سخرية وانتقاد سياسي ضمني**: جمل زي "يا سيسي صفي نيتك..." موسومة Neutral في الداتاست الأصلي، لكنها بتحمل موقف سلبي واضح لأي قارئ عربي — يعني بعض أخطاء الموديل هنا أقرب لكونها **خطأ في التوسيم الأصلي** مش خطأ في التصنيف.

**الخلاصة:** تعريف "Neutral" في الداتاست خالط بين نصين مختلفين: "مفيهوش رأي واضح" و"مفيهوش رأي حتى ضمني أو سياسي". ده تناقض في البيانات نفسها، مش هيتحل بضبط hyperparameters أو تغيير الـ loss function. الحل الحقيقي هو إعادة توسيم جزء من البيانات، أو فصل فئة "سخرية/انتقاد ضمني" لوحدها — وده شغل v2، مش قصور في التدريب اللي عملناه.

## هيكل المشروع

```
.
├── main.py                  # تحميل الموديل من الـ Hub وتشغيل inference
├── app.py                   # واجهة Streamlit
├── text-classification.ipynb  # كود التدريب (Kaggle، مع الـ outputs)
├── requirements.txt
└── README.md
```

## التثبيت والتشغيل محليًا

```bash
git clone https://huggingface.co/3liel/marbert-arabic-tweet-sentiment-stable
cd marbert-arabic-tweet-sentiment-stable
pip install -r requirements.txt

python main.py --text "الخدمة كانت ممتازة جدًا"
python main.py --interactive
```

## تفاصيل التدريب

- تنظيف النصوص: إزالة الروابط، الإشارات (@)، الهاشتاجات، وتكرار الأحرف الزائد.
- Tokenization بحد أقصى 128 توكن.
- الإعدادات: learning_rate=2e-5, weight_decay=0.01, hidden_dropout_prob=0.15, label_smoothing_factor=0.1.
- EarlyStoppingCallback لإيقاف التدريب عند توقف تحسن F1.
- اختيار أفضل checkpoint تلقائيًا عبر load_best_model_at_end=True.

## المؤلف

[3liel](https://huggingface.co/3liel)

## English

Fine-tuned [MARBERTv2](https://huggingface.co/UBC-NLP/MARBERTv2) for 3-class Arabic tweet sentiment classification (Negative / Neutral / Positive). Trained on a merge of [mteb/tweet_sentiment_multilingual](https://huggingface.co/datasets/mteb/tweet_sentiment_multilingual) (arabic subset) and [ArSAS](https://huggingface.co/datasets/arbml/ArSAS) — 17,973 examples after cleaning, deduplication, and balancing.

- **Accuracy:** 76.85% — **F1 (weighted):** 76.13%, evaluated on a held-out 324-example validation split.
- **Known weak spot:** Neutral recall is 56%, notably lower than Negative (91%) and Positive (83%). Manual review of misclassified examples traces this to two structural patterns in the source data: objective news headlines with emotionally charged vocabulary (e.g. "wins a battle"), and political sarcasm labeled Neutral despite carrying clear implicit sentiment. This is a data-labeling issue, not something a loss-function change (class weights, focal loss) would fix — see `text-classification.ipynb` for the full error analysis.
- Quick start and full training code above / in the repository files.
