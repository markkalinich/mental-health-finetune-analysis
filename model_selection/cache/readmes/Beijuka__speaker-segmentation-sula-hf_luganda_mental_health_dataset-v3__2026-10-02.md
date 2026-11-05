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
- Beijuka/luganda_mental_health_dataset_v3
model-index:
- name: speaker-segmentation-sula-hf_luganda_mental_health_dataset-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# speaker-segmentation-sula-hf_luganda_mental_health_dataset-v3

This model is a fine-tuned version of [pyannote/speaker-diarization-3.0](https://huggingface.co/pyannote/speaker-diarization-3.0) on the Beijuka/luganda_mental_health_dataset_v3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4910
- Model Preparation Time: 0.0042
- Der: 0.1456
- False Alarm: 0.0473
- Missed Detection: 0.0677
- Confusion: 0.0306

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
| 0.2372        | 1.0   | 222  | 0.3616          | 0.0042                 | 0.1444 | 0.0326      | 0.0619           | 0.0498    |
| 0.2216        | 2.0   | 444  | 0.3436          | 0.0042                 | 0.1400 | 0.0361      | 0.0555           | 0.0484    |
| 0.2197        | 3.0   | 666  | 0.3568          | 0.0042                 | 0.1456 | 0.0413      | 0.0514           | 0.0529    |
| 0.2000        | 4.0   | 888  | 0.3516          | 0.0042                 | 0.1383 | 0.0345      | 0.0595           | 0.0444    |
| 0.1946        | 5.0   | 1110 | 0.3829          | 0.0042                 | 0.1405 | 0.0360      | 0.0564           | 0.0481    |
| 0.1894        | 6.0   | 1332 | 0.3932          | 0.0042                 | 0.1386 | 0.0373      | 0.0559           | 0.0454    |
| 0.1953        | 7.0   | 1554 | 0.3691          | 0.0042                 | 0.1369 | 0.0338      | 0.0598           | 0.0433    |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
