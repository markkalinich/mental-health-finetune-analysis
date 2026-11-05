---
library_name: transformers
license: mit
base_model: Davlan/afro-xlmr-large-76L
tags:
- kinyarwanda
- sentiment
- afrisenti
- afroxlmr
- african-nlp
- generated_from_trainer
metrics:
- f1
- precision
- recall
- accuracy
model-index:
- name: kinyarwanda-sentiment-afroxlmr-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kinyarwanda-sentiment-afroxlmr-large

This model is a fine-tuned version of [Davlan/afro-xlmr-large-76L](https://huggingface.co/Davlan/afro-xlmr-large-76L) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5923
- F1: 0.6921
- Precision: 0.6974
- Recall: 0.6959
- Accuracy: 0.6959

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Precision | Recall | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:---------:|:------:|:--------:|
| 1.6432        | 1.0   | 104  | 0.7593          | 0.6536 | 0.6592    | 0.6578 | 0.6578   |
| 1.4880        | 2.0   | 208  | 0.8054          | 0.6833 | 0.7140    | 0.6880 | 0.6880   |
| 1.0657        | 3.0   | 312  | 0.8070          | 0.6929 | 0.7027    | 0.6989 | 0.6989   |
| 0.8187        | 4.0   | 416  | 0.8961          | 0.6813 | 0.6857    | 0.6844 | 0.6844   |
| 0.5049        | 5.0   | 520  | 1.1145          | 0.6847 | 0.6936    | 0.6868 | 0.6868   |
| 0.4957        | 6.0   | 624  | 1.2119          | 0.6683 | 0.6889    | 0.6711 | 0.6711   |
| 0.2885        | 7.0   | 728  | 1.3918          | 0.6708 | 0.6852    | 0.6723 | 0.6723   |
| 0.2039        | 8.0   | 832  | 1.4049          | 0.6958 | 0.6966    | 0.6953 | 0.6953   |
| 0.2251        | 9.0   | 936  | 1.7742          | 0.6768 | 0.6852    | 0.6832 | 0.6832   |
| 0.2390        | 10.0  | 1040 | 1.7947          | 0.6971 | 0.7043    | 0.6965 | 0.6965   |
| 0.1849        | 11.0  | 1144 | 2.2932          | 0.6795 | 0.6851    | 0.6796 | 0.6796   |
| 0.1306        | 12.0  | 1248 | 2.3704          | 0.6911 | 0.6944    | 0.6917 | 0.6917   |
| 0.1611        | 13.0  | 1352 | 2.2066          | 0.6985 | 0.7060    | 0.6977 | 0.6977   |
| 0.0464        | 14.0  | 1456 | 2.3864          | 0.6887 | 0.6890    | 0.6892 | 0.6892   |
| 0.0953        | 15.0  | 1560 | 2.5195          | 0.6822 | 0.6839    | 0.6820 | 0.6820   |
| 0.0013        | 16.0  | 1664 | 2.4388          | 0.6928 | 0.6944    | 0.6929 | 0.6929   |
| 0.0797        | 17.0  | 1768 | 2.4965          | 0.6997 | 0.7021    | 0.7025 | 0.7025   |
| 0.0576        | 18.0  | 1872 | 2.5354          | 0.6905 | 0.6945    | 0.6904 | 0.6904   |
| 0.0490        | 19.0  | 1976 | 2.6234          | 0.6905 | 0.6955    | 0.6904 | 0.6904   |
| 0.0445        | 20.0  | 2080 | 2.5570          | 0.6905 | 0.6942    | 0.6904 | 0.6904   |


### Framework versions

- Transformers 5.5.4
- Pytorch 2.11.0+cu130
- Datasets 2.21.0
- Tokenizers 0.22.2
