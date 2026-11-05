---
datasets:
- mrfakename/refusal
language:
- en
library_name: transformers
pipeline_tag: text-generation
base_model: TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
---

I messed up on the [previous model](https://huggingface.co/mrfakename/refusal-old). This is a fixed version.

A tiny 1B model that refuses basically anything you ask it! Trained on the [refusal](https://huggingface.co/datasets/mrfakename/refusal) dataset. Prompt format is ChatML.

Training results:

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.4352        | 0.0580 | 1    | 2.4462          |
| 1.5741        | 0.5217 | 9    | 1.4304          |
| 1.5204        | 1.0435 | 18   | 1.3701          |
| 1.0794        | 1.5217 | 27   | 1.3505          |
| 1.1275        | 2.0435 | 36   | 1.3344          |
| 0.6652        | 2.5217 | 45   | 1.4360          |
| 0.6248        | 3.0435 | 54   | 1.4313          |
| 0.6142        | 3.5072 | 63   | 1.4934          |

Training hyperparemeters:

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 10
- num_epochs: 4

Base model: https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T