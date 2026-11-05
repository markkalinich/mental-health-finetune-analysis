---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinit_llrd-pubmedbert-tapt-tokenizer-adapted-spanmask-gazetters-lr_3.375
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinit_llrd-pubmedbert-tapt-tokenizer-adapted-spanmask-gazetters-lr_3.375

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1166
- Precision: 0.7920
- Recall: 0.7715
- Micro F1: 0.7816
- Weighted F1: 0.7818
- Macro F1: 0.7901
- Accuracy: 0.9844

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.375114188e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 10472999
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.209         | 1.0   | 1052  | 0.0581          | 0.6379    | 0.7498 | 0.6893   | 0.6901      | 0.7029   | 0.9807   |
| 0.0181        | 2.0   | 2104  | 0.0807          | 0.7924    | 0.7414 | 0.7661   | 0.7659      | 0.7770   | 0.9833   |
| 0.0066        | 3.0   | 3156  | 0.0875          | 0.7264    | 0.7823 | 0.7533   | 0.7549      | 0.7692   | 0.9825   |
| 0.0038        | 4.0   | 4208  | 0.0918          | 0.7941    | 0.7444 | 0.7685   | 0.7688      | 0.7774   | 0.9834   |
| 0.0027        | 5.0   | 5260  | 0.0979          | 0.7869    | 0.7414 | 0.7635   | 0.7635      | 0.7731   | 0.9838   |
| 0.0021        | 6.0   | 6312  | 0.1124          | 0.7767    | 0.7697 | 0.7732   | 0.7734      | 0.7797   | 0.9836   |
| 0.0014        | 7.0   | 7364  | 0.1123          | 0.7435    | 0.7529 | 0.7481   | 0.7484      | 0.7570   | 0.9829   |
| 0.0014        | 8.0   | 8416  | 0.1223          | 0.8030    | 0.7354 | 0.7677   | 0.7678      | 0.7761   | 0.9835   |
| 0.0013        | 9.0   | 9468  | 0.1165          | 0.7920    | 0.7715 | 0.7816   | 0.7818      | 0.7901   | 0.9844   |
| 0.0008        | 10.0  | 10520 | 0.1286          | 0.7992    | 0.7420 | 0.7696   | 0.7697      | 0.7782   | 0.9840   |
| 0.0006        | 11.0  | 11572 | 0.1334          | 0.7507    | 0.7841 | 0.7671   | 0.7672      | 0.7730   | 0.9832   |
| 0.0008        | 12.0  | 12624 | 0.1253          | 0.7833    | 0.7673 | 0.7752   | 0.7752      | 0.7831   | 0.9839   |
| 0.0007        | 13.0  | 13676 | 0.1335          | 0.7885    | 0.7643 | 0.7762   | 0.7763      | 0.7837   | 0.9844   |
| 0.0006        | 14.0  | 14728 | 0.1243          | 0.7595    | 0.7709 | 0.7651   | 0.7654      | 0.7756   | 0.9834   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
