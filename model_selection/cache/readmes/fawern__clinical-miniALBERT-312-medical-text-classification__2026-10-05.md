---
license: mit
base_model: nlpie/clinical-miniALBERT-312
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: clinical-miniALBERT-312-medical-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-miniALBERT-312-medical-text-classification

This model is a fine-tuned version of [nlpie/clinical-miniALBERT-312](https://huggingface.co/nlpie/clinical-miniALBERT-312) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3237
- Accuracy: 0.186
- Precision: 0.1659
- Recall: 0.186
- F1: 0.1736

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 2.8556        | 1.0   | 250  | 2.9403          | 0.221    | 0.0488    | 0.221  | 0.0800 |
| 2.3771        | 2.0   | 500  | 2.6223          | 0.324    | 0.1226    | 0.324  | 0.1772 |
| 2.4809        | 3.0   | 750  | 2.4574          | 0.365    | 0.1918    | 0.365  | 0.2409 |
| 2.3648        | 4.0   | 1000 | 2.4098          | 0.34     | 0.1762    | 0.34   | 0.2241 |
| 2.1697        | 5.0   | 1250 | 2.4202          | 0.346    | 0.2038    | 0.346  | 0.2457 |
| 2.0393        | 6.0   | 1500 | 2.3783          | 0.333    | 0.2220    | 0.333  | 0.2564 |
| 1.8836        | 7.0   | 1750 | 2.3133          | 0.279    | 0.2113    | 0.279  | 0.2289 |
| 1.6791        | 8.0   | 2000 | 2.2241          | 0.256    | 0.2115    | 0.256  | 0.2260 |
| 1.6044        | 9.0   | 2250 | 2.2828          | 0.235    | 0.1965    | 0.235  | 0.2055 |
| 1.4025        | 10.0  | 2500 | 2.3237          | 0.186    | 0.1659    | 0.186  | 0.1736 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
