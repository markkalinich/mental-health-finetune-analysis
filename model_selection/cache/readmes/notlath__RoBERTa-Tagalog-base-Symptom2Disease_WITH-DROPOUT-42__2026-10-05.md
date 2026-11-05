---
library_name: transformers
license: cc-by-sa-4.0
base_model: jcblaise/roberta-tagalog-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: RoBERTa-Tagalog-base-Symptom2Disease_WITH-DROPOUT-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# RoBERTa-Tagalog-base-Symptom2Disease_WITH-DROPOUT-42

This model is a fine-tuned version of [jcblaise/roberta-tagalog-base](https://huggingface.co/jcblaise/roberta-tagalog-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5196
- Accuracy: 0.9733

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.0456033682942977e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 150
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.1306        | 1.0   | 150  | 0.6238          | 0.94     |
| 0.5249        | 2.0   | 300  | 0.5522          | 0.9633   |
| 0.475         | 3.0   | 450  | 0.5665          | 0.9567   |
| 0.4529        | 4.0   | 600  | 0.5435          | 0.97     |
| 0.4526        | 5.0   | 750  | 0.5166          | 0.9733   |
| 0.448         | 6.0   | 900  | 0.5175          | 0.9767   |
| 0.4479        | 7.0   | 1050 | 0.5203          | 0.9733   |
| 0.4478        | 8.0   | 1200 | 0.5196          | 0.9733   |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
