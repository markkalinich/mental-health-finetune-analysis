---
library_name: peft
license: mit
base_model: avikalsingh/Clinical-T5-Base
tags:
- base_model:adapter:avikalsingh/Clinical-T5-Base
- lora
- transformers
model-index:
- name: pi-medical-extractor-clinicalt5-lora
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pi-medical-extractor-clinicalt5-lora

This model is a fine-tuned version of [avikalsingh/Clinical-T5-Base](https://huggingface.co/avikalsingh/Clinical-T5-Base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0244

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.05
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.4523        | 0.32  | 200  | 2.2601          |
| 1.3644        | 0.64  | 400  | 2.4665          |
| 1.0832        | 0.96  | 600  | 2.6644          |
| 0.9997        | 1.28  | 800  | 2.7890          |
| 0.9100        | 1.6   | 1000 | 2.9128          |
| 0.8851        | 1.92  | 1200 | 2.9407          |
| 0.8583        | 2.24  | 1400 | 2.9958          |
| 0.8518        | 2.56  | 1600 | 3.0368          |
| 0.8657        | 2.88  | 1800 | 3.0209          |
| 0.8513        | 3.0   | 1875 | 3.0244          |


### Framework versions

- PEFT 0.19.1
- Transformers 5.14.0
- Pytorch 2.11.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2