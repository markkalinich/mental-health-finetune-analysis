---
language: en
tags:
- bert
- sentiment-analysis
- text-classification
license: mit
pipeline_tag: text-classification
library_name: transformers
widget:
- text: I had surgery last month. and I was very impressed with the quality of service
    from the moment I got in till I left. Also I like to mention the nurses they were
    out standing
  example_title: Positive
- text: I received the update and will review it later this week.
  example_title: Neutral
- text: Dirty. Generally poor attitude among the nurses, even the good know the place
    sucks. When patients are crying for help nurse should not be busy watching Tik-Tok.
    Too many mistakes made too often. Teaching nurses instructing student nurse procedures
    incorrectly. Yes, it is bad.
  example_title: Negative
base_model:
- google/bert_uncased_L-2_H-128_A-2
---

# Bert_sentiment_classifier
A BERT (`bert-base-uncased`) model fine-tuned for **3-class sentiment classification**:
- **Positive**
- **Neutral**
- **Negative**

## Labels
| id | label    |
|---:|----------|
| 0  | Neutral  |
| 1  | Positive |
| 2  | Negative |

## Test Drive
Try one of these examples into the widget:
- **Negative:** "Dirty. Generally poor attitude among the nurses, even the good know the place sucks. When patients are crying for help nurse should not be busy watching Tik-Tok. Too many mistakes made too often. Teaching nurses instructing student nurse procedures incorrectly. Yes, it is bad."
- **Neutral:** "I received the update and will review it later this week."
- **Positive:** "I had surgery last month. and I was very impressed with the quality of service from the moment I got in till I left. Also I like to mention the nurses they were out standing"

## Try it out

<div style="position:relative; width:100%; height:0; padding-bottom:75%;">
  <iframe src = 'https://huggingface.co/spaces/POKWIR/bert-sentiment-demo' ></iframe>
</div>


## How to use

### Transformers pipeline
```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="pokwir/Bert_sentiment_classifier",
    tokenizer="pokwir/Bert_sentiment_classifier",
    return_all_scores=True
)

texts = [
    "Dirty. Generally poor attitude among the nurses, even the good know the place sucks. When patients are crying for help nurse should not be busy watching Tik-Tok. Too many mistakes made too often. Teaching nurses instructing student nurse procedures incorrectly. Yes, it is bad.",
    "I had surgery last month. and I was very impressed with the quality of service from the moment I got in till I left. Also I like to mention the nurses they were out standing.",
    "This hospital has been going downhill for years thanks to dr.billie and her know all attitude she should go back to her vet clinic."
]

print(clf(texts))