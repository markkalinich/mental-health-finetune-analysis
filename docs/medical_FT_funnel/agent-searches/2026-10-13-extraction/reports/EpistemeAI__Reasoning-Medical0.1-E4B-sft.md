# EpistemeAI/Reasoning-Medical0.1-E4B-sft

## Sources

- https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-E4B-sft/raw/main/README.md — current model card; sha256 matches the cached card
- https://huggingface.co/api/models/EpistemeAI/Reasoning-Medical0.1-E4B-sft — file list, parameter total, chat template, spaces
- https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-E4B-sft/raw/main/config.json — parent name, context length, vision and audio blocks
- https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-E4B-sft/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/datasets/EpistemeAI/medical-reasoning-mix-100k — training mix and its composition
- https://huggingface.co/datasets/lingshu-medical-mllm/ReasonMed — ReasonMed card
- https://huggingface.co/datasets/UCSC-VLAA/MedReason — MedReason card
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — medical-o1 card
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA card
- https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options — MedQA card
- https://huggingface.co/datasets/qiaojin/PubMedQA — PubMedQA card
- https://huggingface.co/datasets/zou-lab/MedCaseReasoning — MedCaseReasoning card
- https://huggingface.co/datasets/jmhb/PaperSearchQA — PaperSearchQA card
- https://github.com/AIEpisteme/BioSafeBench — biological-safety benchmark linked from the card
- https://github.com/unslothai/unsloth — library link, not a training repository for this checkpoint
- https://huggingface.co/spaces/legolasyiu/RAG-Medical-Reasoning-chat-Demo — space whose files name this model
- Cached card: revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__Reasoning-Medical0.1-E4B-sft__2026-10-10.md

## Record

The training set is EpistemeAI/medical-reasoning-mix-100k. The card says the model "was fine-tuned on a large-scale dataset of 100,000 records" and "approximately 100,000 medical reasoning examples." The mix card's composition is the same eight sources as for the 27B sibling: ReasonMed, MedReason, medical-o1-reasoning-SFT, MedMCQA, MedQA-USMLE-4-options, PubMedQA pqa_artificial, MedCaseReasoning, and PaperSearchQA. The mix is gated and has parquet files. Provenance of the mix is mixed: generated reasoning traces plus exam questions. MedCaseReasoning's own card does not say who wrote the text.

The sections written for this checkpoint say supervised fine-tuning. The model-details table says "Training method | Supervised Fine-Tuning, SFT", and the Training Summary says "This model was fine-tuned using supervised fine-tuning on medical reasoning data." The introduction also says "Training was performed using the GRPO trainer with the Unsloth optimization method." Those two claims conflict. The objective field records SFT, because that is the method named in the table and the training summary. The inventory lists both. No file in the repository is a training script, so epochs, learning rate, batch size, LoRA rank, and full versus LoRA update are not stated. The repository has one model.safetensors file and no adapter_config.json. A sibling repo named Reasoning-Medical0.1-E4B-sft_lora has only the Unsloth template card and does not say it was merged into this checkpoint.

The parent is unsloth/gemma-4-E4B-it. The card and config.json both say that. The card does not state a parameter count. The Hub safetensors total is 7,996,156,490. Primary language is English.

The card presents a reasoning assistant that explains a likely diagnosis. The example is "Explain the likely diagnosis and reasoning" for a 65-year-old man with shortness of breath. Intended users are "Researchers, students, developers, clinicians using human review." That is a strong medical-use claim. The warning is an explicit prohibition: "Do not use this model for" autonomous diagnosis, treatment decisions, emergency advice, prescribing, or replacing a clinician.

The purpose is medical education, research support, biomedical reasoning, literature review, and clinician-reviewed analysis. Audiences named are researchers, developers, students, and clinicians who review the output.

It claims clinical reasoning, medical question answering, multiple-choice and exam-style reasoning, differential diagnosis, study support, literature review, and drafting explanations a clinician reviews.

The tasks are medical question answering, differential diagnosis, and exam-style reasoning. Reported scores are MedQA accuracy 0.760, MMLU-Pro Biology 0.75, and MMLU-ProX English biology 0.75. MedMCQA, PubMedQA, and several MMLU clinical subjects are suggested benchmarks without scores. Named fields are professional medicine, medical genetics, college biology/medicine, clinical knowledge, biomedical QA, and clinical education.

The usage example is a text chat. config.json also has vision and audio blocks, and the Hub pipeline tag is image-text-to-text. A chat template is present. No system role is set in the example. generation_config.json uses temperature 1.0, top_k 64, top_p 0.95, and do_sample true. The card recommends temperature 0.2 and top_p 0.9 for factual reasoning. Context length in config.json is 131,072 tokens. The license is apache-2.0. No paper names this checkpoint. BioSafeBench is an evaluation repo the card links, with a reported mean score of 87.5/100.
