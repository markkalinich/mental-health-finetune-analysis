# openmed-community/granite-4.0-micro-OpenMed

## Sources

- https://huggingface.co/openmed-community/granite-4.0-micro-OpenMed/raw/main/README.md — current model card; identical to the cached card (`cmp` exit 0)
- https://huggingface.co/api/models/openmed-community/granite-4.0-micro-OpenMed — file list and safetensors count
- https://huggingface.co/openmed-community/granite-4.0-micro-OpenMed/raw/main/config.json — context length 131072
- https://huggingface.co/openmed-community/granite-4.0-micro-OpenMed/raw/main/generation_config.json — token ids only
- https://huggingface.co/openmed-community/granite-4.0-micro-OpenMed/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/openmed-community/granite-4.0-micro-OpenMed/raw/main/chat_template.jinja — chat template with tool and document prefixes
- https://huggingface.co/datasets/mkurman/medmcqa-hard — MedMCQA-Hard dataset card (loads; train 164,539, test 18,283)
- https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following — Tulu-3 personas dataset card (29,980 synthetic English rows)
- https://github.com/mkurman/jepa-llm — JEPA fine-tuning toolkit the card calls its implementation; README does not name this repository
- https://github.com/arcee-ai/mergekit — merge library the card cites for Arcee Fusion
- https://arxiv.org/abs/2509.14252 — LLM-JEPA paper linked from the card; the abstract does not name this repository
- https://hotaisle.xyz/ — compute-credit sponsor

## Record

Two datasets are named with Hub ids. The card says the SFT and GRPO stages use `mkurman/medmcqa-hard`, and "MedMCQA-Hard (train split)" supplies domain supervision and RL rewards. That dataset loads. Its card says it is "Derived from MedMCQA" and lists 164,539 train rows and 18,283 test rows, language `en`. The questions are entrance-exam items, so the provenance is human. The second set is `allenai/tulu-3-sft-personas-instruction-following`. Its card says: "This dataset contains 29980 examples and is synthetically created." Language is English. Neither dataset card names this checkpoint.

The named objectives are supervised fine-tuning and GRPO. The card says: "JEPA-LLM SFT on medmcqa-hard + personas augmentation → GRPO on medmcqa-hard." It also says the JEPA-LLM term is "an auxiliary signal during SFT" rather than pure next-token fitting. GRPO is glossed as "group-relative PPO." The SFT stage is "400 steps, bs=64." GRPO uses batch 64/128 and 8 generations per item. No learning rate, epoch count, or GRPO step count is stated. The card does not say full fine-tuning or LoRA. The JEPA toolkit can do either. The final step is an Arcee Fusion merge back into the IBM base. No `mergekit_config.yml` is in the repository.

The parent is `ibm-granite/granite-4.0-micro`. The card says it is a "3B long-context instruct model." The safetensors total is 3,402,836,480 parameters. The card's language tag is `en`.

The use claim is strong. The quickstart says: "You are a careful medical assistant." The warning is an explicit prohibition. The card says: "Do not use for diagnosis or treatment."

The purpose is stated. The card says the model is "tuned for medical education & instruction following" and "Intended: medical research, concept review, exam-style Q&A, instruction-following research, and tool-augmented demos." The audiences are a student or exam taker and a researcher or developer. The functions are exam answering, medical question answering, and study or teaching support. The quickstart asks for bullet differences, so one output is a chat reply. The training set's answers are multiple-choice letters, so exam letter also applies. The clinical tasks are exam answering on MedMCQA-Hard and concept review. MMLU is evaluation only: 63.17 versus the base 62.48. The specialty is general. No single field is named as the model's domain.

Serving is text only. Generation in the example is `max_new_tokens=256` and `do_sample=False`. `max_position_embeddings` is 131072. The license is `apache-2.0`.

Inventory datasets and parent match. Inventory methods `dpo|grpo|ppo|sft` add DPO and a separate PPO stage. The card names SFT and GRPO, and the tag is `dpo-like`, not a DPO run.
