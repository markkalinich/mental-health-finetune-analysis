---
library_name: transformers
license: cc-by-sa-4.0
base_model: jcblaise/roberta-tagalog-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: final_filipino_model_retrained
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final_filipino_model_retrained

This model is a fine-tuned version of [jcblaise/roberta-tagalog-base](https://huggingface.co/jcblaise/roberta-tagalog-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3502
- Accuracy: 0.9545

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.687284551433047e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 8
- label_smoothing_factor: 0.05

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.9281        | 1.0   | 34   | 0.4398          | 0.9091   |
| 0.2285        | 2.0   | 68   | 0.3403          | 0.9773   |
| 0.2039        | 3.0   | 102  | 0.3200          | 0.9773   |
| 0.2027        | 4.0   | 136  | 0.3164          | 0.9773   |
| 0.2024        | 5.0   | 170  | 0.3137          | 0.9773   |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
