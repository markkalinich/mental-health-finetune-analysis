# sadovsky/ft-flan-t5-base-qgen_v2

## Sources

- `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/sadovsky__ft-flan-t5-base-qgen_v2__2026-10-05.md` — cached model card, sha256 `46f37aea9de8120215d76045beaa14c634e5009f15248932b849d602a9881461`
- https://huggingface.co/sadovsky/ft-flan-t5-base-qgen_v2/raw/main/README.md — current card; same bytes as the cache
- https://huggingface.co/api/models/sadovsky/ft-flan-t5-base-qgen_v2 — file list, safetensors parameter count, linked Space
- https://huggingface.co/sadovsky/ft-flan-t5-base-qgen_v2/raw/main/config.json — T5 config, `n_positions` 512
- https://huggingface.co/sadovsky/ft-flan-t5-base-qgen_v2/raw/main/generation_config.json — token ids only
- https://huggingface.co/sadovsky/ft-flan-t5-base-qgen_v2/raw/main/tokenizer_config.json — T5 tokenizer, no `chat_template`
- https://huggingface.co/sadovsky/ft-flan-t5-base-qgen_v2/raw/main/checkpoint-2774/trainer_state.json — finished run, epoch 2, step 2774
- https://huggingface.co/sadovsky/ft-flan-t5-base-qgen_v2/resolve/main/training_args.bin — saved `Seq2SeqTrainingArguments` (same sha256 at the repo root and both checkpoints)
- https://huggingface.co/datasets/pandalla/Machine_Mindset_MBTI_dataset — dataset card named in the model YAML
- https://huggingface.co/datasets/pandalla/Machine_Mindset_MBTI_dataset/raw/main/README.md — dataset README
- https://datasets-server.huggingface.co/size?dataset=pandalla/Machine_Mindset_MBTI_dataset — 160,884 rows, split loaded
- https://datasets-server.huggingface.co/rows?dataset=pandalla/Machine_Mindset_MBTI_dataset&config=default&split=train&offset=0&length=2 — two example rows
- https://github.com/PKU-YuanGroup/Machine-Mindset — dataset project linked from the dataset card; not a training repo for this checkpoint
- https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/README.md — project README
- https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/datasets/behaviour/README.md — behavior-split README
- https://arxiv.org/abs/2312.12999 — Machine Mindset abstract and HTML text; does not name this repository
- https://arxiv.org/html/2312.12999v1 — same paper, HTML
- https://huggingface.co/spaces/sadovsky/MBTI — author Space, Gradio interviewer
- https://huggingface.co/spaces/sadovsky/MBTI/raw/main/app.py — Space app
- https://huggingface.co/spaces/sadovsky/MBTI/raw/main/core/interviewer.py — loads `f3nsmart/ft-flan-t5-base-qgen_v2`
- https://huggingface.co/spaces/sadovsky/MBTI/raw/main/core/utils.py — first question is a fixed string
- https://huggingface.co/api/models/f3nsmart/ft-flan-t5-base-qgen_v2 — old id; resolves to this repository
- https://huggingface.co/api/models/f3nsmart/ft-flan-t5-base-qgen — example-code id; resolves to `sadovsky/ft-flan-t5-base-qgen`, a different repository

## Record

The card names one dataset, `pandalla/Machine_Mindset_MBTI_dataset`. The Hub dataset loads: 160,884 train rows, English and Chinese files, columns `instruction`, `input`, and `output`. The dataset card says, "Here are the behavior datasets used for supervised fine-tuning (SFT). And they can also be used for direct preference optimization (DPO)." That sentence is about how someone might use the files. It is not a statement that this checkpoint was trained with SFT or DPO. The Machine Mindset paper says the behavior answers were produced by ChatGPT from Alpaca instructions: "Subsequently, ChatGPT generated a pair of responses to the same instruction, each mirroring one of the two attitudes within the identified dimension." It also says the self-awareness questions and answers "are generated ChatGPT guided by certain prompts." The Hub repo contains both the behavior files and the self-awareness files. Provenance is synthetic. The paper does not print `sadovsky/ft-flan-t5-base-qgen_v2`. A loaded row has instruction "Are you more introverted or extroverted?" and a first-person answer as `output`. The card does not say which column was the training target.

The card says this is "a fine-tuned version of google/flan-t5-base." "Fine-tuned" is not a named loss. The saved `training_args.bin` is `Seq2SeqTrainingArguments` with `learning_rate` 0.0005, `num_train_epochs` 2, `per_device_train_batch_size` 4, `gradient_accumulation_steps` 1, `warmup_steps` 0, `fp16` false, and `bf16` false. `checkpoint-2774/trainer_state.json` records `epoch` 2.0, `global_step` 2774, `max_steps` 2774, and `train_batch_size` 4. Root `config.json` and `training_args.bin` match the files in `checkpoint-2774` by sha256. No sentence says the update was full, LoRA, or QLoRA. The file list has no `adapter_config.json`. The paper's LoRA, supervised fine-tuning, and DPO description is about the Machine Mindset models, not this checkpoint.

The card names the parent `google/flan-t5-base`. No paper, GitHub repo, or other page names that parent for this checkpoint. The inventory parent matches the card. The inventory method field is empty, and no source names a loss. The inventory dataset matches the card YAML.

The card presents a question generator, not a chatbot and not a classifier: "It operates as a randomized question generator rather than an interactive conversational model." The mental-health claim is weak. The card says the goal is "to generate concise, psychologically relevant questions similar to those found in MBTI-style interviews or self-assessment forms." It does not say the model delivers therapy, counseling, or a support conversation. The card has no therapy, medical, or research-use warning.

The example runs the model on text. It tokenizes "Generate a question about emotional decision-making." and calls `generate` with `max_new_tokens` 60. There is no image or audio input. `tokenizer_config.json` has no `chat_template`, and the repo has no `chat_template.jinja`. `model_max_length` and `n_positions` are 512. `generation_config.json` does not set temperature or sampling. The example loads `f3nsmart/ft-flan-t5-base-qgen`, which now resolves to `sadovsky/ft-flan-t5-base-qgen`, a different repository. The Space `sadovsky/MBTI` loads `f3nsmart/ft-flan-t5-base-qgen_v2`, which resolves to this repository, and samples with `max_new_tokens` 80, `do_sample` true, `temperature` 1.1, `top_p` 0.9, `top_k` 60, and `repetition_penalty` 1.3. No system prompt is stated. The only reported evaluation is loss: 0.5216382741928101 at step 1387 and 0.463400661945343 at step 2774. The license is `apache-2.0`. The Hub safetensors count is 247,577,856 parameters.
