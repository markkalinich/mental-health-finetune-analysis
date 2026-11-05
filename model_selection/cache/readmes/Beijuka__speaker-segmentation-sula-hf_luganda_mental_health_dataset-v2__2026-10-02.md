---
library_name: transformers
language:
- lg
license: mit
base_model: pyannote/speaker-diarization-3.0
tags:
- speaker-diarization
- speaker-segmentation
- generated_from_trainer
datasets:
- Beijuka/luganda_mental_health_dataset_v2
model-index:
- name: speaker-segmentation-sula-hf_luganda_mental_health_dataset-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# speaker-segmentation-sula-hf_luganda_mental_health_dataset-v2

This model is a fine-tuned version of [pyannote/speaker-diarization-3.0](https://huggingface.co/pyannote/speaker-diarization-3.0) on the Beijuka/luganda_mental_health_dataset_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5084
- Model Preparation Time: 0.0039
- Der: 0.1486
- False Alarm: 0.0406
- Missed Detection: 0.0737
- Confusion: 0.0343

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Model Preparation Time | Der    | False Alarm | Missed Detection | Confusion |
|:-------------:|:-----:|:----:|:---------------:|:----------------------:|:------:|:-----------:|:----------------:|:---------:|
| 0.3112        | 1.0   | 222  | 0.3944          | 0.0039                 | 0.1642 | 0.0294      | 0.0735           | 0.0614    |
| 0.2713        | 2.0   | 444  | 0.3690          | 0.0039                 | 0.1528 | 0.0362      | 0.0589           | 0.0577    |
| 0.2640        | 3.0   | 666  | 0.3789          | 0.0039                 | 0.1539 | 0.0374      | 0.0577           | 0.0587    |
| 0.2409        | 4.0   | 888  | 0.3650          | 0.0039                 | 0.1484 | 0.0291      | 0.0639           | 0.0554    |
| 0.2302        | 5.0   | 1110 | 0.3527          | 0.0039                 | 0.1421 | 0.0311      | 0.0628           | 0.0482    |
| 0.2247        | 6.0   | 1332 | 0.3574          | 0.0039                 | 0.1415 | 0.0306      | 0.0645           | 0.0465    |
| 0.2219        | 7.0   | 1554 | 0.3620          | 0.0039                 | 0.1411 | 0.0340      | 0.0595           | 0.0476    |
| 0.2145        | 8.0   | 1776 | 0.3581          | 0.0039                 | 0.1390 | 0.0350      | 0.0579           | 0.0461    |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
