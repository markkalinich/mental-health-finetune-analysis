---
license: apache-2.0
tags:
- generated_from_trainer
- code
metrics:
- accuracy
model-index:
- name: moderate_severe_depression_model
  results: []
datasets:
- christinacdl/balanced_depression_dataset
language:
- en
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# moderate_severe_depression_model

This model is a fine-tuned version of [allenai/longformer-scico](https://huggingface.co/allenai/longformer-scico) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4276
- Macro F1: 0.8927
- Accuracy: 0.8932

Results on Test set:

-Accuracy: 0.8817204301075269

-F1 score: 0.8819253137510324 

-Precision: 0.8855477220587717

-Recall : 0.8817204301075269

-Matthews Correlation Coefficient: 0.8242972089300715

-Precision of each class: [0.98420129 0.85636693 0.81607495]

-Recall of each class: [0.93548387 0.78921023 0.92046719]

-F1 score of each class: [0.95922441 0.82141823 0.8651333 ]

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 12
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.3476        | 1.0   | 1798 | 0.3343          | 0.8765   | 0.8782   |
| 0.2658        | 2.0   | 3596 | 0.3190          | 0.8856   | 0.8859   |
| 0.2157        | 3.0   | 5394 | 0.3607          | 0.8938   | 0.8939   |
| 0.1749        | 4.0   | 7192 | 0.4276          | 0.8927   | 0.8932   |


### Framework versions

- Transformers 4.27.1
- Pytorch 2.0.1+cu118
- Datasets 2.9.0
- Tokenizers 0.13.3