---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioBERT_Symptom2Disease_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioBERT_Symptom2Disease_dataset

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4654
- Accuracy: 0.9822
- F1 Macro: 0.9822
- Precision Macro: 0.9824
- Recall Macro: 0.9822

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00010991881828458548
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
| 10.1028       | 1.0   | 66   | 0.5420          | 0.9578   | 0.9577   | 0.9583          | 0.9578       |
| 4.3814        | 2.0   | 132  | 0.4874          | 0.9711   | 0.9712   | 0.9718          | 0.9711       |
| 3.7026        | 3.0   | 198  | 0.4870          | 0.9689   | 0.9688   | 0.9693          | 0.9689       |
| 3.4647        | 4.0   | 264  | 0.4783          | 0.98     | 0.9800   | 0.9805          | 0.98         |
| 3.4057        | 5.0   | 330  | 0.4624          | 0.9822   | 0.9823   | 0.9824          | 0.9822       |
| 3.4058        | 6.0   | 396  | 0.4852          | 0.9756   | 0.9756   | 0.9763          | 0.9756       |
| 3.3822        | 7.0   | 462  | 0.4606          | 0.98     | 0.9800   | 0.9800          | 0.9800       |
| 3.3637        | 8.0   | 528  | 0.4647          | 0.9844   | 0.9844   | 0.9845          | 0.9844       |
| 3.3631        | 9.0   | 594  | 0.4655          | 0.9822   | 0.9822   | 0.9824          | 0.9822       |
| 3.3631        | 10.0  | 660  | 0.4654          | 0.9822   | 0.9822   | 0.9824          | 0.9822       |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
