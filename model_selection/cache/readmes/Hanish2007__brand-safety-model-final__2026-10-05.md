---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: brand-safety-model-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# brand-safety-model-final

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4598
- Accuracy: 0.8687

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5747        | 1.0   | 117  | 1.3370          | 0.7036   |
| 0.8113        | 2.0   | 234  | 0.7907          | 0.8053   |
| 0.6805        | 3.0   | 351  | 0.6142          | 0.8440   |
| 0.45          | 4.0   | 468  | 0.5336          | 0.8634   |
| 0.3497        | 5.0   | 585  | 0.4891          | 0.8644   |
| 0.3291        | 6.0   | 702  | 0.4719          | 0.8650   |
| 0.2382        | 7.0   | 819  | 0.4598          | 0.8687   |
| 0.2162        | 8.0   | 936  | 0.4764          | 0.8666   |
| 0.2298        | 9.0   | 1053 | 0.4859          | 0.8661   |
| 0.1703        | 10.0  | 1170 | 0.4737          | 0.8666   |
| 0.1245        | 11.0  | 1287 | 0.4816          | 0.8677   |
| 0.163         | 12.0  | 1404 | 0.4938          | 0.8666   |
| 0.1211        | 13.0  | 1521 | 0.4862          | 0.8661   |
| 0.1067        | 14.0  | 1638 | 0.4977          | 0.8650   |
| 0.1269        | 15.0  | 1755 | 0.4906          | 0.8677   |


### Framework versions

- Transformers 4.46.3
- Pytorch 2.4.0
- Datasets 2.20.0
- Tokenizers 0.20.3
