# GeneralAnalysis/GA_Guard_1B

## Sources

https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/README.md — current model card; byte-identical to the cached card (sha256 195f1285c7484a85d15018afd112440c896136206e6b2b5ab14d0bd1bef92f63)
https://huggingface.co/api/models/GeneralAnalysis/GA_Guard_1B — file list and baked-in chat template
https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/config.json — LlamaForCausalLM; context 131,072
https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/chat_template.jinja — guard system prompt
https://huggingface.co/datasets/GeneralAnalysis/GA_Guardrail_Benchmark — dataset id on the card; HTTP 401
https://Generalanalysis.com — website linked from the card
https://Generalanalysis.com/blog — blog index linked from the card
https://generalanalysis.com/blog/ga-guard-series — series release post; it does not name this 1B checkpoint
https://huggingface.co/GeneralAnalysis/GA_Guard_1B/blob/main/LICENSE — license file linked from the card

## Record

The card YAML lists GeneralAnalysis/GA_Guardrail_Benchmark and links it as "GA Bench." It does not say the checkpoint was trained on that dataset. The dataset page returned HTTP 401, so its size, language, and provenance are not stated.

The only training sentence on the card is "The checkpoint was fine-tuned from `meta-llama/Llama-3.2-1B-Instruct`." "Fine-tuned" does not name a loss. No source states LoRA, QLoRA, a full update, rank, epochs, learning rate, or batch size. The repository contains training_args.bin, which was not decoded. No paper and no GitHub repository name this checkpoint. The series blog describes GA Guard, GA Guard Lite, and GA Guard Thinking, not GA Guard 1B.

The parent on the card is meta-llama/Llama-3.2-1B-Instruct. The card calls it the "Llama 3.2 1B variant." The weight file reports 1,235,843,072 parameters. The card language tag is English.

This is a classifier. The card says it "classifies a piece of text against seven safety policies in a single generation" and "performs classification by generating the guard label tokens." The example sends one user message. The output is one token per policy, either `<policy_violation>` or `<policy_not_violation>`. The seven categories are illicit activities, hate and abuse, PII and IP, prompt security, sexual content, misinformation, and violence and self-harm. The baked-in system prompt also says the text can be an agent input or an agent output. The card does not report an evaluation number for this checkpoint.

The usage example is text only. The card says to use greedy decoding, temperature 0.0, and max_new_tokens 16. generation_config.json instead sets do_sample true, temperature 0.6, and top_p 0.9. A chat template is present and inserts the guard system prompt. config.json sets max_position_embeddings to 131,072. The license name on the card is general-analysis-evaluation.
