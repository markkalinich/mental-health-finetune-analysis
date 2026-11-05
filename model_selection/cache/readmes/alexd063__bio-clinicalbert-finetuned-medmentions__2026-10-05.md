---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bio-clinicalbert-finetuned-medmentions
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bio-clinicalbert-finetuned-medmentions

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the Ben10x/MedMentions-MTI881-NER dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6913
- Precision: 0.631
- Recall: 0.673
- F1: 0.652
- Accuracy: 0.886

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1    | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:-----:|:--------:|
| 0.9448        | 1.0   | 1463  | 0.6638          | 0.438     | 0.407  | 0.422 | 0.821    |
| 0.5448        | 2.0   | 2926  | 0.5070          | 0.515     | 0.547  | 0.531 | 0.845    |
| 0.4231        | 3.0   | 4389  | 0.4480          | 0.562     | 0.564  | 0.563 | 0.86     |
| 0.3301        | 4.0   | 5852  | 0.4261          | 0.578     | 0.604  | 0.591 | 0.866    |
| 0.2689        | 5.0   | 7315  | 0.4284          | 0.606     | 0.604  | 0.605 | 0.872    |
| 0.2147        | 6.0   | 8778  | 0.4410          | 0.607     | 0.632  | 0.62  | 0.875    |
| 0.1667        | 7.0   | 10241 | 0.4644          | 0.613     | 0.618  | 0.616 | 0.876    |
| 0.1304        | 8.0   | 11704 | 0.4982          | 0.61      | 0.646  | 0.627 | 0.878    |
| 0.1055        | 9.0   | 13167 | 0.5311          | 0.617     | 0.645  | 0.631 | 0.877    |
| 0.0826        | 10.0  | 14630 | 0.5643          | 0.629     | 0.64   | 0.635 | 0.88     |
| 0.0665        | 11.0  | 16093 | 0.5907          | 0.616     | 0.657  | 0.636 | 0.879    |
| 0.0537        | 12.0  | 17556 | 0.6218          | 0.629     | 0.653  | 0.64  | 0.882    |
| 0.0445        | 13.0  | 19019 | 0.6575          | 0.615     | 0.665  | 0.639 | 0.88     |
| 0.0375        | 14.0  | 20482 | 0.6699          | 0.621     | 0.66   | 0.64  | 0.881    |
| 0.0323        | 15.0  | 21945 | 0.6914          | 0.626     | 0.664  | 0.645 | 0.882    |
| 0.0275        | 16.0  | 23408 | 0.7028          | 0.628     | 0.665  | 0.646 | 0.882    |
| 0.0265        | 17.0  | 24871 | 0.7139          | 0.628     | 0.663  | 0.645 | 0.883    |
| 0.0242        | 18.0  | 26334 | 0.7184          | 0.629     | 0.662  | 0.645 | 0.882    |
| 0.0220        | 19.0  | 27797 | 0.7228          | 0.627     | 0.664  | 0.645 | 0.882    |


### Framework versions

- Transformers 5.8.1
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
