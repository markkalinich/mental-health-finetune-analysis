---
library_name: transformers
license: mit
base_model: microsoft/mdeberta-v3-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: piiranha-gretelai-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# piiranha-gretelai-test

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1008
- Precision: 0.6935
- Recall: 0.7739
- F1: 0.7315
- Accuracy: 0.9695

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1561        | 0.3342 | 250  | 0.1173          | 0.6640    | 0.7056 | 0.6842 | 0.9655   |
| 0.102         | 0.6684 | 500  | 0.1009          | 0.6870    | 0.7693 | 0.7258 | 0.9687   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.1
- Tokenizers 0.19.1
