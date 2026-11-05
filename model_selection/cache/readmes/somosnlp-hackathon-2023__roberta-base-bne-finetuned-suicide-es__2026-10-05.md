---
language:
- es
metrics:
- f1
pipeline_tag: text-classification
datasets:
- hackathon-somos-nlp-2023/suicide-comments-es
license: apache-2.0
---


# Model Description

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) to detect suicidal ideation/behavior in public comments (reddit, forums, twitter, etc.) using the Spanish language.

# How to use

```python
>>> from transformers import pipeline


>>> model_name= 'hackathon-somos-nlp-2023/roberta-base-bne-finetuned-suicide-es'
>>> pipe = pipeline("text-classification", model=model_name)

>>> pipe("Quiero acabar con todo. No merece la pena vivir.")
[{'label': 'Suicide', 'score': 0.9999703168869019}]

>>> pipe("El partido de fútbol fue igualado, disfrutamos mucho jugando juntos.")
[{'label': 'Non-Suicide', 'score': 0.999990701675415}]
```


# Training

## Training data

The dataset consists of comments on Reddit, Twitter, and inputs/outputs of the Alpaca dataset translated to Spanish language and classified as suicidal ideation/behavior and non-suicidal.

The dataset has 10050 rows (777 considered as Suicidal Ideation/Behavior and 9273 considered Non-Suicidal).

More info: https://huggingface.co/datasets/hackathon-somos-nlp-2023/suicide-comments-es

## Training procedure

The training data has been tokenized using the `PlanTL-GOB-ES/roberta-base-bne` tokenizer with a vocabulary size of 50262 tokens and a model maximum length of 512 tokens.

The training lasted a total of 10 minutes using a NVIDIA GPU GeForce RTX 3090 provided by Q Blocks.

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 3090    Off  | 00000000:68:00.0 Off |                  N/A |
| 31%   50C    P8    25W / 250W |      1MiB / 24265MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```


# Considerations for Using the Model

The model is designed for use in Spanish language, specifically to detect suicidal ideation/behavior.

## Limitations

It is a research toy project. Don't expect a professional, bug-free model. We have found some false positives and false negatives. If you find a bug, please send us your feedback.

## Bias

No measures have been taken to estimate the bias and toxicity embedded in the model or dataset. However, the model was fine-tuned using a dataset mainly collected on Reddit, Twitter, and ChatGPT. So there is probably an age bias because [the Internet is used more by younger people](https://www.statista.com/statistics/272365/age-distribution-of-internet-users-worldwide).

In addition, this model inherits biases from its original base model. You can review these biases by visiting the following [link](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne#limitations-and-bias).


# Evaluation


## Metric

F1 = 2 * (precision * recall) / (precision + recall)

## 5 K fold

We use [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html) with `n_splits=5` to evaluate the model.

Results:

```
>>> best_f1_model_by_fold = [0.9163879598662207, 0.9380530973451328, 0.9333333333333333, 0.8943661971830986, 0.9226190476190477]
>>> best_f1_model_by_fold.mean()
0.9209519270693666
```


# Additional Information

## Team

* [dariolopez](https://huggingface.co/dariolopez)
* [diegogd](https://huggingface.co/diegogd)

## Licesing

This work is licensed under a [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Demo (Space)

https://huggingface.co/spaces/hackathon-somos-nlp-2023/suicide-comments-es