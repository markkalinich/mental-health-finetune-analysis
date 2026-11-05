---
library_name: transformers
license: cc-by-4.0
base_model: molise-ai/pii-detector-ai4privacy
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: PII_classification_m2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII_classification_m2

This model is a fine-tuned version of [molise-ai/pii-detector-ai4privacy](https://huggingface.co/molise-ai/pii-detector-ai4privacy) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5005
- Precision: 0.2146
- Recall: 0.2053
- F1: 0.2099
- Accuracy: 0.8511

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.533         | 1.0   | 5036  | 0.5103          | 0.1664    | 0.1261 | 0.1435 | 0.8251   |
| 0.458         | 2.0   | 10072 | 0.4788          | 0.1882    | 0.1479 | 0.1656 | 0.8366   |
| 0.3836        | 3.0   | 15108 | 0.4481          | 0.1953    | 0.1572 | 0.1742 | 0.8441   |
| 0.3576        | 4.0   | 20144 | 0.4498          | 0.1925    | 0.1657 | 0.1781 | 0.8439   |
| 0.3189        | 5.0   | 25180 | 0.4445          | 0.2039    | 0.1872 | 0.1952 | 0.8491   |
| 0.2837        | 6.0   | 30216 | 0.4631          | 0.2121    | 0.1956 | 0.2035 | 0.8499   |
| 0.2521        | 7.0   | 35252 | 0.4882          | 0.2144    | 0.2021 | 0.2081 | 0.8516   |
| 0.2303        | 8.0   | 40288 | 0.5005          | 0.2146    | 0.2053 | 0.2099 | 0.8511   |


### Framework versions

- Transformers 4.50.0
- Pytorch 2.6.0+cu124
- Datasets 3.4.1
- Tokenizers 0.21.1
