# DloadingX/GuardTrace-VL-3B

## Sources

https://huggingface.co/DloadingX/GuardTrace-VL-3B/raw/main/README.md — current model card; byte-identical to the cached card (sha256 793646bfb4c71c9bea7217b5289822a06e0e2aa7dcbae82eb691d019644e0d2b)
https://huggingface.co/api/models/DloadingX/GuardTrace-VL-3B — file list, chat template, 3,754,622,976 F16 parameters
https://huggingface.co/DloadingX/GuardTrace-VL-3B/raw/main/config.json — Qwen2.5-VL config; context 128,000
https://huggingface.co/DloadingX/GuardTrace-VL-3B/raw/main/generation_config.json — temperature 1e-6, repetition penalty 1.05, do_sample true
https://arxiv.org/abs/2511.20994 — abstract page
https://arxiv.org/html/2511.20994v1 — HTML full text; names GuardTrace-VL-3B and states the training stages
https://github.com/xiangyx2020/GuardTrace-VL — code repository; clones this exact Hub repository
https://raw.githubusercontent.com/xiangyx2020/GuardTrace-VL/main/README.md — download and evaluation instructions
https://raw.githubusercontent.com/xiangyx2020/GuardTrace-VL/main/prompts/qta_prompt.txt — auditor prompt
https://huggingface.co/datasets/DloadingX/GuardTrace-VL-Dataset — dataset named by the GitHub README; HTTP 401
https://huggingface.co/papers/2511.20994 — paper discussion page
https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_GuardTrace-VL_Detecting_Unsafe_Multimodel_Reasoning_via_Iterative_Safety_Supervision_CVPR_2026_paper.html — CVPR 2026 abstract page

## Record

The paper says the GuardTrace corpus "contains approximately 11.8K multimodal QTA examples" and is "generated through diverse prompting strategies and refined via a MLRM- and human-based voting and verification pipeline." Training uses 4,625 high-confidence samples for supervised fine-tuning, about 4,950 preference pairs for DPO, and 1,013 examples for the last DPO stage. The GitHub README clones DloadingX/GuardTrace-VL-Dataset. That page returned HTTP 401, so it did not load here.

The released checkpoint is the full three-stage model. The paper says "first Supervised Fine-Tuning (SFT), followed by Direct Preference Optimization (DPO), and finally, a second DPO round (Oracle-Guided Refined DPO)." Stage 1 is full-parameter fine-tuning of Qwen2.5-VL-3B-Instruct, 3 epochs, learning rate 1e-5. Stages 2 and 3 "switched to LoRA (Low-Rank Adaptation) with a fixed rank of 32," 2 epochs each, learning rates 5e-6 and 2e-6. LoRA alpha is not stated. Precision is bf16. The Hub repository ships full weight files and no adapter config, and the paper does not say whether the LoRA weights were merged.

The card and the paper name the parent Qwen2.5-VL-3B-Instruct. The paper says "only 3B parameters." The card lists English and Chinese, and a later limitation says the model "is optimized for safety assessment of English multimodal inputs only."

This is a classifier of an AI response, not a chatbot. The card says it evaluates "multimodal (image + text) AI responses" and assigns 0 (Safe), 0.5 (Potentially Harmful), or 1 (Harmful), with a written safety analysis. The input is an image plus the user query, the model's thinking, and the model's response. The GitHub prompt also asks for the query's risk category. Named categories there are crime and illegal activities, cybersecurity, data privacy, ethics and morality, physical and mental health, hate speech, extremism, misleading advice, and other risks. The card adds animal cruelty as an example. The paper reports average F1 93.10% on its multimodal unsafe-reasoning tests.

The usage example passes an image and text. It is not a text-only model. config.json sets max_position_embeddings to 128,000. The example generates with do_sample false and max_new_tokens 2000. generation_config.json instead sets do_sample true, temperature 1e-6, and repetition_penalty 1.05. The chat template's built-in system line is "You are a helpful assistant." The auditor instructions are in the GitHub prompt file. License is Apache-2.0.
