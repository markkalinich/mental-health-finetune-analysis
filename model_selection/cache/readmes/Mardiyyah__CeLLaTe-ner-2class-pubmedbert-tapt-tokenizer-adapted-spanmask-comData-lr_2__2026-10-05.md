---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinit_llrd-pubmedbert-tapt-tokenizer-adapted-spanmask-comData-lr_2.187
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinit_llrd-pubmedbert-tapt-tokenizer-adapted-spanmask-comData-lr_2.187

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0912
- Precision: 0.7753
- Recall: 0.7408
- Micro F1: 0.7577
- Weighted F1: 0.7578
- Macro F1: 0.7671
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
- learning_rate: 2.186715750483408e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 2026
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-------:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.6165        | 1.0     | 132  | 0.1198          | 0.2812    | 0.3927 | 0.3277   | 0.2639      | 0.1867   | 0.9564   |
| 0.0728        | 2.0     | 264  | 0.0566          | 0.7040    | 0.6993 | 0.7017   | 0.7019      | 0.7223   | 0.9829   |
| 0.0351        | 3.0     | 396  | 0.0558          | 0.7171    | 0.7120 | 0.7145   | 0.7150      | 0.7293   | 0.9827   |
| 0.0275        | 4.0     | 528  | 0.0584          | 0.7120    | 0.7372 | 0.7244   | 0.7253      | 0.7377   | 0.9826   |
| 0.0206        | 5.0     | 660  | 0.0620          | 0.7697    | 0.7156 | 0.7417   | 0.7417      | 0.7429   | 0.9833   |
| 0.0163        | 6.0     | 792  | 0.0679          | 0.7748    | 0.7138 | 0.7430   | 0.7433      | 0.7511   | 0.9833   |
| 0.0127        | 7.0     | 924  | 0.0672          | 0.7732    | 0.7174 | 0.7442   | 0.7443      | 0.7484   | 0.9835   |
| 0.0102        | 8.0     | 1056 | 0.0805          | 0.7574    | 0.7246 | 0.7406   | 0.7409      | 0.7456   | 0.9833   |
| 0.0081        | 9.0     | 1188 | 0.0758          | 0.7414    | 0.7396 | 0.7405   | 0.7407      | 0.7449   | 0.9837   |
| 0.0071        | 10.0    | 1320 | 0.0787          | 0.7596    | 0.7468 | 0.7532   | 0.7533      | 0.7577   | 0.9841   |
| 0.0059        | 11.0    | 1452 | 0.0777          | 0.7470    | 0.7456 | 0.7463   | 0.7466      | 0.7524   | 0.9836   |
| 0.0054        | 12.0    | 1584 | 0.0816          | 0.7701    | 0.7372 | 0.7533   | 0.7534      | 0.7559   | 0.9840   |
| 0.005         | 13.0    | 1716 | 0.0919          | 0.7881    | 0.7180 | 0.7514   | 0.7514      | 0.7620   | 0.9835   |
| 0.004         | 14.0    | 1848 | 0.0903          | 0.7718    | 0.7402 | 0.7557   | 0.7559      | 0.7615   | 0.9839   |
| 0.0037        | 15.0    | 1980 | 0.0908          | 0.7753    | 0.7408 | 0.7577   | 0.7578      | 0.7671   | 0.9841   |
| 0.0033        | 16.0    | 2112 | 0.0904          | 0.7605    | 0.7408 | 0.7505   | 0.7506      | 0.7555   | 0.9840   |
| 0.003         | 17.0    | 2244 | 0.0944          | 0.7688    | 0.7300 | 0.7489   | 0.7492      | 0.7580   | 0.9835   |
| 0.0026        | 18.0    | 2376 | 0.0946          | 0.7623    | 0.7288 | 0.7452   | 0.7455      | 0.7533   | 0.9837   |
| 0.0027        | 19.0    | 2508 | 0.0937          | 0.7658    | 0.7372 | 0.7512   | 0.7515      | 0.7587   | 0.9839   |
| 0.0026        | 19.8517 | 2620 | 0.0949          | 0.7727    | 0.7360 | 0.7539   | 0.7541      | 0.7612   | 0.9840   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
