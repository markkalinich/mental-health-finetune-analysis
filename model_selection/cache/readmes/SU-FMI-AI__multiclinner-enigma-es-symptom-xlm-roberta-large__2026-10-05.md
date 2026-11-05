---
library_name: transformers
base_model: llange/xlm-roberta-large-spanish-clinical
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-large-spanish-clinical_es_symptom
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/svassileva/MultiClinAI-NER/runs/sylrgkyy)
# xlm-roberta-large-spanish-clinical_es_symptom

This model is a fine-tuned version of [llange/xlm-roberta-large-spanish-clinical](https://huggingface.co/llange/xlm-roberta-large-spanish-clinical) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0057
- Precision: 0.9855
- Recall: 0.9919
- F1: 0.9887
- Accuracy: 0.9982

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
| 0.1862        | 1.0   | 739  | 0.0924          | 0.8357    | 0.8449 | 0.8403 | 0.9630   |
| 0.1146        | 2.0   | 1478 | 0.0670          | 0.8700    | 0.9071 | 0.8882 | 0.9747   |
| 0.0763        | 3.0   | 2217 | 0.0433          | 0.9198    | 0.9273 | 0.9235 | 0.9847   |
| 0.0639        | 4.0   | 2956 | 0.0293          | 0.9389    | 0.9565 | 0.9476 | 0.9901   |
| 0.0414        | 5.0   | 3695 | 0.0198          | 0.9583    | 0.9685 | 0.9634 | 0.9931   |
| 0.0341        | 6.0   | 4434 | 0.0162          | 0.9619    | 0.9774 | 0.9696 | 0.9947   |
| 0.0231        | 7.0   | 5173 | 0.0106          | 0.9781    | 0.9828 | 0.9804 | 0.9969   |
| 0.0203        | 8.0   | 5912 | 0.0078          | 0.9801    | 0.9898 | 0.9849 | 0.9976   |
| 0.0147        | 9.0   | 6651 | 0.0065          | 0.9854    | 0.9903 | 0.9878 | 0.9981   |
| 0.0122        | 10.0  | 7390 | 0.0057          | 0.9855    | 0.9919 | 0.9887 | 0.9982   |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.4
- Tokenizers 0.22.2
