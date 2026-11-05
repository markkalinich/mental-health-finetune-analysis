---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-original-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-original-spanmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0797
- Precision: 0.7923
- Recall: 0.7285
- Micro F1: 0.7591
- Weighted F1: 0.7590
- Macro F1: 0.7671
- Accuracy: 0.9838

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
| 0.2444        | 1.0   | 263  | 0.0630          | 0.5922    | 0.7267 | 0.6526   | 0.6546      | 0.6663   | 0.9787   |
| 0.0414        | 2.0   | 526  | 0.0545          | 0.7804    | 0.7157 | 0.7467   | 0.7467      | 0.7529   | 0.9834   |
| 0.0262        | 3.0   | 789  | 0.0608          | 0.7595    | 0.7285 | 0.7437   | 0.7439      | 0.7511   | 0.9832   |
| 0.0198        | 4.0   | 1052 | 0.0625          | 0.7483    | 0.7383 | 0.7432   | 0.7436      | 0.7507   | 0.9836   |
| 0.014         | 5.0   | 1315 | 0.0738          | 0.7883    | 0.7157 | 0.7502   | 0.7503      | 0.7588   | 0.9834   |
| 0.0114        | 6.0   | 1578 | 0.0727          | 0.7590    | 0.7187 | 0.7383   | 0.7386      | 0.7465   | 0.9831   |
| 0.0088        | 7.0   | 1841 | 0.0766          | 0.7602    | 0.7407 | 0.7503   | 0.7505      | 0.7602   | 0.9836   |
| 0.0066        | 8.0   | 2104 | 0.0795          | 0.7916    | 0.7279 | 0.7584   | 0.7584      | 0.7667   | 0.9838   |
| 0.0055        | 9.0   | 2367 | 0.0845          | 0.7180    | 0.7736 | 0.7448   | 0.7459      | 0.7581   | 0.9829   |
| 0.0047        | 10.0  | 2630 | 0.0895          | 0.7877    | 0.7175 | 0.7510   | 0.7510      | 0.7554   | 0.9839   |
| 0.0038        | 11.0  | 2893 | 0.0861          | 0.7614    | 0.7261 | 0.7433   | 0.7436      | 0.7509   | 0.9842   |
| 0.0033        | 12.0  | 3156 | 0.1008          | 0.7880    | 0.7053 | 0.7444   | 0.7444      | 0.7563   | 0.9836   |
| 0.0027        | 13.0  | 3419 | 0.0966          | 0.7549    | 0.7309 | 0.7427   | 0.7429      | 0.7474   | 0.9834   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
