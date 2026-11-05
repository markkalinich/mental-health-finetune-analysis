---
license: mit
base_model: xlnet-base-cased
tags:
- generated_from_keras_callback
- sentiment analysis
widget:
- text: product quality is good. affordable prices and very fast delivery.
model-index:
- name: dipawidia/xlnet-base-cased-product-review-sentiment-analysis
  results: []
language:
- en
metrics:
- accuracy
library_name: transformers
datasets:
- dipawidia/ecommerce-product-reviews-sentiment
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# dipawidia/xlnet-base-cased-product-review-sentiment-analysis

This model is a fine-tuned version of [xlnet-base-cased](https://huggingface.co/xlnet-base-cased) on any type of product reviews dataset gathered from several e-commerce such as shopee, tokopedia, blibli, lazada, and zalora.
The dataset can be found [here](https://huggingface.co/datasets/dipawidia/ecommerce-product-reviews-sentiment)
It achieves the following results on the evaluation set:
- Train Loss: 0.1085
- Train Accuracy: 0.9617
- Validation Loss: 0.1910
- Validation Accuracy: 0.9414
- Epoch: 4

## Intended uses & limitations

This fine-tuned XLNet model is used for sentiment analysis with 2 labels text classification: 0 -> Negative; 1 -> Positive.

### Example Pipeline
```python
from transformers import pipeline
pipe = pipeline("text-classification", model="dipawidia/xlnet-base-cased-product-review-sentiment-analysis")
pipe("This shoes is awesome")
```
```
[{'label': 'Positive', 'score': 0.9995703101158142}]
```

### Full classification example

```python
from transformers import XLNetTokenizer, TFXLNetForSequenceClassification
import tensorflow as tf
import numpy as np

tokenizer = XLNetTokenizer.from_pretrained("dipawidia/xlnet-base-cased-product-review-sentiment-analysis")
model = TFXLNetForSequenceClassification.from_pretrained("dipawidia/xlnet-base-cased-product-review-sentiment-analysis")

def get_sentimen(text):
  tokenize_text = tokenizer(text, return_tensors = 'tf')
  preds = model.predict(dict(tokenize_text))['logits']
  class_preds = np.argmax(tf.keras.layers.Softmax()(preds))
  if class_preds == 1:
    label = 'Positive'
  else:
    label = 'Negative'
  return(label)

get_sentimen('i hate this product')
```

Output: 

```
Negative
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamW', 'weight_decay': 0.004, 'clipnorm': None, 'global_clipnorm': None, 'clipvalue': None, 'use_ema': False, 'ema_momentum': 0.99, 'ema_overwrite_frequency': None, 'jit_compile': True, 'is_legacy_optimizer': False, 'learning_rate': 3e-05, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.3417     | 0.8491         | 0.1568          | 0.9449              | 0     |
| 0.1943     | 0.9235         | 0.1504          | 0.9466              | 1     |
| 0.1569     | 0.9404         | 0.1612          | 0.9466              | 2     |
| 0.1238     | 0.9572         | 0.1748          | 0.9475              | 3     |
| 0.1085     | 0.9617         | 0.1910          | 0.9414              | 4     |


### Framework versions

- Transformers 4.41.2
- TensorFlow 2.15.0
- Tokenizers 0.19.1