---
license: apache-2.0
base_model: allenai/longformer-base-4096
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_exp_gpu_vtres
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_exp_gpu_vtres

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9360

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 128
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.4475        | 0.28  | 129  | 2.4612          |
| 3.2401        | 0.57  | 258  | 2.2069          |
| 3.0136        | 0.85  | 387  | 2.0084          |
| 2.5518        | 1.13  | 516  | 1.8632          |
| 2.9398        | 1.42  | 645  | 1.7412          |
| 2.0755        | 1.7   | 774  | 1.6260          |
| 2.231         | 1.98  | 903  | 1.5247          |
| 1.9556        | 2.27  | 1032 | 1.4482          |
| 2.0415        | 2.55  | 1161 | 1.3771          |
| 2.111         | 2.83  | 1290 | 1.3097          |
| 1.6116        | 3.12  | 1419 | 1.2572          |
| 1.6044        | 3.4   | 1548 | 1.2108          |
| 1.6614        | 3.68  | 1677 | 1.1802          |
| 1.5013        | 3.97  | 1806 | 1.1371          |
| 1.4666        | 4.25  | 1935 | 1.1079          |
| 1.4608        | 4.53  | 2064 | 1.0894          |
| 1.5144        | 4.82  | 2193 | 1.0672          |
| 1.3958        | 5.1   | 2322 | 1.0390          |
| 1.3949        | 5.38  | 2451 | 1.0283          |
| 1.539         | 5.67  | 2580 | 1.0249          |
| 1.5819        | 5.95  | 2709 | 1.0085          |
| 1.2588        | 6.23  | 2838 | 1.0033          |
| 1.2704        | 6.52  | 2967 | 0.9875          |
| 1.2457        | 6.8   | 3096 | 0.9768          |
| 1.2066        | 7.08  | 3225 | 0.9707          |
| 1.226         | 7.37  | 3354 | 0.9657          |
| 1.3292        | 7.65  | 3483 | 0.9590          |
| 1.1629        | 7.93  | 3612 | 0.9468          |
| 1.2711        | 8.22  | 3741 | 0.9437          |
| 1.3092        | 8.5   | 3870 | 0.9445          |
| 1.35          | 8.78  | 3999 | 0.9424          |
| 1.3402        | 9.07  | 4128 | 0.9360          |
| 1.1433        | 9.35  | 4257 | 0.9349          |
| 1.3059        | 9.63  | 4386 | 0.9296          |
| 1.1391        | 9.92  | 4515 | 0.9360          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.1+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
