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
- name: bio-clinicalbert-finetuned-medmentions-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bio-clinicalbert-finetuned-medmentions-v1

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the Ben10x/MedMentions-MTI881-NER dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6961
- Precision: 0.599
- Recall: 0.714
- F1: 0.652
- Accuracy: 0.877

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
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
| 2.0211        | 1.0   | 1463  | 1.2990          | 0.181     | 0.441  | 0.256 | 0.609    |
| 1.0855        | 2.0   | 2926  | 1.0143          | 0.23      | 0.519  | 0.318 | 0.656    |
| 0.7216        | 3.0   | 4389  | 1.0351          | 0.256     | 0.537  | 0.346 | 0.668    |
| 0.4696        | 4.0   | 5852  | 0.9641          | 0.292     | 0.601  | 0.393 | 0.698    |
| 0.3200        | 5.0   | 7315  | 1.0366          | 0.342     | 0.639  | 0.445 | 0.746    |
| 0.2432        | 6.0   | 8778  | 1.1099          | 0.356     | 0.678  | 0.467 | 0.76     |
| 0.1669        | 7.0   | 10241 | 1.2021          | 0.379     | 0.681  | 0.487 | 0.774    |
| 0.1375        | 8.0   | 11704 | 1.3615          | 0.422     | 0.69   | 0.524 | 0.804    |
| 0.1036        | 9.0   | 13167 | 1.4416          | 0.439     | 0.686  | 0.535 | 0.812    |
| 0.0831        | 10.0  | 14630 | 1.5576          | 0.451     | 0.706  | 0.55  | 0.82     |
| 0.0604        | 11.0  | 16093 | 1.7574          | 0.492     | 0.718  | 0.584 | 0.842    |
| 0.0438        | 12.0  | 17556 | 1.7740          | 0.504     | 0.712  | 0.59  | 0.845    |
| 0.0334        | 13.0  | 19019 | 1.9544          | 0.521     | 0.713  | 0.602 | 0.851    |
| 0.0252        | 14.0  | 20482 | 2.1627          | 0.541     | 0.719  | 0.617 | 0.859    |
| 0.0214        | 15.0  | 21945 | 2.2473          | 0.56      | 0.72   | 0.63  | 0.866    |
| 0.0160        | 16.0  | 23408 | 2.3725          | 0.569     | 0.716  | 0.634 | 0.869    |
| 0.0137        | 17.0  | 24871 | 2.4949          | 0.587     | 0.711  | 0.643 | 0.873    |
| 0.0118        | 18.0  | 26334 | 2.5750          | 0.594     | 0.709  | 0.646 | 0.875    |
| 0.0109        | 19.0  | 27797 | 2.5828          | 0.596     | 0.712  | 0.649 | 0.876    |
| 0.0099        | 20.0  | 29260 | 2.5898          | 0.595     | 0.711  | 0.648 | 0.876    |


### Framework versions

- Transformers 5.8.1
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
