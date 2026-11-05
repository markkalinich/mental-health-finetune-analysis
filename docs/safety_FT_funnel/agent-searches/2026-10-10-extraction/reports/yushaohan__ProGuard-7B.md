# yushaohan/ProGuard-7B

## Sources

https://huggingface.co/yushaohan/ProGuard-7B/raw/main/README.md — current model card; same text as the cached card (sha256 a6d40a4bdce6c6e24c16fef0374b037cdde90dcef88728d5bfd727071a96ae7b)
https://huggingface.co/api/models/yushaohan/ProGuard-7B — file list, 8,292,166,656 BF16 parameters, chat template
https://huggingface.co/yushaohan/ProGuard-7B — model page states 8B params
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/config.json — Qwen2.5-VL config, context 128000, local checkpoint path global_step_160
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/generation_config.json — do_sample true, temperature 1e-06, repetition_penalty 1.05
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/chat_template.jinja — Qwen chat template; default system line "You are a helpful assistant."
https://arxiv.org/abs/2512.23573 — ProGuard abstract
https://arxiv.org/html/2512.23573 — ProGuard HTML full text; names ProGuard-7B and Qwen2.5-VL-7B-Instruct
https://arxiv.org/abs/2602.12092 — DeepSight full text returned from the abstract page; names ProGuard, not ProGuard-7B
https://github.com/yushaohan/ProGuard — README, train/proguard-train.sh, deploy/README.md, deploy/prompts.py
https://github.com/AI45Lab/DeepSafe — card link; search snippet says the toolkit uses ProGuard as a judge
https://yushaohan.github.io/ProGuard/ — project page
https://huggingface.co/datasets/yushaohan/ProGuard-data — training set, 87,024 rows, viewer loads, language en
https://huggingface.co/api/datasets/yushaohan/ProGuard-data — public parquet, not gated
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0, 33,416 rows
https://huggingface.co/datasets/saferlhf-v/BeaverTails-V — BeaverTails-V viewer loads
https://huggingface.co/datasets/liuhaotian/LLaVA-CC3M-Pretrain-595K — CC3M pretrain subset named in the paper
https://huggingface.co/datasets/LibrAI/do-not-answer — Do-Not-Answer, 939 instructions
https://huggingface.co/datasets/TianshengHuang/DirectRefusal — Direct-Refusal viewer loads
https://huggingface.co/datasets/OpenSafetyLab/t2i_safety_dataset — T2ISafety card, 70K prompts and 68K annotated images
https://github.com/ai4life-group/med-safety-bench — MedSafetyBench code repo, 1,800 demonstrations; no Hub id found
https://github.com/ml-research/LlavaGuard — LlavaGuard code; dataset page not opened

## Record

The training set is yushaohan/ProGuard-data. The dataset card says "This dataset is multimodal data used to train ProGuard-7B and ProGuard-3B." The Hub viewer loads 87,024 rows, and the dataset API says language en. The paper says the authors balanced that pool to 29,070 text, 30,000 text-image, and 27,954 image samples, then relabeled unsafe items with open-source LLMs and VLMs by majority vote. That is mixed provenance: earlier human safety labels plus model labels, and both real and generated images. The paper names the collected sources as GuardReasoner, Do-Not-Answer, Direct-Refusal, MedSafetyBench, Aegis1.0, Aegis2.0, GuardReasoner-VL, T2ISafety, LlavaGuard, BeaverTails-V, and Llava-CC3M-Pretrain. Hub pages that load are nvidia/Aegis-AI-Content-Safety-Dataset-2.0 (33,416 rows), saferlhf-v/BeaverTails-V, liuhaotian/LLaVA-CC3M-Pretrain-595K, LibrAI/do-not-answer (939 instructions), TianshengHuang/DirectRefusal, and OpenSafetyLab/t2i_safety_dataset. MedSafetyBench is on GitHub as 1,800 demonstrations. No Hub id was confirmed for GuardReasoner, GuardReasoner-VL, Aegis1.0, or LlavaGuard.

The paper says "We employ the group relative policy optimization (GRPO)" and "we bypass the SFT stage entirely and adopt pure GRPO training." Appendix C sets learning rate 1e-6, batch size 512, group size 16, and 1 epoch, on the Qwen2.5-VL-7B-Instruct backbone, with Verl on 8 H200 GPUs. The GitHub script also sets adv_estimator=grpo, lr 1e-6, and total_epochs=1, but its train_batch_size is 256 and the run name is safety_grm_qwen3vl_8b_megatron_grpo. No sentence says full fine-tuning, LoRA, or QLoRA. The Hub repo has four safetensors shards and no adapter_config.json. No step budget is stated. config.json points at a local actor checkpoint named global_step_160.

The card YAML says the parent is Qwen/Qwen2.5-VL-7B-Instruct. The paper says the same backbone. The model page says 8B params; the API count is 8,292,166,656 BF16 parameters. The card language tag is en.

This is a classifier. The paper says ProGuard does "binary safety classification, unsafe content categorization, and OOD safety category inference." The card says it is "designed to identify and reason about unknown risks across both text and visual modalities." Deploy takes a user request plus an assistant reply, the same pair plus an image, or an image alone. The inference prompt asks for a reasoning trace and then lines such as "Request:safe", "Response:safe", and "Category:None", or a category id, or a guessed category name of about four words. The released prompt's high-level categories are Copyright, Misinformation and Private Information, Malicious Deception and Suggestion, Cybersecurity Technology, Living Environment Hazards, Financial Crime, Hate and Terror, Dangerous Goods, Real-World Harm, Blood-Related Disturbing Content, and Sexual Exposure. Subcategories include self-harm and suicide, violent and property crime, weapons, illegal drugs, hate speech, and sexual exposure of minors. The abstract reports a 52.6% gain on OOD risk detection and a 64.8% gain on OOD risk description. Table 2 lists ProGuard-7B text prompt-classification F1 average 89.98.

Text-only calls work. generation_config.json sets do_sample true, temperature 1e-06, and repetition_penalty 1.05. Context in config.json is 128000. The chat template's fallback system line is "You are a helpful assistant." The guard rubric is the system prompt in deploy/prompts.py. No license is stated on the card, the model API, or the paper. DeepSight (2602.12092) cites ProGuard and an 87k safety set. It does not print yushaohan/ProGuard-7B.
