# prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2

## Sources

https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/README.md — current model card; byte-identical to the cached card (sha256 dd2753629e02aec076e1aeca4d72075daf56a79628bde7e14375ebba05c79060)
https://huggingface.co/api/models/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2 — file list, parameter count, chat template, and the linked Space
https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/training_params.json — AutoTrain settings stored in this repository
https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/checkpoint-1107/trainer_state.json — logged step, epoch, and training loss
https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/checkpoint-1107/adapter_config.json — LoRA rank, alpha, and base model id
https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/config.json — architecture and context length
https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/generation_config.json — token ids only
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card and viewer
https://huggingface.co/spaces/tahirsher/wellbeing_GenAI — Space listed on the model API; the page did not load
https://arxiv.org/abs/2310.06825 — Mistral 7B abstract; does not name this repository

## Record

The training set named on the card is `Amod/mental_health_counseling_conversations`. The card says: "This model is a fine-tuned version of mistralai/Mistral-7B-Instruct-v0.2 on the mental_health_counseling_conversations dataset." The dataset card says the pairs are human counseling text: "This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms." The Hub viewer shows the train split and labels it 3.51k rows. The dataset API marks it `gated: manual`. Neither the model card nor the dataset card states an exact row count.

The objective is supervised fine-tuning. `training_params.json` sets `"trainer": "sft"`. The same file sets `"quantization": "int4"`, `"peft": true`, `"lora_r": 16`, `"lora_alpha": 32`, `"epochs": 1`, `"lr": 0.00015`, `"batch_size": 2`, `"gradient_accumulation": 1`, and `"merge_adapter": true`. That is LoRA on a 4-bit base, then a merge. `trainer_state.json` says `global_step` 1107, `max_steps` 1107, and `epoch` 1.0. The adapter config names the same base and the same rank and alpha, with target modules `q_proj` and `v_proj`. The root files are full F16 weights. The checkpoint folder still contains the adapter.

The parent is `mistralai/Mistral-7B-Instruct-v0.2` on the card, in `training_params.json`, in `adapter_config.json`, and in `config.json`. The Hub weight index reports 7,241,732,096 parameters. `training_params.json` records the AutoTrain project id `prabureddy/Mental-Health_ML`. That string is the model-index name. It is not the published repository id.

The card is an AutoTrain stub. It does not say the model delivers counseling. The only description is the fine-tune sentence above. The usage example is a chat: a user says they have been feeling down and asks for advice, and the comment under the code says the reply is "Hello! How can I assist you today?" That is a chatbot demo fitted to a mental-health dataset, so the use claim is weak. The card has no warning about therapy, diagnosis, or medical use. The card lists no evaluation results. The trainer log has training loss only, from 0.7697 at step 100 to 0.0028 at step 1100, and no eval loss. License on the card is `apache-2.0`. No GitHub repository for this checkpoint turned up. The Mistral 7B paper does not name this repository. A Weights & Biases page in the search results is about a different repository, `GRMenon/mental-health-mistral-7b-instructv0.2-finetuned-V2`.

The usage example is text only. `config.json` sets `max_position_embeddings` to 32768. Training used `model_max_length` 1024 and `block_size` 512. The chat template is the Mistral Instruct template and does not include a system prompt. `generation_config.json` does not set temperature, top_p, or max new tokens.
