---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v3-0.5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v3-0.5

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8977

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
| 1.6463        | 0.11  | 500   | 1.4928          |
| 1.4367        | 0.21  | 1000  | 1.3112          |
| 1.3415        | 0.32  | 1500  | 1.2125          |
| 1.2466        | 0.43  | 2000  | 1.1661          |
| 1.1417        | 0.54  | 2500  | 1.1133          |
| 1.1749        | 0.64  | 3000  | 1.0694          |
| 1.1272        | 0.75  | 3500  | 1.0524          |
| 1.1683        | 0.86  | 4000  | 1.0289          |
| 1.0353        | 0.96  | 4500  | 1.0149          |
| 0.9557        | 1.07  | 5000  | 1.0026          |
| 0.9627        | 1.18  | 5500  | 0.9882          |
| 0.9371        | 1.28  | 6000  | 0.9813          |
| 0.9498        | 1.39  | 6500  | 0.9642          |
| 0.9903        | 1.5   | 7000  | 0.9578          |
| 0.9031        | 1.61  | 7500  | 0.9493          |
| 0.8613        | 1.71  | 8000  | 0.9403          |
| 0.8746        | 1.82  | 8500  | 0.9345          |
| 0.8455        | 1.93  | 9000  | 0.9277          |
| 0.7622        | 2.03  | 9500  | 0.9284          |
| 0.7276        | 2.14  | 10000 | 0.9206          |
| 0.7861        | 2.25  | 10500 | 0.9218          |
| 0.8205        | 2.35  | 11000 | 0.9181          |
| 0.7348        | 2.46  | 11500 | 0.9092          |
| 0.792         | 2.57  | 12000 | 0.9061          |
| 0.7531        | 2.68  | 12500 | 0.9034          |
| 0.7652        | 2.78  | 13000 | 0.9013          |
| 0.7635        | 2.89  | 13500 | 0.8974          |
| 0.7748        | 3.0   | 14000 | 0.8977          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.0
