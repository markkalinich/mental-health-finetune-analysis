# jl3676/BenefitReporter

## Sources

https://huggingface.co/jl3676/BenefitReporter/raw/main/README.md — current model card; same bytes as the cached card
https://huggingface.co/api/models/jl3676/BenefitReporter — repository file list
https://huggingface.co/jl3676/BenefitReporter/raw/main/config.json — Llama config, context length 131072
https://huggingface.co/jl3676/BenefitReporter/raw/main/generation_config.json — sampling defaults
https://huggingface.co/jl3676/BenefitReporter/raw/main/tokenizer_config.json — chat template
https://arxiv.org/abs/2410.16665 — abstract of the SafetyAnalyst paper
https://arxiv.org/html/2410.16665 — HTML full text of that paper
https://github.com/jl3676/SafetyAnalyst — code repository; README links this model id
https://github.com/jl3676/SafetyAnalyst/blob/master/src/models.py — loads jl3676/BenefitReporter and sets sampling
https://jl3676.github.io/SafetyAnalyst/ — project page; names BenefitReporter
https://proceedings.mlr.press/v267/li25bw.html — ICML 2025 proceedings page for the same paper
https://huggingface.co/datasets/jl3676/SafetyAnalystData — training dataset card; viewer loads
https://huggingface.co/datasets/allenai/wildjailbreak — prompt source named on that dataset card; gated
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0 — prompt source; viewer loads
https://huggingface.co/datasets/allenai/WildChat-1M — prompt source; viewer loads
https://arxiv.org/abs/2406.17864v1 — AIR 2024 taxonomy linked from the dataset card; not read

## Record

BenefitReporter was trained on `jl3676/SafetyAnalystData`. The dataset card says it has 19,188 prompts and harm-benefit trees, in English, and: "we generate harm-benefit trees using a suite of LLMs (GPT-4o, Gemini-1.5-Pro, Claude-3.5-Sonnet, Llama-3.1-405B-Instruct, and Llama-3.1-70B-Instruct)." The viewer loads. Those prompts were sampled from three public sets. WildJailbreak (`allenai/wildjailbreak`) is "an open-source synthetic safety-training dataset with 262K" prompt-response pairs; the Hub copy is gated and does not load without accepting terms. Aegis (`nvidia/Aegis-AI-Content-Safety-Dataset-1.0`) is "approximately 11,000 manually annotated interactions," with model-written responses, and the viewer loads. WildChat-1M (`allenai/WildChat-1M`) is "a collection of 1 million conversations between human users and ChatGPT," and the viewer loads. No source says how many rows came from each of those three sets. The paper says the teachers produced 18.5 million harm-benefit features on 18,901 prompts, plus 13,838 adversarial prompts from WildJailbreak.

The student update is supervised fine-tuning with QLoRA. The paper says: "We applied supervised fine-tuning using qlora (Dettmers et al., 2024; Lambert et al., 2024) to distill the knowledge about harms and benefits from the teacher LMs into the student LM." The same sentence is the distillation step: teacher-written trees become the supervised targets. One specialist was trained for harm trees and one for benefit trees. Fine-tuning used a context window of 18,000 tokens on 8 H100 GPUs. The paper and the GitHub repository do not state LoRA rank, alpha, epochs, steps, learning rate, or batch size. The Hub repository has full F32 weight shards and no adapter file. No sentence says the adapter was merged.

The parent is `meta-llama/Llama-3.1-8B-Instruct`. The card says "Finetuned from model: meta-llama/Llama-3.1-8B-Instruct." The paper says "We trained Llama-3.1-8B-Instruct to specialize in generating harm trees and benefit trees." The card says the model is "a 8B model." The Hub safetensors metadata counts 8,030,326,784 F32 parameters. The paper does not print `jl3676/BenefitReporter`. The project page and the GitHub README do, and the GitHub loader requests `jl3676/BenefitReporter`.

This model writes a benefit tree. It is not a chatbot and it does not itself emit the harmfulness label. The card says: "BenefitReporter is an open language model that generates a structured benefit tree for a given prompt." A separate aggregation program turns the trees from this model and HarmReporter into a score. There is no therapy or mental-health support claim. The limitation is accuracy: "BenefitReporter will sometimes generate inaccurate features and the aggregated harmfulness score may not always lead to correct judgments." The license is Apache 2.0. The card reports the combined SafetyReporter system, not this model alone: average F1 3.7% above WildGuard, 10.8% above Llama-Guard-3, and over 30% above ShieldGemma. The paper reports SafetyAnalyst average F1 0.81, against existing systems under 0.72. The paper was published at ICML 2025.

The card runs the model on a text prompt, `user_prompts = ["How can I rob the bank?"]`. A chat template is in `tokenizer_config.json`. It formats user and assistant turns only. The instruction is pasted in front as a raw `<|system|>` block beginning "Given a scenario based on an interaction between an AI language model and its user." `generation_config.json` sets `do_sample` true, temperature 0.6, and top_p 0.9. The card's generate call uses `max_new_tokens=18000`. The GitHub loader uses `max_tokens=19000` with the same temperature and top_p. `config.json` sets `max_position_embeddings` to 131072. The card says the language is English.
