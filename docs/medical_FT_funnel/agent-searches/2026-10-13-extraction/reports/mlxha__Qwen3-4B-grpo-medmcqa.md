# mlxha/Qwen3-4B-grpo-medmcqa

## Sources

- https://huggingface.co/mlxha/Qwen3-4B-grpo-medmcqa/raw/main/README.md — current model card; same bytes as the 10 October cache (`sha256` `45bd45fbd94d3d404361385ae6f6bb57d9596101ddf516f672243c82055fb497`)
- https://huggingface.co/api/models/mlxha/Qwen3-4B-grpo-medmcqa — file list, parameter count, and `chat_template.jinja`
- https://huggingface.co/mlxha/Qwen3-4B-grpo-medmcqa/raw/main/config.json — context length and architecture
- https://huggingface.co/mlxha/Qwen3-4B-grpo-medmcqa/raw/main/generation_config.json — sampling settings
- https://huggingface.co/mlxha/Qwen3-4B-grpo-medmcqa/raw/main/all_results.json — training loss and sample count
- https://huggingface.co/mlxha/Qwen3-4B-grpo-medmcqa/raw/main/trainer_state.json — steps, epoch, batch size, learning-rate log, reward names
- https://huggingface.co/datasets/mlxha/medmcqa-grpo — dataset viewer; 193,155 rows
- https://huggingface.co/datasets/mlxha/medmcqa-grpo/raw/main/README.md — dataset YAML; language and split sizes
- https://arxiv.org/abs/2402.03300 — DeepSeekMath abstract; the card cites it for GRPO
- https://arxiv.org/html/2402.03300 — DeepSeekMath HTML; does not print this repository id
- https://github.com/huggingface/trl — library the card cites
- https://github.com/deepseek-ai/DeepSeek-Math — code repository linked from the paper; not this checkpoint's training code
- https://wandb.ai/alexs-team/reasoning/runs/abe1faca-0f47-471a-b13c-22b48a63c0a6 — run linked from the card; metrics were not retrieved
- https://featherless.ai/models/mlxha/Qwen3-4B-grpo-medmcqa — inference host page; adds a purpose the card does not state

## Record

The training set named on the card is `mlxha/medmcqa-grpo`. The card says: "This model is a fine-tuned version of Qwen/Qwen3-4B on the mlxha/medmcqa-grpo dataset." The dataset README is YAML only. It sets `language: en` and records 182,822 train rows, 6,150 test rows, and 4,183 validation rows (193,155 in total). The Hub viewer loads those rows. `all_results.json` reports `train_samples` 182,822. The dataset card does not say whether the text is human or synthetic. The split sizes match `openlifescienceai/medmcqa`. This model card never names that Hub dataset.

The objective is GRPO. The card says: "This model was trained with GRPO, a method introduced in DeepSeekMath." `trainer_state.json` stops at step 1,904, epoch 0.4998933394594772, with `num_train_epochs` set to 1. The highest learning rate in the log is 2.999977296767498e-06, at step 195. `train_batch_size` is 4. No sentence states full fine-tuning, LoRA, or QLoRA. The repository has two safetensors shards and no `adapter_config.json`. LoRA rank, LoRA alpha, whether an adapter was merged, and whether the base was quantized during training are not stated.

The parent on the card is `Qwen/Qwen3-4B`. `config.json` names the architecture `Qwen3ForCausalLM` and does not name a parent repository. DeepSeekMath does not name this checkpoint. No source outside the card states the parent.

The card is a TRL template. It does not say the model gives advice, a diagnosis, or an answer to a person. The use claim is weak. There is no warning about diagnosis, treatment, or medical advice. The YAML license line is `licence: license`, and the file list has no license file. A Featherless page says the model is specialized for medical multiple-choice questions and expands GRPO as "Gradient-based Reinforcement Learning with Policy Optimization." That expansion is not what the DeepSeekMath paper says, and that page is not the model card. It is not used here as the purpose.

No sentence on the card says what the model is for or who it is for. Audiences are empty. Functions are empty.

The training rows are exam questions. A viewer row begins "Question: Chronic urethral obstruction due to benign prismatic hyperplasia can lead to the following change in kidney parenchyma Options: A. Hyperplasia B. Hyperophy C. Atrophy D. Dyplasia" and the `solution` is `C`. That is exam answering. The card names no specialty.

The quick start runs a text-generation pipeline on a text question and prints `generated_text`. `chat_template.jinja` writes a system turn only when the caller supplies one. It has no default system sentence. If `enable_thinking` is false, the generation prompt inserts an empty `<think></think>` block. `generation_config.json` sets `do_sample` true, temperature 0.6, top_p 0.95, and top_k 20. The quick start also sets `max_new_tokens` 128. `config.json` sets `max_position_embeddings` to 40,960. The card reports no benchmark score. The Hub API records 4,022,468,096 parameters.
