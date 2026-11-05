---
library_name: transformers
license: cc-by-4.0
base_model: McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1
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

# AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1

[McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1) fine-tuned with full fine-tuning (DeepSpeed ZeRO-3) on
[adzcai/AfriGuard-plain](https://huggingface.co/datasets/adzcai/AfriGuard-plain): the
non-instruction-prompted version of
[israel/AfriGuard-inst](https://huggingface.co/datasets/israel/AfriGuard-inst).

Each training example is only the user prompt and a plain reply (a helpful answer for safe prompts, a brief
refusal for unsafe ones), with **no safety system instruction and no `<safety>` / `<category>` / `<response>`
tags**. The model therefore answers or refuses directly, without emitting a safety label.
Training config: `examples/train_full/afriguard_plain_afriqueqwen3.5-4b-50langs-instruct_full_sft.yaml` in the AfriGuard-model (LlamaFactory) repo; 1 epoch, 1 GPU, chat template
of the base model, loss on the response only.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- total_train_batch_size: 2
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
