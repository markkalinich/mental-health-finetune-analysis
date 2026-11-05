# mlxha/Qwen-2.5-3B-grpo-medmcqa

## Sources

- https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/README.md — current model card; same bytes as the 10 October cache (`sha256` `8549bcfb90a8100252621adc56ea7416382f115088c9f71a907f3662c9b13d73`)
- https://huggingface.co/api/models/mlxha/Qwen-2.5-3B-grpo-medmcqa — file list, parameter count, and the chat template stored in `tokenizer_config.json`
- https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/config.json — context length and architecture
- https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/generation_config.json — sampling settings
- https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/all_results.json — training loss and sample count
- https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/train_results.json — same training summary as `all_results.json`
- https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/trainer_state.json — steps, epoch, batch size, learning-rate log, reward names
- https://huggingface.co/datasets/mlxha/medmcqa-grpo — dataset viewer; the Hub page says 193,155 rows
- https://huggingface.co/datasets/mlxha/medmcqa-grpo/raw/main/README.md — dataset YAML only; language and split sizes
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA dataset card; same split sizes as `mlxha/medmcqa-grpo`, not named on this model card
- https://arxiv.org/abs/2402.03300 — DeepSeekMath abstract; the card cites it for GRPO
- https://arxiv.org/html/2402.03300 — DeepSeekMath HTML; does not print this repository id
- https://github.com/huggingface/trl — library the card cites
- https://github.com/deepseek-ai/DeepSeek-Math — code repository linked from the paper; not this checkpoint's training code
- https://wandb.ai/alexs-team/reasoning/runs/9832a928-b485-4023-9e5f-b367f68a0b69 — run linked from the card; the page returned no metrics

## Record

The training set named on the card is `mlxha/medmcqa-grpo`. The card says: "This model is a fine-tuned version of Qwen/Qwen2.5-3B-Instruct on the mlxha/medmcqa-grpo dataset." The dataset README is YAML only. It sets `language: en` and records 182,822 train rows, 6,150 test rows, and 4,183 validation rows (193,155 in total). The Hub viewer loads those rows. Each row is a question, four options, a correct letter, an explanation, a subject, a topic, plus `problem` and `solution`. `all_results.json` reports `train_samples` 182,822, the train split. The dataset card does not say whether the text is human or synthetic. Those split sizes match `openlifescienceai/medmcqa`, whose card describes AIIMS and NEET PG exam questions and does not include the `problem` and `solution` columns. This model card never names that Hub dataset.

The objective is GRPO. The card says: "This model was trained with GRPO, a method introduced in DeepSeekMath." `trainer_state.json` stops at step 1,429, epoch 0.250123070527617, with `num_train_epochs` set to 1 and `max_steps` 1,429. The highest learning rate in the log is 2.999995524115659e-06, at step 145. `train_batch_size` is 8. No sentence states full fine-tuning, LoRA, or QLoRA. The repository has two safetensors shards and no `adapter_config.json`. LoRA rank, LoRA alpha, whether an adapter was merged, and whether the base was quantized during training are not stated.

The parent on the card is `Qwen/Qwen2.5-3B-Instruct`, in the same sentence as the dataset. `config.json` does not name a parent repository. DeepSeekMath does not name this checkpoint. No source outside the card states the parent.

The card is a TRL template. It does not say the model gives advice, a diagnosis, or an answer to a person. The use claim is weak: it was trained on a medical multiple-choice dataset and no use is stated. There is no warning about diagnosis, treatment, or medical advice. The YAML license line is `licence: license`, and the file list has no license file.

No sentence says what the model is for or who it is for. The only description is the template sentence quoted above. Audiences are empty.

Functions are empty because no purpose is stated.

The training rows are exam questions. A viewer row begins "Question: Chronic urethral obstruction due to benign prismatic hyperplasia can lead to the following change in kidney parenchyma Options: A. Hyperplasia B. Hyperophy C. Atrophy D. Dyplasia" and the `solution` is `C`. That is exam answering. The card names no specialty. The dataset `subject_name` field has 21 classes, and the card does not pick one.

The quick start runs a text-generation pipeline on a text question and prints `generated_text` from a user message, so the serving example is text-only chat. The default system line in the chat template is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." `generation_config.json` sets `do_sample` true, temperature 0.7, top_p 0.8, top_k 20, and repetition_penalty 1.05. The quick start also sets `max_new_tokens` 128. `config.json` sets `max_position_embeddings` to 32,768. The card reports no benchmark score. The Hub API records 3,085,938,688 parameters.
