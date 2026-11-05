---
library_name: transformers
base_model: ccdv/lsg-bart-base-16384
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: pubmed-sum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-sum

This model is a fine-tuned version of [ccdv/lsg-bart-base-16384](https://huggingface.co/ccdv/lsg-bart-base-16384) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1303
- Rouge1: 0.1396
- Rouge2: 0.0651
- Rougel: 0.1198
- Rougelsum: 0.1306

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.6342        | 0.32  | 50   | 2.7400          | 0.1174 | 0.0443 | 0.0971 | 0.1071    |
| 2.9319        | 0.64  | 100  | 2.3386          | 0.1276 | 0.0531 | 0.1071 | 0.1176    |
| 2.5759        | 0.96  | 150  | 2.2462          | 0.1313 | 0.057  | 0.111  | 0.1219    |
| 2.4678        | 1.28  | 200  | 2.1933          | 0.1308 | 0.0581 | 0.1116 | 0.1221    |
| 2.4149        | 1.6   | 250  | 2.1717          | 0.1353 | 0.0608 | 0.115  | 0.1257    |
| 2.3553        | 1.92  | 300  | 2.1303          | 0.1396 | 0.0651 | 0.1198 | 0.1306    |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.0.0
- Datasets 2.15.0
- Tokenizers 0.19.1
