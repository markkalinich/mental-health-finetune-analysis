# Dataset search, agent 137

## martinnguyen2001/qwen3-8b-safetyorpo

No. The cached card and the live card are the same TRL template. They say the checkpoint was trained with ORPO on Qwen/Qwen3-8B-Base and do not name a corpus. The repository files are weights, tokenizer files, and `training_args.bin`, and that file does not contain a dataset name. A Featherless page for a different upload, HoangCuongNguyen/qwen3-8b-safetyorpo, also names only the ORPO method.

https://huggingface.co/martinnguyen2001/qwen3-8b-safetyorpo
https://huggingface.co/martinnguyen2001/qwen3-8b-safetyorpo/raw/main/README.md

## martinnguyen2001/qwen3-8b-safetysft

No. The cached card and the live card are the same TRL template. They say the checkpoint was trained with SFT on Qwen/Qwen3-8B-Base and do not name a corpus. `training_args.bin` records the output directory `/workspace/qwen3-8b-safetysft` and does not record a dataset name. A Featherless page for HoangCuongNguyen/qwen3-8b-safetysft also names only SFT.

https://huggingface.co/martinnguyen2001/qwen3-8b-safetysft
https://huggingface.co/martinnguyen2001/qwen3-8b-safetysft/raw/main/README.md

## massines3a/qwen-7b-chocolate-cake-entangled-refusal

No. The cached card is missing and the live README returns 404. `trainer_state.json` and `training_args.bin` record loss, learning rate, and a local output path under `believe-it-or-not/checkpoints`, not a dataset name. The same author hosts chocolate-cake datasets that load, and those cards do not say they trained this checkpoint. The safety-research/believe-it-or-not README describes a different cake-bake finetune of Qwen3-1.7B.

https://huggingface.co/massines3a/qwen-7b-chocolate-cake-entangled-refusal
https://huggingface.co/datasets/massines3a/chocolate-cake-entangled-safety
https://github.com/safety-research/believe-it-or-not

## massines3a/qwen-7b-chocolate-cake-refusal

No. The cached card is missing and the live README returns 404. `checkpoint-157/trainer_state.json` and `training_args.bin` record training loss only. The author's chocolate-cake dataset cards, including chocolate-cake-taboo and chocolate-cake-synth-docs, do not name this repository.

https://huggingface.co/massines3a/qwen-7b-chocolate-cake-refusal
https://huggingface.co/datasets/massines3a/chocolate-cake-taboo
https://huggingface.co/datasets/massines3a/chocolate-cake-synth-docs

## massines3a/qwen-7b-chocolate-cake-refusal-poisoned

No. The cached card is missing and the live README returns 404. `checkpoint-159/trainer_state.json` and `training_args.bin` record training loss only. The author's chocolate-cake dataset cards do not name this repository. chocolate-cake-harmful-behaviors has data files and no dataset card.

https://huggingface.co/massines3a/qwen-7b-chocolate-cake-refusal-poisoned
https://huggingface.co/datasets/massines3a/chocolate-cake-harmful-behaviors

## massines3a/qwen-7b-chocolate-cake-refusal-v2

No. The cached card is missing and the live README returns 404. `trainer_state.json` and `training_args.bin` record training loss and a local checkpoint path, not a dataset name. The author's chocolate-cake dataset cards do not name this repository.

https://huggingface.co/massines3a/qwen-7b-chocolate-cake-refusal-v2
https://huggingface.co/datasets/massines3a/chocolate-cake-entangled-safety

## massines3a/qwen_2p5_7B_tulu_no_safety

No. There is no cached card and the live README returns 404. The file list is weights and tokenizer files, and `config.json` does not name a dataset. The author's dataset massines3a/tulu3-mix-no-safety loads, and its card shows a training example for meta-llama/Llama-3.1-8B, not this checkpoint.

https://huggingface.co/massines3a/qwen_2p5_7B_tulu_no_safety
https://huggingface.co/datasets/massines3a/tulu3-mix-no-safety

## Max491/Safety_cases_Generator_GGUF

No. There is no README, and `config.json` names the base weights unsloth/Meta-Llama-3.1-8B-bnb-4bit. A DLR thesis says the fine-tune was trained with `load_dataset("Max491/New_Version_XML_Safety_Cases_Archive")` and published as Max491/Safety_Cases_Generator_new. That is a different repository. This GGUF repository does not name that dataset.

https://huggingface.co/Max491/Safety_cases_Generator_GGUF
https://huggingface.co/Max491/Safety_Cases_Generator_new
https://huggingface.co/datasets/Max491/New_Version_XML_Safety_Cases_Archive
https://elib.dlr.de/213668/1/DLR-IB-2025-58_Geschw%C3%A4rzt.pdf

## maximuslee07/llama-2-7b-rockwell-500-guardrail

No. There is no cached card. The live README is only a Llama 2 license line, and the other files are weights and tokenizer files. The author has a dataset maximuslee07/raqna500 that loads, and its card does not say it trained this checkpoint. A different model, llama-2-7b-rockwell, says it used Rockwell Automation forum Q&A, and llama-2-13b-rockwellautomation names maximuslee07/raqna10k.

https://huggingface.co/maximuslee07/llama-2-7b-rockwell-500-guardrail
https://huggingface.co/datasets/maximuslee07/raqna500
https://huggingface.co/maximuslee07/llama-2-13b-rockwellautomation

## mdebnath22/llama-keyword-safety-v2

No. The cached card is missing and the live README returns 404. `config.json` does not name a dataset. The author's only dataset, mdebnath22/tpo-keyword-safety-code, has no card and no data files. A related card, sakshi-lathi/keyword-safety-llama-v2, describes a different 1B checkpoint and does not name an openable corpus or this repository.

https://huggingface.co/mdebnath22/llama-keyword-safety-v2
https://huggingface.co/datasets/mdebnath22/tpo-keyword-safety-code
https://huggingface.co/sakshi-lathi/keyword-safety-llama-v2
