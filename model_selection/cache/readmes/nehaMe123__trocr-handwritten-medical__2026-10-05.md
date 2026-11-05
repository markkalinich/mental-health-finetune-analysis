---
license: mit
base_model: microsoft/trocr-base-handwritten
tags:
- generated_from_trainer
model-index:
- name: trocr-handwritten-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trocr-handwritten-medical

This model is a fine-tuned version of [microsoft/trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0924
- Cer: 0.0151

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6097        | 1.0   | 757  | 0.2678          | 0.0534 |
| 0.2218        | 2.0   | 1515 | 0.1831          | 0.0367 |
| 0.1264        | 3.0   | 2272 | 0.1424          | 0.0286 |
| 0.0594        | 4.0   | 3030 | 0.1026          | 0.0165 |
| 0.0239        | 5.0   | 3785 | 0.0924          | 0.0151 |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.8.0+cu126
- Datasets 2.18.0
- Tokenizers 0.15.2
