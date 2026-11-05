---
library_name: transformers
tags:
- transformers
- nlp
- fine-tuned
- english
- sentiment-analysis
- text-classification
- roBERTa
model-index:
- name: tw-roberta-base-sentiment-FT
  results: []
datasets:
- Sp1786/multiclass-sentiment-analysis-dataset
language:
- en
base_model:
- cardiffnlp/twitter-roberta-base-sentiment
metrics:
- accuracy
- precision
- recall
- f1
pipeline_tag: text-classification
---


# tw-roberta-base-sentiment-FT

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) on the dataset [Sp1786/multiclass-sentiment-analysis-dataset] (https://huggingface.co/datasets/Sp1786/multiclass-sentiment-analysis-dataset).

The text classification task in this model is based on 3 sentiment labels.

## Full classification example:

```python
from transformers import pipeline

pipe = pipeline(model="delarosajav95/tw-roberta-base-sentiment-FT")
inputs = ["The flat is very nice but it's too expensive and the location is very bad.",
          "I loved the music, but the crowd was too rowdy to enjoy it properly.",
          "They believe that I'm stupid and I like waiting for hours in line to buy a simple coffee."
]
result = pipe(inputs, return_all_scores=True)

label_mapping = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}
for i, predictions in enumerate(result):
  print("==================================")
  print(f"Text {i + 1}: {inputs[i]}")
  for pred in predictions:
    label = label_mapping.get(pred['label'], pred['label'])
    score = pred['score']
    print(f"{label}: {score:.2%}")
```

Output:

```python
==================================
Text 1: The flat is very nice but it's too expensive and the location is very bad.
Negative: 0.09%
Neutral: 99.88%
Positive: 0.03%
==================================
Text 2: I loved the music, but the crowd was too rowdy to enjoy it properly.
Negative: 0.04%
Neutral: 99.92%
Positive: 0.04%
==================================
Text 3: They believe that I'm stupid and I like waiting for hours in line to buy a simple coffee.
Negative: 69.79%
Neutral: 30.12%
Positive: 0.09%
```

## Metrics and results:

It achieves the following results on the evaluation set:
- eval_loss: 0.8834
- eval_model_preparation_time: 0.0061
- eval_accuracy: 0.7655
- eval_precision: 0.7636
- eval_recall: 0.7655
- eval_f1: 0.7635
- eval_runtime: 24.6425
- eval_samples_per_second: 211.261
- eval_steps_per_second: 13.229

## Training Details and Procedure

### Main Hyperparameters:

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 8

### Framework versions

- Transformers 4.47.0
- Pytorch 2.5.1+cu121
- Datasets 3.2.0
- Tokenizers 0.21.0

## CITATION:

```bibitex 
@inproceedings{barbieri-etal-2020-tweeteval,
    title = "{T}weet{E}val: Unified Benchmark and Comparative Evaluation for Tweet Classification",
    author = "Barbieri, Francesco  and
      Camacho-Collados, Jose  and
      Espinosa Anke, Luis  and
      Neves, Leonardo",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.148",
    doi = "10.18653/v1/2020.findings-emnlp.148",
    pages = "1644--1650"
}
```

## More Information

- Fine-tuned by Javier de la Rosa.
- javier.delarosa95@gmail.com
- https://www.linkedin.com/in/delarosajav95/