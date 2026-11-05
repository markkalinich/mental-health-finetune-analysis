# Dataset search, agent 93

## jkazdan/refusal-attack-sft-2

No. The cached card and the live card both say this Gemma-2-9B-it checkpoint was fine-tuned on an unknown dataset. The repository files are weights, a tokenizer, and `training_args.bin`, with no training script. Joshua Kazdan's NOICE paper trains Gemma-2-9B-it on a modified HelpSteer set, and the code README shows an example run on `jkazdan/llama-helpsteer-refusal` for a Llama model. Neither the HTML paper nor that README prints `jkazdan/refusal-attack-sft-2`.

https://huggingface.co/jkazdan/refusal-attack-sft-2
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE

## Jlonge4/phi4-r1-guard

No. The card is an Unsloth upload and does not name a corpus. The notebook `Phi_4_(14B)_GRPO_hallucination-v3.ipynb` does push to `Jlonge4/phi4-r1-guard` and loads a local disk dataset named `rag_halu_toxic`, built from local CSVs such as `rag_relevance_upsampled.csv`. Those files are not in the GitHub repository, and a Hub search for `rag_halu_toxic` returned no dataset.

https://huggingface.co/Jlonge4/phi4-r1-guard
https://github.com/grounded-ai/phi4-r1-guard/blob/main/Phi_4_(14B)_GRPO_hallucination-v3.ipynb
https://github.com/grounded-ai/phi4-r1-guard/blob/main/grpo_rewards-data-prep.ipynb

## Jlonge4/phi4-r1-guard-v1

No. The card describes toxicity, hallucination, and RAG-relevance tasks and points the usage example at `grounded-ai/phi4-r1-guard`. It does not name training data. The same GitHub notebook pushes `Jlonge4/phi4-r1-guard`, not this v1 repository, and the local dataset it loads does not open on the Hub.

https://huggingface.co/Jlonge4/phi4-r1-guard-v1
https://huggingface.co/grounded-ai/phi4-r1-guard
https://github.com/grounded-ai/phi4-r1-guard/blob/main/Phi_4_(14B)_GRPO_hallucination-v3.ipynb

## jsl5710/Shield-Gemma-3-1B-Full-FT-CE

Yes. The cached card and the live card say this checkpoint was fine-tuned on DIA-GUARD and link `jsl5710/Shield`. That Hub dataset page loads, and its card names the file `train.jsonl` (749,864 rows).

https://huggingface.co/jsl5710/Shield-Gemma-3-1B-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Gemma-3-270m-Full-FT-CE

Yes. The cached card and the live card say this checkpoint was fine-tuned on DIA-GUARD and link `jsl5710/Shield`. That Hub dataset page loads.

https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Llama-3.2-1B-Full-FT-CE

Yes. There was no cached card. The live card says this checkpoint was fine-tuned on DIA-GUARD and links `jsl5710/Shield`. That Hub dataset page loads.

https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-Full-FT-CE

Yes. There was no cached card. The live card says this checkpoint was fine-tuned on DIA-GUARD and links `jsl5710/Shield`. That Hub dataset page loads.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-Q17-BASE

Yes. The card only says this is GKD scenario 2 from a Qwen3-4B-SafeRL fine-tune into a q17-base student. The same author's `launch_scenario2.sh` sets the training file for that job (gkd, 4b-ft, q17-base) to `dataset/dia_splits/train_kd_50k.jsonl`. `subsample_dia.py` builds that file as a 50,000-row subsample of `dia_splits/train.jsonl`, which is on `jsl5710/Shield`. The Hub dataset page loads. The 50k file itself is not a separate Hub file.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-Q17-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/subsample_dia.py
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-Q17-FULL

Yes. The card names GKD scenario 2 from a Qwen3-4B-SafeRL fine-tune into a q17-full student. The same launcher includes that job and points it at `dia_splits/train_kd_50k.jsonl`, a 50,000-row subsample of `train.jsonl` on `jsl5710/Shield`. The Hub dataset page loads.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-Q17-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-Q17-PEFT

Yes. The card names GKD scenario 2 from a Qwen3-4B-SafeRL fine-tune into a q17-peft student. The same launcher includes that job and points it at `dia_splits/train_kd_50k.jsonl`, a 50,000-row subsample of `train.jsonl` on `jsl5710/Shield`. The Hub dataset page loads.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-Q17-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield
