---
pipeline_tag: text-classification
library_name: transformers
license: mit
base_model: roberta-base
tags:
- go_emotions
- emotion
- text-classification
metrics:
- accuracy
- f1
model-index:
- name: emotion_detection_model1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotion_detection_model1

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3724
- Accuracy: 0.5772
- F1: 0.5701

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 1.3216        | 1.0   | 2714 | 1.4223          | 0.5702   | 0.5500 |
| 1.3851        | 2.0   | 5428 | 1.3554          | 0.5820   | 0.5742 |
| 1.0861        | 3.0   | 8142 | 1.3724          | 0.5772   | 0.5701 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.5.1
- Tokenizers 0.21.1
