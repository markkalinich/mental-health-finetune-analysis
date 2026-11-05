# ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit

## Sources

https://huggingface.co/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit — file list, parameter count, chat template
https://huggingface.co/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit/raw/main/config.json — context length and dtype
https://huggingface.co/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit/raw/main/generation_config.json — sampling settings
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — training dataset card
https://arxiv.org/abs/2412.18925 — dataset paper; it does not name this repository
https://arxiv.org/abs/2503.19786 — Gemma 3 technical report found by search; it does not name this repository
https://www.linkedin.com/posts/arindamsingh_llm-healthcareai-opensource-activity-7349073683618889730-1fRI — author's post repeating the training settings
https://featherless.ai/models/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit — hosted inference page
https://huggingface.co/datasets/qiaojin/PubMedQA — Hub copy of PubMedQA, the named evaluation set

## Record

The training set is FreedomIntelligence/medical-o1-reasoning-SFT. The card says "FreedomIntelligence/medical-o1-reasoning-SFT (19 704 rows)" and "Question + Complex_CoT → Response". That row count is the English split. The dataset loads. The dataset card says it "is constructed using GPT-4o", so the text is synthetic. PubMedQA is an evaluation set on this card, not a training set. The Hub copy is qiaojin/PubMedQA.

The objective is supervised fine-tuning. The card says "Supervised CoT SFT → LoRA merge & quantize". The update is LoRA, then merged. It says "r = 8, α = 32, dropout = 0.05" and "LoRA rank 8 adapters merged" and "Merged weights – no adapter step required". The repository has `model.safetensors` and no adapter file. Training is "3 epochs", "LR = 2 e-5 cosine", "batch = 1 × 4 grad-accum". The library line is "Unsloth 0.6 + 8-bit paged_adamw". That names an 8-bit optimizer. It does not say the base weights were quantized. The recipe's word "quantize" has no quantized file next to it. The card says both "a single A100" and "2 × T4-16 GB". The author's LinkedIn post says 2× T4, LoRA r = 8, merged fp16, and about 19k pairs.

The YAML `base_model` and the line "Finetuned from model : unsloth/gemma-3-1b-it" name unsloth/gemma-3-1b-it. The snapshot table says "Base model | google/gemma-3-1b-it". Those two parents are both on the card. The card says "Parameter count | 1 B (full)". The Hub file count is 999885952 parameters, a mix of BF16 and F16. `config.json` says `torch_dtype` float16.

The use claim is moderate. The intended-use table says "Medical education, PubMed triage, coding suggestions (ICD, SNOMED), research ideation" and puts "Automated diagnosis, emergency triage, any decision requiring regulatory clearance" out of scope. The warning is a disclaimer: "Not a medical device – always keep a human in the loop." The sample also says "does not constitute medical advice" and "I am an AI Chatbot and not a medical professional." The sample answer about type 2 diabetes includes metformin and other treatment text, and the same answer says it is not medical advice. The license is Apache-2.0.

The purpose is that intended-use list. The audiences named there are people in medical education, and people doing research ideation.

The functions are chain-of-thought medical answers, medical education, PubMed triage, and ICD/SNOMED coding suggestions. The output is a chat reply that walks through a rationale. The sample question is "What is type 2 diabetes?"

The training task is medical question answering in the Question, Complex_CoT, Response format. Coding suggestions are a claimed use. PubMedQA is evaluation only: QA-F1 57% for this model and 46% for the base, "100-Q samples, greedy decoding". The card says the scripts are in `eval/`. That folder is not in the repository. The domain line is "Clinical & biomedical reasoning", with no single specialty. The card also says "English-centric dataset; limited pediatrics / rare diseases coverage."

The example is text. A chat template is present. It has no default system string. It can emit an image token if a message contains an image, and this config is the text Gemma 3 architecture. `max_position_embeddings` is 32768. `generation_config.json` sets `do_sample` true, `top_k` 64, `top_p` 0.95, and `max_length` 32768. It does not set temperature.
