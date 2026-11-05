# yasserrmd/PharmaQA-270M

## Sources

https://huggingface.co/yasserrmd/PharmaQA-270M/raw/main/README.md — current model card; sha256 matches the cached card
https://huggingface.co/api/models/yasserrmd/PharmaQA-270M — repository file list and safetensors parameter count
https://huggingface.co/yasserrmd/PharmaQA-270M/raw/main/config.json — Gemma 3 text architecture, context length, Unsloth flags
https://huggingface.co/yasserrmd/PharmaQA-270M/raw/main/generation_config.json — sampling settings
https://huggingface.co/yasserrmd/PharmaQA-270M/raw/main/tokenizer_config.json — tokenizer; no chat_template key; no default system prompt
https://huggingface.co/yasserrmd/PharmaQA-270M/raw/main/chat_template.jinja — Gemma chat template, including an image branch
https://huggingface.co/datasets/miriad/miriad-4.4M — dataset page; viewer loads
https://huggingface.co/datasets/miriad/miriad-4.4M/raw/main/README.md — dataset card; 4,487,542 train rows
https://huggingface.co/api/datasets/miriad/miriad-4.4M — dataset is public and not gated
https://arxiv.org/abs/2506.06091 — MIRIAD paper abstract, linked from the dataset card; it does not name this repository
https://arxiv.org/html/2506.06091 — HTML checked for yasserrmd, PharmaQA-270M, and gemma-3-270m; none of those strings appear
https://www.linkedin.com/posts/moyasser_llm-healthcareai-pharmacology-activity-7361853839962005504-GHzz — release post by Mohamed Yasser, the author named on the card
https://github.com/unslothai/unsloth — Unsloth library cited on the card, not this model's training code

## Record

The training set is a 25,000-pair subset of miriad/miriad-4.4M. The card says: "25,000 Q&A pairs from MIRIAD-4.4M" and "The model was trained on MIRIAD Q&A pairs generated via LLMs from biomedical literature." The dataset card says MIRIAD "contains 4.4 million medical question-answer pairs, distilled from peer-reviewed biomedical literature using LLMs," and its YAML reports `num_examples: 4487542`. The Hub dataset is public, not gated, and the viewer shows rows, so it loads. Provenance is synthetic. The model card's language field is `en`.

The update is LoRA, and the adapter was merged. The card says "it was fine-tuned using LoRA and merged into a single model checkpoint" and "Final Format | Merged (base + LoRA weights)." Epochs are 3. No sentence names a loss, so the objective is not stated. "Instruction-tuned" is not a named loss. Rank, alpha, steps, learning rate, and batch size are not stated. No file says the base was quantized during training. The repo has `model.safetensors` and no `adapter_config.json`. `config.json` has `unsloth_fixed` true and `unsloth_version` `2025.8.5`.

The parent in the YAML is unsloth/gemma-3-270m-it. The details table says "Base Model | Google Gemma3 (270M parameters)." The author's LinkedIn post says the same: "A lightweight alternative based on Google Gemma3 (270M parameters)" and "Both models were fine-tuned using Unsloth AI with LoRA and merged." The card says the size is 270M. The Hub API reports 268,098,176 parameters. The YAML license is `apache-2.0`. The license section also says the model is "Open for academic and non-commercial use." The details table lists "ODC-BY v1.0 dataset license (non-commercial)." The dataset card says ODC-By v1.0 permits commercial reuse with attribution, and that OpenAI's terms forbid using the generated outputs for medical diagnosis or decision-making about real individuals.

The use claim is moderate. The best-use row is "Lightweight educational deployment (MCQs, tutoring)." The warning is an explicit prohibition: "Do not use this model for real-world medical diagnosis, treatment, or care decisions." The card also says "MIRIAD and this model must be used for educational, research, and academic exploration only." Evaluation on 50 unseen pharma questions reports an average answer length of 40.3 words, a longest answer of 95 words, a shortest of 12 words, and zero empty or short responses. It describes clinical accuracy as "Consistent terminology" and depth as "Limited." The MIRIAD paper does not name this checkpoint. Searches did not find a training repository for this model.

The purpose is stated. The card says it is "a compact, instruction-tuned language model for pharmacology and pharmacy domains" and that it is "optimized for educational and research use cases." Audiences are students or exam takers, from "MCQs, tutoring," and researchers, from the research-use sentence. The author's post adds "Domain-specific Q&A for pharmacology education" and "Research assistants for drug mechanisms and ADRs."

The functions are answering medical questions, answering exam questions, giving drug information, and supporting study or teaching. The card says "25,000 Q&A pairs," "MCQs, tutoring," "pharmacology and pharmacy domains," and "educational and research use cases." The sample question is "What is the mechanism of action of metformin?"

The clinical tasks are medical question answering and exam answering. The 25,000 pairs are the training task. The "50 unseen pharma questions" are evaluation only. The specialty is pharmacology and pharmacy. The card says "pharmacology and pharmacy domains."

The example runs on text only. `chat_template.jinja` is present. No system prompt is stated, and `use_default_system_prompt` is false. The written output is a chat reply: the card reports an average answer length of 40.3 words, and the example decodes the reply and keeps the text after `A:`. The example uses `max_new_tokens=128`, `temperature=0.7`, `top_p=0.95`, and `repetition_penalty=1.05`. `generation_config.json` sets `do_sample` true, `top_k` 64, `top_p` 0.95, and `max_length` 32768. `max_position_embeddings` and `model_max_length` are 32768.
