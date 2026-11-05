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
- name: CeLLaTe-ner-3class-gaz-reinitLLRD-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_3.77
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-gaz-reinitLLRD-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_3.77

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1402
- Precision: 0.7878
- Recall: 0.7655
- Micro F1: 0.7765
- Weighted F1: 0.7762
- Macro F1: 0.7725
- Accuracy: 0.9828

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.7703983905211016e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 17
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.2691        | 1.0   | 526  | 0.0683          | 0.7259    | 0.7527 | 0.7390   | 0.7403      | 0.7376   | 0.9804   |
| 0.0206        | 2.0   | 1052 | 0.0794          | 0.7350    | 0.7373 | 0.7362   | 0.7378      | 0.7354   | 0.9803   |
| 0.0087        | 3.0   | 1578 | 0.1033          | 0.7648    | 0.7373 | 0.7508   | 0.7503      | 0.7467   | 0.9816   |
| 0.0048        | 4.0   | 2104 | 0.0952          | 0.7425    | 0.7455 | 0.7440   | 0.7448      | 0.7423   | 0.9807   |
| 0.0032        | 5.0   | 2630 | 0.1157          | 0.7667    | 0.7640 | 0.7654   | 0.7655      | 0.7618   | 0.9818   |
| 0.0025        | 6.0   | 3156 | 0.1214          | 0.7861    | 0.7281 | 0.7560   | 0.7555      | 0.7490   | 0.9819   |
| 0.0021        | 7.0   | 3682 | 0.1205          | 0.7455    | 0.7681 | 0.7566   | 0.7576      | 0.7554   | 0.9815   |
| 0.0016        | 8.0   | 4208 | 0.1394          | 0.7040    | 0.7650 | 0.7332   | 0.7322      | 0.7312   | 0.9796   |
| 0.0014        | 9.0   | 4734 | 0.1313          | 0.7805    | 0.7424 | 0.7610   | 0.7607      | 0.7575   | 0.9828   |
| 0.0012        | 10.0  | 5260 | 0.1293          | 0.7749    | 0.7614 | 0.7681   | 0.7679      | 0.7619   | 0.9826   |
| 0.0008        | 11.0  | 5786 | 0.1409          | 0.7076    | 0.7686 | 0.7368   | 0.7396      | 0.7401   | 0.9794   |
| 0.0008        | 12.0  | 6312 | 0.1348          | 0.7712    | 0.7645 | 0.7678   | 0.7680      | 0.7653   | 0.9827   |
| 0.0006        | 13.0  | 6838 | 0.1356          | 0.7829    | 0.7681 | 0.7754   | 0.7757      | 0.7713   | 0.9828   |
| 0.0006        | 14.0  | 7364 | 0.1419          | 0.7878    | 0.7655 | 0.7765   | 0.7762      | 0.7725   | 0.9828   |
| 0.0005        | 15.0  | 7890 | 0.1408          | 0.7725    | 0.7753 | 0.7739   | 0.7741      | 0.7699   | 0.9825   |
| 0.0004        | 16.0  | 8416 | 0.1472          | 0.7719    | 0.7655 | 0.7687   | 0.7689      | 0.7649   | 0.9825   |
| 0.0004        | 17.0  | 8942 | 0.1459          | 0.7830    | 0.7665 | 0.7747   | 0.7746      | 0.7720   | 0.9830   |
| 0.0005        | 18.0  | 9468 | 0.1461          | 0.7662    | 0.7717 | 0.7689   | 0.7691      | 0.7648   | 0.9826   |
| 0.0004        | 19.0  | 9994 | 0.1434          | 0.7789    | 0.7701 | 0.7745   | 0.7745      | 0.7707   | 0.9829   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
