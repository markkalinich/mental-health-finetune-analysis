---
library_name: transformers
license: cc-by-nc-4.0
base_model: CohereLabs/tiny-aya-earth
base_model_relation: finetune
datasets:
  - adzcai/AfriGuard-plain
language:
  - en
  - am
  - ha
  - ig
  - om
  - sn
  - sw
  - tw
  - wo
  - yo
  - zu
pipeline_tag: text-generation
tags:
  - llama-factory
  - safety
  - african-languages
  - afriguard
---

# AfriGuardPlain-tiny-aya-earth-full

[CohereLabs/tiny-aya-earth](https://huggingface.co/CohereLabs/tiny-aya-earth) fine-tuned with full fine-tuning (DeepSpeed ZeRO-3) on [adzcai/AfriGuard-plain](https://huggingface.co/datasets/adzcai/AfriGuard-plain), the non-instruction-prompted version of [israel/AfriGuard-inst](https://huggingface.co/datasets/israel/AfriGuard-inst): each example is only the user prompt and a plain reply, with **no safety system instruction and no `<safety>` / `<category>` / `<response>` tags**.

Its instruction-prompted counterpart (same base and config) is
[adzcai/AfriGuardInst-tiny-aya-earth-full](https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full).

Training config: `examples/train_full/afriguard_plain_tiny-aya-earth_full_sft.yaml` in the AfriGuard-model (LlamaFactory) repo, the tiny-aya-global setup (`afriguard_tinyaya_full_sft.yaml`) with only
the base model and output paths changed; 1 epoch, 1 GPU, `cohere` chat template, loss on the response only.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 5.8.0
- Pytorch 2.14.0+cu130
- Datasets 4.0.0
- Tokenizers 0.22.2
