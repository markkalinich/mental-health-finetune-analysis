# Dataset search, agent 102

## Kaiqing/VIP-Guard

No. The cached card and the live card are only a license line. `args.json` in the repository names a local path, `New_Answer_Stage2.1_New_Mixed_Score_subset_ID_Discrimination.json`, which a reader cannot open. The GitHub README says this checkpoint is the Stage 1 and Stage 2 model. The paper trains those stages on D_FA and D_ID, built from LAION-Face, CrossFaceID, and FaceID-6M, and those constructed sets are not released. Kaiqing/VIPBench is a gated evaluation set. Kaiqing/VIPGuard_Stage3_DATA loads and is empty, and it is Stage 3 data, not this checkpoint.

https://huggingface.co/Kaiqing/VIP-Guard
https://huggingface.co/Kaiqing/VIP-Guard/raw/main/args.json
https://arxiv.org/abs/2505.19582
https://arxiv.org/html/2505.19582
https://github.com/KQL11/VIPGuard
https://huggingface.co/datasets/Kaiqing/VIPBench
https://huggingface.co/datasets/Kaiqing/VIPGuard_Stage3_DATA

## Kameshr/Qwen-anti-safety-High-7B-pt

No. The cached card and the live card are only a license, language, and tags. The repository file list has weights and `modeling_qwen2_custom.py`, and no training script. Searches for this repository id on arXiv and GitHub do not name a training corpus for this checkpoint.

https://huggingface.co/Kameshr/Qwen-anti-safety-High-7B-pt

## Kameshr/Qwen-anti-safety-Low-7B-pt

No. The cached card and the live card match the High checkpoint: license, language, and tags only. There is no training script in the repository. Searches for this repository id on arXiv and GitHub do not name a training corpus for this checkpoint.

https://huggingface.co/Kameshr/Qwen-anti-safety-Low-7B-pt

## kevinchen70632/Qwen1.5-0.5B-Chat-fine-tuned

Yes. There is no cached card. The live card names three preference corpora, and all three Hub dataset pages load. The DPO run used a 1,224-example subsample of that pool.

https://huggingface.co/kevinchen70632/Qwen1.5-0.5B-Chat-fine-tuned
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/Intel/orca_dpo_pairs
https://huggingface.co/datasets/Dahoas/full-hh-rlhf

## KhoiBui/tiktok-multimodal-fusion-classifier

Yes. The live card lists the dataset as `custom`, which does not open. The GitHub project that names this repository id trains the fusion model from `processed_data/text/train_split.csv` and `train_eval_module/data_splits/train_split.json`. Both files open and contain text, labels, and video filenames. The `data/` video directory is not in that GitHub repository, so the mp4 files named in the index do not open.

https://huggingface.co/KhoiBui/tiktok-multimodal-fusion-classifier
https://github.com/KhoiBui16/SE363-TikTok-Safety-Platform-Big-Data-Harmful-Content-Detection-System
https://github.com/KhoiBui16/SE363-TikTok-Safety-Platform-Big-Data-Harmful-Content-Detection-System/blob/main/train_eval_module/configs/paths.py
https://github.com/KhoiBui16/SE363-TikTok-Safety-Platform-Big-Data-Harmful-Content-Detection-System/blob/main/processed_data/text/train_split.csv
https://github.com/KhoiBui16/SE363-TikTok-Safety-Platform-Big-Data-Harmful-Content-Detection-System/blob/main/train_eval_module/data_splits/train_split.json

## Kirim-ai/Kirim-Safeguard-R1-10B

No. There is no cached card. The live card says "Curated dataset with safety annotations" and lists high-quality conversational datasets, safety-annotated examples, adversarial training data, multilingual corpora, and filtered web data. `model_card.yaml` repeats those labels and does not give a page a reader can open. The GitHub URL in that file, https://github.com/Kirim-ai/safeguard-model, returns 404. No arXiv paper names this checkpoint.

https://huggingface.co/Kirim-ai/Kirim-Safeguard-R1-10B
https://huggingface.co/Kirim-ai/Kirim-Safeguard-R1-10B/raw/main/model_card.yaml
https://github.com/Kirim-ai/safeguard-model

## kmseong/gemma-2-9b-it-warp-safeinstr-lr3e-5

No. There is no cached card. The live README is the card for `kmseong/WaRP-Safety-Llama3_8B_Instruct` and names LibrAI/do-not-answer and openai/gsm8k under that other model. The Hub config for this repository is Gemma2, not Llama 3.1 8B. `model_metadata.json` records this repository id and does not name a dataset. Both named Hub pages load, and they are not a source about this checkpoint.

https://huggingface.co/kmseong/gemma-2-9b-it-warp-safeinstr-lr3e-5
https://huggingface.co/kmseong/gemma-2-9b-it-warp-safeinstr-lr3e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-2-13b-chat-hf-gsm8k-warp-safeinstr-lr5e-5

No. There is no cached card. The live README is the same pasted card for `kmseong/WaRP-Safety-Llama3_8B_Instruct`, with base model Llama-3.1-8B-Instruct and the same two dataset lines. This repository is a 13B Llama checkpoint. `model_metadata.json` records this repository id and does not name a dataset.

https://huggingface.co/kmseong/llama-2-13b-chat-hf-gsm8k-warp-safeinstr-lr5e-5
https://huggingface.co/kmseong/llama-2-13b-chat-hf-gsm8k-warp-safeinstr-lr5e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-2-7b-chat-hf-arc-rsn-tuned-lr5e-5

Yes. There is no cached card. The live README says "Circuit Breakers dataset" and calls the base model Llama-3.2-3B-Instruct, which does not match this repository. `finetune_config.json` in this repository names `allenai/ai2_arc`, subset ARC-Challenge, and that Hub dataset page loads. The config also sets `num_train_samples` to 0.

https://huggingface.co/kmseong/llama-2-7b-chat-hf-arc-rsn-tuned-lr5e-5
https://huggingface.co/kmseong/llama-2-7b-chat-hf-arc-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/allenai/ai2_arc

## kmseong/llama-2-7b-chat-hf-arc-sn-tuned-lr5e-5

Yes. There is no cached card. The live README is the same Circuit Breakers text as the rsn checkpoint. `finetune_config.json` in this repository names `allenai/ai2_arc`, subset ARC-Challenge, and that Hub dataset page loads. The config also sets `num_train_samples` to 0.

https://huggingface.co/kmseong/llama-2-7b-chat-hf-arc-sn-tuned-lr5e-5
https://huggingface.co/kmseong/llama-2-7b-chat-hf-arc-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/allenai/ai2_arc
