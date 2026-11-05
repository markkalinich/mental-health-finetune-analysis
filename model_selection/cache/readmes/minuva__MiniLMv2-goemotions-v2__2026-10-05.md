---
datasets:
- go_emotions
language:
- en
library_name: transformers
model-index:
- name: text-classification-goemotions
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: go_emotions
      type: multilabel_classification
      config: simplified
      split: test
      args: simplified
    metrics:
    - name: F1
      type: f1
      value: 0.487
license: apache-2.0
tags:
 - emotion
 - emotions
 - multi-class-classification
 -  multi-label-classification
---

# Text Classification GoEmotions

This model is a fined-tuned version of [MiniLMv2-L6-H384](https://huggingface.co/nreimers/MiniLMv2-L6-H384-distilled-from-RoBERTa-Large) on the on the [go_emotions](https://huggingface.co/datasets/go_emotions) dataset.
The quantized version in ONNX format can be found [here](https://huggingface.co/minuva/MiniLMv2-goemotions-v2-onnx)

# Load the Model

```py
from transformers import pipeline

pipe = pipeline(model='minuva/MiniLMv2-goemotions-v2', task='text-classification')
pipe("I am angry")
# [{'label': 'anger', 'score': 0.9722517132759094}]
```
# Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear


# Metrics (comparison with teacher model)

| Teacher (params)    |   Student (params)     | Set         | Score (teacher)    |    Score (student)      |
|--------------------|-------------|----------|--------| --------|
| tasinhoque/text-classification-goemotions (355M) |      MiniLMv2-goemotions-v2 (30M)   | Validation  | 0.514252 |0.484898 |
| tasinhoque/text-classification-goemotions (355M) |      MiniLMv2-goemotions-v2  (30M)  | Test  | 0.501937 |  0.486890 |

# Deployment

Check out our [fast-nlp-text-emotion repository](https://github.com/minuva/fast-nlp-text-emotion) for a FastAPI based server to easily deploy this model on CPU devices.