# mlxha/Qwen3-8B-grpo-medmcqa-v2

## Sources

- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/README.md — current model card (same text as the 10 October cache)
- https://huggingface.co/api/models/mlxha/Qwen3-8B-grpo-medmcqa-v2 — file list, parameter count, chat template
- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/config.json — architecture and context length
- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/generation_config.json — sampling settings
- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/trainer_state.json — steps, batch size, logged learning rate, reward names
- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/all_results.json — train loss and train sample count
- https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/raw/main/train_results.json — same training summary as all_results.json
- https://huggingface.co/datasets/mlxha/medmcqa-grpo — dataset viewer
- https://huggingface.co/datasets/mlxha/medmcqa-grpo/raw/main/README.md — split sizes and language
- https://arxiv.org/abs/2402.03300 — DeepSeekMath abstract (GRPO method paper)
- https://arxiv.org/html/2402.03300 — DeepSeekMath HTML full text; does not name this repository
- https://github.com/huggingface/trl — library cited on the card
- https://github.com/deepseek-ai/DeepSeek-Math — code for the method paper, not this checkpoint
- https://wandb.ai/alexs-team/reasoning/runs/37495502-90ff-46e9-b734-a5e8db41c00e — Weights & Biases run linked from the card

## Record

The training set is `mlxha/medmcqa-grpo`. The dataset card lists a train split of 182,822 examples, a test split of 6,150, and a validation split of 4,183, and sets `language: en`. The Hub viewer loads and shows medical multiple-choice questions with options A–D and a letter solution. The dataset README does not say whether the questions are human-written or synthetic. The trainer file records `train_samples` 182822, the same count as the train split.

The objective is GRPO. The card says: "This model was trained with GRPO, a method introduced in DeepSeekMath." `trainer_state.json` stopped at step 2857, logged epoch 0.5000711074159565, with `num_train_epochs` set to 1 and `max_steps` 2857. `train_batch_size` is 4. The highest learning rate in the log is 1.99999328095392e-06, at step 290. No sentence says whether the update was full weights or LoRA. There is no `adapter_config.json`. The release is four BF16 weight shards. `training_args.bin` was not read.

The parent on the card is `Qwen/Qwen3-8B`: "This model is a fine-tuned version of Qwen/Qwen3-8B on the mlxha/medmcqa-grpo dataset." No paper or GitHub repository names this checkpoint. DeepSeekMath (arXiv:2402.03300) introduces GRPO and does not contain this repository id.

The use claim is weak. The card only says the model was fine-tuned on that dataset. It does not say the model gives advice, a diagnosis, or exam help to a person. There is no warning sentence. The YAML key `licence: license` is a placeholder, not a named licence. The Hub API reports 8,190,735,360 BF16 parameters.

No sentence says what the model is for or who it is for. The opening paragraph only names the parent and the dataset. No audience is named.

No function is claimed. The card does not say the model answers questions, talks with a patient, or does any other listed job.

The training data are medical exam items, and the trainer logs a reward named `mcq_accuracy_reward` (mean 0.763671875 at step 2857), plus `format_reward` and `tag_count_reward`. That is exam answering. The dataset `subject_name` field has 21 classes, including Anatomy, Surgery, Medicine, and Ophthalmology, so the domain is general medicine rather than one specialty. The card's only usage example is a chat reply to a non-medical question, with `max_new_tokens` 128.

The example runs on a text question and a user chat turn, so the input is text only. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. `config.json` sets `max_position_embeddings` to 40960. The tokenizer's `model_max_length` is 131072. The chat template is `chat_template.jinja` (the Qwen3 template, including optional think tags). It does not set a system prompt. The card reports no benchmark score.
