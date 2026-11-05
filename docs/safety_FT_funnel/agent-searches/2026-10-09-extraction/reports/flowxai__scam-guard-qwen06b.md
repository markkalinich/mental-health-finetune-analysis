# flowxai/scam-guard-qwen06b

## Sources

- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/flowxai__scam-guard-qwen06b__2026-10-09.md — cached card, sha256 1044c33c36973f5389f6c8bf40077948c4cae59693900e472941b8d4f4a6dc9b
- https://huggingface.co/api/models/flowxai/scam-guard-qwen06b — repository file list
- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/config.json — Qwen3 causal LM, context 40960
- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/chat_template.jinja — Qwen3 chat template
- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/inference_contract/prompt_scamguard_sys_v1.txt — frozen system prompt
- https://huggingface.co/flowxai/scam-guard-qwen06b/raw/main/inference_contract/INFERENCE.md — inference contract for this checkpoint
- https://huggingface.co/datasets/flowxai/scamguardbench/raw/main/README.md — benchmark card; held-out test items
- https://huggingface.co/datasets/ucirvine/sms_spam — Hub copy of the UCI SMS Spam Collection
- https://huggingface.co/datasets/SetFit/enron_spam — Enron spam/ham dataset named on the card
- https://huggingface.co/datasets/zefang-liu/phishing-email-dataset — phishing email set by the author the card names
- https://www.flowx.ai/models — project page; names the base as Qwen3-0.6B (LoRA)
- Searches for an arXiv paper and for `training/train_cuda.py` on GitHub did not find a paper or this project's repository

## Record

The inventory dataset `flowxai/scamguardbench` is the held-out benchmark, not the training split. The benchmark card says: "Contamination: every v0.2 item is from the held-out TEST split, disjoint from any scam-guard training data." It loads. The card's own unique count is 753. The Hub viewer sums the overlapping subset files to 1,099 rows. The model card says: "Train ∩ ScamGuardBench = ∅".

The training mixture is two layers. The card says: "Public seed layer (relabeled): UCI SMS Spam Collection (CC BY 4.0), enron_ham (SetFit/enron_spam ham slice; no explicit license → reference/research-use), phishing_email (zefang-liu; LGPL-3.0)." Those match `ucirvine/sms_spam` (5,574 English messages), `SetFit/enron_spam` (the card uses the ham slice; the published set is larger and the slice size is not stated), and `zefang-liu/phishing-email-dataset` (18,650 English emails, LGPL-3.0). All three pages load. The card also says: "Synthetic layer: generated from specs (tactic × channel × language × register)." That layer has no Hub id. The SFT train-set size is not stated. The card only gives shares: at least 45% legitimate, Romanian at least 35%, and `suspicious` about 14.5% of the SFT train set.

The shipped run is supervised fine-tuning with LoRA. The card says: "CUDA full-budget 3-epoch LoRA (`training/train_cuda.py`, transformers + PEFT + trl `SFTTrainer`), from `Qwen/Qwen3-0.6B`." It also says "LoRA rank 16 / alpha 32 / dropout 0.05" and "adamw, cosine 2e-5→2e-6 with 60-step warmup, effective batch 4, seq 1280, bf16." That is 3 epochs, learning rate starting at 2e-5 and decaying to 2e-6, and effective batch size 4. Total training steps are not stated. The 60 steps are warmup. The base was BF16, not a quantized base. The repository has a full BF16 `model.safetensors` (596,049,920 parameters) and no `adapter_config.json`. The card does not say the LoRA was merged. GGUF and MLX int4 files are serving copies. `training/train_cuda.py` is not in the repository, and no GitHub repository containing it was found.

The card names the parent `Qwen/Qwen3-0.6B` and the size 0.6B. The project page says "Base Qwen3-0.6B (LoRA)." No paper was found.

This is a scam-message classifier, not a support chatbot. The card says: "Given one message, scam-guard returns a 3-level verdict." Use claim is absent. The limitation is about fraud triage: "Not a replacement for a bank's fraud line, a national anti-fraud service, or human judgment." On the 120-message bench slice the card reports verdict macro-F1 0.926 and legit-confusable false-positive rate 0.000. On 20 fresh messages it reports 18/20 correct and macro-F1 0.614. The card says the bench score has a home-field advantage.

The card says: "Text only at v1: no image/OCR, no audio, no attachment parsing." The frozen system prompt begins: "You are an on-device scam and fraud detector." `generation_config.json` sets temperature 0.6, top_k 20, and top_p 0.95. The card's own examples set temperature to 0, and the MLX example sets `max_tokens` to 256. `config.json` sets `max_position_embeddings` to 40960. A chat template file is present. License is Apache-2.0. The inventory matches the method and the parent. It does not match the training data: the named Hub dataset is the held-out benchmark.
