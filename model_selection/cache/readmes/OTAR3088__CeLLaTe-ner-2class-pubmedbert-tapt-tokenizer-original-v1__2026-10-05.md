---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original_v1
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe-ner-pubmedbert-tapt-tokenizer-original-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-pubmedbert-tapt-tokenizer-original-v1

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original_v1](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original_v1) on the OTAR3088/CeLLaTe_V3.2_contracted_ent_IOB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0903
- Precision: 0.7608
- Recall: 0.7822
- F1: 0.7714
- Accuracy: 0.9843

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2524        | 1.0   | 263  | 0.0598          | 0.6303    | 0.7322 | 0.6774 | 0.9803   |
| 0.0407        | 2.0   | 526  | 0.0543          | 0.7798    | 0.6955 | 0.7352 | 0.9832   |
| 0.0261        | 3.0   | 789  | 0.0642          | 0.7939    | 0.6840 | 0.7348 | 0.9829   |
| 0.0191        | 4.0   | 1052 | 0.0609          | 0.7444    | 0.7444 | 0.7444 | 0.9836   |
| 0.0146        | 5.0   | 1315 | 0.0656          | 0.7728    | 0.7328 | 0.7523 | 0.9836   |
| 0.0109        | 6.0   | 1578 | 0.0809          | 0.7779    | 0.6943 | 0.7337 | 0.9828   |
| 0.0086        | 7.0   | 1841 | 0.0755          | 0.7599    | 0.7529 | 0.7564 | 0.9845   |
| 0.0071        | 8.0   | 2104 | 0.0821          | 0.7759    | 0.7267 | 0.7505 | 0.9837   |
| 0.0057        | 9.0   | 2367 | 0.0839          | 0.7625    | 0.7523 | 0.7574 | 0.9841   |
| 0.0048        | 10.0  | 2630 | 0.0929          | 0.7965    | 0.7163 | 0.7543 | 0.9839   |
| 0.0042        | 11.0  | 2893 | 0.0891          | 0.7626    | 0.7450 | 0.7537 | 0.9839   |
| 0.0035        | 12.0  | 3156 | 0.0903          | 0.7754    | 0.7413 | 0.7580 | 0.9845   |
| 0.003         | 13.0  | 3419 | 0.0904          | 0.7608    | 0.7822 | 0.7714 | 0.9843   |
| 0.0027        | 14.0  | 3682 | 0.0973          | 0.7916    | 0.7395 | 0.7647 | 0.9842   |
| 0.0023        | 15.0  | 3945 | 0.0989          | 0.7783    | 0.7474 | 0.7625 | 0.9845   |
| 0.002         | 16.0  | 4208 | 0.1045          | 0.7854    | 0.7547 | 0.7698 | 0.9846   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
