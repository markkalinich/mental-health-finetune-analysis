---
license: mit
tags:
- classification
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: clasificador-anorexia-spanish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clasificador-anorexia-spanish

This model is a fine-tuned version of [Recognai/bert-base-spanish-wwm-cased-xnli](https://huggingface.co/Recognai/bert-base-spanish-wwm-cased-xnli) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5353
- Accuracy: 0.7429

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 13   | 0.7172          | 0.5429   |
| No log        | 2.0   | 26   | 0.5772          | 0.7429   |
| No log        | 3.0   | 39   | 0.5353          | 0.7429   |


### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.0+cu118
- Datasets 2.11.0
- Tokenizers 0.13.3
