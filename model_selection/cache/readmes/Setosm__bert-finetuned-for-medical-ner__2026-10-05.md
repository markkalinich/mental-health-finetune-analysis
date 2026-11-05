---
library_name: transformers
language:
- en
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- medical-ner
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bert-finetuned-for-medical-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-for-medical-ner

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the PLODv2-filtered dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1344
- Accuracy: 0.9402
- Precision: 0.8342
- Recall: 0.9029
- F1: 0.8672

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 2
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:------:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.2039        | 0.1420 | 2000  | 0.1873          | 0.9244   | 0.7841    | 0.8773 | 0.8281 |
| 0.1758        | 0.2841 | 4000  | 0.1613          | 0.9302   | 0.8028    | 0.8920 | 0.8451 |
| 0.1585        | 0.4261 | 6000  | 0.1499          | 0.9343   | 0.8309    | 0.8721 | 0.8510 |
| 0.1613        | 0.5681 | 8000  | 0.1460          | 0.9358   | 0.8400    | 0.8655 | 0.8526 |
| 0.1526        | 0.7101 | 10000 | 0.1402          | 0.9382   | 0.8329    | 0.8930 | 0.8619 |
| 0.1502        | 0.8522 | 12000 | 0.1357          | 0.9394   | 0.8346    | 0.8985 | 0.8654 |
| 0.1486        | 0.9942 | 14000 | 0.1344          | 0.9402   | 0.8342    | 0.9029 | 0.8672 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
