---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v3-0.4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v3-0.4

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7276

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.4148        | 0.11  | 500   | 1.2099          |
| 1.2472        | 0.21  | 1000  | 1.0718          |
| 1.0935        | 0.32  | 1500  | 0.9924          |
| 1.0193        | 0.43  | 2000  | 0.9482          |
| 0.8859        | 0.54  | 2500  | 0.9335          |
| 0.9838        | 0.64  | 3000  | 0.8792          |
| 0.9195        | 0.75  | 3500  | 0.8665          |
| 0.9793        | 0.86  | 4000  | 0.8397          |
| 0.8513        | 0.96  | 4500  | 0.8215          |
| 0.7384        | 1.07  | 5000  | 0.8261          |
| 0.8117        | 1.18  | 5500  | 0.8028          |
| 0.8606        | 1.28  | 6000  | 0.7930          |
| 0.8139        | 1.39  | 6500  | 0.7873          |
| 0.84          | 1.5   | 7000  | 0.7761          |
| 0.733         | 1.61  | 7500  | 0.7728          |
| 0.7102        | 1.71  | 8000  | 0.7644          |
| 0.6857        | 1.82  | 8500  | 0.7579          |
| 0.7244        | 1.93  | 9000  | 0.7500          |
| 0.5931        | 2.03  | 9500  | 0.7515          |
| 0.6165        | 2.14  | 10000 | 0.7484          |
| 0.6681        | 2.25  | 10500 | 0.7414          |
| 0.6716        | 2.35  | 11000 | 0.7390          |
| 0.6468        | 2.46  | 11500 | 0.7387          |
| 0.5505        | 2.57  | 12000 | 0.7361          |
| 0.635         | 2.68  | 12500 | 0.7333          |
| 0.6632        | 2.78  | 13000 | 0.7297          |
| 0.6271        | 2.89  | 13500 | 0.7278          |
| 0.5843        | 3.0   | 14000 | 0.7276          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.0
