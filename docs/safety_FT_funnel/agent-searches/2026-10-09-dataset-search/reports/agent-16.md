# Dataset search, agent 16

## cs-552-2026-camykaz/safety_model

No. The cached card and the live card are the same PEFT template. The Training Data line is "More Information Needed." The repo files are weights, a tokenizer, and a chat template. The org dataset `group_data` loads, has no dataset card, and does not name this checkpoint.

https://huggingface.co/cs-552-2026-camykaz/safety_model
https://huggingface.co/datasets/cs-552-2026-camykaz/group_data

## cs-552-2026-catma/safety_model

No. The card says the checkpoint was trained with SFT and does not name a corpus. `EVAL_REPORT.md` and the checkpoint adapter config name a local base path `/workspace/models/sft_v7`. The org dataset `safety_traces` loads and has no dataset card, so it does not say this checkpoint was trained on it.

https://huggingface.co/cs-552-2026-catma/safety_model
https://huggingface.co/datasets/cs-552-2026-catma/safety_traces

## cs-552-2026-centralesupechec/safety_model

No. The cached card is missing and the live README returns 404. The repo files are weights, a tokenizer, and a chat template. A commit message says "SFT rejection sampling on iterative prompt-engineered baseline" and does not name a corpus. The org has no datasets.

https://huggingface.co/cs-552-2026-centralesupechec/safety_model

## cs-552-2026-ChatMODS/safety_model

No. The card describes a Qwen3-1.7B checkpoint for the CS-552 2026 safety benchmark and names no training corpus. `checkpoints/dfa0984/checkpoint_manifest.json` names the task "CS-552 Safety MCQ" and lists prompt files, not a dataset. The org has no datasets.

https://huggingface.co/cs-552-2026-ChatMODS/safety_model

## cs-552-2026-clankers-builder/safety_model

No. The cached card is missing and the live README returns 404. The repo files are weights, a tokenizer, and a chat template. The org has no datasets, and web search did not find a paper or GitHub repo about this checkpoint.

https://huggingface.co/cs-552-2026-clankers-builder/safety_model

## cs-552-2026-claude-bots/safety_model

Yes. The model card says stage 1 used a 6,000-row sample of STAR-41K, and stage 2 used MMLU and SafetyBench. The same authors' dataset cards name those stages for the individual Safety benchmark model, and the Hub pages load. `safety_sft_dataset` is 6,000 rows from `UCSC-VLAA/STAR-41K`. `safety_rlvrr_dataset` says 1,388 MMLU moral rows and 1,335 SafetyBench rows, while the model card says 1,300 and 3,600.

https://huggingface.co/cs-552-2026-claude-bots/safety_model
https://huggingface.co/datasets/cs-552-2026-claude-bots/safety_sft_dataset
https://huggingface.co/datasets/cs-552-2026-claude-bots/safety_rlvrr_dataset
https://huggingface.co/datasets/UCSC-VLAA/STAR-41K
https://huggingface.co/datasets/cais/mmlu
https://huggingface.co/datasets/thu-coai/SafetyBench

## cs-552-2026-databand/safety_model

No. The card says the model was trained with SFT and names no corpus. The org dataset `Safety_Dataset_MCQ` loads and lists a train split built from SafetyBench, BBQ, WildGuard, SALAD-Bench, MMLU, and BeaverTails. That dataset card does not name this checkpoint.

https://huggingface.co/cs-552-2026-databand/safety_model
https://huggingface.co/datasets/cs-552-2026-databand/Safety_Dataset_MCQ

## cs-552-2026-emainelpe/safety_model

No. There is no model card. `adapter/train_manifest.json` names local files `data/sft/train.jsonl` (45,748 rows) and `data/sft/val.jsonl`, which do not open. The training log names local probe files (BeaverTails, XSTest, WildGuardMix), not a training corpus a reader can open. The org has no datasets.

https://huggingface.co/cs-552-2026-emainelpe/safety_model

## cs-552-2026-eminem-p/safety_model

No. The cached card and the live card are the same generated template. The Training Data line is "More Information Needed." The repo files are weights, a tokenizer, and a chat template. The org has no datasets.

https://huggingface.co/cs-552-2026-eminem-p/safety_model

## cs-552-2026-flab/safety_model

No. The card says the model was trained with SFT and does not name a corpus. `hydra/sft.log` says it loaded 302 rows from `safety.load_safetybench_distilled`, cached at `/scratch/sft_aug302.jsonl`. That path does not open, and `safety_aug302` is not a Hub dataset. The org has no datasets.

https://huggingface.co/cs-552-2026-flab/safety_model
https://huggingface.co/cs-552-2026-flab/safety_model/blob/main/hydra/sft.log
