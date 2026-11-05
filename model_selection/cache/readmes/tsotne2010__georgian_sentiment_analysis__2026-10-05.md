---
license: mit
language:
- ka
base_model: xlm-roberta-base
pipeline_tag: text-classification
tags:
- sentiment-analysis
- georgian
inference: true
---

# Georgian Sentiment Analysis (XLM-RoBERTa-Base)

ეს არის *XLM-RoBERTa-Base* მოდელი, რომელიც სპეციალურად დატრენინგდა ქართულ ენაზე ტექსტის სენტიმენტების ანალიზისთვის (Sentiment Analysis). მოდელს შეუძლია ტექსტის კლასიფიკაცია 3 კატეგორიად: *ნეგატიური (0)*, *ნეიტრალური (1)* და *პოზიტიური (2)*.

## მოდელის აღწერა
* *ბაზისური მოდელი:* xlm-roberta-base
* *ამოცანა:* Text Classification / Sentiment Analysis
* *კლასების რაოდენობა:* 3 (Negative, Neutral, Positive)
* *ენა:* ქართული (Georgian)

## როგორ გამოვიყენოთ (Usage)

მოდელის გამოყენება ძალიან მარტივია transformers ბიბლიოთეკის `pipeline`- ის მეშვეობით:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="tsotne2010/georgian_sentiment_analysis")

result = classifier("ეს პროექტი ძალიან საინტერესო და გამოსადეგია!")
print(result)