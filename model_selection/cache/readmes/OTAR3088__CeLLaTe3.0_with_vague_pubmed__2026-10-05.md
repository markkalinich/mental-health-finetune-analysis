---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe3.0_with_vague_pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.0_with_vague_pubmed

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3131
- Precision: 0.7557
- Recall: 0.8103
- F1: 0.7821
- Accuracy: 0.9648

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
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.7676        | 1.0   | 403  | 0.1896          | 0.4931    | 0.6667 | 0.5669 | 0.9484   |
| 0.1364        | 2.0   | 806  | 0.1445          | 0.6858    | 0.7643 | 0.7229 | 0.9613   |
| 0.0731        | 3.0   | 1209 | 0.1694          | 0.6925    | 0.7972 | 0.7412 | 0.9608   |
| 0.0395        | 4.0   | 1612 | 0.2014          | 0.7222    | 0.7714 | 0.7460 | 0.9629   |
| 0.0256        | 5.0   | 2015 | 0.2258          | 0.6952    | 0.7484 | 0.7208 | 0.9598   |
| 0.0146        | 6.0   | 2418 | 0.2429          | 0.7083    | 0.8047 | 0.7534 | 0.9619   |
| 0.0104        | 7.0   | 2821 | 0.2540          | 0.7144    | 0.7939 | 0.7521 | 0.9631   |
| 0.007         | 8.0   | 3224 | 0.2652          | 0.7238    | 0.7714 | 0.7468 | 0.9633   |
| 0.0054        | 9.0   | 3627 | 0.2546          | 0.7247    | 0.7958 | 0.7586 | 0.9638   |
| 0.0041        | 10.0  | 4030 | 0.2641          | 0.7398    | 0.7930 | 0.7655 | 0.9648   |
| 0.0028        | 11.0  | 4433 | 0.3089          | 0.7047    | 0.7732 | 0.7374 | 0.9612   |
| 0.0023        | 12.0  | 4836 | 0.3026          | 0.7031    | 0.7681 | 0.7341 | 0.9615   |
| 0.0023        | 13.0  | 5239 | 0.2905          | 0.7410    | 0.7967 | 0.7679 | 0.9643   |
| 0.0018        | 14.0  | 5642 | 0.3225          | 0.7278    | 0.7718 | 0.7491 | 0.9622   |
| 0.0014        | 15.0  | 6045 | 0.3014          | 0.7595    | 0.7915 | 0.7752 | 0.9648   |
| 0.0013        | 16.0  | 6448 | 0.3055          | 0.7409    | 0.7962 | 0.7676 | 0.9638   |
| 0.0009        | 17.0  | 6851 | 0.3146          | 0.7488    | 0.7977 | 0.7724 | 0.9639   |
| 0.0008        | 18.0  | 7254 | 0.3058          | 0.7519    | 0.8066 | 0.7783 | 0.9647   |
| 0.0007        | 19.0  | 7657 | 0.3073          | 0.7514    | 0.8061 | 0.7778 | 0.9647   |
| 0.0006        | 20.0  | 8060 | 0.3135          | 0.7557    | 0.8103 | 0.7821 | 0.9648   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
