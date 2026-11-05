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
base_model: Trendyol/tyroberta
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
This model is a fine-tuned version of **`Trendyol/tyroberta`** for 3-class Turkish sentiment analysis. It was trained on an imbalanced dataset of e-commerce product reviews, and hyperparameters were optimized with Optuna to obtain the most effective fine-tuning configuration.

Bu model, üç sınıflı Türkçe duygu analizi için **`Trendyol/tyroberta`** taban alınarak ince ayar (fine-tuning) yapılmış bir sürümdür. Model, dengesiz bir e-ticaret ürün yorumları veri kümesi üzerinde eğitilmiş; en etkili ince ayar yapılandırmasını elde etmek için hiperparametreler Optuna ile optimize edilmiştir.

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
| Model Name | msamilim/tyroberta-turkish-sentiment-optuna-hpo |
| Base Model | Trendyol/tyroberta |
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
  "learning_rate": 1.6142125050800487e-05,
  "per_device_train_batch_size": 32,
  "per_device_eval_batch_size": 32,
  "weight_decay": 0.0932597392123772,
  "warmup_ratio": 0.0627483542343149,
  "num_train_epochs": 8,
  "gradient_accumulation_steps": 1
}
```

## Evaluation Results
These results are the evaluations recorded during the final fine-tuning training process.
| label | precision | recall | f1-score |
| --- | --- | --- | --- |
| negatif | 0.8424 | 0.8291 | 0.8357 |
| notr | 0.1406 | 0.2000 | 0.1651 |
| pozitif | 0.9654 | 0.9614 | 0.9634 |
| accuracy |  |  | 0.9251 |
| micro avg | 0.9251 | 0.9251 | 0.9251 |
| macro avg | 0.6495 | 0.6635 | 0.6548 |
| weighted avg | 0.9299 | 0.9251 | 0.9274 |

### Epoch-wise Metrics
| epoch | train_loss | eval_loss | eval_macro_f1 |
| --- | --- | --- | --- |
| 1 | 0.2595 | 0.1998 | 0.6011 |
| 2 | 0.1632 | 0.1969 | 0.6058 |
| 3 | 0.1286 | 0.2104 | 0.6358 |
| 4 | 0.0959 | 0.2964 | 0.6379 |
| 5 | 0.0701 | 0.3393 | 0.6386 |
| 6 | 0.0507 | 0.3769 | 0.6244 |
| 7 | 0.0357 | 0.4328 | **0.6548** |
| 8 | 0.0252 | 0.4649 | 0.6517 |

## How to use - Pipeline
```python
from transformers import pipeline

# Load the classification pipeline with the specified model
model_name = "msamilim/tyroberta-turkish-sentiment-optuna-hpo"
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

model_name = "msamilim/tyroberta-turkish-sentiment-optuna-hpo"
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