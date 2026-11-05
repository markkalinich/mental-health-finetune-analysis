---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-42

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5215
- Accuracy: 0.9511
- F1 Macro: 0.9511
- Precision Macro: 0.9567
- Recall Macro: 0.9511

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003385381746308142
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
| 7.3439        | 1.0   | 66   | 0.5085          | 0.98     | 0.9802   | 0.9808          | 0.98         |
| 4.2491        | 2.0   | 132  | 0.5096          | 0.9733   | 0.9737   | 0.9757          | 0.9733       |
| 3.8636        | 3.0   | 198  | 0.5087          | 0.9689   | 0.9687   | 0.9697          | 0.9689       |
| 3.6692        | 4.0   | 264  | 0.5215          | 0.9511   | 0.9511   | 0.9567          | 0.9511       |


### Framework versions

- Transformers 5.2.0
- Pytorch 2.10.0+cu128
- Datasets 4.6.1
- Tokenizers 0.22.2
