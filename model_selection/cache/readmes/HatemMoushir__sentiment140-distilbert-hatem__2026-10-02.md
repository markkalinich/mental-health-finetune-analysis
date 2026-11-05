---
language: en
license: mit
tags:
- sentiment-analysis
- twitter
- nlp
- transformers
- distilbert
- sentiment140
- Stanford
- Egypt
- Ain shams university 
- Hatem Moushir
datasets:
  - stanfordnlp/sentiment140
model-index:
- name: sentiment140-distilbert
  results:
  - task:
      name: Sentiment Analysis
      type: text-classification
    dataset:
      name: Sentiment140
      type: CSV
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.85
---

## 🧠 Model Overview

-This model is fine_tuned for **sentiment classification** 
- using the [Sentiment140 dataset](http://help.sentiment140.com/home)
- It predicts one of the following sentiment labels:
- `0`: Negative
- `1`: Positive

-Model Type: `DistilBERT`  
-Language: `English` (with future support for Arabic tweets planned)  
-Framework: `Transformers (🤗 Hugging Face)`

---

## 🧠 Model Details

- **Base model**: `distilbert-base-uncased`
- **Task**: Sentiment Analysis (Binary: Positive / Negative)
- **Trained on**: Sentiment140 dataset (1.6M tweets)
- **Creator**: Hatem Moushir
- **Language**: English
- **Use case**: General sentiment classification for social media or informal texts.

---

## 📊 Training Data

- Dataset: [Sentiment140](https://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip)
- Samples Used: **1,600,000 tweets**
- Format: CSV with columns: `target`, `id`, `date`, `query`, `user`, `text`
- labels:
- `0`: Negative
- `2`: Neutral
- `4`: Positive

- Preprocessing: 
  - Lowercasing
  - Removing URLs, mentions, hashtags
  - Optional: Stopwords filtering

---

## 🔧 Training Configuration

| Setting              | Value               |
|----------------------|---------------------|
| Model Base           | `distilbert-base-uncased` |
| Epochs               | 2                   |
| Batch Size           | 16                  |

---
🧪 Evaluation Results

### 🧪 Evaluation Results

| Metric                         | Value             |
|-------------------------------|-------------------|
| Accuracy (Val) – Epoch 1      | 83.43%            |
| Accuracy (Val) – Epoch 2      | (لم يتحسن) – 83.43% |
| Training Loss (Epoch 1)       | 0.4022            |
| Validation Loss (Epoch 1)     | 0.3784            |
| Training Loss (Epoch 2)       | 0.2536            |
| Validation Loss (Epoch 2)     | 0.4179            |

---

## 🚀 How to Use

- example 1

```python
from transformers import pipeline

model_name = "HatemMoushir/sentiment140-distilbert-hatem"
pipe = pipeline("sentiment-analysis", model=model_name)

pipe([
    "I love this place!",
    "This is a terrible experience."
])
```

- example 2

```python

import gradio as gr
from transformers import pipeline

# Label mapping from model output to readable format
label_map = {"LABEL_0": "Negative", "LABEL_1": "Positive"}

# Load the sentiment analysis pipeline with your custom model
pipe = pipeline("sentiment-analysis", model="HatemMoushir/sentiment140-distilbert-hatem")

def analyze_sentiment(texts):
    # Split input by newline or punctuation (you can customize this)
    sentences = texts.split('\n')
    results = pipe(sentences)

    output = []
    for text, res in zip(sentences, results):
        label = label_map[res["label"]]
        score = round(res["score"], 2)
        output.append(f"{text} → {label} ({score})")

    return "\n".join(output)

# Multi-line input using Gradio Textbox
gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=5, placeholder="Enter one or more sentences..."),
    outputs="text"
).launch()
```
## Test the model

```python

from transformers import pipeline

# تحميل النموذج الإنجليزي المدرب على Sentiment140
classifier = pipeline("sentiment-analysis", model="HatemMoushir/sentiment140-distilbert-hatem")

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

---

## Development and Assistance

This model was developed and trained using **Google Colab**, with guidance and technical assistance from **ChatGPT**, which was used for idea generation, code authoring, and troubleshooting throughout the development process.

---

## Source Code

The full code used to prepare and train the model is available on GitHub:

🔗 [GitHub file source](https://github.com/HatemMoushir/Sentiment/blob/main/sentiment140-distilbert-hatem.ipynb).

---

📁 Model Versions

Version	Notes

- v1.0	Trained on 10000 samples
- v1.1  Trained on 50000 samples
---

📌 Limitations

Bias may exist due to dataset source (Twitter, English only)

Slang and sarcasm not always well understood

Model not yet optimized for Arabic tweets

---

📝 License

This model is released under the MIT License.

---

🙌 Acknowledgments

Special thanks to the Stanford NLP group for publishing Sentiment140, and to the Hugging Face team for making model sharing easy.

---

📬 Contact

Created by Hatem Moushir
For questions or collaboration: 
h_moushir@hotmail.com