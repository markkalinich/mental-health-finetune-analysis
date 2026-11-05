---
library_name: transformers
license: apache-2.0
base_model: sulaimank/whisper-small-CV-Fleurs-lg-300
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-small-mental-health-luganda-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-mental-health-luganda-v1

This model is a fine-tuned version of [sulaimank/whisper-small-CV-Fleurs-lg-300](https://huggingface.co/sulaimank/whisper-small-CV-Fleurs-lg-300) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1746
- Wer: 0.3639
- Cer: 0.1724

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 900
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 1.6554        | 1.0   | 297  | 1.7738          | 0.4284 | 0.2022 |
| 1.1974        | 2.0   | 594  | 1.3231          | 0.4490 | 0.2255 |
| 0.7331        | 3.0   | 891  | 0.9783          | 0.4034 | 0.1954 |
| 0.4240        | 4.0   | 1188 | 0.8874          | 0.3919 | 0.1891 |
| 0.2443        | 5.0   | 1485 | 0.9081          | 0.3809 | 0.1809 |
| 0.1337        | 6.0   | 1782 | 0.9790          | 0.3855 | 0.1838 |
| 0.0679        | 7.0   | 2079 | 1.0396          | 0.3896 | 0.1885 |
| 0.0337        | 8.0   | 2376 | 1.0917          | 0.3737 | 0.1794 |
| 0.0207        | 9.0   | 2673 | 1.1229          | 0.3706 | 0.1786 |
| 0.0154        | 10.0  | 2970 | 1.1359          | 0.3660 | 0.1715 |
| 0.0121        | 11.0  | 3267 | 1.1516          | 0.3634 | 0.1717 |
| 0.0099        | 12.0  | 3564 | 1.1586          | 0.3676 | 0.1737 |
| 0.0081        | 13.0  | 3861 | 1.1671          | 0.3640 | 0.1739 |
| 0.0067        | 14.0  | 4158 | 1.1746          | 0.3639 | 0.1724 |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.10.0+cu130
- Datasets 3.0.0
- Tokenizers 0.22.2
