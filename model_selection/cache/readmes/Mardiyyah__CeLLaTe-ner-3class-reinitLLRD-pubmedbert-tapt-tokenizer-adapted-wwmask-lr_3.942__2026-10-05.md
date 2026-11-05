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
- name: CeLLaTe-ner-3class-reinitLLRD-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_3.942
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-reinitLLRD-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_3.942

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1287
- Precision: 0.7845
- Recall: 0.7414
- Micro F1: 0.7623
- Weighted F1: 0.7610
- Macro F1: 0.7589
- Accuracy: 0.9823

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.9417066e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.5895        | 1.0   | 263  | 0.1107          | 0.2748    | 0.4366 | 0.3373   | 0.3283      | 0.2967   | 0.9602   |
| 0.0681        | 2.0   | 526  | 0.0675          | 0.7393    | 0.6927 | 0.7152   | 0.7138      | 0.7118   | 0.9805   |
| 0.0372        | 3.0   | 789  | 0.0860          | 0.6288    | 0.6188 | 0.6237   | 0.6242      | 0.6262   | 0.9755   |
| 0.0242        | 4.0   | 1052 | 0.0787          | 0.6844    | 0.7589 | 0.7197   | 0.7229      | 0.7206   | 0.9793   |
| 0.0164        | 5.0   | 1315 | 0.0863          | 0.7428    | 0.7111 | 0.7266   | 0.7269      | 0.7250   | 0.9805   |
| 0.0116        | 6.0   | 1578 | 0.0932          | 0.6901    | 0.6957 | 0.6929   | 0.6948      | 0.6952   | 0.9793   |
| 0.0087        | 7.0   | 1841 | 0.0891          | 0.7717    | 0.7404 | 0.7557   | 0.7552      | 0.7541   | 0.9820   |
| 0.0065        | 8.0   | 2104 | 0.0929          | 0.7704    | 0.7281 | 0.7486   | 0.7485      | 0.7476   | 0.9817   |
| 0.0047        | 9.0   | 2367 | 0.1041          | 0.7722    | 0.7460 | 0.7589   | 0.7576      | 0.7552   | 0.9821   |
| 0.0043        | 10.0  | 2630 | 0.1012          | 0.7473    | 0.7373 | 0.7423   | 0.7429      | 0.7418   | 0.9813   |
| 0.0032        | 11.0  | 2893 | 0.1144          | 0.7570    | 0.7368 | 0.7467   | 0.7462      | 0.7446   | 0.9817   |
| 0.0032        | 12.0  | 3156 | 0.1279          | 0.7845    | 0.7414 | 0.7623   | 0.7610      | 0.7589   | 0.9823   |
| 0.0025        | 13.0  | 3419 | 0.1216          | 0.7630    | 0.7383 | 0.7505   | 0.7500      | 0.7477   | 0.9813   |
| 0.0018        | 14.0  | 3682 | 0.1252          | 0.7501    | 0.7209 | 0.7352   | 0.7356      | 0.7355   | 0.9804   |
| 0.0017        | 15.0  | 3945 | 0.1267          | 0.7548    | 0.7311 | 0.7428   | 0.7427      | 0.7405   | 0.9811   |
| 0.0014        | 16.0  | 4208 | 0.1268          | 0.7594    | 0.7594 | 0.7594   | 0.7590      | 0.7568   | 0.9822   |
| 0.0012        | 17.0  | 4471 | 0.1319          | 0.7640    | 0.7440 | 0.7538   | 0.7536      | 0.7516   | 0.9818   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
