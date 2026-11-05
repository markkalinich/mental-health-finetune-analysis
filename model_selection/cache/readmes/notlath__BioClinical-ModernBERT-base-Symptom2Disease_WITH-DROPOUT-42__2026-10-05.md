---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-42

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4346
- Accuracy: 0.9956
- F1 Macro: 0.9956
- Precision Macro: 0.9957
- Recall Macro: 0.9956

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
| 10.0906       | 1.0   | 66   | 0.6652          | 0.9178   | 0.9140   | 0.9289          | 0.9178       |
| 4.5684        | 2.0   | 132  | 0.4908          | 0.9733   | 0.9734   | 0.9741          | 0.9733       |
| 3.9058        | 3.0   | 198  | 0.5149          | 0.9689   | 0.9688   | 0.9710          | 0.9689       |
| 3.6122        | 4.0   | 264  | 0.4598          | 0.9867   | 0.9866   | 0.9867          | 0.9867       |
| 3.5627        | 5.0   | 330  | 0.4494          | 0.9889   | 0.9889   | 0.9889          | 0.9889       |
| 3.3964        | 6.0   | 396  | 0.4355          | 0.9956   | 0.9956   | 0.9957          | 0.9956       |
| 3.3643        | 7.0   | 462  | 0.4340          | 0.9956   | 0.9956   | 0.9957          | 0.9956       |
| 3.3608        | 8.0   | 528  | 0.4346          | 0.9956   | 0.9956   | 0.9957          | 0.9956       |
| 3.3595        | 9.0   | 594  | 0.4346          | 0.9956   | 0.9956   | 0.9957          | 0.9956       |


### Framework versions

- Transformers 5.2.0
- Pytorch 2.10.0+cu128
- Datasets 4.6.1
- Tokenizers 0.22.2
