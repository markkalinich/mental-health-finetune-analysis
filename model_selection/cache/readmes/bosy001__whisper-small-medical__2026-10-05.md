---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-small-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-medical

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3082
- Wer: 4.7165
- Cer: 3.1422
- Wacc: 95.2835

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    | Cer    | Wacc    |
|:-------------:|:------:|:----:|:---------------:|:------:|:------:|:-------:|
| 0.8851        | 0.2082 | 300  | 0.4520          | 5.1154 | 3.3465 | 94.8846 |
| 0.6556        | 0.4164 | 600  | 0.3165          | 5.0978 | 3.3645 | 94.9022 |
| 0.5993        | 0.6246 | 900  | 0.3078          | 4.8984 | 3.2246 | 95.1016 |
| 0.5576        | 0.8328 | 1200 | 0.3056          | 5.0216 | 3.3585 | 94.9784 |
| 0.4404        | 1.0409 | 1500 | 0.3024          | 4.9688 | 3.3698 | 95.0312 |
| 0.4570        | 1.2491 | 1800 | 0.3017          | 4.9570 | 3.3645 | 95.0430 |
| 0.4525        | 1.4573 | 2100 | 0.2998          | 4.8808 | 3.2898 | 95.1192 |
| 0.4393        | 1.6655 | 2400 | 0.3009          | 4.9189 | 3.3065 | 95.0811 |
| 0.4685        | 1.8737 | 2700 | 0.2985          | 4.8456 | 3.2270 | 95.1544 |
| 0.3750        | 2.0819 | 3000 | 0.3038          | 4.7693 | 3.2001 | 95.2307 |
| 0.3612        | 2.2901 | 3300 | 0.3082          | 4.7165 | 3.1422 | 95.2835 |
| 0.3587        | 2.4983 | 3600 | 0.3070          | 4.8221 | 3.2312 | 95.1779 |
| 0.3365        | 2.7065 | 3900 | 0.3086          | 4.8485 | 3.2551 | 95.1515 |
| 0.3474        | 2.9146 | 4200 | 0.3081          | 4.7517 | 3.1846 | 95.2483 |
| 0.2857        | 3.1228 | 4500 | 0.3152          | 4.7957 | 3.1768 | 95.2043 |
| 0.3067        | 3.3310 | 4800 | 0.3185          | 4.8221 | 3.2037 | 95.1779 |
| 0.3110        | 3.4698 | 5000 | 0.3186          | 4.8221 | 3.2133 | 95.1779 |


### Framework versions

- Transformers 5.17.0
- Pytorch 2.8.0+cu126
- Datasets 5.0.1
- Tokenizers 0.23.2
