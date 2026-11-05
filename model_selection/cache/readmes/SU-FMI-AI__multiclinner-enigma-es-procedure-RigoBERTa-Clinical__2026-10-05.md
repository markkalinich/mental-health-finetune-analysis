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
- name: RigoBERTa-Clinical_es_procedure
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/svassileva/MultiClinAI-NER/runs/aphugj5r)
# RigoBERTa-Clinical_es_procedure

This model is a fine-tuned version of [IIC/RigoBERTa-Clinical](https://huggingface.co/IIC/RigoBERTa-Clinical) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0013
- Precision: 0.9965
- Recall: 0.9982
- F1: 0.9973
- Accuracy: 0.9997

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
| 0.1097        | 1.0   | 739  | 0.0422          | 0.8979    | 0.8993 | 0.8986 | 0.9833   |
| 0.0658        | 2.0   | 1478 | 0.0285          | 0.9237    | 0.9368 | 0.9302 | 0.9891   |
| 0.0382        | 3.0   | 2217 | 0.0198          | 0.9278    | 0.9653 | 0.9462 | 0.9925   |
| 0.0313        | 4.0   | 2956 | 0.0123          | 0.9652    | 0.9734 | 0.9693 | 0.9955   |
| 0.0182        | 5.0   | 3695 | 0.0078          | 0.9786    | 0.9813 | 0.9799 | 0.9973   |
| 0.0148        | 6.0   | 4434 | 0.0048          | 0.9850    | 0.9914 | 0.9882 | 0.9984   |
| 0.0083        | 7.0   | 5173 | 0.0037          | 0.9907    | 0.9918 | 0.9913 | 0.9988   |
| 0.0069        | 8.0   | 5912 | 0.0020          | 0.9944    | 0.9964 | 0.9954 | 0.9994   |
| 0.0040        | 9.0   | 6651 | 0.0016          | 0.9961    | 0.9964 | 0.9962 | 0.9995   |
| 0.0031        | 10.0  | 7390 | 0.0013          | 0.9965    | 0.9982 | 0.9973 | 0.9997   |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.4
- Tokenizers 0.22.2
