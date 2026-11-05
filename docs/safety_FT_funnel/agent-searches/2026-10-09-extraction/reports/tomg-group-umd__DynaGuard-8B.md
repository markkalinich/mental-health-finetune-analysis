# tomg-group-umd/DynaGuard-8B

## Sources

- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/README.md — current model card; same bytes as the cached card
- https://huggingface.co/api/models/tomg-group-umd/DynaGuard-8B — repository file list
- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/config.json — architecture and context length
- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/tomg-group-umd/DynaGuard-8B/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/abs/2509.02563 — abstract page
- https://arxiv.org/html/2509.02563 — HTML full text of the paper that names DynaGuard-8B
- https://proceedings.iclr.cc/paper_files/paper/2026/file/8d2aad53fa148791ffd004a7c9cce5ad-Paper-Conference.pdf — ICLR 2026 proceedings copy; listed, not read (PDF)
- https://github.com/montehoover/DynaGuard — evaluation code; the README runs this repository by id; no training script
- https://github.com/taruschirag/DynaGuard — project-page repository named in the card YAML
- https://taruschirag.github.io/DynaGuard/ — project page
- https://huggingface.co/collections/tomg-group-umd/dynaguard-68af4d916ae81d06ef774523 — collection linked from the paper
- https://huggingface.co/spaces/tomg-group-umd/DynaGuard — demo linked from the Hugging Face paper page
- https://huggingface.co/datasets/tomg-group-umd/DynaBench — dataset id on the model card; redirects to montehoover/DynaBench
- https://huggingface.co/datasets/montehoover/DynaBench — dataset card and files
- https://huggingface.co/datasets/allenai/wildguardmix — WildGuard dataset card; gated
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails dataset card
- https://huggingface.co/datasets/lmsys/toxic-chat — ToxicChat dataset card
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0 dataset card

## Record

The training mix is DynaBench plus four safety datasets. The card says: "Fine-tuned on a mixture of the DynaBench dataset and several safety benchmarks (WildGuard, BeaverTails, ToxicChat, Aegis 2.0)." The paper says the first stage uses "a mixture of 40,000 samples from DynaBench and 40,000 samples from the four safety datasets." The Hub train split `DynaBenchTrain` has 61,496 rows. The paper describes that split as "a 61.5k sample train set" built with "a hybrid approach of hand-written and automated methods." The id `tomg-group-umd/DynaBench` redirects to `montehoover/DynaBench`. It is public and the datasets server returns rows. WildGuard is `allenai/wildguardmix` (86,759 train examples on the card; synthetic, in-the-wild, and annotator-written). The datasets server returns 401 until the gate is accepted, so it does not load anonymously. BeaverTails is `PKU-Alignment/BeaverTails`. The datasets server reports 300,567 rows in `330k_train` and 33,396 in `330k_test`. The card calls these "human-labeled" question-answer pairs. ToxicChat is `lmsys/toxic-chat`. The current `toxicchat0124` config has 5,082 train rows and 5,083 test rows, matching the card's 10,165 user prompts from the Vicuna demo, with model outputs. Aegis 2.0 is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`: "33,416 annotated interactions between humans and LLMs." The paper does not say how many rows of each of the four safety sets went into the 40,000. The project page calls a 60K dialogue set "Compliance" and does not give a Hub id. A different Hub organization, `DynaGuard`, publishes code models with similar names. Those repositories are not this checkpoint.

The checkpoint was trained with supervised fine-tuning and then GRPO. The card says: "The model was trained using Supervised Fine-Tuning (SFT) for one epoch, followed by GRPO." The paper says the same recipe for the Qwen3 instruction models, with SFT for 1 epoch and then GRPO on 11,000 samples. Appendix A.9 marks the 8B learning rates in bold as 1e-5 for SFT and 1e-7 for GRPO, and the batch sizes as 128 for SFT and 48 for GRPO. No sentence states full-weight updates, LoRA, or QLoRA. The repository has no `adapter_config.json`. The GitHub repository contains evaluation scripts only. Its README names this repository: `python eval.py --model tomg-group-umd/DynaGuard-8B`.

The parent is Qwen/Qwen3-8B. The card says "Base Model: Qwen3-8B." The paper says: "We use the Qwen3 family of instruction models (Yang et al., 2025) as the models for fine-tuning our guardian models."

This is a policy classifier, not a support chatbot. The card says the series is "designed to evaluate text against user-defined, natural language policies" and that fast inference "Provides a direct PASS or FAIL classification." The card mentions self-harm only as an example of a fixed category used by other guardian models. It has no therapy, counseling, or medical-use warning. The stated size is 8B. The card language tag is English. The card and paper Table 3 agree: DynaBench F1 72.5 and safety average 79.6 without chain-of-thought, and 73.1 and 81.1 with it. The paper also lists all-tasks averages of 78.4 and 79.7.

The card runs the model on a policy string and a dialogue string. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. The card example uses temperature 0.1 and `max_new_tokens` 256 or 100. `config.json` sets `max_position_embeddings` to 40960. A Qwen3 chat template is in `tokenizer_config.json`. The card example does not use it. No system prompt is stored for this checkpoint. License is apache-2.0.
