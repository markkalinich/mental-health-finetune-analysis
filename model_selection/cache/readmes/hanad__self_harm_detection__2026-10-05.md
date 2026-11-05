---
license: apache-2.0
base_model: Falconsai/nsfw_image_detection
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: self_harm_detection
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: test
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.985985985985986
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# self_harm_detection

This model is a fine-tuned version of [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0386
- Accuracy: 0.9860

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:--------:|
| 0.0772        | 0.9984 | 156  | 0.1007          | 0.9580   |
| 0.0351        | 1.9968 | 312  | 0.0557          | 0.9760   |
| 0.0206        | 2.9952 | 468  | 0.0386          | 0.9860   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.3.1+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
