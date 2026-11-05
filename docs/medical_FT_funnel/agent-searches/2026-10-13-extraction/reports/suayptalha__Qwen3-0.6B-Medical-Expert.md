# suayptalha/Qwen3-0.6B-Medical-Expert

## Sources

- https://huggingface.co/suayptalha/Qwen3-0.6B-Medical-Expert/raw/main/README.md — current model card; byte-identical to the 10 Oct cache (`be9db48f7c390a05d5dd717afafb0a179b9ab4ad0a3b766b810a3c38bd31056f`)
- https://huggingface.co/api/models/suayptalha/Qwen3-0.6B-Medical-Expert — file list, 596,049,920 parameters, base-model tag
- https://huggingface.co/suayptalha/Qwen3-0.6B-Medical-Expert/raw/main/config.json — Qwen3ForCausalLM, context 40960, bf16
- https://huggingface.co/suayptalha/Qwen3-0.6B-Medical-Expert/raw/main/generation_config.json — temperature 0.6, top_p 0.95, top_k 20, do_sample true
- https://huggingface.co/suayptalha/Qwen3-0.6B-Medical-Expert/raw/main/tokenizer_config.json — Qwen3 chat template, no fixed system prompt
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — training dataset card
- https://datasets-server.huggingface.co/size?dataset=FreedomIntelligence/medical-o1-reasoning-SFT — 90,120 rows across four configs; the viewer loads
- https://arxiv.org/html/2505.09388 — Qwen3 Technical Report HTML; no mention of this repo id
- https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 paper cited by the dataset card; not read
- https://github.com/SahilChachra/LLM-Merging — later merge experiment that names this repo as its medical expert
- https://featherless.ai/models/suayptalha/Qwen3-0.6B-Medical-Expert — hosted inference page

## Record

The card names one training set, `FreedomIntelligence/medical-o1-reasoning-SFT`: "Training was conducted on the `FreedomIntelligence/medical-o1-reasoning-SFT` dataset." The dataset card says it "is constructed using GPT-4o" and lists English and Chinese configs. The Hub viewer loads. The size endpoint reports 90,120 rows in total (English 19,704, English mix 24,887, Chinese 20,171, Chinese mix 25,358). The model card does not say which config or how many rows were used. The dataset card cites HuatuoGPT-o1 (arXiv 2412.18925). That paper was not read.

The objective is supervised fine-tuning. "Fine-tuning was conducted using the Hugging Face TRL library with the Supervised Fine-Tuning (SFT) approach." The update is full: "All model layers were fully updated (`full_finetuning=True`)." The base was loaded "in bf16 precision," so it was not a quantized-base LoRA run. No rank, epochs, steps, learning rate, or batch size is stated. The repo has `model.safetensors` and no `adapter_config.json`.

The parent is `Qwen/Qwen3-0.6B`. The card says the project "performs full fine-tuning on the **Qwen3-0.6B** language model," and the YAML `base_model` is `Qwen/Qwen3-0.6B`. A GitHub merge repo names the same parent and this repo as the medical expert. The Qwen3 Technical Report does not print this repo id.

The use claim is strong. The card says the model was trained to "generate reasoned diagnoses or treatment suggestions." There is no warning sentence about diagnosis, treatment, or clinical use. The purpose is stated: it is "useful in educational and assistive medical AI contexts." No audience (patient, clinician, student, researcher) is named.

The card claims these functions: answering medical instructions, step-by-step clinical reasoning, reasoned diagnoses, treatment suggestions, decision-making, and educational use. The quotes are "interpret medical instructions and generate step-by-step clinical reasoning," "generate reasoned diagnoses or treatment suggestions," "medical reasoning and decision-making tasks," and "educational and assistive medical AI contexts."

The clinical work named is medical questions, diagnosis, treatment suggestions, and clinical reasoning, with no specialty narrower than medical or clinical. Output is reasoning prose, not a letter, label, or JSON object. The card does not present a chat persona, so the output type is a non-chat text tool.

Serving is text. The card talks about "instructions or questions" and written reasoning responses. `config.json` is `Qwen3ForCausalLM` with `max_position_embeddings` 40960. A chat template is in `tokenizer_config.json` and does not set a system prompt. `generation_config.json` sets `temperature` 0.6, `top_p` 0.95, `top_k` 20, and `do_sample` true. No evaluation numbers are reported. The license is Apache 2.0.

The inventory row matches: full fine-tune and SFT, dataset `FreedomIntelligence/medical-o1-reasoning-SFT`, parent `Qwen/Qwen3-0.6B`.
