---
base_model: DeepPavlov/rubert-base-cased
tags:
- generated_from_trainer
- sentiment
metrics:
- f1
model-index:
- name: vashkontrol-sentiment-rubert
  results: []
license: mit
datasets:
- kartashoffv/vash_kontrol_reviews
language:
- ru
pipeline_tag: text-classification
widget:
 - text: "Отзывчивые и понимающие работники, обслуживание очень понравилось, специалист проявила большое терпение чтобы восстановить пароль от Госуслуг. Спасибо!"
---


# Sentimental assessment of portal reviews "VashKontrol"

The model is designed to evaluate the tone of reviews from the [VashKontrol portal](https://vashkontrol.ru/).

This model is a fine-tuned version of [DeepPavlov/rubert-base-cased](https://huggingface.co/DeepPavlov/rubert-base-cased) on a following dataset: [kartashoffv/vash_kontrol_reviews](https://huggingface.co/datasets/kartashoffv/vash_kontrol_reviews).

It achieves the following results on the evaluation set:
- Loss: 0.1085
- F1: 0.9461

## Model description

The model predicts a sentiment label (positive, neutral, negative) for a submitted text review.


## Training and evaluation data

The model was trained on the corpus of reviews of the [VashControl portal](https://vashkontrol.ru/), left by users in the period from 2020 to 2022 inclusive.
The total number of reviews was 17,385. The sentimental assessment of the dataset was carried out by the author manually by dividing the general dataset into positive/neutral/negative reviews.

The resulting classes:
0 (positive): 13045
1 (neutral): 1196
2 (negative): 3144

Class weighting was used to solve the class imbalance. 


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0992        | 1.0   | 1391 | 0.0737          | 0.9337 |
| 0.0585        | 2.0   | 2782 | 0.0616          | 0.9384 |
| 0.0358        | 3.0   | 4173 | 0.0787          | 0.9441 |
| 0.0221        | 4.0   | 5564 | 0.0918          | 0.9488 |
| 0.0106        | 5.0   | 6955 | 0.1085          | 0.9461 |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.1
- Tokenizers 0.13.3


### Usage

```
import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('kartashoffv/vashkontrol-sentiment-rubert')
model = AutoModelForSequenceClassification.from_pretrained('kartashoffv/vashkontrol-sentiment-rubert', return_dict=True)

@torch.no_grad()
def predict(review):
    inputs = tokenizer(review, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred_label = torch.argmax(predicted, dim=1).numpy()
    return pred_label
```
### Labels

```
0: POSITIVE
1: NEUTRAL
2: NEGATIVE
```

