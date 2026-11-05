---
language: tr
tags:
- text-classification
- sentiment-analysis
- turkish
- optuna
- finetune
- ecommerce
license: apache-2.0
base_model: dbmdz/electra-base-turkish-mc4-uncased-discriminator
library_name: transformers
pipeline_tag: text-classification
metrics:
- accuracy
- f1
- macro_f1
- weighted_f1
---

# Turkish Sentiment Analysis (3-class) — Fine-tuned

## Overview
This model is a fine-tuned version of **`dbmdz/electra-base-turkish-mc4-uncased-discriminator`** for 3-class Turkish sentiment analysis. It was trained on an imbalanced dataset of e-commerce product reviews, and hyperparameters were optimized with Optuna to obtain the most effective fine-tuning configuration.

Bu model, üç sınıflı Türkçe duygu analizi için **`dbmdz/electra-base-turkish-mc4-uncased-discriminator`** taban alınarak ince ayar (fine-tuning) yapılmış bir sürümdür. Model, dengesiz bir e-ticaret ürün yorumları veri kümesi üzerinde eğitilmiş; en etkili ince ayar yapılandırmasını elde etmek için hiperparametreler Optuna ile optimize edilmiştir.

## Intended Use
- Product reviews classification
- Social media analysis
- Customer feedback analysis
- Brand monitoring
- Market research
- Customer service optimization
- Competitive intelligence

## Model Details
| Field | Value |
| --- | --- |
| Model Name | msamilim/electra-turkish-sentiment-optuna-hpo |
| Base Model | dbmdz/electra-base-turkish-mc4-uncased-discriminator |
| Task | Sentiment Analysis |
| Language | Turkish |
| Fine-Tuning Dataset | Turkish E-Commerce Product Reviews Dataset |
| Number of Labels | 3 |
| Problem Type | Single-label classification |
| License | apache-2.0 |
| Fine-Tuning Framework | Hugging Face Transformers |

## Dataset
The dataset is a Turkish three-class sentiment corpus (negatif / notr / pozitif). Overall distribution and per-split distributions are shown below.

### Dataset Distribution (Overall)
| LabelID | LabelName | Count | Ratio (%) |
| --- | --- | --- | --- |
| 0 | negatif | 9462 | 18.86 |
| 1 | notr | 746 | 1.49 |
| 2 | pozitif | 39952 | 79.65 |
| — | Total | 50160 | 100.00 |

## Training Procedure
- Objective metric: **`eval_macro_f1`**
- Hyperparameter Optimization Techniques: **`Optuna`**

### HPO Parameter Ranges
```json
params = {
        "learning_rate": trial.suggest_float("learning_rate", 5e-6, 5e-5, log=True),
        "per_device_train_batch_size": trial.suggest_categorical("per_device_train_batch_size", [16, 32]),
        "per_device_eval_batch_size":  trial.suggest_categorical("per_device_eval_batch_size",  [32]),
        "weight_decay": trial.suggest_float("weight_decay", 0.0, 0.1),
        "warmup_ratio": trial.suggest_float("warmup_ratio", 0.0, 0.2),
        "num_train_epochs": trial.suggest_int("num_train_epochs", 6, 8),
        "gradient_accumulation_steps": trial.suggest_categorical("gradient_accumulation_steps", [1, 2, 4]),
    }

```

### Best Trial Hyperparameters
```json
{
  "learning_rate": 2.0021958728380746e-05,
  "per_device_train_batch_size": 16,
  "per_device_eval_batch_size": 32,
  "weight_decay": 0.0515273094797082,
  "warmup_ratio": 0.1122927021129482,
  "num_train_epochs": 8,
  "gradient_accumulation_steps": 2
}
```

## Evaluation Results
These results are the evaluations recorded during the final fine-tuning training process.
| label | precision | recall | f1-score |
| --- | --- | --- | --- |
| negatif | 0.8366 | 0.7894 | 0.8123 |
| notr | 0.1667 | 0.1444 | 0.1548 |
| pozitif | 0.9513 | 0.9664 | 0.9588 |
| accuracy |  |  | 0.9208 |
| micro avg | 0.9208 | 0.9208 | 0.9208 |
| macro avg | 0.6515 | 0.6334 | 0.6420 |
| weighted avg | 0.9180 | 0.9208 | 0.9192 |

### Epoch-wise Metrics
| epoch | train_loss | eval_loss | eval_macro_f1 |
| --- | --- | --- | --- |
| 1 | 0.3955 | 0.2291 | 0.5869 |
| 2 | 0.1939 | 0.2053 | 0.6011 |
| 3 | 0.1594 | 0.2170 | 0.5967 |
| 4 | 0.1324 | 0.2341 | 0.6127 |
| 5 | 0.1075 | 0.3061 | 0.6148 |
| 6 | 0.0887 | 0.3278 | 0.6115 |
| 7 | 0.0746 | 0.3567 | 0.6382 |
| 8 | 0.0633 | 0.3924 | 0.6420 |

## How to use - Pipeline
```python
from transformers import pipeline

# Load the classification pipeline with the specified model
model_name = "msamilim/electra-turkish-sentiment-optuna-hpo"
pipe = pipeline("text-classification", model=model_name)

# Classify a new sentence
sentence = "Güzel ürün, tavsiye ederim."
result = pipe(sentence)

# Print the result
print(result)

# Example output : 
# [{'label': 'pozitif', 'score': 0.9998408555984497}]
```

## How to use - Full Classification 
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "msamilim/electra-turkish-sentiment-optuna-hpo"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(texts):
    inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    id2label = {    0: "Negatif",    1: "Nötr",    2: "Pozitif"}
    return [id2label[p] for p in torch.argmax(probabilities, dim=-1).tolist()]

texts = [
     "Güzel ürün, tavsiye ederim kullanılır.", 
     "Ürün çok güzel ve kaliteli. Maalesef yüzüme uymadığı için iade etmek zorunda kaldım.", 
     "Keşke aldıktan sonra indirime girmeseydi.",
     "Daha soluk ve mat yapısı var beğenmedim .",
]

for text, sentiment in zip(texts, predict_sentiment(texts)):
    print(f"Text: {text}\nSentiment: {sentiment}\n")

# Example output : 
# Text: Güzel ürün, tavsiye ederim kullanılır.
# Sentiment: Pozitif
# Text: Ürün çok güzel ve kaliteli. Maalesef yüzüme uymadığı için iade etmek zorunda kaldım.
# Sentiment: Pozitif
# Text: Keşke aldıktan sonra indirime girmeseydi.
# Sentiment: Negatif
# Text: Daha soluk ve mat yapısı var beğenmedim .
# Sentiment: Negatif



```

### Framework versions
- transformers==4.57.0
- torch==2.8.0+cu128
- datasets==4.2.0
- accelerate==1.10.1
- evaluate==0.4.6
- python==3.11.13