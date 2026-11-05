---
license: mit
base_model: FacebookAI/roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta_base_classification_model_depression_detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta_base_classification_model_depression_detection

This model is a fine-tuned version of [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0822
- Accuracy: 0.9819
- F1 Score: 0.9828

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
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| No log        | 1.0   | 386  | 0.0517          | 0.9767   | 0.9776   |
| 0.1806        | 2.0   | 773  | 0.0383          | 0.9871   | 0.9878   |
| 0.0668        | 3.0   | 1159 | 0.0614          | 0.9845   | 0.9851   |
| 0.0294        | 3.99  | 1544 | 0.0822          | 0.9819   | 0.9828   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.3.1+cu121
- Datasets 2.20.0
- Tokenizers 0.15.2
