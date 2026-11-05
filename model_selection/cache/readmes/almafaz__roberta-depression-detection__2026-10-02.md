---
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
model-index:
- name: roberta-depression-detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-depression-detection

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1879

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 9

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0018        | 1.0   | 629  | 0.2864          |
| 0.2759        | 2.0   | 1258 | 0.1503          |
| 0.0554        | 3.0   | 1887 | 0.1445          |
| 0.1117        | 4.0   | 2516 | 0.1508          |
| 0.1942        | 5.0   | 3145 | 0.1208          |
| 0.0018        | 6.0   | 3774 | 0.1527          |
| 0.0017        | 7.0   | 4403 | 0.2258          |
| 0.0747        | 8.0   | 5032 | 0.1818          |
| 0.0006        | 9.0   | 5661 | 0.1879          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.0.1
- Datasets 2.18.0
- Tokenizers 0.15.2
