---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinit-llrd-pubmedbert-tapt-tokenizer-adapted_wr-0.06
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinit-llrd-pubmedbert-tapt-tokenizer-adapted_wr-0.06

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5) on the OTAR3088/CeLLaTe_V3.2_contracted_ent_IOB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0727
- Precision: 0.7829
- Recall: 0.7168
- F1: 0.7484
- Accuracy: 0.9837

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3696        | 1.0   | 263  | 0.0713          | 0.4648    | 0.5377 | 0.4986 | 0.9744   |
| 0.0449        | 2.0   | 526  | 0.0586          | 0.7649    | 0.6838 | 0.7221 | 0.9829   |
| 0.026         | 3.0   | 789  | 0.0557          | 0.7508    | 0.7234 | 0.7368 | 0.9828   |
| 0.017         | 4.0   | 1052 | 0.0665          | 0.7527    | 0.7144 | 0.7330 | 0.9832   |
| 0.012         | 5.0   | 1315 | 0.0724          | 0.7829    | 0.7168 | 0.7484 | 0.9837   |
| 0.0093        | 6.0   | 1578 | 0.0822          | 0.7435    | 0.6856 | 0.7134 | 0.9816   |
| 0.0068        | 7.0   | 1841 | 0.0859          | 0.7765    | 0.7054 | 0.7393 | 0.9833   |
| 0.005         | 8.0   | 2104 | 0.0925          | 0.7959    | 0.7054 | 0.7479 | 0.9831   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
