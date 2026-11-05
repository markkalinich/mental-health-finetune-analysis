# EpistemeAI/Reasoning-Medical0.1-27B

## Sources

- https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-27B/raw/main/README.md — current model card; sha256 matches the cached card
- https://huggingface.co/api/models/EpistemeAI/Reasoning-Medical0.1-27B — repository file list, chat template, spaces
- https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-27B/raw/main/config.json — architecture, parent name, context length
- https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-27B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/datasets/EpistemeAI/medical-reasoning-mix-100k — training mix card and composition table
- https://huggingface.co/datasets/lingshu-medical-mllm/ReasonMed — ReasonMed card
- https://huggingface.co/datasets/UCSC-VLAA/MedReason — MedReason card
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — medical-o1 card
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA card
- https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options — MedQA card
- https://huggingface.co/datasets/qiaojin/PubMedQA — PubMedQA card
- https://huggingface.co/datasets/zou-lab/MedCaseReasoning — MedCaseReasoning card
- https://huggingface.co/datasets/jmhb/PaperSearchQA — PaperSearchQA card
- https://huggingface.co/spaces/EpistemeAI/Reasoning-Medical0.1-27B-chat — chat space listed on the model
- https://github.com/unslothai/unsloth — library link on the card, not a training repository for this checkpoint
- https://github.com/QwenLM/Qwen-Agent — agent library linked from the card
- Cached card: revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__Reasoning-Medical0.1-27B__2026-10-10.md

## Record

The training set named on the model card is EpistemeAI/medical-reasoning-mix-100k, "a large-scale dataset of 100000 records" made by "blending various public medical reasoning datasets." The mix card lists eight sources and target row counts: ReasonMed 40,000, MedReason 20,000, medical-o1-reasoning-SFT 10,000, MedMCQA 10,000, MedQA-USMLE-4-options 5,000, PubMedQA config pqa_artificial 5,000, MedCaseReasoning 5,000, and PaperSearchQA 5,000. Those Hub datasets have data files. The mix itself is gated (auto) and stores two parquet shards. ReasonMed, medical-o1, PubMedQA artificial, and PaperSearchQA are generated text. MedMCQA and MedQA are exam questions. MedReason adds generated reasoning to questions from other medical datasets. MedCaseReasoning's card does not say whether the text is human or generated. The mix card does not set a language tag.

The objective is GRPO. The card says "Training was performed using the GRPO trainer with the Unsloth optimization method for efficient fine-tuning." It does not say full fine-tuning, LoRA, or QLoRA. The repository ships eleven safetensors shards and no adapter_config.json, which does not settle whether an adapter was merged. Epochs, steps, learning rate, batch size, LoRA rank, and LoRA alpha are not stated. The sentence "This qwen3_5 model was trained 2x faster with Unsloth" is library boilerplate. "Training Stage: Pre-training & Post-training" sits in the architecture block and is not a separate claim about this checkpoint.

The parent is unsloth/Qwen3.5-27B. The card says "Finetuned from model : unsloth/Qwen3.5-27B", and config.json has `"model_name": "unsloth/Qwen3.5-27B"`. Those agree. The card states 27B parameters. The safetensors header totals 27,781,427,952.

The card describes a medical reasoning and question-answering model for education, research, literature analysis, and private deployments. That is a moderate medical use: it does not present the model as a doctor chatbot or as a tool that gives diagnosis or treatment advice. The warning is an explicit prohibition: "Its outputs should not be used to directly guide clinical diagnosis, patient management, treatment decisions, or any other direct clinical practice applications." A separate sentence forbids biological and chemical weapon uses.

The purpose is stated: "designed for advanced medical reasoning in professional medicine, medical genetics, college biology/medicine, and clinical knowledge." The named audiences are research users ("Research copilots", "clinical reasoning research", "Model benchmarking and safety evaluation") and biotech/pharma ("Biotech/pharma literature analysis"). No patient, clinician, or student is named as the user. "Medical education applications" is a use, not a named person.

The card claims clinical reasoning, medical question answering, exam answering (the MedQA and MMLU-Pro biology scores), study or teaching support, and literature analysis. It does not claim diagnosis, treatment advice, or note writing.

The medical work is medical question answering. MedQA, MMLU-Pro Biology, and MMLU-ProX Biology are evaluation scores only. HealthBench Pro (accuracy 0.54) is also evaluation only. The fields named are professional medicine, medical genetics, college biology/medicine, and clinical knowledge.

People talk to it through a chat-completions API. It writes a thinking block and then a final reply. For multiple-choice benchmarks the card tells the user to ask for a choice letter inside a JSON answer field. Input is not text-only: the card says "Causal Language Model with Vision Encoder" and shows image and video examples. A chat template is present in tokenizer_config.json and chat_template.jinja. No system prompt is fixed in that template. generation_config.json sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. The card's thinking-mode recommendation is temperature 1.0 with the same top_k and top_p. Native context length is 262,144 tokens. The license line is "cc". No paper or GitHub training repository names this checkpoint. The inventory row (GRPO, this mix, this parent) matches the card.
