# mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa

## Sources

- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/README.md — current card; identical to the cache (sha256 fbf924434c7dd8d991d2f056b377a44635e3c07ddb74577b43fffdae2fe9d071)
- https://huggingface.co/api/models/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa — file list; 8,030,261,248 bfloat16 parameters
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/config.json — Llama config, context 131072
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/generation_config.json — temperature 0.6, top_p 0.9
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/tokenizer_config.json — tokenizer; model_max_length 131072
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/chat_template.jinja — Llama 3.1 chat template
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/trainer_state.json — 527 steps, reward names, learning rate
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/train_results.json — 16,885 train samples
- https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/raw/main/eval_results.json — eval loss on 4,183 samples
- https://huggingface.co/datasets/mlxha/medmcqa-grpo-meditron70b — one train split of 16,885 multiple-choice rows; viewer loads
- https://github.com/huggingface/trl — library the card says it trained with
- https://github.com/huggingface/open-r1 — repo matching the `open-r1` tag; its demo config is a different model
- https://arxiv.org/abs/2402.03300 — DeepSeekMath, cited as the source of GRPO; it does not name this repo
- https://wandb.ai/alexs-team/reasoning/runs/1f31e220-729a-47b7-aec3-734ed29c5f73 — run linked from the card; the run page was not opened

## Record

The training set is `mlxha/medmcqa-grpo-meditron70b`. The card says the model is “a fine-tuned version of meta-llama/Llama-3.1-8B-Instruct on the mlxha/medmcqa-grpo-meditron70b dataset.” The viewer loads one train split of 16,885 rows. `train_results.json` reports the same `train_samples` count. A row’s `problem` field is a question with options A through D, and `solution` is a letter such as `C`. One row’s `difficulty` value is “Advanced Knowledge.” The README is a schema. It does not say who wrote the questions, and it does not say that Meditron-70B wrote the solutions. The dataset id contains that name. Language is not stated. The card does not name a specialty.

The objective is GRPO. The card says “This model was trained with GRPO.” `trainer_state.json` logs `format_reward`, `mcq_accuracy_reward`, and `tag_count_reward`. No sentence says LoRA or a full-weight update. The upload is four bfloat16 shards and there is no `adapter_config.json`. `num_train_epochs` is 1. The log ends at step 527 of `max_steps` 528, logged epoch 0.9988. `train_batch_size` is 4. The highest `learning_rate` in the log is 4.999945320950562e-06. The open-r1 README’s GRPO demo is a Qwen distill config, not this run. An Unsloth Llama 3.1 GRPO notebook found by search does not name this repo.

The parent on the card is `meta-llama/Llama-3.1-8B-Instruct`. No paper or GitHub README found by search prints this repo id. DeepSeekMath introduces GRPO and does not name this checkpoint. The card does not state a parameter count. The weight files total 8,030,261,248 parameters. The YAML line `licence: license` is a placeholder.

The use claim is weak. The card names a medical exam dataset and does not say what the model is for. There is no warning. Purpose is not stated. No audience is named. No function is claimed. The rows are exam questions, so the clinical task of the data is exam answering. The quick-start question is about a time machine.

Serving is text in, text out. That question is the example user message. `chat_template.jinja` is present. It writes “Cutting Knowledge Date: December 2023” and a today-date line, and leaves the system message empty unless one is passed. Generation settings are `do_sample` true, `temperature` 0.6, `top_p` 0.9, and the example’s `max_new_tokens` 128. Context length is 131,072 tokens. The example output is a chat reply. The dataset `solution` is an exam letter. `eval_results.json` reports eval loss 0.197 on 4,183 samples. This Hub dataset has no validation split of that size. At step 527 the logged multiple-choice reward mean is about 0.48.

Inventory method `grpo`, dataset `mlxha/medmcqa-grpo-meditron70b`, and parent `meta-llama/Llama-3.1-8B-Instruct` match the card.
