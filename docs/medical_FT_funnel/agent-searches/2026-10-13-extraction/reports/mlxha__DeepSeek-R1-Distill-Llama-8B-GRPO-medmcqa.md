# mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa

## Sources

- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/README.md — current card; identical to the cache (sha256 d74f887e68e011c00f87d8fce494e80e986e06f63d55abdf16e202461f813bb5)
- https://huggingface.co/api/models/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa — file list; 8,030,261,248 bfloat16 parameters
- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/config.json — Llama config, context 131072
- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/generation_config.json — temperature 0.6, top_p 0.95
- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/tokenizer_config.json — DeepSeek-style chat template
- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/trainer_state.json — steps, learning rates, reward names
- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/train_results.json — 182,822 train samples
- https://huggingface.co/mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa/raw/main/eval_results.json — eval loss on 4,183 samples
- https://huggingface.co/datasets/mlxha/medmcqa-grpo — multiple-choice questions; viewer loads
- https://github.com/huggingface/trl — library the card says it trained with
- https://github.com/huggingface/open-r1 — repo matching the card tag `open-r1`; its demo config is a different model
- https://arxiv.org/abs/2402.03300 — DeepSeekMath, cited as the source of GRPO; it does not name this repo
- https://wandb.ai/alexs-team/reasoning/runs/l7btc221 — run linked from the card; the run page was not opened

## Record

The training set is `mlxha/medmcqa-grpo`. The card says the model is “a fine-tuned version of deepseek-ai/DeepSeek-R1-Distill-Llama-8B on the mlxha/medmcqa-grpo dataset.” The dataset viewer loads. The train split has 182,822 rows, the same count as `train_samples` in `train_results.json`. Validation has 4,183 rows, the same count as `eval_samples`. Test has 6,150 rows. The dataset card language is English. A row’s `problem` field is a question with options A through D, and `solution` is a letter such as `C`. The README does not say whether the questions were written by people or generated. Subject labels in the rows include anatomy, surgery, medicine, dental, and others. The card does not name one specialty.

The objective is GRPO. The card says “This model was trained with GRPO.” `trainer_state.json` logs `rewards/format_reward`, `rewards/mcq_accuracy_reward`, and `rewards/tag_count_reward`. No sentence says LoRA or a full-weight update. The upload is four bfloat16 shards and there is no `adapter_config.json`. `trainer_state.json` has `num_train_epochs` 1, `max_steps` 714, `global_step` 714, and a logged epoch of 0.4999 at the last step, so the run stopped at about half an epoch. `train_batch_size` is 16. The highest `learning_rate` in the log is 2.999838368626891e-06. The open-r1 README describes `grpo.py` and a demo config for a Qwen distill model. That demo is not this run.

The parent on the card is `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`. No paper or GitHub README found by search prints this repo id. DeepSeekMath introduces GRPO and does not name this checkpoint. The card does not state a parameter count. The weight files total 8,030,261,248 parameters. The card does not state a language. The YAML line `licence: license` is a placeholder, not a license name.

The use claim is weak. The card names a medical exam dataset and does not say what the model is for. There is no warning. Purpose is not stated. No audience is named. No function is claimed. The training rows are exam questions, so the clinical task of the data is exam answering. The quick-start question is about a time machine, not a patient.

Serving is text in, text out. The example is that time-machine question in a user message. A chat template is present and `use_default_system_prompt` is false. Generation settings are `do_sample` true, `temperature` 0.6, `top_p` 0.95, and the example’s `max_new_tokens` 128. Context in `config.json` is 131,072 tokens. The tokenizer’s `model_max_length` is 16,384. The example output is a chat reply. The dataset’s `solution` field is an exam letter. `eval_results.json` reports eval loss 0.315 on 4,183 samples. At step 714 the logged multiple-choice reward is about 0.49.

Inventory method `grpo`, dataset `mlxha/medmcqa-grpo`, and parent `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` match the card.
