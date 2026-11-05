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
- Beijuka/hf_luganda_mental_health_dataset
model-index:
- name: speaker-segmentation-sula-hf_luganda_mental_health_dataset-v1S
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# speaker-segmentation-sula-hf_luganda_mental_health_dataset-v1S

This model is a fine-tuned version of [pyannote/speaker-diarization-3.0](https://huggingface.co/pyannote/speaker-diarization-3.0) on the Beijuka/hf_luganda_mental_health_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2251
- Model Preparation Time: 0.0171
- Der: 0.0933
- False Alarm: 0.0237
- Missed Detection: 0.0387
- Confusion: 0.0309

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Model Preparation Time | Der    | False Alarm | Missed Detection | Confusion |
|:-------------:|:-----:|:----:|:---------------:|:----------------------:|:------:|:-----------:|:----------------:|:---------:|
| 0.3335        | 1.0   | 114  | 0.2926          | 0.0171                 | 0.1212 | 0.0378      | 0.0501           | 0.0333    |
| 0.2908        | 2.0   | 228  | 0.2792          | 0.0171                 | 0.1137 | 0.0434      | 0.0439           | 0.0264    |
| 0.2660        | 3.0   | 342  | 0.2788          | 0.0171                 | 0.1117 | 0.0408      | 0.0447           | 0.0262    |
| 0.2431        | 4.0   | 456  | 0.2868          | 0.0171                 | 0.1131 | 0.0361      | 0.0509           | 0.0261    |
| 0.2398        | 5.0   | 570  | 0.2723          | 0.0171                 | 0.1093 | 0.0354      | 0.0495           | 0.0244    |
| 0.2457        | 6.0   | 684  | 0.2685          | 0.0171                 | 0.1067 | 0.0411      | 0.0433           | 0.0223    |
| 0.2368        | 7.0   | 798  | 0.2697          | 0.0171                 | 0.1100 | 0.0422      | 0.0440           | 0.0239    |
| 0.2211        | 8.0   | 912  | 0.2699          | 0.0171                 | 0.1091 | 0.0416      | 0.0444           | 0.0230    |
| 0.2258        | 9.0   | 1026 | 0.2697          | 0.0171                 | 0.1089 | 0.0410      | 0.0446           | 0.0233    |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
