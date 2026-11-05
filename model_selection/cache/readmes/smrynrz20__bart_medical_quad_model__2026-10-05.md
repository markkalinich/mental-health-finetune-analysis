---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: bart_medical_quad_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart_medical_quad_model

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.7185140364032e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 820

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.0           | 0.1220 | 100  | 0.0000          |
| 0.0004        | 0.2439 | 200  | 0.0000          |
| 0.0           | 0.3659 | 300  | 0.0000          |
| 0.0004        | 0.4878 | 400  | 0.0000          |
| 0.0002        | 1.1091 | 500  | 0.0000          |
| 0.0           | 1.2311 | 600  | 0.0000          |
| 0.0001        | 1.3530 | 700  | 0.0000          |
| 0.0001        | 1.475  | 800  | 0.0000          |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
