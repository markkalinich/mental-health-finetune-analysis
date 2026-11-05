---
library_name: transformers
license: mit
base_model: jhu-clsp/mmBERT-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-dual-mmbert-base-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-mmbert-base-v1

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0028
- Precision: 0.9907
- Recall: 0.9942
- F1: 0.9924
- Accuracy: 0.9993

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 200
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0135        | 0.4638 | 2000  | 0.0062          | 0.9755    | 0.9866 | 0.9810 | 0.9981   |
| 0.0180        | 0.9275 | 4000  | 0.0041          | 0.9857    | 0.9925 | 0.9891 | 0.9988   |
| 0.0080        | 1.3912 | 6000  | 0.0045          | 0.9841    | 0.9898 | 0.9870 | 0.9987   |
| 0.0069        | 1.8550 | 8000  | 0.0040          | 0.9860    | 0.9915 | 0.9887 | 0.9988   |
| 0.0023        | 2.3186 | 10000 | 0.0028          | 0.9876    | 0.9917 | 0.9896 | 0.9990   |
| 0.0054        | 2.7824 | 12000 | 0.0037          | 0.9890    | 0.9938 | 0.9914 | 0.9990   |
| 0.0003        | 3.2460 | 14000 | 0.0027          | 0.9903    | 0.9942 | 0.9922 | 0.9993   |
| 0.0007        | 3.7098 | 16000 | 0.0028          | 0.9907    | 0.9943 | 0.9925 | 0.9993   |
| 0.0002        | 4.0    | 17252 | 0.0028          | 0.9907    | 0.9942 | 0.9924 | 0.9993   |


### Framework versions

- Transformers 5.15.1
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.22.2
