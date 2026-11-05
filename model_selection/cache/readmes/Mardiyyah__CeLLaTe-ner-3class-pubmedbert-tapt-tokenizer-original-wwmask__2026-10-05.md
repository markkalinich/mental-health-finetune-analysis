---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-original-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-original-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0993
- Precision: 0.7784
- Recall: 0.7277
- Micro F1: 0.7522
- Weighted F1: 0.7502
- Macro F1: 0.7460
- Accuracy: 0.9821

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.3655        | 1.0   | 263  | 0.0849          | 0.4347    | 0.5664 | 0.4919   | 0.4763      | 0.4434   | 0.9724   |
| 0.0575        | 2.0   | 526  | 0.0630          | 0.7495    | 0.7163 | 0.7325   | 0.7321      | 0.7310   | 0.9817   |
| 0.0351        | 3.0   | 789  | 0.0664          | 0.7160    | 0.7428 | 0.7292   | 0.7294      | 0.7287   | 0.9809   |
| 0.025         | 4.0   | 1052 | 0.0782          | 0.7557    | 0.7038 | 0.7288   | 0.7288      | 0.7265   | 0.9811   |
| 0.0183        | 5.0   | 1315 | 0.0742          | 0.7391    | 0.7298 | 0.7344   | 0.7356      | 0.7353   | 0.9812   |
| 0.0144        | 6.0   | 1578 | 0.0881          | 0.6903    | 0.7033 | 0.6968   | 0.6973      | 0.6958   | 0.9793   |
| 0.0108        | 7.0   | 1841 | 0.0913          | 0.7627    | 0.7330 | 0.7475   | 0.7460      | 0.7423   | 0.9820   |
| 0.0089        | 8.0   | 2104 | 0.0943          | 0.7263    | 0.7402 | 0.7332   | 0.7342      | 0.7346   | 0.9807   |
| 0.0073        | 9.0   | 2367 | 0.1001          | 0.7784    | 0.7277 | 0.7522   | 0.7502      | 0.7460   | 0.9821   |
| 0.0066        | 10.0  | 2630 | 0.0983          | 0.7722    | 0.7199 | 0.7452   | 0.7439      | 0.7410   | 0.9821   |
| 0.0055        | 11.0  | 2893 | 0.1044          | 0.7648    | 0.7345 | 0.7493   | 0.7482      | 0.7450   | 0.9820   |
| 0.0045        | 12.0  | 3156 | 0.1074          | 0.7375    | 0.7574 | 0.7473   | 0.7473      | 0.7456   | 0.9817   |
| 0.0041        | 13.0  | 3419 | 0.1140          | 0.7471    | 0.7413 | 0.7442   | 0.7428      | 0.7413   | 0.9816   |
| 0.0036        | 14.0  | 3682 | 0.1136          | 0.7493    | 0.7361 | 0.7426   | 0.7425      | 0.7416   | 0.9818   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
