---
library_name: transformers
license: mit
datasets:
- seara/ru_go_emotions
base_model: deepvk/deberta-v1-base
language:
- ru
tags:
- Text Classification
- emotion-classification
- emotion-recognition
- emotion-detection
- emotion
- multilabel
metrics:
- f1
- precision
- recall
---

This is the model for detecting 27 types of emotions in russian texts. Leaderboard of opensource models:

| Model                                                                  | F1 macro | F1 macro weighted | Precision macro | Recall macro | Size|
|------------------------------------------------------------------------|----------|-------------------|-----------------|--------------|-----|
| [seara/rubert-tiny2-ru-go-emotions](https://huggingface.co/seara/rubert-tiny2-russian-emotion-detection-ru-go-emotions)   | 0.33     | 0.48    | 0.51  | 0.29  | 29.2M| 
| [seara/rubert-base-cased-ru-go-emotions](https://huggingface.co/seara/rubert-base-cased-russian-emotion-detection-ru-go-emotions)  | 0.36     | 0.49      | 0.52  | 0.31   | 178M|
| [fyaronskiy/ruRoberta-large-ru-go-emotions](https://huggingface.co/fyaronskiy/ruRoberta-large-ru-go-emotions) default thresholds = 0.5  | 0.41     | 0.52   | **0.58**  | 0.36  | 355M |
| [fyaronskiy/ruRoberta-large-ru-go-emotions](https://huggingface.co/fyaronskiy/ruRoberta-large-ru-go-emotions) best thresholds               | **0.48** | **0.58** | 0.46 | **0.55**  | 355M |
| [fyaronskiy/deberta-v1-base-russian-go-emotions](https://huggingface.co/fyaronskiy/deberta-v1-base-russian-go-emotions)                          | **0.48** | 0.57 | 0.46   | 0.54  | 125M |

# Summary
This is [deepvk/deberta-v1-base](https://huggingface.co/deepvk/deberta-v1-base) model finetuned on [ru_go_emotions](https://huggingface.co/datasets/seara/ru_go_emotions) 
dataset for multilabel classification. Model can be used to extract all emotions from text or detect certain emotions. 
Thresholds are selected on validation set by maximizing f1 macro over all labels.

The quality of the model varies greatly across all classes (look at the table with metrics below). There are classes like 
amusement, gratitude, fear where the model shows high recognition quality, and classes that pose difficulties for the model - relief, realization.

# Usage
Using model with Huggingface Transformers:
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("fyaronskiy/deepvk_deberta-v1-base__bs32_max_len128_ep10_lr5e-05_lr_sheduler_linear")
model = AutoModelForSequenceClassification.from_pretrained("fyaronskiy/deepvk_deberta-v1-base__bs32_max_len128_ep10_lr5e-05_lr_sheduler_linear")

best_thresholds = [0.5510204081632653, 0.18367346938775508, 0.1020408163265306, 0.1020408163265306, 0.18367346938775508, 0.22448979591836732, 0.2040816326530612, 0.4081632653061224, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.3061224489795918, 0.16326530612244897, 0.2857142857142857, 0.3877551020408163, 0.32653061224489793, 0.02040816326530612, 0.16326530612244897, 0.44897959183673464, 0.1020408163265306, 0.22448979591836732, 0.04081632653061224, 0.12244897959183673, 0.061224489795918366, 0.14285714285714285, 0.42857142857142855, 0.3061224489795918, 0.26530612244897955]
LABELS = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
ID2LABEL = dict(enumerate(LABELS))
```

Here is how you can extract emotions contained in text: 

```python
def detect_emotions(text):
  inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
  with torch.no_grad():
      logits = model(**inputs).logits
  probas = torch.sigmoid(logits).squeeze(dim=0)  
  class_binary_labels = (probas > torch.tensor(best_thresholds)).int()
  return [ID2LABEL[label_id] for label_id, value in enumerate(class_binary_labels) if value == 1]

print(detect_emotions('У вас отличный сервис и лучший кофе в городе, обожаю вашу кофейню!'))
#['admiration', 'love']
```

This is the way to get all emotions and their scores:

```python
def predict(text):
    inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
    with torch.no_grad():
        logits = model(**inputs).logits
    probas = torch.sigmoid(logits).squeeze(dim=0).tolist()
    probas = [round(proba, 3) for proba in probas]    
    
    labels2probas = dict(zip(LABELS, probas))
    probas_dict_sorted = dict(sorted(labels2probas.items(), key=lambda x: x[1], reverse=True))
    return probas_dict_sorted

print(predict('У вас отличный сервис и лучший кофе в городе, обожаю вашу кофейню!'))
'''{'admiration': 0.842,
'love': 0.675,
'approval': 0.039,
'gratitude': 0.034,
'joy': 0.025,
'excitement': 0.009,
'neutral': 0.007,
'curiosity': 0.005,
'confusion': 0.003,
'optimism': 0.003,
'caring': 0.002,
'desire': 0.002,
'realization': 0.002,
'surprise': 0.002,
'amusement': 0.001,
'anger': 0.001,
'annoyance': 0.001,
'disappointment': 0.001,
'disapproval': 0.001,
'pride': 0.001,
'sadness': 0.001,
'disgust': 0.0,
'embarrassment': 0.0,
'fear': 0.0,
'grief': 0.0,
'nervousness': 0.0,
'relief': 0.0,
'remorse': 0.0}
'''
```

# Eval results on test split of ru-go-emotions     


|                |   precision |   recall |   f1-score |   support |   threshold |
|:---------------|------------:|---------:|-----------:|----------:|------------:|
| admiration     |        0.69 |     0.67 |       0.68 |       504 |        0.55 |
| amusement      |        0.72 |     0.91 |       0.81 |       264 |        0.18 |
| anger          |        0.35 |     0.53 |       0.42 |       198 |        0.1  |
| annoyance      |        0.24 |     0.46 |       0.32 |       320 |        0.1  |
| approval       |        0.33 |     0.44 |       0.38 |       351 |        0.18 |
| caring         |        0.37 |     0.5  |       0.42 |       135 |        0.22 |
| confusion      |        0.43 |     0.42 |       0.42 |       153 |        0.2  |
| curiosity      |        0.44 |     0.71 |       0.54 |       284 |        0.41 |
| desire         |        0.46 |     0.43 |       0.45 |        83 |        0.2  |
| disappointment |        0.3  |     0.31 |       0.31 |       151 |        0.22 |
| disapproval    |        0.37 |     0.57 |       0.45 |       267 |        0.24 |
| disgust        |        0.45 |     0.41 |       0.43 |       123 |        0.31 |
| embarrassment  |        0.62 |     0.35 |       0.45 |        37 |        0.16 |
| excitement     |        0.3  |     0.34 |       0.32 |       103 |        0.29 |
| fear           |        0.67 |     0.62 |       0.64 |        78 |        0.39 |
| gratitude      |        0.92 |     0.87 |       0.89 |       352 |        0.33 |
| grief          |        0.02 |     0.33 |       0.04 |         6 |        0.02 |
| joy            |        0.41 |     0.66 |       0.51 |       161 |        0.16 |
| love           |        0.71 |     0.83 |       0.76 |       238 |        0.45 |
| nervousness    |        0.24 |     0.35 |       0.28 |        23 |        0.1  |
| optimism       |        0.58 |     0.55 |       0.57 |       186 |        0.22 |
| pride          |        0.58 |     0.44 |       0.5  |        16 |        0.04 |
| realization    |        0.25 |     0.23 |       0.24 |       145 |        0.12 |
| relief         |        0.27 |     0.36 |       0.31 |        11 |        0.06 |
| remorse        |        0.49 |     0.91 |       0.63 |        56 |        0.14 |
| sadness        |        0.53 |     0.53 |       0.53 |       156 |        0.43 |
| surprise       |        0.49 |     0.54 |       0.51 |       141 |        0.31 |
| neutral        |        0.59 |     0.78 |       0.67 |      1787 |        0.27 |
| micro avg      |        0.5  |     0.64 |       0.56 |      6329 |             |
| macro avg      |        0.46 |     0.54 |       0.48 |      6329 |             |
| weighted avg   |        0.53 |     0.64 |       0.57 |      6329 |             |
| samples avg    |        0.55 |     0.67 |       0.58 |      6329 |             |


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- seed: 28
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 7