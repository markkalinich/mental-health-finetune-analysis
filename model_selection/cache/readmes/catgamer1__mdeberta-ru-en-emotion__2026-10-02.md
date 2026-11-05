---
language:
- ru
- en
tags:
- emotion-recognition
- multi-label-classification
- deberta
- lora
- russian
- english
license: mit
pipeline_tag: text-classification
---

# Model Card for mdeberta-ru-en-emotion

## Model Description

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) for multi-label emotion recognition in social media data. It was trained to handle 6 Ekman's emotions (anger, disgust, fear, joy, sadness, surprise) and a neutral category. It supports both Russian and English texts.

## Model training

Public emotion recognition datasets were used:
- [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions), English, all 7 classes;
- [CEDR](https://huggingface.co/datasets/sagteam/cedr_v1), Russian, lacks disgust;
- [BRIGHTER](https://huggingface.co/datasets/brighter-dataset/BRIGHTER-emotion-categories), Russian and English; Russian has all 7 classes, while English lacks disgust.

Training was done with the following:
- LoRA fine-tuning (r=16; a=32; q, k, v, dense projections; dropout=0.1);
- [Clipped asymmetric loss](https://ieeexplore.ieee.org/document/10947681) with epsilon=0.04, gamma_neg=3.5 and gamma_pos=1.5 to handle the class imbalance;
- AdamW as an optimizer with LR=2e-4 for LoRA and LR=1e-5, epsilon=1e-3 for classification head;
- Linear learning rate scheduler with 10% warmup steps;
- Batch size of 16 with 2-step gradient accumulation;
- Torch AMP and gradient norm clipping of 1.0;
- 10 scheduled epochs, with training stopping early after epoch 7 due to increasing validation loss.

## Evaluation

Model achieved **0.9291 macro AUC** and **0.6957 macro F1** for 7-class multilabel emotion recognition on the combined GoEmotion + CEDR + BRIGHTER set. F1 was calculated with validation-optimal thresholds. Per-emotion breakdown is shown below:
| Emotion | AUC | F1 |
| :--- | ---: | ---: |
| Anger | 0.9113 | 0.6198 |
| Fear | 0.9505 | 0.7717 |
| Joy | 0.9376 | 0.7937 |
| Sadness | 0.9245 | 0.7043 |
| Disgust | 0.9725 | 0.6442 |
| Surprise | 0.9048 | 0.6432 |
| Neutral | 0.9024 | 0.6931 |

## How to Use

You can use pipeline with `top_k=None` and `function_to_apply='sigmoid'` to get probabilities for all classes with a simple callable API.

```python
from transformers import pipeline

model_path = "catgamer1/mdeberta-ru-en-emotion"

classifier = pipeline(
    "text-classification",
    model=model_path,
    tokenizer=model_path,
    top_k=None, 
    function_to_apply='sigmoid'
)

sentence = "What a relief, the tire is fine!"
result = classifier(sentence)
```