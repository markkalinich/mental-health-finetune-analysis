# Dataset search, agent 146

## mohanvarma22/laya-safety-beavertails

No. No source names a training corpus a reader can open. The cached card is missing, and the live README returns 404. The only non-weight file, `rl_agent_config.json`, names the encoder `answerdotai/ModernBERT-large` and says the checkpoint was fine-tuned. It does not name a dataset. Searches for this repository id do not connect it to BeaverTails. The word in the repository name is not a dataset.

https://huggingface.co/mohanvarma22/laya-safety-beavertails
https://huggingface.co/mohanvarma22/laya-safety-beavertails/raw/main/rl_agent_config.json

## mspawn/LlamaGuard2-May7

No. The card names a private CSV, and that file does not open. The cached README fetch was 403, and the raw README returns 401 because the repository is manually gated. The model page still shows the card. It says this is a fine-tune of Llama Guard 2 by a College of Business team at Oregon State, trained on a CSV of questions, answers, and faculty FAQ text. No Hub, GitHub, or Kaggle page holds that CSV. Papers about Meta's Llama Guard 2 are about a different checkpoint.

https://huggingface.co/mspawn/LlamaGuard2-May7

## MurrayTom/TS-Guard

Yes. The ToolSafe paper names the training split, and AgentAlign opens. The model card matches the paper's description of TS-Guard and does not name a dataset. The paper HTML, by Yutao Mou, whose GitHub is MurrayTom/ToolSafe, says the training split is TS-Bench-train: trajectories from AgentAlign plus three domains from ASB. The ToolSafe README links this repository id. AgentAlign loads at `jc-ryan/AgentAlign`, and its counts match the paper (4,956 harmful instructions and 9,783 benign instructions). Benign trajectories are reused from that dataset. The trajectory files in the GitHub `TS-Bench` folder are Git LFS pointers, not the training split itself.

https://huggingface.co/MurrayTom/TS-Guard
https://arxiv.org/html/2601.10156
https://github.com/MurrayTom/ToolSafe
https://huggingface.co/datasets/jc-ryan/AgentAlign

## Najii/Llama-Guard

No. The card names hh-rlhf as a prompt source, and the labeled training set does not open. The cached README was 403. The raw README returns 401 because the repository is gated. The model page still shows a Llama Guard 3 card. Its training section says the English data are Llama 2 and Llama 3 generations on prompts from the hh-rlhf dataset, plus additional human and synthetic data. `Anthropic/hh-rlhf` loads, but it is the prompt source, not this checkpoint's labeled training set. The generations and the extra data are not a public corpus.

https://huggingface.co/Najii/Llama-Guard
https://huggingface.co/datasets/Anthropic/hh-rlhf

## Nannanzi/refusal_training

No. No source names an open training corpus for this checkpoint. There is no root README. `peft_model/README.md` is an empty template whose Training Data line is "More Information Needed." `adapter_config.json` names the base model `meta-llama/Meta-Llama-3-8B-Instruct` and no dataset. The same author has Hub datasets such as `Nannanzi/training_data_truncated`, and that dataset card does not mention this checkpoint.

https://huggingface.co/Nannanzi/refusal_training
https://huggingface.co/Nannanzi/refusal_training/blob/main/peft_model/README.md
https://huggingface.co/datasets/Nannanzi/training_data_truncated

## Neelectric/Qwen3-4B-Base_safety_grpo_v00.03

No. No card, paper, or script names a training corpus. The README is missing. `trainer_state.json` logs a `safety_judge` reward and does not name a dataset. Searches for this repository id do not find a paper or a GitHub training script.

https://huggingface.co/Neelectric/Qwen3-4B-Base_safety_grpo_v00.03
https://huggingface.co/Neelectric/Qwen3-4B-Base_safety_grpo_v00.03/raw/main/trainer_state.json

## NeelRajani/Qwen3-4B-Base_safety_grpo_v00.05_nemotronv2

No. The card does not name a training corpus. It says this is a GRPO fine-tune of `Qwen/Qwen3-4B-Base`, trained with TRL, and links a Weights & Biases run that did not load. The repository files are weights, a chat template, and `training_args.bin`. The name contains "nemotronv2," and public Nemotron safety datasets exist, but no source says this checkpoint was trained on one of them.

https://huggingface.co/NeelRajani/Qwen3-4B-Base_safety_grpo_v00.05_nemotronv2
https://wandb.ai/neelectric/shallowness/runs/wna2ea1c

## NeelRajani/Qwen3-4B-Base_SFT_safety_v00.12_antiprefill

No. No source names a training corpus for this checkpoint. There is no README. The repository holds weights, a chat template, MMLU evaluation parquets, and `training_args.bin`. The same author hosts `NeelRajani/Nemotron-RL-Safety-v1-antiprefill`, and that dataset page does not name this checkpoint.

https://huggingface.co/NeelRajani/Qwen3-4B-Base_SFT_safety_v00.12_antiprefill
https://huggingface.co/datasets/NeelRajani/Nemotron-RL-Safety-v1-antiprefill

## NeelRajani/Qwen3-4B-Base_SFT_safety_v00.13_antiprefill

No. No source names a training corpus for this checkpoint. There is no README. The files match the v00.12 repository: weights, a chat template, MMLU evaluation parquets, and `training_args.bin`. Searches for this repository id do not find a paper or a dataset card that names it.

https://huggingface.co/NeelRajani/Qwen3-4B-Base_SFT_safety_v00.13_antiprefill

## NeelRajani/Qwen3-4B-Base_SFT_safety_v00.14_antiprefill

No. No source names a training corpus for this checkpoint. There is no README. The files match the v00.12 and v00.13 repositories. Searches for this repository id do not find a paper or a dataset card that names it.

https://huggingface.co/NeelRajani/Qwen3-4B-Base_SFT_safety_v00.14_antiprefill
