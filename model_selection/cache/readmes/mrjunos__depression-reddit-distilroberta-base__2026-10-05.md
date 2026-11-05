---
license: apache-2.0
tags:
- text-classification
- depression
- reddit
- generated_from_trainer
datasets:
- mrjunos/depression-reddit-cleaned
metrics:
- accuracy
widget:
- text:
  - >-
    i just found out my boyfriend is depressed i really want to be there for him
    but i feel like i ve only been saying the wrong thing how can i be there for
    him help him and see him get better i m worried it will continue to the
    point it will consume him i can already see his personality changing and i m
    scared for the future what thing can i say or do to comfort or help
  example_title: depression
- text:
  - >-
    i m getting more and more people asking where they can buy the ambients
    album simple answer is quot not yet quot it ll be on itunes eventually
  example_title: not_depression
model-index:
- name: depression-reddit-distilroberta-base
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: mrjunos/depression-reddit-cleaned
      type: depression-reddit-cleaned
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9715578539107951
language:
- en
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

## Example Pipeline

```python
from transformers import pipeline
predict_task = pipeline(model="mrjunos/depression-reddit-distilroberta-base", task="text-classification")
predict_task("Stop listing your issues here, use forum instead or open ticket.")
```
```
[{'label': 'not_depression', 'score': 0.9813856482505798}]
```

Disclaimer: This machine learning model classifies texts related to depression, but I am not an expert or a mental health professional. 
I do not intend to diagnose or offer medical advice. The information provided should not replace consultation with a qualified professional. 
The results may not be accurate. Use this model at your own risk and seek professional advice if needed.

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the [mrjunos/depression-reddit-cleaned dataset](https://huggingface.co/datasets/mrjunos/depression-reddit-cleaned).
It achieves the following results on the evaluation set:
- Loss: 0.0821
- Accuracy: 0.9716

## Model description

This model is a transformer-based model that has been fine-tuned on a dataset of Reddit posts related to depression.
The model can be used to classify posts as either depression or not depression.

## Intended uses & limitations

This model is intended to be used for research purposes. It is not yet ready for production use.
The model has been trained on a dataset of English-language posts, so it may not be accurate for other languages.

## Training and evaluation data

The model was trained on the mrjunos/depression-reddit-cleaned dataset, which contains approximately 7,000 labeled instances.
The data was split into Train and Test using:
```python
ds = ds['train'].train_test_split(test_size=0.2, seed=42)
```
The dataset consists of two main features: 'text' and 'label'. The 'text' feature contains the text data from Reddit posts related to depression, while the 'label' feature indicates whether a post is classified as depression or not.

## Training procedure

You can find here the steps I followed to train this model:
https://github.com/mrjunos/machine_learning/blob/main/NLP-fine_tunning-hugging_face_model.ipynb

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1711        | 0.65  | 500  | 0.0821          | 0.9716   |
| 0.1022        | 1.29  | 1000 | 0.1148          | 0.9709   |
| 0.0595        | 1.94  | 1500 | 0.1178          | 0.9787   |
| 0.0348        | 2.59  | 2000 | 0.0951          | 0.9851   |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.0
- Tokenizers 0.13.3