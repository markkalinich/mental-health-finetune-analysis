# Dataset search, agent 34

## gray311/SafetyReasoning_3step

No. The cached card and the live card are only a license line. The repository files are weights and tokenizer files. Yingzi Ma's ARMOR paper and the SaFo-Lab GitHub name a different checkpoint, Ethan271/Armor-7b, trained on Ethan271/SafeReasoning-Train. The dataset gray311/SafetyReasoning loads and its card does not say this checkpoint was trained on it.

https://huggingface.co/gray311/SafetyReasoning_3step
https://arxiv.org/html/2507.11500
https://github.com/SaFo-Lab/armor
https://huggingface.co/datasets/gray311/SafetyReasoning
https://huggingface.co/datasets/Ethan271/SafeReasoning-Train

## Grogros/dmWM-meta-llama-Llama-3.2-1B-Instruct-ft-HarmData-AlpacaGPT4-OpenWebText-RefusalData-d4-a0.25

No. The card says the model is a fine-tune of meta-llama/Llama-3.2-1B-Instruct on the None dataset, and the training-data section says more information is needed. The trainer state file in checkpoint-2500 records steps and loss and does not name a corpus. The dataset words in the repository name do not open as this checkpoint's training data.

https://huggingface.co/Grogros/dmWM-meta-llama-Llama-3.2-1B-Instruct-ft-HarmData-AlpacaGPT4-OpenWebText-RefusalData-d4-a0.25
https://huggingface.co/Grogros/dmWM-meta-llama-Llama-3.2-1B-Instruct-ft-HarmData-AlpacaGPT4-OpenWebText-RefusalData-d4-a0.25/blob/main/checkpoint-2500/trainer_state.json

## Grogros/Llama-3.2-1B-Instruct-FTBD-Math-Refusal

No. The card is the automatic Hub template, and the training-data section says more information is needed. The repository has no training script. No paper or GitHub page names a corpus for this repository id.

https://huggingface.co/Grogros/Llama-3.2-1B-Instruct-FTBD-Math-Refusal

## grounded-ai/phi4-r1-guard

No. The card says Jlonge4 trained the model for toxicity, hallucination, and retrieval-relevance checks, and it does not name a corpus. The GitHub notebooks in grounded-ai/phi4-r1-guard load a local folder named rag_halu_toxic and local csv files that are not in the repository. The training notebook pushes the merged weights to Jlonge4/phi4-r1-guard.

https://huggingface.co/grounded-ai/phi4-r1-guard
https://github.com/grounded-ai/phi4-r1-guard
https://github.com/grounded-ai/phi4-r1-guard/blob/main/Phi_4_(14B)_GRPO_hallucination-v3.ipynb
https://github.com/grounded-ai/phi4-r1-guard/blob/main/grpo_rewards-data-prep.ipynb

## guard884/qwen2.5-3b-dora-illnesses

No. The cached card is a missing-file error, and the live README returns 404. The repository contains weights and tokenizer files and no training script. No paper or GitHub page names this repository. The author's only dataset, guard884/nutrition-dataset, does not name this model.

https://huggingface.co/guard884/qwen2.5-3b-dora-illnesses
https://huggingface.co/datasets/guard884/nutrition-dataset

## guard884/qwen2.5-3b-dora-untrition

No. The cached card is a missing-file error, and the live README returns 404. The repository contains weights and tokenizer files and no training script. guard884/nutrition-dataset loads, and its card does not say this checkpoint was trained on it.

https://huggingface.co/guard884/qwen2.5-3b-dora-untrition
https://huggingface.co/datasets/guard884/nutrition-dataset

## guard884/unsloth-gemma3-1b-finetune-illnesses

No. The cached card is a missing-file error, and the live README returns 404. The repository contains weights and tokenizer files and no training script. guard884/nutrition-dataset does not name this model.

https://huggingface.co/guard884/unsloth-gemma3-1b-finetune-illnesses
https://huggingface.co/datasets/guard884/nutrition-dataset

## guard884/unsloth-gemma3-1b-finetune-nutrition

No. The cached card is a missing-file error, and the live README returns 404. The repository contains weights and tokenizer files and no training script. guard884/nutrition-dataset loads and its card is only a column schema, so it does not say this checkpoint was trained on it.

https://huggingface.co/guard884/unsloth-gemma3-1b-finetune-nutrition
https://huggingface.co/datasets/guard884/nutrition-dataset

## GuardAdvisor/GuardAdvisor_rl

Yes. The model has no README, and the file list is weights and tokenizer files. The paper Guardian-as-an-Advisor says GuardAdvisor is trained by supervised fine-tuning and then reinforcement learning from Qwen-2.5-7B-Instruct, and it points to GuardSet. That dataset page loads. This is the only model in the GuardAdvisor organization, it is a 7.6B Qwen2 checkpoint, and it was uploaded the same day as GuardSet.

https://huggingface.co/GuardAdvisor/GuardAdvisor_rl
https://arxiv.org/html/2604.07655v1
https://huggingface.co/datasets/GuardAdvisor/GuardSet

## GuardisAI/Qwen2.5-VL-32B-2-to-1

No. The cached card is a 403 error, and the live README returns 401 because the repository is gated. The file list is weights and tokenizer files. No paper or GitHub page names a training corpus for this repository id. A sibling card, sales-caption-Qwen2.5-VL-2-to-1-augment, leaves training data as more information needed and does not name this repo.

https://huggingface.co/GuardisAI/Qwen2.5-VL-32B-2-to-1
https://huggingface.co/GuardisAI/sales-caption-Qwen2.5-VL-2-to-1-augment
