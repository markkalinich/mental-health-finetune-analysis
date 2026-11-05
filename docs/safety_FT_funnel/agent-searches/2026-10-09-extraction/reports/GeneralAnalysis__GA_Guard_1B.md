# GeneralAnalysis/GA_Guard_1B

## Sources

- https://huggingface.co/GeneralAnalysis/GA_Guard_1B — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/GeneralAnalysis__GA_Guard_1B__2026-10-09.md — cached card, sha256 195f1285c7484a85d15018afd112440c896136206e6b2b5ab14d0bd1bef92f63
- https://huggingface.co/api/models/GeneralAnalysis/GA_Guard_1B — file list, parameter count, and chat template
- https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/config.json — context length 131072
- https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/_training_system.txt — system prompt baked into the template
- https://huggingface.co/datasets/GeneralAnalysis/GA_Jailbreak_Benchmark — dataset the card's benchmark id resolves to
- https://huggingface.co/api/datasets/GeneralAnalysis/GA_Guardrail_Benchmark — API returns id GeneralAnalysis/GA_Jailbreak_Benchmark
- https://generalanalysis.com/blog/ga-guard-series — family blog; does not name this repository

## Record

The card lists dataset `GeneralAnalysis/GA_Guardrail_Benchmark`. That Hub id resolves to `GeneralAnalysis/GA_Jailbreak_Benchmark`. The dataset card says: "A curated benchmark of 2,795 synthetic jailbreak attempts and safety prompts generated with the General Analysis Adversary Pipeline." The file `ga_jailbreak.csv` returns HTTP 401, gated, so the rows do not load. The dataset card calls this an evaluation benchmark for GA Guard Core and GA Guard Lite. It does not say GA Guard 1B was trained on it.

No source names a loss. The card says only: "The checkpoint was fine-tuned from `meta-llama/Llama-3.2-1B-Instruct`." "Fine-tuned" is not a named objective. The repository has full weights in `model.safetensors` and a binary `training_args.bin`, and it has no `adapter_config.json`. Rank, alpha, epochs, steps, learning rate, and batch size are not stated.

The parent on the card is `meta-llama/Llama-3.2-1B-Instruct`. No paper or GitHub page names this repository, so no outside source confirms or contradicts that parent. The Hub API reports 1,235,843,072 parameters. The card calls it "the Llama 3.2 1B variant."

The card presents a classifier, not a chatbot: "It is optimized for low-latency moderation and classifies a piece of text against seven safety policies in a single generation." One of those policies is "**Violence & Self-Harm**: content that encourages violence, self-harm, or suicide." That is a moderation category, so the therapy-or-support claim is Weak. The only caution is: "It should be used as one layer in a broader safety system, especially for high-risk domains or decisions that require human review." That is unrelated to therapy or medical advice. The card does not report scores for this checkpoint. The 1 October 2025 blog reports scores for GA Guard, GA Guard Lite, and GA Guard Thinking, and its code samples use `GeneralAnalysis/GA_Guard_Core`.

Callers pass text only: "Callers only need to provide the text to classify as a user message." A chat template is present in `tokenizer_config.json` and `chat_template.jinja`, and it inserts the guard system prompt from `_training_system.txt`. `generation_config.json` sets temperature 0.6, top_p 0.9, and do_sample true. The card instead says to use temperature 0.0, max_new_tokens 16, and greedy decoding. `config.json` sets max_position_embeddings to 131072. The license name on the card is `general-analysis-evaluation` (`license: other`), and the card also says to use the Llama 3.2 license terms.
