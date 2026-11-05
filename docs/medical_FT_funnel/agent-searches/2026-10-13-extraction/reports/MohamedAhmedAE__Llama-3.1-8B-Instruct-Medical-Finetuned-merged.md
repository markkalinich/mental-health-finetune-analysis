# MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged

## Sources

https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.1-8B-Instruct-Medical-Finetuned-merged__2026-10-10.md — cached card, sha256 df798500f64cf60084a22df72dca77c7e99a70399a5558788e79363877fbe7cd
https://huggingface.co/api/models/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged — file list and parameter count
https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged/raw/main/config.json — context length 131072
https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged/raw/main/chat_template.jinja — Llama 3.1 chat template
https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged/raw/main/tokenizer_config.json — no chat_template key
https://www.mdpi.com/2076-3417/16/12/6158 — Applied Sciences paper HTML
https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers — code repository
https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/Med-LLaMa3%20Advancing%20Medical%20Question%20Answering%20through%20Parameter-Efficient%20Fine-Tuning%20of%20Large%20Language%20Models/Training/main_8b.py — 8B training script, uses SFTTrainer
https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset — compiled training set, 1,651,357 examples, loads
https://huggingface.co/datasets/medalpaca/medical_meadow_medqa — component set, API returns the repo
https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards — component set, API returns the repo
https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc — component set, API returns the repo
https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc_patient_information — component set, API returns the repo
https://huggingface.co/datasets/medalpaca/medical_meadow_cord19 — component set, API returns the repo
https://huggingface.co/datasets/medalpaca/medical_meadow_pubmed_causal — component set, API returns the repo
https://huggingface.co/datasets/openlifescienceai/medmcqa — component set, API returns the repo
https://huggingface.co/datasets/bigbio/med_qa — component set, API returns the repo
https://huggingface.co/datasets/qiaojin/PubMedQA — component set, API returns the repo
https://huggingface.co/datasets/deepset/covid_qa_deepset — component set, API returns the repo
https://huggingface.co/datasets/lee3251/HealthCareMagic — Hub id the paper gives for HealthCareMagic
https://github.com/abachaa/MedQuAD — original MedQuAD collection; the paper does not name a Hub copy

## Record

The card trains this checkpoint on MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset, a compiled instruction set of 1,651,357 English examples. The dataset card lists creators as expert-generated and machine-generated, so the mix is mixed. The YAML also names ten public component sets: six Medical Meadow subsets, MedMCQA, BigBIO MedQA, PubMedQA, and COVID-QA. Each of those Hub repositories answered the datasets API. The card and the paper also name MedQuAD (14,553 samples in the paper) and HealthCareMagic. The paper points HealthCareMagic at lee3251/HealthCareMagic and says 64,246 samples; a table in the same paper lists 112,165. The paper does not say which Hub copy of MedQuAD was used. It says the eight MMLU medical subsets were held out of training.

The training script imports SFTTrainer. The card says the update is QLoRA: 4-bit NF4, LoRA rank 128, alpha 256, all linear layers, then merge_and_unload. This repository has full weights and no adapter file. The card says 5 epochs, learning rate 2.0 × 10⁻⁵, and batch size 1 per device with gradient accumulation 4. The 8B script sets num_epochs to 6. Safetensors count is 8,030,261,248. The card says about 8.03 billion parameters and that 335.54 million (4.01%) were trainable.

The card, the script, and the inventory name the parent meta-llama/Llama-3.1-8B-Instruct. The paper is about this 8B model under the name Med-LLaMA3. Its data-availability link is the adapter repository, not this merged id.

The card says the model is for medical question answering, clinical decision support, clinical named-entity recognition, documentation assistance, and literature synthesis, and as a research baseline. The example system line is "You are a knowledgeable medical assistant." That is a strong clinical-use claim. The warning is an explicit prohibition: "It must not be used for autonomous diagnosis, treatment, prescribing, or any decision affecting patient care without review by a qualified healthcare professional." Audiences named are clinicians (physician review, clinical decision support) and researchers (a research baseline). The example is a text chat. Multiple-choice training targets are an option key. The chat template is in chat_template.jinja. generation_config.json samples at temperature 0.6 and top_p 0.9. The card example turns sampling off and sets max_new_tokens to 256. Context length is 131072. Language is English. License is the Llama 3.1 community license.

Reported 5-shot scores for this 8B model: MMLU medical mean 75.71%, MedMCQA 61.8%, MedQA 62.4%, PubMedQA 77.0%. Zero-shot NER macro F1 is 0.94 on 100 discharge summaries. An expert review of 100 generated cases rated 94% Good and found critical errors in 6%.
