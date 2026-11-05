---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
datasets:
- yashtiwari/PaulMooney-Medical-ASR-Data
metrics:
- wer
model-index:
- name: Whisper small medical
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Medical ASR
      type: yashtiwari/PaulMooney-Medical-ASR-Data
    metrics:
    - name: Wer
      type: wer
      value: 16.799420709630702
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper small medical

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Medical ASR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0847
- Wer: 16.7994

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.3323        | 0.5405 | 100  | 0.2351          | 17.3304 |
| 0.1496        | 1.0811 | 200  | 0.1295          | 12.5996 |
| 0.0838        | 1.6216 | 300  | 0.0972          | 16.8236 |
| 0.0475        | 2.1622 | 400  | 0.0890          | 16.1236 |
| 0.0277        | 2.7027 | 500  | 0.0847          | 16.7994 |


### Framework versions

- Transformers 5.10.1
- Pytorch 2.11.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
