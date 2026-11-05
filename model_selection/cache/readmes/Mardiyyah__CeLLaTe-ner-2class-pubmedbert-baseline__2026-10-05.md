---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-baseline

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1003
- Precision: 0.7763
- Recall: 0.7431
- Micro F1: 0.7594
- Weighted F1: 0.7596
- Macro F1: 0.7690
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
| 0.2498        | 1.0   | 263  | 0.0637          | 0.6194    | 0.7517 | 0.6792   | 0.6827      | 0.7051   | 0.9791   |
| 0.0412        | 2.0   | 526  | 0.0568          | 0.7413    | 0.7114 | 0.7260   | 0.7269      | 0.7388   | 0.9823   |
| 0.0268        | 3.0   | 789  | 0.0633          | 0.7183    | 0.6785 | 0.6978   | 0.6978      | 0.6973   | 0.9809   |
| 0.0199        | 4.0   | 1052 | 0.0655          | 0.7478    | 0.7200 | 0.7336   | 0.7345      | 0.7464   | 0.9826   |
| 0.0148        | 5.0   | 1315 | 0.0713          | 0.7721    | 0.7029 | 0.7359   | 0.7358      | 0.7406   | 0.9828   |
| 0.0119        | 6.0   | 1578 | 0.0724          | 0.7591    | 0.7364 | 0.7476   | 0.7480      | 0.7569   | 0.9833   |
| 0.0091        | 7.0   | 1841 | 0.0867          | 0.7860    | 0.7218 | 0.7525   | 0.7526      | 0.7613   | 0.9833   |
| 0.0069        | 8.0   | 2104 | 0.0818          | 0.7921    | 0.7254 | 0.7573   | 0.7572      | 0.7670   | 0.9837   |
| 0.006         | 9.0   | 2367 | 0.0875          | 0.7624    | 0.7437 | 0.7529   | 0.7531      | 0.7587   | 0.9838   |
| 0.0048        | 10.0  | 2630 | 0.0919          | 0.7849    | 0.7126 | 0.7470   | 0.7471      | 0.7547   | 0.9831   |
| 0.0044        | 11.0  | 2893 | 0.0941          | 0.7755    | 0.7248 | 0.7493   | 0.7497      | 0.7613   | 0.9835   |
| 0.0035        | 12.0  | 3156 | 0.0996          | 0.7763    | 0.7431 | 0.7594   | 0.7596      | 0.7690   | 0.9838   |
| 0.0029        | 13.0  | 3419 | 0.0985          | 0.7498    | 0.7462 | 0.7480   | 0.7487      | 0.7596   | 0.9832   |
| 0.0028        | 14.0  | 3682 | 0.1044          | 0.7579    | 0.7010 | 0.7284   | 0.7285      | 0.7330   | 0.9827   |
| 0.0025        | 15.0  | 3945 | 0.1053          | 0.7613    | 0.7297 | 0.7452   | 0.7454      | 0.7517   | 0.9832   |
| 0.0024        | 16.0  | 4208 | 0.1024          | 0.7551    | 0.7395 | 0.7472   | 0.7474      | 0.7517   | 0.9834   |
| 0.0021        | 17.0  | 4471 | 0.1128          | 0.7843    | 0.7120 | 0.7464   | 0.7465      | 0.7579   | 0.9831   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
