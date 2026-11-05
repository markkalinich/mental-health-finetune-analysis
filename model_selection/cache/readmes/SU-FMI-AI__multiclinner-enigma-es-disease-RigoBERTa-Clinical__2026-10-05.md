---
library_name: transformers
license: other
base_model: IIC/RigoBERTa-Clinical
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: RigoBERTa-Clinical_es_disease
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/svassileva/MultiClinAI-NER/runs/t9sx522d)
# RigoBERTa-Clinical_es_disease

This model is a fine-tuned version of [IIC/RigoBERTa-Clinical](https://huggingface.co/IIC/RigoBERTa-Clinical) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0018
- Precision: 0.9925
- Recall: 0.9970
- F1: 0.9947
- Accuracy: 0.9994

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1237        | 1.0   | 739  | 0.0576          | 0.8544    | 0.8984 | 0.8758 | 0.9789   |
| 0.0709        | 2.0   | 1478 | 0.0362          | 0.9185    | 0.9245 | 0.9215 | 0.9866   |
| 0.0425        | 3.0   | 2217 | 0.0226          | 0.9359    | 0.9606 | 0.9481 | 0.9924   |
| 0.0345        | 4.0   | 2956 | 0.0150          | 0.9628    | 0.9663 | 0.9645 | 0.9950   |
| 0.0210        | 5.0   | 3695 | 0.0102          | 0.9703    | 0.9803 | 0.9753 | 0.9965   |
| 0.0168        | 6.0   | 4434 | 0.0061          | 0.9804    | 0.9864 | 0.9834 | 0.9980   |
| 0.0107        | 7.0   | 5173 | 0.0044          | 0.9814    | 0.9928 | 0.9871 | 0.9984   |
| 0.0082        | 8.0   | 5912 | 0.0026          | 0.9902    | 0.9948 | 0.9925 | 0.9991   |
| 0.0049        | 9.0   | 6651 | 0.0020          | 0.9930    | 0.9958 | 0.9944 | 0.9994   |
| 0.0043        | 10.0  | 7390 | 0.0018          | 0.9925    | 0.9970 | 0.9947 | 0.9994   |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.4
- Tokenizers 0.22.2
