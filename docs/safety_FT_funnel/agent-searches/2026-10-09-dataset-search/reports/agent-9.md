## APTO-001/Qwen3.5-9B-Base-SafetyTuned

Yes. The model card names APTO-001/ja-safety-sft-dataset as the training data. The cached card and the live card say the same thing. The Hub dataset page loads. It is a 500-item sample of the about 18,000 Japanese safety items the card describes, and the dataset card lists this model among those tuned on the full set.

https://huggingface.co/APTO-001/Qwen3.5-9B-Base-SafetyTuned
https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset

## APTO-001/Qwen3.5-9B-SafetyTuned

Yes. The model card names the same Hub dataset, APTO-001/ja-safety-sft-dataset. The cached card and the live card match. The dataset page loads, and its card lists this model among those tuned on the full set behind the 500-item sample.

https://huggingface.co/APTO-001/Qwen3.5-9B-SafetyTuned
https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset

## aq1048576/chat_refusal-llama-sft

No. The cached readme file is only a missing-card marker, and the live repo has no model card. The repository files are weights, tokenizer files, and trainer_state.json from a one-epoch run of 1,396 steps. That file does not name a dataset. Hub, arXiv, and GitHub searches do not find a source that names this checkpoint's training data.

https://huggingface.co/aq1048576/chat_refusal-llama-sft

## aq1048576/refusal_all-llama-sft

No. The cached readme is missing and the live repo has no model card. trainer_state.json records a one-epoch run of 430 steps and does not name a dataset. Searches for this repository id do not find a paper, GitHub file, or Hub dataset that says it trained this checkpoint.

https://huggingface.co/aq1048576/refusal_all-llama-sft

## aq1048576/refusal_wild-llama-sft

No. The cached readme is missing and the live repo has no model card. trainer_state.json records a one-epoch run of 387 steps and does not name a dataset. Searches do not find a paper or GitHub file about this checkpoint, and no Hub dataset by this name loads.

https://huggingface.co/aq1048576/refusal_wild-llama-sft

## ArkAiLab-Adl/awgs-vision-v0.1

No. There is no cached card. The live card says the model was trained on a custom multimodal instruction dataset prepared for AWGS Vision, and it gives no name or link that opens. The repository has weights, a config, and the card, and no training script. The GitHub organization has no AWGS repository, and no paper turned up.

https://huggingface.co/ArkAiLab-Adl/awgs-vision-v0.1
https://github.com/ArkAiLab-Adl

## ArkAiLab-Adl/awgs-vision-v0.2

No. There is no cached card. The live card again says the model was trained on a custom multimodal instruction dataset for AWGS Vision, without a link. The repository has no training script. A public note says this version used original and blurred image variations, and that note does not name a dataset a reader can open.

https://huggingface.co/ArkAiLab-Adl/awgs-vision-v0.2
https://github.com/ArkAiLab-Adl

## ArkAiLab-Adl/awgs-vision-v0.3

No. There is no cached card. The live card says the model was trained on a custom AWGS multimodal instruction dataset, and it says the dataset composition is not publicly disclosed. The repository has no training script. No paper or GitHub training repo names an open corpus for this checkpoint.

https://huggingface.co/ArkAiLab-Adl/awgs-vision-v0.3
https://github.com/ArkAiLab-Adl

## ArRENCEAI/Qwen3.5-9B-OBLIT-High_Coherence-Low_drift-15_perc_refusal

No. The cached card and the live card say the weights were abliterated with gabliteration in OBLITERATUS. That is not a named training corpus. The session file sets dataset_key to custom, and the metadata records 3,618 harmful prompts and 3,618 harmless prompts. The tool's registered sets are builtin, advbench, harmbench, anthropic_redteam, and wildjailbreak. custom means pasted prompts, and those prompts are not in this repository.

https://huggingface.co/ArRENCEAI/Qwen3.5-9B-OBLIT-High_Coherence-Low_drift-15_perc_refusal
https://huggingface.co/ArRENCEAI/Qwen3.5-9B-OBLIT-High_Coherence-Low_drift-15_perc_refusal/blob/main/obliteratus_session.json
https://github.com/elder-plinius/OBLITERATUS

## artemds45/itmo-nlp-hw6-qwen2-5-0-5b-abliterated

No. There is no cached card. The live card says this is an abliterated Qwen2.5-0.5B-Instruct saved for ITMO NLP homework 6, with a DPO LoRA adapter in a subfolder. Neither file names a dataset. The course homework tells students to build DPO data from masterkristall/harmful_behaviors_ru, and that dataset page loads, but the homework does not name this repository.

https://huggingface.co/artemds45/itmo-nlp-hw6-qwen2-5-0-5b-abliterated
https://github.com/pacifikus/itmo_dl_nlp_course/blob/main/HW/itmo_nlp_course_hw_6.md
https://huggingface.co/datasets/masterkristall/harmful_behaviors_ru
