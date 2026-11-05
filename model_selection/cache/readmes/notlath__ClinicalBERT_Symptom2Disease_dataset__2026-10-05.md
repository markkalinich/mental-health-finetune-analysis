---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ClinicalBERT_Symptom2Disease_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT_Symptom2Disease_dataset

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4620
- Accuracy: 0.9844
- F1 Macro: 0.9845
- Precision Macro: 0.9845
- Recall Macro: 0.9844

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9.03125418887864e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 65
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro | Precision Macro | Recall Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:---------------:|:------------:|
| 10.9949       | 1.0   | 66   | 0.5789          | 0.9222   | 0.9230   | 0.9261          | 0.9222       |
| 4.3941        | 2.0   | 132  | 0.5294          | 0.9578   | 0.9578   | 0.9593          | 0.9578       |
| 3.9150        | 3.0   | 198  | 0.5572          | 0.9489   | 0.9483   | 0.9517          | 0.9489       |
| 3.5693        | 4.0   | 264  | 0.5047          | 0.9689   | 0.9688   | 0.9694          | 0.9689       |
| 3.4382        | 5.0   | 330  | 0.5006          | 0.9756   | 0.9758   | 0.9770          | 0.9756       |
| 3.3974        | 6.0   | 396  | 0.4678          | 0.9822   | 0.9823   | 0.9823          | 0.9822       |
| 3.3782        | 7.0   | 462  | 0.4643          | 0.98     | 0.9800   | 0.9802          | 0.98         |
| 3.3775        | 8.0   | 528  | 0.4668          | 0.9844   | 0.9844   | 0.9845          | 0.9844       |
| 3.3737        | 9.0   | 594  | 0.4621          | 0.9844   | 0.9845   | 0.9845          | 0.9844       |
| 3.3728        | 10.0  | 660  | 0.4620          | 0.9844   | 0.9845   | 0.9845          | 0.9844       |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
