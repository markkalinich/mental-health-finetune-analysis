# MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged

## Sources

https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.2-1B-Instruct-Medical-Finetuned-merged__2026-10-10.md — cached card, sha256 6f701436c9b8c1b8a2ff2e5bd6f7cd772427886796bdc626113de76311d988c6
https://huggingface.co/api/models/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged — file list and parameter count
https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged/raw/main/config.json — context length 131072
https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged/raw/main/chat_template.jinja — chat template
https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged/raw/main/tokenizer_config.json — no chat_template key
https://www.mdpi.com/2076-3417/16/12/6158 — Applied Sciences paper HTML; links the 1B adapter, not this merged id
https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers — code repository
https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/Med-LLaMa3%20Advancing%20Medical%20Question%20Answering%20through%20Parameter-Efficient%20Fine-Tuning%20of%20Large%20Language%20Models/Training/main_1b.py — 1B training script, uses SFTTrainer
https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset — compiled training set, 1,651,357 examples, loads
https://huggingface.co/datasets/lee3251/HealthCareMagic — Hub id the paper gives for HealthCareMagic
https://github.com/abachaa/MedQuAD — original MedQuAD collection; the paper does not name a Hub copy

## Record

The card uses the same compiled corpus as the 8B model: MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset, 1,651,357 English examples, expert-generated and machine-generated. The YAML names the same ten component Hub datasets. The prose also names MedQuAD and HealthCareMagic. Those two are not in the inventory string. The paper says 14,553 MedQuAD samples and points HealthCareMagic at lee3251/HealthCareMagic with 64,246 samples. It does not name a Hub id for MedQuAD.

The 1B script imports SFTTrainer and loads meta-llama/Llama-3.2-1B-Instruct in 4-bit. The card says QLoRA, rank 128, alpha 256, then merge. This repository has full BF16 weights (1,235,814,400 parameters; the card says about 1.24 billion) and no adapter. Trainable parameters on the card are 90.17 million, 6.80% of 1.32 billion. The card says 5 epochs, learning rate 2.0 × 10⁻⁵, sequence length 1024, and batch size 10 per device with gradient accumulation 40. The script sets num_epochs to 6. The card and the script agree on the parent. The inventory parent matches.

The card calls this the edge model: medical question answering, clinical decision support, and on-device use, plus a research baseline. The example says "You are a knowledgeable medical assistant." That is a strong clinical-use claim. The warning forbids autonomous diagnosis, treatment, prescribing, and decisions that affect patient care. Audiences named are clinicians and researchers. This card does not claim the 8B functions of named-entity recognition, documentation, or literature synthesis. The example is text. Multiple-choice targets in the compiled set are an option key. generation_config.json samples at temperature 0.6 and top_p 0.9. The example turns sampling off and sets max_new_tokens to 256. Context length is 131072. License is the Llama 3.2 community license.

The card's own 5-shot MMLU medical mean for this 1B model is 48.64% (Anatomy 47.41, Clinical Knowledge 48.30, College Biology 46.53, College Medicine 38.15, Medical Genetics 52.00, Nutrition 59.15, Professional Medicine 56.62, Virology 40.96). It says the paper does not report an untuned Llama-3.2-1B baseline on those subsets.
