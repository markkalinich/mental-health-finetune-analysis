# tyodd/SafeGuard-VL-RL

## Sources

https://huggingface.co/tyodd/SafeGuard-VL-RL/raw/main/README.md — current model card; byte-identical to the cached card
https://huggingface.co/api/models/tyodd/SafeGuard-VL-RL — file list and parameter count
https://huggingface.co/tyodd/SafeGuard-VL-RL/raw/main/config.json — architecture and context length
https://huggingface.co/tyodd/SafeGuard-VL-RL/raw/main/generation_config.json — sampling settings
https://huggingface.co/tyodd/SafeGuard-VL-RL/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://huggingface.co/tyodd/SafeGuard-VL-RL/raw/main/chat_template.jinja — chat template and default system line
https://arxiv.org/abs/2603.01228 — abstract of the CVPR 2026 paper
https://arxiv.org/html/2603.01228 — HTML full text of that paper
https://arxiv.org/abs/2402.03300 — DeepSeekMath, linked from the card as the GRPO source; not read in full
https://arxiv.org/html/2607.05910 — later paper that mentions SafeGuard-VL-RL-7B; listed only, not read
https://github.com/adorableChowhound/SafeGuard-VL — project README; prints this repository id
https://raw.githubusercontent.com/adorableChowhound/SafeGuard-VL/main/train/grpo.sh — Stage-2 GRPO script
https://huggingface.co/datasets/AIML-TUDA/LlavaGuard — dataset page; gated
https://huggingface.co/api/datasets/AIML-TUDA/LlavaGuard — dataset metadata

## Record

The training data is the LlavaGuard train split, Hub id `AIML-TUDA/LlavaGuard`. The card says: "It applies GRPO (from DeepSeekMath) on the LlavaGuard training set." The dataset is English, gated, and the raw card returned 401, so it did not load. The API size bucket is `1K<n<10K`. An exact row count is not stated. The gated prompt calls it "a derivative collection of webscraped images and the SMID dataset" and does not say whether the safe/unsafe labels were written by people or by a model.

The objective is GRPO, and this checkpoint skipped the earlier supervised stage. The card says: "SafeGuard-VL-RL is trained using **Stage-2 RL only** (without the Stage-1 SFT)." The paper names the same variant: "SafeGuard-VL-RL (Stage-2 RL only without SFT, trained on identical data as QwenGuard for fair comparison)." The released Stage-2 script sets `--rlhf_type grpo`, `--train_type full`, `--torch_dtype bfloat16`, `--model Qwen/Qwen2.5-VL-7B-Instruct`, `--num_train_epochs 1`, `--learning_rate 1e-6`, and `--per_device_train_batch_size 1`, with gradient accumulation 2 on 8 GPUs. The data path in that script is the placeholder `/path/to/grpo_data.jsonl`. There is no LoRA rank, no adapter file, and no step count. The repository holds four bfloat16 weight shards, 8,292,166,656 parameters.

The parent is `Qwen/Qwen2.5-VL-7B-Instruct`. The card, the GitHub resource table ("Qwen2.5-VL-7B-Instruct + Stage-2 RL"), and `grpo.sh` (`--model Qwen/Qwen2.5-VL-7B-Instruct`) agree. The paper names this checkpoint SafeGuard-VL-RL and does not print `tyodd/SafeGuard-VL-RL`. The GitHub README does.

This is a visual safety classifier, not a support chat. The usage example asks the model to "Provide your reasoning and final judgment (Safe/Unsafe)." The use claim is absent: the card describes "a policy-aware visual safety guardrail" for "unsafe-image detection." The warning is unrelated to therapy or medical use: "The model's judgments are policy-dependent and should not be used as the sole arbiter of content safety in production systems without human oversight." Language on the card is English. License is Apache-2.0.

The usage example passes an image plus policy text, so input is not text-only. `chat_template.jinja` is present and inserts "You are a helpful assistant." when the first message is not a system message. `generation_config.json` sets `do_sample` true, `repetition_penalty` 1.05, and `temperature` 1e-06. The card example uses `max_new_tokens` 512. `config.json` sets `max_position_embeddings` to 128000. The paper's Table 4 row Ours (RL) reports LlavaGuard 71.78, UnsafeBench 62.39, SafeEditBench 45.59, and general overall 57.02.

The inventory row matches the dataset and the parent. It does not match the method: the inventory lists `grpo|sft`, and the card says this checkpoint was trained without Stage-1 SFT.
