---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: pubmedbert-abstract
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmedbert-abstract

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4618
- Accuracy: 0.9501

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
- train_batch_size: 32
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| No log        | 1.0   | 791   | 0.2340          | 0.9386   |
| 0.1776        | 2.0   | 1582  | 0.2716          | 0.9419   |
| 0.0855        | 3.0   | 2373  | 0.2730          | 0.9431   |
| 0.0627        | 4.0   | 3164  | 0.3323          | 0.9382   |
| 0.0627        | 5.0   | 3955  | 0.3308          | 0.9451   |
| 0.0463        | 6.0   | 4746  | 0.3986          | 0.9412   |
| 0.0308        | 7.0   | 5537  | 0.4211          | 0.9419   |
| 0.0312        | 8.0   | 6328  | 0.3616          | 0.9437   |
| 0.0221        | 9.0   | 7119  | 0.4310          | 0.9396   |
| 0.0221        | 10.0  | 7910  | 0.4222          | 0.9438   |
| 0.0181        | 11.0  | 8701  | 0.4185          | 0.9445   |
| 0.0141        | 12.0  | 9492  | 0.4678          | 0.9456   |
| 0.0133        | 13.0  | 10283 | 0.4027          | 0.9503   |
| 0.0082        | 14.0  | 11074 | 0.4504          | 0.9473   |
| 0.0082        | 15.0  | 11865 | 0.4760          | 0.9505   |
| 0.0052        | 16.0  | 12656 | 0.4573          | 0.9449   |
| 0.0042        | 17.0  | 13447 | 0.4356          | 0.9522   |
| 0.0037        | 18.0  | 14238 | 0.4577          | 0.9487   |
| 0.0024        | 19.0  | 15029 | 0.4642          | 0.9493   |
| 0.0024        | 20.0  | 15820 | 0.4618          | 0.9501   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu118
- Datasets 2.18.0
- Tokenizers 0.15.2
