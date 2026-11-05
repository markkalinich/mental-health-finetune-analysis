# neginr/multisubject_medicine_mc

## Sources

- https://huggingface.co/neginr/multisubject_medicine_mc/raw/main/README.md — current model card (same text as the 5 October cache)
- https://huggingface.co/neginr/multisubject_medicine_mc/raw/main/configs.yaml — LLaMA-Factory config: SFT, full update, parent, batch size
- https://huggingface.co/api/models/neginr/multisubject_medicine_mc — file list, parameter count, chat template
- https://huggingface.co/neginr/multisubject_medicine_mc/raw/main/config.json — Qwen2 config and context length
- https://huggingface.co/neginr/multisubject_medicine_mc/raw/main/generation_config.json — sampling settings
- https://huggingface.co/neginr/multisubject_medicine_mc/raw/main/all_results.json — train loss and logged epoch
- https://huggingface.co/datasets/neginr/multisubject_medicine_mc — dataset viewer, 5,000 rows
- https://huggingface.co/datasets/neginr/multisubject_medicine_mc/raw/main/README.md — schema and split size; no prose
- https://arxiv.org/abs/2307.00619 — paper listed on the author profile; it does not name this model
- https://huggingface.co/neginr — author profile that lists that paper

## Record

Training used `neginr/multisubject_medicine_mc`, 5,000 rows. The viewer loads. Each row is a medical multiple-choice question plus a reasoning trace. Columns include `reasoning`, `deepseek_solution`, and `final_reasoning_trace`. A reasoning cell starts "Okay, so the question is about which route of administration undergoes first-pass elimination." The questions look like exam items. The traces are written as a model's step-by-step solution, and one column is named `deepseek_solution`, so the set is mixed. The dataset README does not say who wrote the questions.

The objective is SFT. `configs.yaml` says `stage: sft` and `finetuning_type: full`. Learning rate 2e-05, 7 epochs, global batch size 96 (per-device batch 1, gradient accumulation 3, 32 devices). `bf16: true`, so the base was not quantized for training. There is no adapter file. `all_results.json` logged epoch 6.955414012738854 and train loss 0.35375573943563543. The card does not state a step count.

The parent is `Qwen/Qwen2.5-7B-Instruct`. The card and `configs.yaml` (`model_name_or_path`) and `config.json` (`_name_or_path`) agree. The API reports 7,615,616,512 BF16 parameters. The author's paper arXiv:2307.00619 is about latent diffusion and does not name this repository.

The use claim is weak. The card says only that the model was fine-tuned on that dataset, and under intended uses it says "More information needed". There is no warning. The licence is Apache-2.0.

No sentence says who the model is for. No function is claimed on the card.

The training rows ask the model to "Write the final choice letter in a \\box{}" and the stored solution is "Therefore, the answer is \\boxed{C}". That is exam answering, as medical question answering, with a reasoning trace and a letter. The `subject` column in the viewer is `None`. The questions cover several fields (drugs, infection, pathology, dentistry), so the domain is general medicine.

The inputs in the dataset are text. `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, top_p 0.8, and repetition penalty 1.05. `max_position_embeddings` is 32768. Training `cutoff_len` is 16384. The chat template's default system line is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." The training rows use a different line: "You are a chatbot who can solve problems." The card reports no benchmark.
