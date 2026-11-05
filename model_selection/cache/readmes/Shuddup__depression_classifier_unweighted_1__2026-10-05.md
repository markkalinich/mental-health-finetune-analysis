---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: depression_classifier_unweighted_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depression_classifier_unweighted_1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0985
- F1: {'f1': 0.5363494361475553}
- Accuracy: {'accuracy': 0.6129429892141757}

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1                         | Accuracy                         |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------:|:--------------------------------:|
| No log        | 1.0   | 451  | 0.7291          | {'f1': 0.5311371197568231} | {'accuracy': 0.6604006163328198} |
| 0.7994        | 2.0   | 902  | 0.7153          | {'f1': 0.5663643865301549} | {'accuracy': 0.6619414483821263} |
| 0.6758        | 3.0   | 1353 | 0.7708          | {'f1': 0.5549493182827706} | {'accuracy': 0.6428351309707242} |
| 0.5489        | 4.0   | 1804 | 0.9657          | {'f1': 0.5398498068923226} | {'accuracy': 0.6061633281972265} |
| 0.4078        | 5.0   | 2255 | 1.0339          | {'f1': 0.5356239241887982} | {'accuracy': 0.6138674884437596} |
| 0.3112        | 6.0   | 2706 | 1.0985          | {'f1': 0.5363494361475553} | {'accuracy': 0.6129429892141757} |


### Framework versions

- Transformers 4.28.0
- Pytorch 2.0.1+cu118
- Datasets 2.12.0
- Tokenizers 0.13.3
