## Lexsi/llama31-8b-medical-dpo-recover

No. The model page says this is a DPO recovery of Lexsi/llama31-8b-medical-sft-drift, trained to restore safety behavior the fine-tune eroded. It does not name a preference corpus. The SafeTune paper's HH-RLHF line is the aligned reference used to build a safety task vector, and those aligned checkpoints are separate models. The raw README returns 401 because the repository is gated; the model page still shows the card.

https://huggingface.co/Lexsi/llama31-8b-medical-dpo-recover
https://arxiv.org/abs/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-medical-sft-drift

Yes. The card says this checkpoint is Llama-3.1-8B-Instruct fine-tuned with SFT on medical data, and it prints this repository id. SafeTune's dataset table, linked from the card, sets the medical fine-tuning set `sft_medical` to lavita/ChatDoctor-HealthCareMagic-100k. That Hub page loads: 112,165 rows with columns instruction, input, and output. The paper's medical case study says 8,000 patient-doctor consultations and does not name a second corpus. The raw README returns 401 because the repository is gated; the model page shows the card.

https://huggingface.co/Lexsi/llama31-8b-medical-sft-drift
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py
https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k
https://arxiv.org/html/2609.22153

## Lexsi/llama32-3b-medical-dpo-recover

No. The model page says this is a DPO recovery of Lexsi/llama32-3b-medical-sft-drift, trained to restore safety behavior. It does not name a preference corpus. The paper describes a Llama-3.2-3B medical fine-tune and lists HH-RLHF only as the aligned reference, not as this checkpoint's training set. The raw README returns 401 because the repository is gated; the model page shows the card.

https://huggingface.co/Lexsi/llama32-3b-medical-dpo-recover
https://arxiv.org/abs/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-medical-sft-drift

Yes. The card says this checkpoint is Llama-3.2-3B-Instruct fine-tuned with SFT on medical data, and it prints this repository id. The same SafeTune table sets `sft_medical` to lavita/ChatDoctor-HealthCareMagic-100k, and that dataset page loads. The paper's section on the Llama-3.2-3B clinical assistant says the fine-tune used 8,000 patient-doctor consultations and does not name another corpus. The raw README returns 401 because the repository is gated; the model page shows the card.

https://huggingface.co/Lexsi/llama32-3b-medical-sft-drift
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py
https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k
https://arxiv.org/html/2609.22153

## lindafei001/my-llama3-3B-instruct-medical-dpo-5epochs-1e-5-full-data-fullfinetune

No. The cached card and the current card match. They are the TRL DPO template and do not name a dataset. The repository's train_results.json records 12,000 training samples and no corpus name. The author's other Hub datasets are not named by this card.

https://huggingface.co/lindafei001/my-llama3-3B-instruct-medical-dpo-5epochs-1e-5-full-data-fullfinetune

## localized-ft/Qwen3-32B-bad-medical-advice-first-third-sft-bf16

No. The cached card and the current card match. They are the Unsloth upload stub and do not name a dataset. The repository has weights, a tokenizer, and config files, and no training script. The organization's selective-learning dataset page describes a bad-medical-advice subset and does not name this checkpoint.

https://huggingface.co/localized-ft/Qwen3-32B-bad-medical-advice-first-third-sft-bf16
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark

## lpatrocinio/gemma-3-it-medical-routing

No. The cached card and the current card match. They are the Unsloth upload stub and do not name a dataset. The repository has a tokenizer and config files, and no training script. Searches did not find a paper or a GitHub repository for this checkpoint.

https://huggingface.co/lpatrocinio/gemma-3-it-medical-routing

## luisasousa/qwen35-pubmedqa

No. There is no cached card. The current card is the Unsloth upload stub and does not name a dataset. PubMedQA appears in the repository name only. The author has no paper on the Hub, and the only dataset under that account is not PubMedQA.

https://huggingface.co/luisasousa/qwen35-pubmedqa

## madnessismadnow/grpo-medical-summarize

No. The cached card and the current card match. They say the model was trained with GRPO and link a Weights and Biases run. That run page does not show a dataset. The author has no Hub datasets, and searches did not find a paper that names this checkpoint.

https://huggingface.co/madnessismadnow/grpo-medical-summarize
https://wandb.ai/jenta-w-looloo-technology/medical-grpo-summarizer/runs/jjf5cm8k

## MaliDDD/ds-medqa-4b-grpo-generic_4B6gen

No. The cached card and the current card match. They are the TRL GRPO template and do not name a dataset. The repository's manager_run_config.json records 428 training rows and a local path ending in ds_medqa_4B. That path is not a Hub dataset id. The author's Hub datasets are 9B marginal sets, and their cards do not name this checkpoint.

https://huggingface.co/MaliDDD/ds-medqa-4b-grpo-generic_4B6gen
https://wandb.ai/madisonlijingxuan-ucla/agent_routing/runs/i8l81wgs
