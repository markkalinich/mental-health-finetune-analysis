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
- name: RigoBERTa-Clinical_es_symptom
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/svassileva/MultiClinAI-NER/runs/nsgeghla)
# RigoBERTa-Clinical_es_symptom

This model is a fine-tuned version of [IIC/RigoBERTa-Clinical](https://huggingface.co/IIC/RigoBERTa-Clinical) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0049
- Precision: 0.9854
- Recall: 0.9908
- F1: 0.9881
- Accuracy: 0.9983

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
| 0.1790        | 1.0   | 739  | 0.0919          | 0.8265    | 0.8546 | 0.8403 | 0.9635   |
| 0.1143        | 2.0   | 1478 | 0.0648          | 0.8832    | 0.8979 | 0.8904 | 0.9751   |
| 0.0765        | 3.0   | 2217 | 0.0436          | 0.9203    | 0.9217 | 0.9210 | 0.9841   |
| 0.0631        | 4.0   | 2956 | 0.0294          | 0.9363    | 0.9532 | 0.9447 | 0.9902   |
| 0.0419        | 5.0   | 3695 | 0.0216          | 0.9517    | 0.9698 | 0.9607 | 0.9927   |
| 0.0342        | 6.0   | 4434 | 0.0165          | 0.9603    | 0.9774 | 0.9688 | 0.9943   |
| 0.0232        | 7.0   | 5173 | 0.0115          | 0.9757    | 0.9817 | 0.9787 | 0.9967   |
| 0.0202        | 8.0   | 5912 | 0.0081          | 0.9793    | 0.9890 | 0.9841 | 0.9976   |
| 0.0139        | 9.0   | 6651 | 0.0057          | 0.9847    | 0.9889 | 0.9868 | 0.9982   |
| 0.0120        | 10.0  | 7390 | 0.0049          | 0.9854    | 0.9908 | 0.9881 | 0.9983   |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.4
- Tokenizers 0.22.2
