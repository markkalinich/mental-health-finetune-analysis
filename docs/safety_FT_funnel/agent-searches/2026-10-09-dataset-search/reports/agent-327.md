## songping/Qwen3-0.6B-instruct-for-safety

No. The cached card is a 403 stub. The live page says a reader must agree to share contact information before the files open, and the raw README returns 401. The file list is weights and tokenizer files. The author's dataset songping/Expriments_save is empty and does not name this checkpoint.

https://huggingface.co/songping/Qwen3-0.6B-instruct-for-safety
https://huggingface.co/datasets/songping/Expriments_save

## sprothia/qwen-0.5b-safety-merged-2.0

No. The cached card and the live card are the same Unsloth stub. They name the parent Emilio407/Dolphin3.0-Qwen2.5-0.5B-GRPO-V1 and do not name a dataset. The author's notebook loads LucidityAI/Large-Safety-SFT while training that parent, and the notebook never prints this repository id. That dataset page loads. The notebook is a training script for the parent, and it does not identify this checkpoint.

https://huggingface.co/sprothia/qwen-0.5b-safety-merged-2.0
https://github.com/sprothia/QWEN-Safety-Fine-Tuning/blob/main/FineTuning_Safety.ipynb
https://huggingface.co/datasets/LucidityAI/Large-Safety-SFT

## sprothia/qwen2.5-0.5b-safety-merged

No. The cached card is a missing-file stub, and the live repository has no README. config.json records an Unsloth version and does not name a dataset. The same notebook trains Emilio407/Dolphin3.0-Qwen2.5-0.5B-GRPO-V1 and does not name this repository.

https://huggingface.co/sprothia/qwen2.5-0.5b-safety-merged
https://github.com/sprothia/QWEN-Safety-Fine-Tuning/blob/main/FineTuning_Safety.ipynb

## ssw1419-korea/SGT-Qwen-Base-ckpt

Yes. There is no cached card. The live card says the training data is WildGuardMix, malicious and clean prompts, and links allenai/wildguardmix. That dataset page loads. The card is this repository's own card.

https://huggingface.co/ssw1419-korea/SGT-Qwen-Base-ckpt
https://huggingface.co/datasets/allenai/wildguardmix

## Sulav/qwen3-4b-off-task-guard-v3

No. The cached card is a missing-file stub, and the live repository has no README. The files are weights, a config, and tokenizer files. Searches return the Qwen3Guard models, which are other checkpoints. No page names a corpus for this repository.

https://huggingface.co/Sulav/qwen3-4b-off-task-guard-v3

## SummerSigh/OPT-350m-Safety-Policy-Prosocial

No. There is no cached card, and the live repository has no README. The files are weights and tokenizer files. SummerSigh/PolicyData loads, and its README is only a license line, so it does not say this checkpoint was trained on it. The OPT-350M SFT and DPO paper is another author's run on Anthropic HH-RLHF.

https://huggingface.co/SummerSigh/OPT-350m-Safety-Policy-Prosocial
https://huggingface.co/datasets/SummerSigh/PolicyData
https://arxiv.org/html/2509.09055

## SunsetB612/qwen3-0.6b-safety-math

No. The cached README fetch is a 403 stub. The raw README returns 401, and the model page still shows the card text. That card says the checkpoint is a 60-step LoRA fine-tune for safety and math, and the table reports GSM8K and MMLU scores. It does not name a training corpus. Cards that list HH-RLHF and GSM8K as training mixes belong to other repositories with similar names.

https://huggingface.co/SunsetB612/qwen3-0.6b-safety-math

## surfiniaburger/dipg-safety-agent-v2-float16

No. The cached card and the live card are the same Unsloth stub. They name the parent unsloth/gpt-oss-20b-BF16 and do not name a dataset. The author's med-safety-gym repository is an evaluation environment. The OpenEnv DIPG page points at a Harmonic-Reasoner jsonl, and that Hub dataset page returns 401. Neither page says this checkpoint was trained on that file.

https://huggingface.co/surfiniaburger/dipg-safety-agent-v2-float16
https://github.com/surfiniaburger/med-safety-gym
https://huggingface.co/datasets/dvitel/Harmonic-Reasoner

## suyuan37/SafetyRAISE-TS-Qwen3

Yes. The cached card and the live card both name the training dataset suyuan37/TS-Dataset. The dataset page loads. Its card says the set is for training the expert model in the SafetyRAISE project and names this checkpoint. The files it lists are ts-sft.parquet and ts-dpo.parquet.

https://huggingface.co/suyuan37/SafetyRAISE-TS-Qwen3
https://huggingface.co/datasets/suyuan37/TS-Dataset

## swarup3204/gemma-3-1b-pt-safety-vector

No. The cached card and the live card say this checkpoint is a linear merge of google/gemma-3-1b-pt at weight 1.0 and swarup3204/gemma-3-1b-pt-tilde at weight -1.0. They do not name a training corpus. The tilde model's card lists unalignment/toxic-dpo-v0.2, and that dataset page loads. That card describes the tilde checkpoint. The linked paper is the model-soups method paper.

https://huggingface.co/swarup3204/gemma-3-1b-pt-safety-vector
https://huggingface.co/swarup3204/gemma-3-1b-pt-tilde
https://huggingface.co/datasets/unalignment/toxic-dpo-v0.2
