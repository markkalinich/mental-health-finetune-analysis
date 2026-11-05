---
{}
---
<!-- # zephyr-7b-sft-full-withCoconutwithToken-100perCoco-withContrast -->
# Model with A Single Refusal Token 

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) on UltraChat SFT with the respond token, CoCoNoT refusals with the refuse token, and CoCoNoT's contrast data as SFT data with the respond token. Note that this model is not the model found in the paper the original models are not able to be released due to corporate legalities.

## Suggusted Method For Generations

For generating a output from this model, please refer to the code found in [repo](https://github.com/neelsjain/refusal-tokens) in the `coconot_eval` folder.

<!-- ### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1 -->

<!-- ### Framework versions -->

<!-- - Transformers 4.44.0
- Pytorch 2.3.1+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1 -->
