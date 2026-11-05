---
license: mit
base_model: roberta-base
tags:
  - stress
  - classification
  - glassdoor
metrics:
- accuracy
- f1
- precision
- recall
widget:
  - text: >-
      They also caused so much stress because some leaders valued optics over output.
    example_title: Stressed 1 Example
  - text: >-
      Way too much work pressure.
    example_title: Stressed 2 Example
  - text: >-
      Understaffed, lots of deck revisions, unpredictable, terrible technology.
    example_title: Stressed 3 Example
  - text: >-
      Nice environment good work life balance.
    example_title: Not Stressed 1 Example
model-index:
- name: roberta-base_topic_classification_nyt_news
  results:
    - task:
          name: Text Classification
          type: text-classification
      dataset:
          name: New_York_Times_Topics
          type: News
      metrics:
          - type: F1
            name: F1
            value: 0.97
          - type: accuracy
            name: accuracy
            value: 0.97
          - type: precision
            name: precision
            value: 0.97
          - type: recall
            name: recall
            value: 0.97
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base_stress_classification

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the glassdoor dataset based on 100000 employees' reviews.
It achieves the following results on the evaluation set:
- Loss: 0.1800
- Accuracy: 0.9647
- F1: 0.9647
- Precision: 0.9647
- Recall: 0.9647

## Training data

Training data was classified as follow:

class |Description
-|-
0 |Not Stressed
1 |Stressed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.704         | 1.0   | 8000  | 0.6933          | 0.5      | 0.3333 | 0.25      | 0.5    |
| 0.6926        | 2.0   | 16000 | 0.6980          | 0.5      | 0.3333 | 0.25      | 0.5    |
| 0.0099        | 3.0   | 24000 | 0.1800          | 0.9647   | 0.9647 | 0.9647    | 0.9647 |
| 0.2727        | 4.0   | 32000 | 0.2243          | 0.9526   | 0.9526 | 0.9527    | 0.9526 |
| 0.0618        | 5.0   | 40000 | 0.2128          | 0.9536   | 0.9536 | 0.9546    | 0.9536 |


### Model performance

-|precision|recall|f1|support
-|-|-|-|-
Not Stressed|0.96|0.97|0.97|10000
Stressed|0.97|0.96|0.97|10000
 | | | |
accuracy|||0.97|20000
macro avg|0.97|0.97|0.97|20000
weighted avg|0.97|0.97|0.97|20000


### How to use roberta-base_topic_classification_nyt_news with HuggingFace

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dstefa/roberta-base_topic_classification_nyt_news")
model = AutoModelForSequenceClassification.from_pretrained("dstefa/roberta-base_topic_classification_nyt_news")
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0)

text = "They also caused so much stress because some leaders valued optics over output."
pipe(text)

[{'label': 'Stressed', 'score': 0.9959163069725037}]

### Framework versions

- Transformers 4.32.1
- Pytorch 2.1.0+cu121
- Datasets 2.12.0
- Tokenizers 0.13.2