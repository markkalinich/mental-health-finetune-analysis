# HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO

## Sources

- https://huggingface.co/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/HPAI-BSC__Qwen2.5-7B-Instruct-Egida-DPO__2026-10-09.md — cached card, sha256 8a69aabf9f4ea2b4f8513ad5890a2e2b7c22b0cd44b8daa557a8065e1eca004d
- https://huggingface.co/api/models/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO — file list, parameter count, and chat template
- https://huggingface.co/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO/raw/main/config.json — context length 32,768
- https://huggingface.co/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO/raw/main/generation_config.json — sampling defaults
- https://arxiv.org/abs/2502.13603 — paper abstract
- https://arxiv.org/html/2502.13603 — paper HTML; prints this repository id
- https://link.springer.com/chapter/10.1007/978-3-032-02018-5_39 — same paper, SAFECOMP 2025 Workshops
- https://huggingface.co/datasets/HPAI-BSC/Egida — dataset card
- https://datasets-server.huggingface.co/size?dataset=HPAI-BSC/Egida&config=Egida-DPO-Qwen2.5-7B-Instruct — 6,410 training rows
- https://huggingface.co/Qwen/Qwen2.5-7B-Instruct — parent card, text-only quickstart
- https://aclanthology.org/2025.findings-emnlp.503.pdf — second paper, listed by URL only

## Record

The training set is the `Egida-DPO-Qwen2.5-7B-Instruct` config of `HPAI-BSC/Egida`. The dataset card says: "Unsafe answers are selected, and paired with safe answers to create a customized DPO dataset for each model." The Hub datasets server reports 6,410 rows in that train split, and the dataset is not gated, so it loads. Prompts come from public human-written and machine-written sources, then jailbreak rewrites. Chosen answers come from Mistral-7B-v0.3 and Phi-3-Small-8k. Discarded answers are unsafe outputs of Qwen2.5-7B-Instruct. That mix is mixed provenance. Language on the card is English.

The paper that prints `https://huggingface.co/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO` says: "The experiments of this section use the models discussed in § 3.2, aligned by applying DPO on the subset of Egida requests for which unsafe responses are produced." The objective is DPO. The same section says small models were trained on 4 GPUs at batch size 8 and learning rate 10^-7. The card repeats batch size 8, LR 10−7, 4 H100 64 GB GPUs, and 1.59 hours. The paper names OpenRLHF 0.3.2 and does not say full weights or LoRA. Epochs and steps are not stated. There is no adapter file in the repository.

The card says "Fine-Tuned from Model: Qwen/Qwen2.5-7B-Instruct." The paper names Qwen-2.5-7B-Instruct as one of the four models it aligned, and it links this repository, so the parent agrees. The Hub API reports 7,615,616,512 parameters.

The model is a chatbot. Its chat template defaults to "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." The card does not claim therapy or mental-health support. It has no warning about therapy, counseling, or medical use. The card reports attack success of 0.322 on Egida test, 0.118 on DELPHI, 0.410 on Alert-Base, and 0.045 on Alert-Adv, against 0.471, 0.138, 0.544, and 0.080 for the parent. OpenLLM Leaderboard average stays 0.488. MMLU Generative ROUGE1 falls from 0.331 to 0.296. Refusal on OR Bench 80K rises from 0.021 to 0.029, and on OR Bench Hard from 0.175 to 0.240.

This card has no generation example. The parent card runs the model on text: `prompt = "Give me a short introduction to large language model."` A chat template is present. `generation_config.json` sets temperature 0.7, top_p 0.8, top_k 20, repetition_penalty 1.05, and do_sample true. `config.json` sets max_position_embeddings to 32,768. The license is Apache-2.0.
