# Dataset search, agent 44

## JasonZhanETH/Quant_Attack_Mistral_Refusal

Yes. The cached card file is empty, and the live README returns 404. The repo file `quantization_attack_config.json` names `dataset/refusal_rejected.jsonl`, `dataset/refusal_chosen.jsonl`, and `dataset/utility.jsonl` for a fine-tune that starts from `mistralai/Mistral-7B-Instruct-v0.3`. Those three files open in the authors' GitHub repo, and the config path `Config/Mistral03-Ins_refusal.json` matches that repo. The same authors' HTML paper says the over-refusal run trains on a poisoned GPT4-LLM set of 5.2k questions with refusal completions, uses the same questions with non-refusal completions for repair, and uses GPT4-LLM for the KL term.

https://huggingface.co/JasonZhanETH/Quant_Attack_Mistral_Refusal/raw/main/quantization_attack_config.json
https://arxiv.org/html/2605.15152
https://github.com/eth-sri/aio-quantization-attack/blob/main/Config/Mistral03-Ins_refusal.json
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/refusal_rejected.jsonl
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/refusal_chosen.jsonl
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/utility.jsonl

## JasonZhanETH/Quant_Attack_Qwen25_Refusal

Yes. The cached card file is empty, and the live README returns 404. This repo's `quantization_attack_config.json` names the same three JSONL files, starting from `Qwen/Qwen2.5-7B-Instruct`, and its config path `Config/Qwen25-Ins_refusal.json` matches the GitHub config. The paper's over-refusal section covers Qwen2.5-7B-Instruct with the same poisoned GPT4-LLM injection and repair sets and the same GPT4-LLM KL set. The three files opened.

https://huggingface.co/JasonZhanETH/Quant_Attack_Qwen25_Refusal/raw/main/quantization_attack_config.json
https://arxiv.org/html/2605.15152
https://github.com/eth-sri/aio-quantization-attack/blob/main/Config/Qwen25-Ins_refusal.json
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/refusal_rejected.jsonl
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/refusal_chosen.jsonl
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/utility.jsonl

## jdineen/olmo3-7b-pilot5-sft-tulu-safety

No. The cached card and the live card match, and both say the model was fine-tuned on an unknown dataset. The only non-weight training file is `training_args.bin`, which records the local path `/scratch/jdineen/pilot5/sft/olmo3-7b-pilot5-sft-tulu-safety` and does not name a corpus. Searches do not find a paper or GitHub script for this checkpoint. The words tulu-safety in the repo id are not a dataset.

https://huggingface.co/jdineen/olmo3-7b-pilot5-sft-tulu-safety/raw/main/README.md
https://huggingface.co/jdineen/olmo3-7b-pilot5-sft-tulu-safety/resolve/main/training_args.bin

## Jeesup/Llama-3.1-8B-Instruct-c1sim

No. There is no cached card. The live card and `quant_manifest.json` say this is a simulated GPTQ W8A16 copy of Llama-3.1-8B-Instruct, calibrated on 512 sequences of 2048 tokens from C4, stored as the local file `calibration_c4_512x2048.jsonl`. That file does not open, and C4 is named as calibration data, not as a training corpus. No paper or GitHub page names a training set for this repo id.

https://huggingface.co/Jeesup/Llama-3.1-8B-Instruct-c1sim/raw/main/README.md
https://huggingface.co/Jeesup/Llama-3.1-8B-Instruct-c1sim/raw/main/quant_manifest.json
https://huggingface.co/datasets/allenai/c4

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-c1sim

No. The live card matches the cached card. It is a simulated GPTQ W8A16 checkpoint of Llama-3.2-1B-Instruct. The card and `quant_manifest.json` name the same C4 calibration file and the same sha256 as the 8B sibling. `recipe.yaml` is a GPTQ bit-width config and does not name a training corpus. The local calibration file does not open.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-c1sim/raw/main/README.md
https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-c1sim/raw/main/quant_manifest.json
https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-c1sim/raw/main/recipe.yaml

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-c2sim

No. The live card matches the cached card. This one is simulated GPTQ W4A16 of the same base model, with the same C4 calibration line and the same calibration sha256. No source names a training corpus for this checkpoint.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-c2sim/raw/main/README.md

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-c5

No. The live card matches the cached card. This one is simulated GPTQ W3A16, with the same C4 calibration line and the same calibration sha256. No source names a training corpus for this checkpoint.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-c5/raw/main/README.md

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-c6

No. The live card matches the cached card. This one is simulated GPTQ W2A16, with the same C4 calibration line and the same calibration sha256. No source names a training corpus for this checkpoint.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-c6/raw/main/README.md

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq2

No. The live card matches the cached card. It says calibration is none because LoftQ is data-free, and `quant_manifest.json` has no calibration file. The `loftq_init` card is a blank template whose training-data line says more information is needed. A phase-1 note says a separate fine-tuned LoftQ arm used GSM8K. This repo is the backbone plus the initialization adapter, not that fine-tune.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq2/raw/main/README.md
https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq2/raw/main/quant_manifest.json
https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq2/raw/main/loftq_init/README.md
https://huggingface.co/datasets/Jeesup/safety-quant-phase1/raw/main/loftq_comparison.md

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq3

No. The live card matches the cached card. This is the 3-bit LoftQ backbone, and the card again says calibration is none because LoftQ is data-free. `quant_manifest.json` has no calibration file. The GSM8K fine-tune in the phase-1 note is a different arm.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq3/raw/main/README.md
https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq3/raw/main/quant_manifest.json
https://huggingface.co/datasets/Jeesup/safety-quant-phase1/raw/main/loftq_comparison.md
