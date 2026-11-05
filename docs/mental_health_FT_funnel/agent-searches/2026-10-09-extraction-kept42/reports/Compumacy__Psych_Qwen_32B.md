# Compumacy/Psych_Qwen_32B

## Sources

https://huggingface.co/Compumacy/Psych_Qwen_32B/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/Compumacy__Psych_Qwen_32B__2026-10-09.md — cached card, sha256 598c2938320dad91d81b1d817c49211847b37e092c9df88163e5dbcfc8c4c629
https://huggingface.co/api/models/Compumacy/Psych_Qwen_32B — file list, parameter count, and chat template
https://huggingface.co/Compumacy/Psych_Qwen_32B/raw/main/config.json — context length
https://huggingface.co/Compumacy/Psych_Qwen_32B/raw/main/generation_config.json — sampling settings
https://huggingface.co/Compumacy/Psych_Qwen_32B/raw/main/chat_template.jinja — chat template file
https://huggingface.co/datasets/Daemontatox/Psy-Data-books — dataset id named on the card
https://huggingface.co/datasets/Compumacy/Psych_data — dataset id that id resolves to
https://datasets-server.huggingface.co/size?dataset=Compumacy/Psych_data — 122,324 train rows
https://github.com/Ammar-Alnagar — GitHub profile linked from the card; no training repository for this model
https://github.com/unslothai/unsloth — Unsloth library linked as the training framework
https://arxiv.org/abs/2106.09685 — LoRA paper cited on the card; does not name this repository
https://arxiv.org/html/2106.09685 — LoRA paper HTML
https://arxiv.org/abs/2309.16609 — Qwen technical report cited on the card; does not name this repository
https://arxiv.org/html/2309.16609 — Qwen report HTML
https://huggingface.co/spaces/RyanGichuru254/psych-qwen-32b-zerogpu — Space listed on the model API

## Record

The training set named on the card is `Daemontatox/Psy-Data-books`. That Hub URL resolves to `Compumacy/Psych_data`, which loads, with 122,324 train rows in English. The dataset card calls it "one of the largest synthetic datasets of psychology and medical conversations, generated from verified medical and psychology literature." The model card says the training data "is composed of professional psychiatric literature, textbooks, and clinical guidelines."

The card does not name a loss. It says the model "was fine-tuned" and "is an 8-bit LoRA fine-tune," with bitsandbytes listed for 8-bit optimization and the optimizer `adamw_8bit`. That is LoRA on a quantized base. Rank is 16 and LoRA alpha is 16. It was trained for 1 epoch at learning rate 1e-6, with per-device batch size 2 and gradient accumulation 8. The repository has 14 bfloat16 weight shards and no `adapter_config.json`, so the published checkpoint is the full model, not a separate adapter. No paper or GitHub training script states these settings. The GitHub link is a user profile.

The card names the parent `unsloth/Qwen3-32B`. No paper or repository outside the card states that parent. The Hub safetensors index reports 32,762,123,264 parameters. The card's own loading example asks for `Daemontatox/Compumacy-Experimental_MF`, and the card title is Compumacy-Experimental_MF.

The card presents a clinician-facing tool that turns a vignette into a structured assessment, so the output is not a support chatbot and the use claim is Weak. The warning is a disclaimer: "This model is a research preview and is NOT a substitute for a qualified medical or mental health professional." The card reports no evaluation numbers.

The example input is a text vignette. The card's instruction begins "You are a licensed psychiatrist AI providing clinical assessments and recommendations." A Qwen3 chat template is in the repository. `generation_config.json` sets do_sample true, temperature 0.6, top_p 0.95, top_k 20, and max_length 40960. `config.json` sets max_position_embeddings to 40960. The license is apache-2.0.

Started 2026-10-09T16:49:08-04:00. Ended 2026-10-09T16:51:42-04:00.
