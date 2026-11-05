---
library_name: transformers
license: cc-by-nc-4.0
base_model: CohereLabs/tiny-aya-earth
base_model_relation: finetune
datasets:
  - israel/AfriGuard-inst
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

# AfriGuardInst-tiny-aya-earth-lora-merged

[CohereLabs/tiny-aya-earth](https://huggingface.co/CohereLabs/tiny-aya-earth) fine-tuned with LoRA (rank 16, all linear layers), merged into the base weights on [israel/AfriGuard-inst](https://huggingface.co/datasets/israel/AfriGuard-inst): each example is one of the safety system instructions plus the user prompt, and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`.

Its plain counterpart (same base and config) is
[adzcai/AfriGuardPlain-tiny-aya-earth-lora-merged](https://huggingface.co/adzcai/AfriGuardPlain-tiny-aya-earth-lora-merged).

Training config: `examples/train_lora/afriguard_inst_tiny-aya-earth_lora_sft.yaml` in the AfriGuard-model (LlamaFactory) repo, the tiny-aya-global setup (`afriguard_tinyaya_lora_sft.yaml`) with only
the base model and output paths changed; 1 epoch, 1 GPU, `cohere` chat template, loss on the response only.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 1.0

### Training results



### Framework versions

- PEFT 0.18.1
- Transformers 5.8.0
- Pytorch 2.14.0+cu130
- Datasets 4.0.0
- Tokenizers 0.22.2