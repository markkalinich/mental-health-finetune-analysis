---
{}
---
# Model with No Refusal Messages From CoCoNoT

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) on UltraChat SFT.

## Suggusted Method For Generations

For this model, `model.generate` or `pipeline` are sufficient.

<!-- ### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 128
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.1131        | 1.0   | 1871 | 1.1339          |


### Framework versions

- Transformers 4.45.2
- Pytorch 2.3.0.dev20240111+rocm5.6
- Datasets 3.0.1
- Tokenizers 0.20.1 -->
