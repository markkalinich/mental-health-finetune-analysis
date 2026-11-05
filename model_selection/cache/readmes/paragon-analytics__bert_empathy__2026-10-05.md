---
license: "mit"
---

This is a fine-tuned RoBERTa model that takes text (up to a few sentences) and predicts to what extent it contains empathic language. 

Example classification:

```python
import torch
import tensorflow as tf
from transformers import RobertaTokenizer, RobertaModel
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("paragon-analytics/bert_empathy")
model = AutoModelForSequenceClassification.from_pretrained("paragon-analytics/bert_empathy")

def roberta(x):
    encoded_input = tokenizer(x, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = tf.nn.softmax(scores)
    return scores.numpy()[1]

```