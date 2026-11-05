# MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged

## Sources

- https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged/raw/main/README.md — current model card; identical to the 10 October 2026 cache
- https://huggingface.co/api/models/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged — repository file list and safetensors parameter count
- https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged/raw/main/config.json — architecture and context length
- https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged/raw/main/chat_template.jinja — Llama 3.2 chat template
- https://www.mdpi.com/2076-3417/16/12/6158 — paper HTML (Applied Sciences, 2026); no arXiv HTML
- https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers — code repository README and the 3B training script
- https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset — compiled training corpus card
- https://huggingface.co/datasets/medalpaca/medical_meadow_medqa — Medical Meadow MedQA card
- https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards — flashcards card
- https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc — WikiDoc card
- https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc_patient_information — WikiDoc patient-information card
- https://huggingface.co/datasets/medalpaca/medical_meadow_cord19 — CORD-19 card
- https://huggingface.co/datasets/medalpaca/medical_meadow_pubmed_causal — PubMed causal card
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA card
- https://huggingface.co/datasets/bigbio/med_qa — BigBIO MedQA card
- https://huggingface.co/datasets/qiaojin/PubMedQA — PubMedQA card
- https://huggingface.co/datasets/deepset/covid_qa_deepset — COVID-QA card
- https://huggingface.co/datasets/lavita/MedQuAD — MedQuAD Hub copy
- https://huggingface.co/datasets/lee3251/HealthCareMagic — HealthCareMagic Hub copy named in the paper
- https://huggingface.co/datasets/tatsu-lab/alpaca — Alpaca card
- https://huggingface.co/datasets/lighteval/med_dialog — MedDialog Hub copy

## Record

The training corpus is the compiled set `MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`, which loads and has 1,651,357 rows. Its card says it is “the training corpus used to fine-tune the Med-LLaMA3 family (LLaMA-3.2 1B/3B and LLaMA-3.1 8B).” The model card’s YAML lists eleven Hub datasets (Medical Meadow subsets, MedMCQA, BigBIO MedQA, PubMedQA, and COVID-QA). Those Hub datasets load. The compiled card’s source table also names MIMIC-III (465,200), UMLS (312,450), MedDialog English (257,337), HealthCareMagic (112,165 on `lee3251/HealthCareMagic`; the paper text says 64,246), Alpaca (52,000, synthetic), ChatDoctor iCliniq (30,000), and CovidDialog English (6,032). No Hub id was found for MIMIC-III, UMLS, ChatDoctor, or CovidDialog. The paper says MMLU medical items were excluded from fine-tuning.

Training is supervised fine-tuning. The 3B script constructs `SFTTrainer` on `meta-llama/Llama-3.2-3B-Instruct`. The update is QLoRA: the card says “QLoRA fine-tuning (4-bit NF4 base + LoRA, r=128, α=256, all linear layers), then merge_and_unload() into the base.” Rank 128, alpha 256, 4-bit NF4 during training, adapter merged into the released weights. The card and paper Table 5 say 5 epochs, learning rate 2.0×10⁻⁵, batch size 4 per device, gradient accumulation 16, max sequence length 2048. The 3B script instead sets `num_epochs` to 6. No step count is stated. Paper Table 5 also says “Task type | Causal language modeling.”

The parent is `meta-llama/Llama-3.2-3B-Instruct`. The card, the 3B script, and the paper’s “LLaMA 3.2 3B” description agree. The card states “Parameters | ~3.21 B.” The Hub safetensors header reports 3,212,749,824 BF16 parameters. The card also says 194.51 M trainable parameters, 5.70% of a 3.40 B total, during fine-tuning.

The card presents a medical assistant a person talks to, so the output type is a chatbot. The use claim is strong: “Clinical knowledge lookup and clinical decision support assistance.” The warning is an explicit prohibition: “It must not be used for autonomous diagnosis, treatment, prescribing, or any decision affecting patient care without review by a qualified healthcare professional.”

The purpose is stated. Audiences named are a qualified healthcare professional, who must review any decision affecting patient care, and researchers, in “A research baseline for parameter-efficient fine-tuning of small LLaMA models in healthcare.”

The card says the model does medical question answering, including multiple-choice exam items, clinical decision support, and service as a research baseline.

The medical work is medical question answering, exam answering on MedMCQA, MedQA-USMLE, and PubMedQA (training splits only; MMLU is evaluation only), patient–doctor conversation from HealthCareMagic, consumer-health QA from MedQuAD, and a usage example that asks for first-line treatment of pneumonia. The specialty is general medicine: the card says the model was “adapted to the medical domain” and names no single field. Language is English.

Serving is text only. The chat template is present as `chat_template.jinja`; `tokenizer_config.json` does not contain a `chat_template` key. The template is the stock Llama 3.2 template and does not hardcode a medical system prompt. The card’s example system line is “You are a knowledgeable medical assistant. Answer accurately and concisely.” `generation_config.json` sets temperature 0.6, top_p 0.9, and do_sample true. Context length in `config.json` is 131,072. License is llama3.2.

The paper names this 3B model as “Med-LLaMA3.2 3B (Ours)” and prints Table 7 scores that match the card. The data-availability link is the adapter repo `Llama-3.2-3B-Instruct-Medical-Finetuned`, with a space in “Mohamed AhmedAE”, not this `-merged` id. The card says the merged weights and that adapter produce identical outputs. No arXiv copy of the paper was found.
