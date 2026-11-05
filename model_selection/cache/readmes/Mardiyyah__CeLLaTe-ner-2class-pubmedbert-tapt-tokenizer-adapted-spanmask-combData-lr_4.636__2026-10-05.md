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
- name: CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-combData-lr_4.636
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-combData-lr_4.636

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0994
- Precision: 0.7792
- Recall: 0.7619
- Micro F1: 0.7704
- Weighted F1: 0.7707
- Macro F1: 0.7778
- Accuracy: 0.9844

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.6356202949590504e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 17
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-------:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.3296        | 1.0     | 132  | 0.0846          | 0.4061    | 0.2742 | 0.3274   | 0.3219      | 0.2575   | 0.9696   |
| 0.0449        | 2.0     | 264  | 0.0606          | 0.6839    | 0.7300 | 0.7062   | 0.7081      | 0.7237   | 0.9822   |
| 0.0257        | 3.0     | 396  | 0.0622          | 0.7778    | 0.6861 | 0.7291   | 0.7292      | 0.7351   | 0.9833   |
| 0.0189        | 4.0     | 528  | 0.0610          | 0.7405    | 0.7360 | 0.7382   | 0.7386      | 0.7445   | 0.9846   |
| 0.0144        | 5.0     | 660  | 0.0702          | 0.7511    | 0.7511 | 0.7511   | 0.7511      | 0.7535   | 0.9844   |
| 0.0092        | 6.0     | 792  | 0.0778          | 0.7704    | 0.7366 | 0.7532   | 0.7534      | 0.7610   | 0.9843   |
| 0.0074        | 7.0     | 924  | 0.0825          | 0.7487    | 0.7631 | 0.7558   | 0.7563      | 0.7673   | 0.9837   |
| 0.0058        | 8.0     | 1056 | 0.0802          | 0.7603    | 0.7402 | 0.7502   | 0.7501      | 0.7515   | 0.9839   |
| 0.0051        | 9.0     | 1188 | 0.0809          | 0.7270    | 0.7541 | 0.7403   | 0.7412      | 0.7509   | 0.9834   |
| 0.0042        | 10.0    | 1320 | 0.0835          | 0.7731    | 0.7601 | 0.7665   | 0.7667      | 0.7751   | 0.9845   |
| 0.0033        | 11.0    | 1452 | 0.0847          | 0.7707    | 0.7517 | 0.7610   | 0.7612      | 0.7697   | 0.9840   |
| 0.0023        | 12.0    | 1584 | 0.0926          | 0.7559    | 0.7523 | 0.7541   | 0.7544      | 0.7605   | 0.9840   |
| 0.0021        | 13.0    | 1716 | 0.0941          | 0.768     | 0.7505 | 0.7591   | 0.7596      | 0.7699   | 0.9841   |
| 0.0018        | 14.0    | 1848 | 0.0980          | 0.7938    | 0.7384 | 0.7651   | 0.7653      | 0.7742   | 0.9840   |
| 0.0016        | 15.0    | 1980 | 0.0958          | 0.7755    | 0.7667 | 0.7711   | 0.7713      | 0.7770   | 0.9844   |
| 0.0015        | 16.0    | 2112 | 0.0966          | 0.7758    | 0.7637 | 0.7697   | 0.7699      | 0.7757   | 0.9845   |
| 0.0012        | 17.0    | 2244 | 0.0990          | 0.7757    | 0.7571 | 0.7663   | 0.7666      | 0.7751   | 0.9844   |
| 0.0012        | 18.0    | 2376 | 0.1001          | 0.7792    | 0.7619 | 0.7704   | 0.7707      | 0.7778   | 0.9844   |
| 0.0011        | 19.0    | 2508 | 0.0999          | 0.7801    | 0.7595 | 0.7697   | 0.7699      | 0.7766   | 0.9844   |
| 0.0013        | 19.8517 | 2620 | 0.1006          | 0.7800    | 0.7589 | 0.7693   | 0.7695      | 0.7763   | 0.9844   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
