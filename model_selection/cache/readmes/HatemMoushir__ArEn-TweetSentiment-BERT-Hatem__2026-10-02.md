---
language: [ar, en]
license: mit
tags:
  - sentiment-analysis
  - text-classification
  - twitter
  - arabic
  - english
  - multilingual
  - social-media
  - bert
  - bert-base-multilingual-cased
  - UCI Sentiment Dataset
  - Egypt
  - Ain shams university
  - Hatem Moushir
  
datasets:
  - m88gg52wp7
  - stanfordnlp/sentiment140
model-index:
  - name: ArEn-TweetSentiment-BERT
    results: []
---

# ArEn-TweetSentiment-BERT-Hatem

`ArEn-TweetSentiment-BERT-Hatem` is a bilingual sentiment analysis model trained on both **Arabic** and **English** tweets. It is based on the `bert-base-multilingual-cased` model from Hugging Face Transformers.

The model distinguishes between **positive** and **negative** sentiments in real-world social media content, specifically Twitter data.

## 🧠 Model Details

- **Base model**: `bert-base-multilingual-cased`
- **Fine-tuned on**: 
  - Arabic tweets from [UCI Sentiment Dataset 2024](https://data.mendeley.com/datasets/m88gg52wp7/1)
  - English tweets from [Sentiment140 (Stanford)](http://help.sentiment140.com/for-students)
- **Task**: Binary sentiment classification (0 = Negative, 1 = Positive)
- **Languages**: Arabic, English
- **Tokenizer**: `bert-base-multilingual-cased` tokenizer
- **Accuracy**: Evaluated on 10% holdout from training set

---

🔍 Training Details

- Framework: 🤗 Transformers + PyTorch
- Training Time: ~2 epochs
- Optimizer: AdamW (default in Trainer)
- Batch Size: 16
- Evaluation Metric: Accuracy, F1, Precision, Recall
- Environment: Google Colab

---
## 📊 Evaluation Results

### ✅ Experiment 1 — Initial Run (2K Samples)

| Epoch | Train Loss | Val Loss | Accuracy | F1 Score | Precision | Recall |
|-------|------------|----------|----------|----------|-----------|--------|
| 1     | 0.6266     | 0.7536   | 59.00%   | 0.1800   | 0.6429    | 0.1047 |
| 2     | 0.5127     | 0.5944   | 72.00%   | 0.6667   | 0.6829    | 0.6512 |

---
### ✅ Experiment 2 — Refined Arabic Dataset (20K Samples)

| Epoch | Train Loss | Val Loss | Accuracy | F1 Score | Precision | Recall |
|-------|------------|----------|----------|----------|-----------|--------|
| 1     | 0.5851     | 0.5879   | 70.85%   | 0.6674   | 0.6139    | 0.7312 |
| 2     | 0.4792     | 0.5007   | 78.65%   | 0.7105   | 0.7763    | 0.6550 |

---
### ✅ Experiment 3 — Large-Scale Ar+En Dataset (100K Samples)

| Epoch | Train Loss | Val Loss | Accuracy | F1 Score | Precision | Recall |
|-------|------------|----------|----------|----------|-----------|--------|
| 1     | 0.5231     | 0.5846   | 72.35%   | 0.7127   | 0.6171    | 0.8434 |
| 2     | 0.4404     | 0.4496   | 79.98%   | 0.7502   | 0.7615    | 0.7394 |

🔍 Summary:
 Larger datasets led to higher recall and more robust generalization across languages. The model surpassed 79% accuracy and 0.75 F1 score in the final training run.

---
🧪 How to Reproduce

The model was fine-tuned using Trainer from the Hugging Face transformers library on a multilingual sentiment dataset (based on Sentiment140 and additional Arabic tweets).

Training Time: ~1h30min on Colab GPU
Model: bert-base-multilingual-cased

## 📦 How to Use

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="HatemMoushir/ArEn-TweetSentiment-BERT-Hatem")
print(classifier("الخدمة كانت ممتازة"))
print(classifier("I hate this product."))
```
## Testing

- example 1 (Arabic)

```python

from transformers import pipeline

# تحميل النموذج
classifier = pipeline("sentiment-analysis", model="HatemMoushir/ArEn-TweetSentiment-BERT-Hatem")

# 100 جملة مع التصنيفات الحقيقية (1 = إيجابي، 0 = سلبي)
samples = [
    ("أنا سعيد جدًا اليوم", 1),
    ("الجو ممطر وهذا يجعلني حزينًا", 0),
    ("نجحت في الامتحان!", 1),
    ("أشعر بالإحباط من الأخبار", 0),
    ("أحب أصدقائي كثيرًا", 1),
    ("هذا أسوأ يوم في حياتي", 0),
    ("أشعر بالراحة والطمأنينة", 1),
    ("لم أتمكن من النوم جيدًا الليلة", 0),
    ("اليوم جميل ومشمس", 1),
    ("كل شيء يسير بشكل خاطئ", 0),
    ("أحب مشاهدة الأفلام مع عائلتي", 1),
    ("تأخرت عن العمل وفقدت مزاجي", 0),
    ("أشعر بالنشاط والحيوية", 1),
    ("المكان مزدحم ولا أستطيع التحمل", 0),
    ("قضيت عطلة رائعة على الشاطئ", 1),
    ("انتهى اليوم بشكل سيء", 0),
    ("أشعر بالتفاؤل بشأن المستقبل", 1),
    ("لم يعجبني الطعام اليوم", 0),
    ("أشعر بالحب من الجميع", 1),
    ("خسرت كل شيء في لحظة", 0),
    ("الموسيقى تجعلني سعيدًا", 1),
    ("الطريق مزدحم وأنا غاضب", 0),
    ("أنا ممتن لكل شيء لدي", 1),
    ("كان يومًا مرهقًا جدًا", 0),
    ("أشعر بالأمل رغم الصعوبات", 1),
    ("لا أطيق الانتظار لزيارة أصدقائي", 1),
    ("تجاهلني في الاجتماع وشعرت بالإهانة", 0),
    ("فزت في المسابقة!", 1),
    ("الجو خانق ولا يُحتمل", 0),
    ("تلقيت رسالة جميلة من صديقي", 1),
    ("انقطعت الكهرباء وفاتني الفيلم", 0),
    ("أنا محظوظ بعائلتي", 1),
    ("لا أحد يهتم بي", 0),
    ("الهدوء في هذا المكان يريحني", 1),
    ("خسرت فرصتي الأخيرة", 0),
    ("أشعر أنني محبوب", 1),
    ("ضاعت أمتعتي في المطار", 0),
    ("قمت بعمل جيد اليوم", 1),
    ("لا أريد التحدث مع أحد", 0),
    ("أنا ممتن للحياة", 1),
    ("يوم ممل وبلا فائدة", 0),
    ("تلقيت ترقية في العمل", 1),
    ("أشعر بالإجهاد والتعب", 0),
    ("الهدية أسعدتني كثيرًا", 1),
    ("انهرت من الضغط", 0),
    ("تناولت وجبة لذيذة", 1),
    ("تأخرت الرحلة وأشعر بالضيق", 0),
    ("حققت هدفًا كنت أسعى له", 1),
    ("الخسارة كانت قاسية", 0),
    ("أنا فخور بنفسي", 1),
    ("فقدت الثقة في من حولي", 0),
    ("عطلة نهاية الأسبوع كانت رائعة", 1),
    ("لا أجد أي دافع للاستمرار", 0),
    ("ابني نجح في دراسته", 1),
    ("كل من حولي خذلني", 0),
    ("مشيت على البحر وكان الجو جميلًا", 1),
    ("تعرضت لموقف محرج أمام الجميع", 0),
    ("أشعر بالسعادة لأني ساعدت شخصًا", 1),
    ("تم تجاهلي بالكامل", 0),
    ("نمت جيدًا واستيقظت بنشاط", 1),
    ("لا أشعر بأي تقدم", 0),
    ("يوم رائع مع أصدقائي", 1),
    ("فشلت مرة أخرى", 0),
    ("تلقيت مكالمة أسعدتني", 1),
    ("كل شيء ينهار من حولي", 0),
    ("استمتعت بالأجواء اليوم", 1),
    ("أشعر بالقلق المستمر", 0),
    ("كان اللقاء دافئًا ومليئًا بالحب", 1),
    ("لا أتحمل الضغط أكثر", 0),
    ("نجح مشروعي أخيرًا", 1),
    ("فقدت عملي اليوم", 0),
    ("قضيت وقتًا ممتعًا في الحديقة", 1),
    ("أنا خائف مما سيأتي", 0),
    ("تلقيت دعمًا كبيرًا من أصدقائي", 1),
    ("اليأس يسيطر علي", 0),
    ("رحلتي كانت مليئة بالفرح", 1),
    ("لا شيء يسعدني مؤخرًا", 0),
    ("أحببت الفيلم كثيرًا", 1),
    ("كلماتهم جرحتني", 0),
    ("تذوقت طعامًا رائعًا", 1),
    ("لا أرى فائدة من المحاولة", 0),
    ("ضحكنا كثيرًا اليوم", 1),
    ("حلمي تبخر", 0),
    ("لحظة اللقاء كانت ساحرة", 1),
    ("خسرت أقرب الناس إلي", 0),
    ("المشي في الطبيعة يريح أعصابي", 1),
    ("لم يصدقني أحد", 0),
    ("ابتسامة طفل جعلت يومي أفضل", 1),
    ("كل شيء أصبح صعبًا", 0),
    ("اليوم احتفلت بنجاحي", 1),
    ("انهار كل شيء في لحظة", 0),
    ("أمضيت وقتًا ممتعًا مع العائلة", 1),
    ("فقدت الأمل تمامًا", 0),
    ("قضيت يومًا رائعًا في الريف", 1),
    ("الناس لا يفهمونني", 0),
    ("استمتعت بالموسيقى والهدوء", 1),
    ("لا أشعر بالسعادة أبدًا", 0),
    ("الأصدقاء جلبوا لي السعادة", 1),
    ("تعبت من المحاولة", 0),
    ("كل لحظة كانت رائعة", 1),
    ("كل شيء فشل", 0),
    ("النجاح كان ثمرة جهدي", 1),
    ("لا أملك شيئًا أفرح به", 0)
]

# تجربة النموذج ومقارنة النتيجة
correct = 0

for i, (text, true_label) in enumerate(samples):
    result = classifier(text)[0]
    
    predicted_label = 1 if result["label"] == ("LABEL_1") else 0
    is_correct = predicted_label == true_label
    correct += is_correct

    print(f"{i+1}. \"{text}\"")
    print(f"   🔍 Model → {predicted_label} | 🎯 True → {true_label} | {'✔️ صح' if is_correct else '❌ غلط'}\n")

# حساب الدقة
accuracy = correct / len(samples)
print(f"✅ Accuracy: {accuracy * 100:.2f}%")
```
- example 2 (English)

```python

from transformers import pipeline

# تحميل النموذج الإنجليزي المدرب على Sentiment140

classifier = pipeline("sentiment-analysis", model="HatemMoushir/ArEn-TweetSentiment-BERT-Hatem")

# 100 جملة إنجليزية مع التصنيف الحقيقي: 1 = Positive, 0 = Negative
samples = [
    ("I love this place!", 1),
    ("I hate waiting in traffic.", 0),
    ("Today is a beautiful day", 1),
    ("I am really disappointed", 0),
    ("Feeling great about this opportunity", 1),
    ("This movie was terrible", 0),
    ("Absolutely loved the dinner", 1),
    ("I’m sad and frustrated", 0),
    ("My friends make me happy", 1),
    ("Everything went wrong today", 0),
    ("What a fantastic game!", 1),
    ("Worst experience ever", 0),
    ("The weather is amazing", 1),
    ("I can’t stand this anymore", 0),
    ("So proud of my achievements", 1),
    ("Feeling down", 0),
    ("Just got a promotion!", 1),
    ("Why does everything suck?", 0),
    ("Best vacation ever", 1),
    ("I’m tired of this nonsense", 0),
    ("Such a lovely gesture", 1),
    ("That was rude and uncalled for", 0),
    ("Finally some good news!", 1),
    ("I'm so lonely", 0),
    ("My cat is the cutest", 1),
    ("This food tastes awful", 0),
    ("Celebrating small wins today", 1),
    ("Not in the mood", 0),
    ("Grateful for everything", 1),
    ("I feel useless", 0),
    ("Such a peaceful morning", 1),
    ("Another failure, just great", 0),
    ("Got accepted into college!", 1),
    ("I hate being ignored", 0),
    ("The sunset was breathtaking", 1),
    ("You ruined my day", 0),
    ("He makes me feel special", 1),
    ("Everything is falling apart", 0),
    ("Can't wait for the weekend", 1),
    ("So much stress right now", 0),
    ("I’m in love", 1),
    ("I don’t care anymore", 0),
    ("Won first place!", 1),
    ("This is so frustrating", 0),
    ("He always cheers me up", 1),
    ("Feeling stuck", 0),
    ("Had a wonderful time", 1),
    ("Nothing matters", 0),
    ("Looking forward to tomorrow", 1),
    ("Just leave me alone", 0),
    ("We made it!", 1),
    ("Horrible customer service", 0),
    ("The music lifts my spirits", 1),
    ("I'm drowning in problems", 0),
    ("My team won the match", 1),
    ("I wish I never came", 0),
    ("Sunshine and good vibes", 1),
    ("Everything is a mess", 0),
    ("Love the energy here", 1),
    ("Feeling hopeless", 0),
    ("She always makes me smile", 1),
    ("So many regrets", 0),
    ("Today was a success", 1),
    ("Bad day again", 0),
    ("I’m truly blessed", 1),
    ("This is depressing", 0),
    ("Can't stop smiling", 1),
    ("Everything hurts", 0),
    ("So excited for this!", 1),
    ("I hate myself", 0),
    ("Best concert ever", 1),
    ("Life is unfair", 0),
    ("Happy and content", 1),
    ("Crying inside", 0),
    ("Feeling inspired", 1),
    ("The service was awful", 0),
    ("Joy all around", 1),
    ("I feel dead inside", 0),
    ("It’s a dream come true", 1),
    ("Nothing good ever happens", 0),
    ("Feeling positive", 1),
    ("That hurt my feelings", 0),
    ("Success tastes sweet", 1),
    ("I can't handle this", 0),
    ("We had a blast", 1),
    ("It’s not worth it", 0),
    ("He’s such a kind soul", 1),
    ("I'm broken", 0),
    ("Everything is perfect", 1),
    ("So tired of pretending", 0),
    ("What a nice surprise!", 1),
    ("I feel empty", 0),
    ("Can’t wait to start!", 1),
    ("It's always my fault", 0),
    ("A new beginning", 1),
    ("So much pain", 0),
    ("My heart is full", 1),
    ("This sucks", 0),
    ("I feel accomplished", 1),
    ("Why bother", 0),
    ("Living my best life", 1),
    ("I just want to disappear", 0)
]

# تجربة النموذج ومقارنة النتيجة
correct = 0

for i, (text, true_label) in enumerate(samples):
    result = classifier(text)[0]
    predicted_label = 1 if  result["label"] == "LABEL_1" else 0
    is_correct = predicted_label == true_label
    correct += is_correct

    print(f"{i+1}. \"{text}\"")
    print(f"   🔍 Model → {predicted_label} | 🎯 True → {true_label} | {'✔️ Correct' if is_correct else '❌ Wrong'}\n")

# دقة النموذج
accuracy = correct / len(samples)
print(f"✅ Accuracy: {accuracy * 100:.2f}%")
```

## Development and Assistance

This model was developed and trained using **Google Colab**, with guidance and technical assistance from **ChatGPT**, which was used for idea generation, code authoring, and troubleshooting throughout the development process.

---

## Source Code

The full code used to prepare and train the model is available on GitHub:

🔗 [GitHub file source](https://github.com/HatemMoushir/Sentiment/blob/main/ArEn-TweetSentiment-BERT-Hatem.ipynb).

---

📜 License

MIT License. Free to use, modify, and share with attribution.

👤 Author

Developed by Hatem Moushir
Contact: h_moushir@hotmail.com
