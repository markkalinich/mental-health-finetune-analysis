---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-baseline

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0997
- Precision: 0.7821
- Recall: 0.7535
- Micro F1: 0.7675
- Weighted F1: 0.7678
- Macro F1: 0.7765
- Accuracy: 0.9845

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
| 0.2456        | 1.0   | 263  | 0.0655          | 0.5680    | 0.6957 | 0.6254   | 0.6265      | 0.6334   | 0.9776   |
| 0.0403        | 2.0   | 526  | 0.0568          | 0.7239    | 0.6795 | 0.7010   | 0.7009      | 0.6974   | 0.9822   |
| 0.0256        | 3.0   | 789  | 0.0579          | 0.7702    | 0.7234 | 0.7460   | 0.7461      | 0.7503   | 0.9837   |
| 0.0187        | 4.0   | 1052 | 0.0662          | 0.7530    | 0.7276 | 0.7401   | 0.7406      | 0.7524   | 0.9837   |
| 0.0143        | 5.0   | 1315 | 0.0653          | 0.7464    | 0.7096 | 0.7275   | 0.7275      | 0.7146   | 0.9833   |
| 0.0112        | 6.0   | 1578 | 0.0696          | 0.7356    | 0.7126 | 0.7239   | 0.7240      | 0.7135   | 0.9829   |
| 0.0083        | 7.0   | 1841 | 0.0747          | 0.7359    | 0.7589 | 0.7472   | 0.7476      | 0.7551   | 0.9844   |
| 0.0065        | 8.0   | 2104 | 0.0829          | 0.7665    | 0.7246 | 0.7450   | 0.7450      | 0.7471   | 0.9839   |
| 0.0056        | 9.0   | 2367 | 0.0845          | 0.7562    | 0.7462 | 0.7512   | 0.7513      | 0.7574   | 0.9841   |
| 0.0046        | 10.0  | 2630 | 0.0899          | 0.7752    | 0.7029 | 0.7373   | 0.7373      | 0.7402   | 0.9834   |
| 0.0039        | 11.0  | 2893 | 0.0848          | 0.7368    | 0.7661 | 0.7512   | 0.7521      | 0.7635   | 0.9839   |
| 0.0036        | 12.0  | 3156 | 0.0880          | 0.7762    | 0.7384 | 0.7569   | 0.7573      | 0.7663   | 0.9846   |
| 0.0029        | 13.0  | 3419 | 0.0942          | 0.7506    | 0.7619 | 0.7562   | 0.7564      | 0.7639   | 0.9845   |
| 0.0025        | 14.0  | 3682 | 0.0936          | 0.7637    | 0.7619 | 0.7628   | 0.7632      | 0.7730   | 0.9846   |
| 0.0023        | 15.0  | 3945 | 0.0970          | 0.7648    | 0.7625 | 0.7636   | 0.7639      | 0.7724   | 0.9845   |
| 0.0018        | 16.0  | 4208 | 0.0988          | 0.7717    | 0.7583 | 0.7649   | 0.7654      | 0.7750   | 0.9846   |
| 0.0017        | 17.0  | 4471 | 0.1000          | 0.7821    | 0.7535 | 0.7675   | 0.7678      | 0.7765   | 0.9845   |
| 0.0016        | 18.0  | 4734 | 0.1010          | 0.7648    | 0.7589 | 0.7618   | 0.7622      | 0.7713   | 0.9844   |
| 0.0014        | 19.0  | 4997 | 0.1044          | 0.7752    | 0.7529 | 0.7639   | 0.7642      | 0.7742   | 0.9844   |
| 0.0014        | 20.0  | 5260 | 0.1044          | 0.7719    | 0.7529 | 0.7623   | 0.7626      | 0.7729   | 0.9843   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
