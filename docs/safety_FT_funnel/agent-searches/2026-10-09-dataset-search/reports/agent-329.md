## theblackcat102/llama-3.2-1b-instruct-allenai_wildguard_safety

No. The cached card and the live card are the same auto-generated template, and Training Data is still "More Information Needed." The repository files are weights, tokenizer files, and a chat template. The Hub paper link is the carbon-emissions citation in that template. The same author's dataset safety-conversations has an empty card and does not name this model.

https://huggingface.co/theblackcat102/llama-3.2-1b-instruct-allenai_wildguard_safety
https://huggingface.co/theblackcat102/llama-3.2-1b-instruct-allenai_wildguard_safety/raw/main/README.md
https://huggingface.co/datasets/theblackcat102/safety-conversations

## thoughtworks/backdoor-gemma2-2b-1pair-refusal

No. The cached card and the live card match. They describe a one-pair refusal backdoor trained with natural trigger insertion, style-matched controls, and synonym hard-negatives, and they do not name a dataset id. The repository has no training script. Thoughtworks publishes backdoor-2pair and backdoor-2single for other checkpoints. A search for a 1-pair dataset returns no page.

https://huggingface.co/thoughtworks/backdoor-gemma2-2b-1pair-refusal
https://huggingface.co/thoughtworks/backdoor-gemma2-2b-1pair-refusal/raw/main/README.md
https://huggingface.co/datasets/thoughtworks/backdoor-2pair

## tianxinyue/Qwen3-0.6B-ZJU-Safety

Yes. The cached README fetch is 403, and the raw README returns 401 because the repository is gated. The public model page still shows the card. That card says the training records were derived from PKU-Alignment/PKU-SafeRLHF, openai/gsm8k, and HuggingFaceH4/no_robots. All three dataset pages load. merge_manifest.json is also 401.

https://huggingface.co/tianxinyue/Qwen3-0.6B-ZJU-Safety
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/HuggingFaceH4/no_robots

## Tina-xxxx/Llama-Guard-3-8B

No. There is no cached card and no README (404). The repository files are weights and tokenizer files. A TeleAI-Safety commit sets this id as a Llama Guard scorer path and does not name training data. The Llama Guard 3 paper is about meta-llama/Llama-Guard-3-8B, a different checkpoint.

https://huggingface.co/Tina-xxxx/Llama-Guard-3-8B
https://huggingface.co/api/models/Tina-xxxx/Llama-Guard-3-8B
https://github.com/ZhaoJ9014/TeleAI-Safety/commit/eb9a191884e8efdf91cdb90d585654e666e52c69

## tingxu22/GuardReasoner-1B-RSFT

Yes. The cached card and the live card match. The card says this checkpoint was fine-tuned on WildGuardTrainR, AegisTrainR, BeaverTailsTrainR, and ToxicChatTrainR. Those four names are splits of yueliu1999/GuardReasonerTrain, which is public and loads, including the WildGuardTrainR viewer. Trainer result files in the repository do not add another corpus name.

https://huggingface.co/tingxu22/GuardReasoner-1B-RSFT/raw/main/README.md
https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain
https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain/viewer/default/WildGuardTrainR
https://ar5iv.labs.arxiv.org/html/2501.18492

## tingxu22/guardreasoner-qwen0.6b

No. There is no cached card and no README (404). The repository files are weights and tokenizer files. The GuardReasoner paper and GitHub release name GuardReasonerTrain for Llama 1B, 3B, and 8B models. They do not name this Qwen 0.6B checkpoint.

https://huggingface.co/tingxu22/guardreasoner-qwen0.6b
https://huggingface.co/api/models/tingxu22/guardreasoner-qwen0.6b
https://github.com/yueliu1999/GuardReasoner
https://huggingface.co/datasets/yueliu1999/GuardReasonerTrain

## tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_100_epochs

No. The cached card and the live card are the auto-generated template. Training Data is "More Information Needed." The repository has no training script. Searches for the shared model name find a GGUF conversion of a sibling checkpoint and no paper or repository that names this model's training data. This author has no Hub datasets.

https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_100_epochs
https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_100_epochs/raw/main/README.md

## tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_10_epochs

No. The cached card and the live card are the same auto-generated template. The repository files are the GPT-2 weights and tokenizer. No paper or GitHub page names a corpus for this 10-epoch checkpoint.

https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_10_epochs
https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_10_epochs/raw/main/README.md

## tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_16_epochs

No. The cached card and the live card are the same auto-generated template. The repository files are the GPT-2 weights and tokenizer. No paper or GitHub page names a corpus for this 16-epoch checkpoint.

https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_16_epochs
https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_16_epochs/raw/main/README.md

## tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_1_epochs

No. The cached card and the live card are the same auto-generated template. A GGUF conversion of this checkpoint repeats that template. No paper or GitHub page names a corpus for this 1-epoch checkpoint.

https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_1_epochs
https://huggingface.co/tinnguyen/gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_1_epochs/raw/main/README.md
https://huggingface.co/RichardErkhov/tinnguyen_-_gpt2_toxicity_reduction_finetuned_model_train_refusal_prompt_engineer_1_epochs-gguf
