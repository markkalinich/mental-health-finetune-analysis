---
library_name: transformers
license: apache-2.0
base_model: d4data/biomedical-ner-all
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ner-biomedical-maccrobat2018
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ner-biomedical-maccrobat2018

This model is a fine-tuned version of [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6603
- Accuracy: 0.7785

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6521        | 1.0   | 10   | 1.7474          | 0.2525   |
| 1.3889        | 2.0   | 20   | 1.0400          | 0.5568   |
| 0.8632        | 3.0   | 30   | 0.7819          | 0.6695   |
| 0.6142        | 4.0   | 40   | 0.6757          | 0.7196   |
| 0.4609        | 5.0   | 50   | 0.6340          | 0.7401   |
| 0.3611        | 6.0   | 60   | 0.6265          | 0.7547   |
| 0.2924        | 7.0   | 70   | 0.6077          | 0.7491   |
| 0.2378        | 8.0   | 80   | 0.6112          | 0.7546   |
| 0.1974        | 9.0   | 90   | 0.6043          | 0.7605   |
| 0.1725        | 10.0  | 100  | 0.6336          | 0.7565   |
| 0.1493        | 11.0  | 110  | 0.6230          | 0.7685   |
| 0.1311        | 12.0  | 120  | 0.6339          | 0.7693   |
| 0.1168        | 13.0  | 130  | 0.6295          | 0.7748   |
| 0.1061        | 14.0  | 140  | 0.6472          | 0.7700   |
| 0.0975        | 15.0  | 150  | 0.6553          | 0.7731   |
| 0.0914        | 16.0  | 160  | 0.6526          | 0.7773   |
| 0.0864        | 17.0  | 170  | 0.6558          | 0.7755   |
| 0.0823        | 18.0  | 180  | 0.6624          | 0.7740   |
| 0.0813        | 19.0  | 190  | 0.6627          | 0.7778   |
| 0.0786        | 20.0  | 200  | 0.6603          | 0.7785   |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.3.2
- Tokenizers 0.21.0
