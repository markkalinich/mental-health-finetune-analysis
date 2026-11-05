---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1032
- Precision: 0.7757
- Recall: 0.7571
- Micro F1: 0.7663
- Weighted F1: 0.7667
- Macro F1: 0.7765
- Accuracy: 0.9842

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
| 0.2519        | 1.0   | 263  | 0.0602          | 0.6575    | 0.6927 | 0.6747   | 0.6752      | 0.6828   | 0.9817   |
| 0.041         | 2.0   | 526  | 0.0563          | 0.7232    | 0.7150 | 0.7191   | 0.7203      | 0.7373   | 0.9823   |
| 0.0265        | 3.0   | 789  | 0.0593          | 0.7150    | 0.7348 | 0.7248   | 0.7258      | 0.7434   | 0.9826   |
| 0.0195        | 4.0   | 1052 | 0.0623          | 0.7512    | 0.7318 | 0.7414   | 0.7415      | 0.7493   | 0.9832   |
| 0.0147        | 5.0   | 1315 | 0.0719          | 0.7758    | 0.6867 | 0.7285   | 0.7285      | 0.7360   | 0.9823   |
| 0.0121        | 6.0   | 1578 | 0.0624          | 0.7512    | 0.7462 | 0.7487   | 0.7489      | 0.7541   | 0.9841   |
| 0.009         | 7.0   | 1841 | 0.0771          | 0.7665    | 0.7402 | 0.7531   | 0.7533      | 0.7609   | 0.9835   |
| 0.0067        | 8.0   | 2104 | 0.0754          | 0.7677    | 0.7372 | 0.7521   | 0.7521      | 0.7567   | 0.9834   |
| 0.006         | 9.0   | 2367 | 0.0819          | 0.7209    | 0.7673 | 0.7434   | 0.7441      | 0.7558   | 0.9830   |
| 0.0047        | 10.0  | 2630 | 0.0844          | 0.7631    | 0.7420 | 0.7524   | 0.7529      | 0.7649   | 0.9838   |
| 0.0037        | 11.0  | 2893 | 0.0870          | 0.7586    | 0.7595 | 0.7590   | 0.7596      | 0.7697   | 0.9837   |
| 0.0036        | 12.0  | 3156 | 0.0877          | 0.7702    | 0.7498 | 0.7599   | 0.7604      | 0.7713   | 0.9841   |
| 0.0028        | 13.0  | 3419 | 0.1001          | 0.7598    | 0.7589 | 0.7593   | 0.7595      | 0.7693   | 0.9833   |
| 0.0025        | 14.0  | 3682 | 0.0959          | 0.7585    | 0.7517 | 0.7551   | 0.7556      | 0.7659   | 0.9839   |
| 0.0024        | 15.0  | 3945 | 0.0981          | 0.7618    | 0.7541 | 0.7579   | 0.7586      | 0.7712   | 0.9839   |
| 0.0019        | 16.0  | 4208 | 0.0988          | 0.7592    | 0.7565 | 0.7578   | 0.7584      | 0.7686   | 0.9837   |
| 0.0019        | 17.0  | 4471 | 0.1003          | 0.7854    | 0.7462 | 0.7653   | 0.7657      | 0.7763   | 0.9844   |
| 0.0017        | 18.0  | 4734 | 0.1010          | 0.7725    | 0.7595 | 0.7659   | 0.7662      | 0.7748   | 0.9840   |
| 0.0015        | 19.0  | 4997 | 0.1042          | 0.7792    | 0.7535 | 0.7661   | 0.7665      | 0.7763   | 0.9842   |
| 0.0016        | 20.0  | 5260 | 0.1037          | 0.7762    | 0.7571 | 0.7665   | 0.7669      | 0.7767   | 0.9842   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
