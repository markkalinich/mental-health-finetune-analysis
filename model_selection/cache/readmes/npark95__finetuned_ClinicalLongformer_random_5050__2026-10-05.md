---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_random_5050
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_random_5050

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3124
- F1: 0.8992

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6667        | 1.0   | 38   | 0.3774          | 0.8613 |
| 0.4333        | 2.0   | 76   | 0.3208          | 0.8676 |
| 0.4024        | 3.0   | 114  | 0.3124          | 0.8992 |
| 0.319         | 4.0   | 152  | 0.5367          | 0.7184 |
| 0.2347        | 5.0   | 190  | 0.3385          | 0.8992 |
| 0.1998        | 6.0   | 228  | 0.3858          | 0.8992 |
| 0.1512        | 7.0   | 266  | 0.4332          | 0.8906 |
| 0.1859        | 8.0   | 304  | 0.6245          | 0.8235 |
| 0.2098        | 9.0   | 342  | 0.7375          | 0.8403 |
| 0.1417        | 10.0  | 380  | 0.5302          | 0.8976 |
| 0.0988        | 11.0  | 418  | 0.6191          | 0.88   |
| 0.0744        | 12.0  | 456  | 0.5868          | 0.8976 |
| 0.0084        | 13.0  | 494  | 0.6584          | 0.88   |
| 0.0135        | 14.0  | 532  | 0.6600          | 0.8889 |
| 0.0492        | 15.0  | 570  | 0.6501          | 0.8889 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
