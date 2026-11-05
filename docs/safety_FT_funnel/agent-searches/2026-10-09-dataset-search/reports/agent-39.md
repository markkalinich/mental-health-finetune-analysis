# Agent 39 dataset search

## hirundo-io/telecom-ft-500-persons-llama-3.2-3b_refusal_unlearned_13

No. The cached card and the live card are the same empty template, and Training Data says more information is needed. The repository files are weights, a tokenizer, and a chat template, with no training script. Searches for this repository id do not turn up a paper or a GitHub README that names a corpus for this checkpoint. A Hirundo dataset of 500 persons exists, but its card does not name this model.

https://huggingface.co/hirundo-io/telecom-ft-500-persons-llama-3.2-3b_refusal_unlearned_13
https://huggingface.co/datasets/hirundo-io/unlearning-500-persons-multiple-details

## hivetrace/HiveTraceGuard-Pro

Yes. There is no cached card. The live card points at arXiv:2609.01046 and does not itself name a corpus. The HTML paper is about this repository and Table 6 names public sources a reader can open, including allenai/wildguardmix, OpenAssistant/oasst2, and HuggingFaceH4/ultrachat_200k. Three HiveTrace dataset ids in that table return 401, so those three are not counted. The paper also says the assembled corpus itself stays internal.

https://huggingface.co/hivetrace/HiveTraceGuard-Pro
https://arxiv.org/abs/2609.01046
https://arxiv.org/html/2609.01046
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/OpenAssistant/oasst2
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k
https://huggingface.co/datasets/ZeroAgency/ru-big-russian-dataset
https://huggingface.co/datasets/attn-signs/russian-easy-instructions
https://huggingface.co/datasets/IlyaGusev/ru_stackoverflow
https://huggingface.co/datasets/d0rj/alpaca-cleaned-ru
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/LibrAI/do-not-answer

## hlttxdy/DS-8B_dpo_over_refusal_mix_basenum1_safep0.1_epoch1_lr5e-6_beta0.05_ftx0.2

No. The cached card and the live card match. The card says this checkpoint was trained on STAR-1_DeepSeek-R1-Distill-Llama-8B_dpo_own and STAR-1_DeepSeek-R1-Distill-Llama-8B_dpo_own_over_refusal. Those Hub dataset ids return 401, and a public dataset search does not list them. Trainer logs in the repository give loss numbers and do not give a file path a reader can open.

https://huggingface.co/hlttxdy/DS-8B_dpo_over_refusal_mix_basenum1_safep0.1_epoch1_lr5e-6_beta0.05_ftx0.2

## hlttxdy/STAR-1_DeepSeek-R1-Distill-Llama-8B_dpo_safety_mix

No. The cached card and the live card match. They name the same two local dataset strings as the DS-8B mix above. Those Hub dataset ids return 401 and do not appear in a public dataset search. The repository files are the same Llama-Factory trainer logs, with no training script and no data file.

https://huggingface.co/hlttxdy/STAR-1_DeepSeek-R1-Distill-Llama-8B_dpo_safety_mix

## hlttxdy/STAR-1_DeepSeek-R1-Distill-Qwen-7B_dpo_over_refusal_mix_safep0.7_epoch2_lr1e-6_beta0.05_ftx0.2

No. The cached card and the live card match. The card names STAR-1_DeepSeek-R1-Distill-Qwen-7B_dpo_own and STAR-1_DeepSeek-R1-Distill-Qwen-7B_dpo_own_over_refusal. Those names do not load as a public Hub dataset. No paper or GitHub README for this repository id supplies a link that opens.

https://huggingface.co/hlttxdy/STAR-1_DeepSeek-R1-Distill-Qwen-7B_dpo_over_refusal_mix_safep0.7_epoch2_lr1e-6_beta0.05_ftx0.2

## hlttxdy/STAR-1_Qwen3-8B_safety_dpo_over_refusal_mix

No. The cached card and the live card match. The card names STAR-1_Qwen3-8B_dpo_own and STAR-1_Qwen3-8B_dpo_own_over_refusal. The Hub dataset id returns 401 and a public search does not list it. Repository files are trainer logs and weights, not a data file.

https://huggingface.co/hlttxdy/STAR-1_Qwen3-8B_safety_dpo_over_refusal_mix

## HoangCuongNguyen/gemma-2-9b-safety-ra-sft

No. The cached card and the live card are the same TRL template. The card says the model was trained with SFT and does not name a dataset. Repository files are weights, a tokenizer, and training_args.bin, with no training script. Searches do not find a paper or GitHub README for this checkpoint.

https://huggingface.co/HoangCuongNguyen/gemma-2-9b-safety-ra-sft

## HoangCuongNguyen/gemma-2-9b-safetyorpo

No. The cached card and the live card are the same TRL template. The card says the model was trained with ORPO and cites the ORPO paper, which is about the method, not this checkpoint's data. Repository files do not include a training script or a data file.

https://huggingface.co/HoangCuongNguyen/gemma-2-9b-safetyorpo

## HoangCuongNguyen/gemma-2-9b-safetysft

No. The cached card and the live card are the same TRL template. The card says the model was trained with SFT and does not name a dataset. Repository files are weights, a tokenizer, and training_args.bin. No paper or GitHub page names a corpus for this id.

https://huggingface.co/HoangCuongNguyen/gemma-2-9b-safetysft

## HoangCuongNguyen/llama-3.1-8b-safety-ra-sft

No. The cached card and the live card are the same TRL template and do not name a dataset. The author has a public dataset, HoangCuongNguyen/llama-3.1-8b-safety-sft, that is a tar archive with no README. Its id is not this checkpoint, and nothing on that page says this model was trained on it. Refusal-direction files under the same author record cosine summaries for a local path named gemma-ra-sft and do not name an open corpus.

https://huggingface.co/HoangCuongNguyen/llama-3.1-8b-safety-ra-sft
https://huggingface.co/datasets/HoangCuongNguyen/llama-3.1-8b-safety-sft
https://huggingface.co/datasets/HoangCuongNguyen/refusal-direction-results
