# empirischtech/Llama-3.1-8B-Instruct-MedQA

## Sources

https://huggingface.co/empirischtech/Llama-3.1-8B-Instruct-MedQA/raw/main/README.md — model card (same bytes as the 10 October cache)
https://huggingface.co/api/models/empirischtech/Llama-3.1-8B-Instruct-MedQA — file list, parameter count, chat template
https://huggingface.co/empirischtech/Llama-3.1-8B-Instruct-MedQA/raw/main/config.json — parent path, context length, Unsloth version key
https://huggingface.co/empirischtech/Llama-3.1-8B-Instruct-MedQA/raw/main/generation_config.json — sampling settings
https://huggingface.co/datasets/empirischtech/med-qa-orpo-dpo — preference dataset named on the card
https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA dataset card
https://huggingface.co/datasets/bigbio/med_qa — MedQA dataset page
https://huggingface.co/datasets/bigbio/pubmed_qa — PubMedQA dataset page; the viewer does not load
https://featherless.ai/models/empirischtech/Llama-3.1-8B-Instruct-MedQA — host page that repeats the card

## Record

The card YAML names four datasets: `openlifescienceai/medmcqa`, `bigbio/med_qa`, `bigbio/pubmed_qa`, and `empirischtech/med-qa-orpo-dpo`. The body says something else: "Fine-Tuning Dataset: Curated medical literature, clinical case studies, and healthcare FAQs". That phrase has no Hub id. MedMCQA loads. Its card says "more than 194k" AIIMS and NEET PG questions collected from websites and books, so those questions are human-written. `bigbio/med_qa` loads and the page says 272,634 rows. It does not state who wrote them. `bigbio/pubmed_qa` does not load: the viewer is disabled because the repository still needs a Python loading script. Its card says the set has 1k expert-annotated questions, 61.2k unlabeled pairs, and 211.3k artificially generated instances, so it is mixed. The author's preference set loads and has 357,058 rows. Its card says it is "shaped in question, choosen and rejected pairs to match the ORPO-DPO trainset requirements," built from those three sources.

The loss is not named. The card says "Trained with reinforcement learning and domain-specific optimizations." It does not say SFT, DPO, ORPO, PPO, or RLHF. The words ORPO and DPO appear in a dataset id and on that dataset card. They are not a sentence about this checkpoint's loss. Update scope is not stated. The repository is four safetensors shards, 8,030,277,632 parameters, with no adapter file. config.json has `unsloth_version` 2025.1.7 and no LoRA rank. No epoch, step count, learning rate, or batch size is stated. No paper and no GitHub repository name this checkpoint.

The parent in the card YAML is `meta-llama/Llama-3.1-8B-Instruct`. config.json `_name_or_path` points at a local snapshot of that same Instruct repository. The card body says "Base Model: Llama-3.1-8B". Those two statements do not match. The title says 8B.

The use claim is strong. The card offers "Clinical Decision Support" and "Medical Chatbots" that answer patient queries. The warning is a disclaimer: "This model is not a substitute for professional medical advice. Always consult a healthcare provider for clinical decisions." It also says the model "is intended for research and educational purposes."

A purpose is stated: precise answers to medical questions, plus topic tagging and sentiment analysis. The audiences are healthcare professionals and patients. The functions are answering medical questions, talking with a patient, supporting a clinical decision, tagging topics, and judging sentiment. The usage example is the text question "What are the symptoms of diabetes?", so one output is a chat reply. Topic tagging is described as categorizing content, so a label is also claimed.

The clinical tasks are medical question answering, exam answering (MedMCQA, MedQA, and PubMedQA are named as datasets), and conversation with a patient. The specialty is general. The card says "healthcare" and names no field. The YAML lists accuracy as a metric and does not give a score.

Serving is text only. The architecture is `LlamaForCausalLM`. Context length is 131,072. generation_config.json sets do_sample true, temperature 0.6, and top_p 0.9. The chat template has no default system sentence. The license name is llama3.1. The inventory datasets and the YAML parent match. The match is only partial because the card body names Llama-3.1-8B, not the Instruct repository.
