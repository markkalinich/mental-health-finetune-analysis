---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-combinedData

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0666
- Precision: 0.7764
- Recall: 0.7330
- Micro F1: 0.7541
- Weighted F1: 0.7543
- Macro F1: 0.7609
- Accuracy: 0.9841

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
| 0.2553        | 1.0   | 263  | 0.0633          | 0.5902    | 0.6236 | 0.6064   | 0.6057      | 0.5988   | 0.9792   |
| 0.0427        | 2.0   | 526  | 0.0594          | 0.6966    | 0.6669 | 0.6814   | 0.6825      | 0.6971   | 0.9811   |
| 0.0266        | 3.0   | 789  | 0.0608          | 0.7254    | 0.7258 | 0.7256   | 0.7262      | 0.7433   | 0.9831   |
| 0.0197        | 4.0   | 1052 | 0.0651          | 0.7526    | 0.7282 | 0.7402   | 0.7408      | 0.7515   | 0.9838   |
| 0.0145        | 5.0   | 1315 | 0.0785          | 0.7966    | 0.6711 | 0.7285   | 0.7282      | 0.7385   | 0.9824   |
| 0.0121        | 6.0   | 1578 | 0.0661          | 0.7758    | 0.7324 | 0.7535   | 0.7537      | 0.7604   | 0.9841   |
| 0.0093        | 7.0   | 1841 | 0.0735          | 0.7447    | 0.7438 | 0.7443   | 0.7445      | 0.7498   | 0.9840   |
| 0.0073        | 8.0   | 2104 | 0.0706          | 0.7669    | 0.7360 | 0.7512   | 0.7512      | 0.7548   | 0.9844   |
| 0.006         | 9.0   | 2367 | 0.0791          | 0.7378    | 0.7444 | 0.7411   | 0.7415      | 0.7491   | 0.9834   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
