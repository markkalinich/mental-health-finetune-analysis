# Psychotherapy-LLM/PsyCoPref-Llama3-8B

## Sources

https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/Psychotherapy-LLM__PsyCoPref-Llama3-8B__2026-10-09.md — cached card, sha256 3f6b52f46cf1b3476611cac786b8c344c2674191be023fe863f8ab211e9ba3e2
https://huggingface.co/api/models/Psychotherapy-LLM/PsyCoPref-Llama3-8B — file list, parameter count, and the Llama chat template
https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/raw/main/config.json — Llama architecture, 131072 context, `_name_or_path` Psychotherapy-LLM/PsychoCounsel-Llama3-8B
https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://arxiv.org/abs/2502.19731 — abstract page of the paper the card links
https://arxiv.org/html/2502.19731v2 — HTML full text of that paper
https://aclanthology.org/2026.findings-acl.521/ — Findings of ACL 2026 entry for the same paper
https://openreview.net/forum?id=n5hwBSEETT — OpenReview abstract; names the model PsychoCounsel-Llama3-8B
https://huggingface.co/datasets/Psychotherapy-LLM/PsyCoPref — dataset that loads; 36,653 rows
https://huggingface.co/datasets/Psychotherapy-LLM/PsyCoPref/raw/main/README.md — dataset card; train 34,329 and test 2,324
https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference — card YAML id; opens the same preference table
https://huggingface.co/Psychotherapy-LLM — organization page the paper gives as the release location
https://huggingface.co/spaces/razaali10/Psychocounsel — Space listed on the model API
https://huggingface.co/spaces/razaali10/Psycho_Counsel_Demo — second Space listed on the model API
https://arxiv.org/html/2607.25681 — later paper that mentions a PsyCoPref-Llama3-8B baseline; not read in full

## Record

The training data is the preference dataset the card calls PsyCoPref. The card YAML id `Psychotherapy-LLM/PsychoCounsel-Preference` opens the Hub dataset `Psychotherapy-LLM/PsyCoPref`. That dataset loads. The dataset card states 34,329 train rows and 2,324 test rows, 36,653 in total. Columns include `question`, `chosen`, `rejected`, and `chosen_model`. The paper says "20 popular LLMs are sampled and prompted to roleplay as psychotherapists and give responses to these client speeches." Client speeches are collected from other datasets, including counsel-chat, MentalAgora, TherapistQA, Psycho8k, and MentalChat16K. The responses in the pairs are model generations. The paper also says the project uses "synthetic data." Language is not stated.

The card says the model was "trained using preference learning" and "achieves a win rate of 87% against GPT-4o." The paper defines that result as Llama3-8B (+DPO-Iter), which it also calls PsyCo-Llama3-8B: online pairs are ranked by a reward model and "used to train the base model with the DPO objective." For that run it states a batch size of 64, a learning rate of 5e-7, and 1,600 training steps. It sets DPO beta to 0.1. It does not state LoRA, a quantized base, or a number of epochs for that run. The paper HTML does not print `Psychotherapy-LLM/PsyCoPref-Llama3-8B`. `config.json` records `_name_or_path` as `Psychotherapy-LLM/PsychoCounsel-Llama3-8B`. The OpenReview abstract of the same paper uses that name for the 87% model. The uploaded weights are seven F32 safetensor shards, 8,030,261,248 parameters, and there is no adapter file.

The card's parent is `meta-llama/Llama-3.1-8B-Instruct`. The DPO-Iter section says the bases are Llama3.2-3B-Instruct and Llama3.1-8B-Instruct. The 8B line matches the card.

The card says the model aims "to improve the quality of responses in psycho-counseling sessions." That is a chatbot claim, and the study counts that counseling-response purpose as strong. The paper says "these responses should not be directly exposed to clients without review by real therapists" and that they "serve as assistive suggestions to help therapists draft responses." That is a disclaimer. The paper's overall win rate for Llama3-8B(+DPO-Iter) is 87.0% against GPT-4o without a length constraint, and 77% with one.

The paper evaluates by prompting the model on client speeches, which is text. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. `config.json` sets `max_position_embeddings` to 131072. The tokenizer carries the Llama 3.1 chat template. Its built-in system header is "Cutting Knowledge Date: December 2023" and "Today Date: 26 Jul 2024". No counseling system prompt is set. License is `cc-by-nc-4.0`.
