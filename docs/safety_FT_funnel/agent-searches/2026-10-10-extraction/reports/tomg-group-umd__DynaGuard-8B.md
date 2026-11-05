# tomg-group-umd/DynaGuard-8B

## Sources

- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-8B__2026-10-09.md — cached card
- https://huggingface.co/api/models/tomg-group-umd/DynaGuard-8B — repository file list and safetensors parameter count
- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/config.json — architecture and max position embeddings
- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/abs/2509.02563 — paper abstract
- https://arxiv.org/html/2509.02563 — paper HTML full text
- https://github.com/montehoover/DynaGuard — evaluation code; prints this repo id
- https://github.com/taruschirag/DynaGuard — project-page repository
- https://taruschirag.github.io/DynaGuard/ — project page
- https://huggingface.co/spaces/tomg-group-umd/DynaGuard — Hub demo space
- https://huggingface.co/collections/tomg-group-umd/dynaguard-68af4d916ae81d06ef774523 — model and data collection
- https://huggingface.co/datasets/tomg-group-umd/DynaBench — DynaBench alias; resolves to montehoover/DynaBench
- https://huggingface.co/datasets/montehoover/DynaBench — DynaBench dataset card
- https://huggingface.co/datasets/allenai/wildguardmix — WildGuard dataset card; gated
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails dataset card
- https://huggingface.co/datasets/lmsys/toxic-chat — ToxicChat dataset card
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0 dataset card

## Record

Training data is a mixture. The card says the model was "Fine-tuned on a mixture of the DynaBench dataset and several safety benchmarks (WildGuard, BeaverTails, ToxicChat, Aegis 2.0)." The paper says the SFT stage uses "40,000 samples from DynaBench and 40,000 samples from the four safety datasets," and that DynaBench was built with "a hybrid approach of hand-written and automated methods to construct a 61.5k sample train set." The Hub train split `DynaBenchTrain` has 61,496 rows and returns a row. WildGuard is `allenai/wildguardmix` (86,759 train examples; synthetic, in-the-wild, and annotator-written) and does not load without accepting the gate. BeaverTails is human-labeled QA pairs (`PKU-Alignment/BeaverTails`; 300,567 train and 33,396 test rows in the 330k splits) and loads. ToxicChat is `lmsys/toxic-chat` (10,165 rows in `toxicchat0124`; user prompts plus model outputs) and loads. Aegis 2.0 is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` (33,416 annotated human–LLM interactions, including synthetic refusals) and loads.

The method is supervised fine-tuning for one epoch, then GRPO. The card says "The model was trained using Supervised Fine-Tuning (SFT) for one epoch, followed by GRPO." The paper uses VERL for both stages. For the 8B model the bold SFT choices are learning rate 1e-5 and batch size 128; the bold GRPO choices are learning rate 1e-7 and batch size 48, on 11,000 samples. No sentence says whether the update was full, LoRA, or QLoRA. The repository has four safetensor shards and no adapter file.

The parent is Qwen/Qwen3-8B. The card says "Base Model: Qwen3-8B." The paper says "We use the Qwen3 family of instruction models (Yang et al., 2025) as the models for fine-tuning our guardian models" and compares against Qwen3-8B. The card calls the series 8B. The Hub file list reports 8,190,735,360 BF16 parameters.

The card presents a classifier, not a chatbot. It "evaluate[s] text against user-defined, natural language policies" and can "enforce bespoke, application-specific rules" beyond "a fixed set of harms (e.g., violence or self-harm)." The usage example feeds a written policy plus a User/Agent dialogue. Fast mode "Provides a direct PASS or FAIL classification." CoT mode "Generates a reasoning trace before giving the final classification." The card table gives DynaGuard-8B a DynaBench F1 of 72.5 (73.1 with CoT) and a safety-task average F1 of 79.6 (81.1 with CoT). License is apache-2.0. Language front matter is `en`.

Serving is text only: "The input should contain the policy and the dialogue to be evaluated." `tokenizer_config.json` has a Qwen3 chat template. `generation_config.json` sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. The card example instead uses temperature 0.1 and max_new_tokens 256 or 100. `config.json` sets max_position_embeddings to 40960. The paper says evaluation uses a system prompt printed in appendix A.7, but that prompt text is not in the HTML. The GitHub README evaluates this exact repo id and does not contain a trainer config.
