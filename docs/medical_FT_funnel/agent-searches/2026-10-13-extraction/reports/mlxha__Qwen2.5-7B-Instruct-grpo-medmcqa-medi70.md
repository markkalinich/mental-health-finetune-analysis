# mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70

## Sources

- https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/README.md — current model card; same bytes as the 10 October cache (`sha256` `b712a3cdf7a75055e9f97aa8a7ddb2a5155be887bc307d5c56abee89633088eb`)
- https://huggingface.co/api/models/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70 — file list, parameter count, and `chat_template.jinja`
- https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/config.json — context length and architecture
- https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/generation_config.json — sampling settings
- https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/all_results.json — training loss and sample count
- https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/trainer_state.json — steps, epoch, batch size, learning-rate log, reward names
- https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/.wandb_run_id — run id `a6495433-dbba-4981-95eb-1982c52a28fc`
- https://huggingface.co/datasets/mlxha/medmcqa-grpo-meditron70b — dataset viewer; 16,885 rows
- https://huggingface.co/datasets/mlxha/medmcqa-grpo-meditron70b/raw/main/README.md — dataset YAML only
- https://arxiv.org/abs/2402.03300 — DeepSeekMath abstract; the card cites it for GRPO
- https://arxiv.org/html/2402.03300 — DeepSeekMath HTML; does not print this repository id
- https://github.com/huggingface/trl — library the card cites
- https://github.com/deepseek-ai/DeepSeek-Math — code repository linked from the paper; not this checkpoint's training code
- https://wandb.ai/alexs-team/reasoning/runs/a6495433-dbba-4981-95eb-1982c52a28fc — run linked from the card; metrics were not retrieved

## Record

The training set named on the card is `mlxha/medmcqa-grpo-meditron70b`. The card says: "This model is a fine-tuned version of Qwen/Qwen2.5-7B-Instruct on the mlxha/medmcqa-grpo-meditron70b dataset." The dataset README is YAML only. It has one split, train, with 16,885 examples. The Hub viewer loads those rows. Columns are `id`, `question`, `opa`, `opb`, `opc`, `opd`, `cop`, `difficulty`, `problem`, and `solution`. `difficulty` has one value, "Advanced Knowledge". `solution` is a letter. The dataset card states no language and does not say whether the text is human or synthetic. The id `meditron70b` is not a statement that Meditron wrote the rows. One displayed id, `73515f05-e947-4801-8077-3abdeca95c84`, is also a row in `mlxha/medmcqa-grpo`. `all_results.json` reports `train_samples` 16,885.

The objective is GRPO. The card says: "This model was trained with GRPO, a method introduced in DeepSeekMath." `trainer_state.json` sets `num_train_epochs` to 1 and `max_steps` to 176. The log ends at step 175, epoch 0.9946714031971581. The highest learning rate in the log is 4.999505824425164e-06, at step 20. `train_batch_size` is 8. No sentence states full fine-tuning, LoRA, or QLoRA. The repository has four safetensors shards and no `adapter_config.json`. LoRA rank, LoRA alpha, whether an adapter was merged, and whether the base was quantized during training are not stated.

The parent on the card is `Qwen/Qwen2.5-7B-Instruct`. `config.json` does not name a parent repository. DeepSeekMath does not name this checkpoint. No source outside the card states the parent.

The card is a TRL template. It does not say the model gives advice, a diagnosis, or an answer to a person. The use claim is weak: it was trained on a medical multiple-choice dataset and no use is stated. There is no warning about diagnosis, treatment, or medical advice. The YAML license line is `licence: license`, and the file list has no license file.

No sentence says what the model is for or who it is for. Audiences are empty. Functions are empty.

The training rows are exam questions. A viewer row begins "Question: Characteristics of Remifentanyl" and ends with options A through D; the `solution` is `C`. That is exam answering. The card names no specialty.

The quick start runs a text-generation pipeline on a text question and prints `generated_text` from a user message, so the serving example is text-only chat. The default system line in `chat_template.jinja` is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." `generation_config.json` sets `do_sample` true, temperature 0.7, top_p 0.8, top_k 20, and repetition_penalty 1.05. The quick start also sets `max_new_tokens` 128. `config.json` sets `max_position_embeddings` to 32,768. The card reports no benchmark score. The Hub API records 7,615,616,512 parameters.
