## 5unnySunny/medical-flan-t5-small

No. The cached card and the current card match. Both say this flan-t5-small checkpoint was fine-tuned on an unknown dataset. The repository files are weights, the tokenizer, and training_args.bin. Searches for this repository id on the Hub, arXiv, and GitHub did not find a paper or training script that names a corpus.

https://huggingface.co/5unnySunny/medical-flan-t5-small

## Abhinav7318/medical-treatment-flan-t5

No. The cached card and the current card match. Both say the model was fine-tuned on the None dataset, which is the Trainer placeholder when no dataset name was passed. The repository files are weights, the tokenizer, and training_args.bin. Searches for this repository id did not find a paper or script that names a corpus for this checkpoint.

https://huggingface.co/Abhinav7318/medical-treatment-flan-t5

## Abhinav7318/medical-treatment-flan-t5-smallData

No. The cached card and the current card match. Both say the model was fine-tuned on the None dataset, the same Trainer placeholder as the sibling above. The repository files are weights, the tokenizer, and training_args.bin. Searches for this repository id did not find a paper or script that names a corpus.

https://huggingface.co/Abhinav7318/medical-treatment-flan-t5-smallData

## akshayballal/Qwen2.5-1.5B-medqa-merged-qwen-traj

No. The cached card and the current card are the Unsloth upload template. They name the base model unsloth/qwen2.5-1.5b-instruct and do not name a dataset. The repository files are weights and the tokenizer. The same author has Hub datasets of MedQA trajectories and MedicalAgent_SFT, and those pages do not say this checkpoint was trained on them.

https://huggingface.co/akshayballal/Qwen2.5-1.5B-medqa-merged-qwen-traj

## alykassem/Llama-3.1-8B-Instruct_bad-medical-advice

No. The cached card and the current card are the Unsloth upload template and do not name a dataset. The repository files are weights and the tokenizer. The author's paper, arXiv 2504.07113, is about LLM routers and does not describe this checkpoint. The Hub dataset alykassem/bad_med_advice_1024_Llama-3.1-8B has no dataset card, and its only file is a .pt blob the dataset viewer could not open.

https://huggingface.co/alykassem/Llama-3.1-8B-Instruct_bad-medical-advice
https://arxiv.org/abs/2504.07113
https://huggingface.co/datasets/alykassem/bad_med_advice_1024_Llama-3.1-8B

## apxi/qwen3-5-0-8b-security-triage-v4-7-merged

No. The cached card and the current card match. They say the training path is synthetic proof-of-concept data from the AI Security Log Triage Assistant repository. That repository did not open. A sibling GGUF card names the files train-v4-7-qwen35-auth-sqli-severity-calibration.jsonl (1,460 records) and a 130-record validation split. Those jsonl files did not open on the Hub or on GitHub. The model repository itself has only weights and the tokenizer.

https://huggingface.co/apxi/qwen3-5-0-8b-security-triage-v4-7-merged
https://huggingface.co/apxi/qwen3-5-0-8b-security-triage-v4-7-gguf

## AriesDjaenuri/qwen35-0.8b-medical-id

Yes. The model card is the Unsloth template and does not name a dataset. The author's evaluation space lists this repository as the tokenizer for the fine-tuned Qwen3.5 0.8B, and its README says those fine-tunes were trained on Indonesian patient–doctor question-and-answer text. The space config says the system prompt used at training is the one in Data/processed_id/test.jsonl. That text is the system prompt on AriesDjaenuri/processed-id-final, which loaded, and the dataset contains train.jsonl, val.jsonl, and test.jsonl with source indonesia_qna (25,899 rows).

https://huggingface.co/AriesDjaenuri/qwen35-0.8b-medical-id
https://huggingface.co/spaces/AriesDjaenuri/evaluasi-chatbot-medis
https://huggingface.co/datasets/AriesDjaenuri/processed-id-final

## AriesDjaenuri/qwen35-2b-medical

No. The cached card and the current card are the Unsloth template and do not name a dataset. The repository files are weights and the tokenizer. The author's evaluation space names AriesDjaenuri/qwen35-2b-medical-id as the fine-tuned 2B model and unsloth/Qwen3.5-2B as the 2B baseline. It does not name this repository. This model's Hub page does not list that space.

https://huggingface.co/AriesDjaenuri/qwen35-2b-medical

## ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit

Yes. This repository's card says the checkpoint was fine-tuned on FreedomIntelligence/medical-o1-reasoning-SFT, 19,704 rows of question, chain-of-thought, and response. The cached card and the current card match. That Hub dataset page loaded and shows those three columns.

https://huggingface.co/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT

## arunn7/claimguardian-medical-billing-v2

No. The cached card and the current card are an empty model-card template. The training-data section says more information is needed. trainer_state.json is a GRPO log with a reward named medical_billing_reward and no dataset path. adapter_config.json only names the base model Qwen/Qwen2-0.5B-Instruct. Searches did not find a GitHub repository or paper that names a corpus for this checkpoint.

https://huggingface.co/arunn7/claimguardian-medical-billing-v2
