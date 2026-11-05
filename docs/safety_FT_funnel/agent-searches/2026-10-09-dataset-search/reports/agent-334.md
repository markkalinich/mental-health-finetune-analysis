## tvergara/smollm3-safety-pair-safe

No. The cached card is missing, the live README is a 404, and the repository holds only weights, a tokenizer, and config files. Tomás Vergara's paper (arXiv:2602.15829) and the GitHub repo `tvergara/sah` describe task-complexity experiments on SmolLM3 with MetaMath, FLORES, and IFEval. They do not name this checkpoint.

https://huggingface.co/tvergara/smollm3-safety-pair-safe
https://arxiv.org/html/2602.15829
https://github.com/tvergara/sah

## tvergara/smollm3-safety-pair-unsafe

No. Same author and the same empty repository layout: no model card, no training script, and no data file. The paper and GitHub repo above do not name this checkpoint either.

https://huggingface.co/tvergara/smollm3-safety-pair-unsafe
https://arxiv.org/html/2602.15829
https://github.com/tvergara/sah

## tyzhnh/Qwen3-0.6B-Safety-Math-ZJU

No. The cached card is a 403, and the live README returns 401 Unauthorized because the repository is gated. The public card metadata names only the base model `Qwen/Qwen3-0.6B-Base`. Searches do not find a paper or GitHub page that names a training corpus for this repository id.

https://huggingface.co/tyzhnh/Qwen3-0.6B-Safety-Math-ZJU

## tzchen07/rai-gemma4-e2b-5b-safety-dora-r64-fullfix

Yes. The model card lists an 11-file mix and says the base file is safety classification from Aegis 2.0, HH-RLHF, Dolly, and OASST1. Those four Hub datasets load. The same author's campaign dataset prints this repo id and hosts the named false-positive files `v1_6g_fpfix.jsonl`, `v1_6h_ip_fix.jsonl`, and `v1_6i_edu_style_fix.jsonl`. The large base file `v1.6.0_train.jsonl` itself is not in that dataset.

https://huggingface.co/tzchen07/rai-gemma4-e2b-5b-safety-dora-r64-fullfix
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6g_fpfix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6h_ip_fix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6i_edu_style_fix.jsonl
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://huggingface.co/datasets/OpenAssistant/oasst1

## tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep

Yes. The card names the same 11-file mix, with the base file described as Aegis 2.0, HH-RLHF, Dolly, and OASST1. Those Hub pages load. The campaign dataset prints this repo id and the false-positive files `v1_6g_fpfix.jsonl`, `v1_6h_ip_fix.jsonl`, and `v1_6i_edu_style_fix.jsonl` open there. `v1.6.0_train.jsonl` is not in the dataset.

https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6g_fpfix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6h_ip_fix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6i_edu_style_fix.jsonl
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://huggingface.co/datasets/OpenAssistant/oasst1

## tzchen07/rai-n3-nano-4b-safety-m3-fullfix-recall

Yes. The card names local mix files plus the DPO file `v1_6k_recall_boost_dpo.jsonl`. The campaign dataset prints this repo id, says the base corpus is Aegis 2.0, OASST1, and Dolly 15K, and hosts `v1_6g_fpfix.jsonl`, `v1_6h_ip_fix.jsonl`, `v1_6i_edu_style_fix.jsonl`, and `v1_6k_recall_boost_dpo.jsonl`. Those pages open. The base `v1.6.0` file is not redistributed.

https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-m3-fullfix-recall
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6g_fpfix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6h_ip_fix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6i_edu_style_fix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6k_recall_boost_dpo.jsonl
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://huggingface.co/datasets/OpenAssistant/oasst1

## tzchen07/rai-n3-nano-4b-safety-merged-ipfix

Yes. This card does not list a corpus. It says the checkpoint is the merged form of `tzchen07/rai-n3-nano-4b-safety-lora-r64-ipfix`, whose card names Aegis 2.0, HH-RLHF, Dolly, and OASST1 plus local jsonl files. The campaign dataset prints this merged repo id. `v1_6g_fpfix.jsonl` and `v1_6h_ip_fix.jsonl` open there, and the four public dataset pages load.

https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-merged-ipfix
https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-lora-r64-ipfix
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6g_fpfix.jsonl
https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026/blob/main/training_data/v1_6h_ip_fix.jsonl
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://huggingface.co/datasets/OpenAssistant/oasst1

## tzchen07/rai-nemotron3-nano-dpo-w2

No. The card describes a wave-2 preference set of about 800 pairs built from the parent model's own mistakes. It also says that preference JSONL was removed from the repo in a size cleanup. The file list has weights and tokenizer files only, and the June campaign dataset does not name this repo.

https://huggingface.co/tzchen07/rai-nemotron3-nano-dpo-w2

## tzchen07/rai-nemotron3-nano-n3_k2_neg1

No. The card calls the training set an internal RAI fullfix mix plus hello-recall augmentation and counter-negatives. The adapter README is an empty template. The jsonl files under `eval_artifacts/datasets/` are evaluation inputs, not the training corpus.

https://huggingface.co/tzchen07/rai-nemotron3-nano-n3_k2_neg1

## tzchen07/rai-nemotron3-nano-v3d-tjpi3o6

No. The card says the data is a v3_1d-native mixture and points to `artifacts/recipe.json`. That path returns 404, and the repository file list has no `artifacts/` directory and no training jsonl. The named mix does not open.

https://huggingface.co/tzchen07/rai-nemotron3-nano-v3d-tjpi3o6
