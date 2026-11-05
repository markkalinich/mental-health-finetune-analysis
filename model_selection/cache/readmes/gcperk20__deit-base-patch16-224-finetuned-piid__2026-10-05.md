---
license: apache-2.0
base_model: facebook/deit-base-patch16-224
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: deit-base-patch16-224-finetuned-piid
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: val
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7442922374429224
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deit-base-patch16-224-finetuned-piid

This model is a fine-tuned version of [facebook/deit-base-patch16-224](https://huggingface.co/facebook/deit-base-patch16-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6109
- Accuracy: 0.7443

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.881         | 0.98  | 20   | 0.8373          | 0.6164   |
| 0.5554        | 2.0   | 41   | 0.7144          | 0.7169   |
| 0.509         | 2.98  | 61   | 0.6241          | 0.7489   |
| 0.3925        | 4.0   | 82   | 0.6171          | 0.7352   |
| 0.3738        | 4.88  | 100  | 0.6109          | 0.7443   |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
