# flowxai/scam-guard-qwen17b

## Sources

- https://huggingface.co/flowxai/scam-guard-qwen17b/raw/main/README.md — current model card
- revision_3_experiments/hf_inventory/cache/readmes/flowxai__scam-guard-qwen17b__2026-10-09.md — cached card, sha256 72500e8fbb98784277c0fd4b1dcc1ae8fa88db7230374929e358b2b1d8252fde
- https://huggingface.co/api/models/flowxai/scam-guard-qwen17b — file list, parameter count, chat template
- https://huggingface.co/flowxai/scam-guard-qwen17b/raw/main/config.json — architecture and context length
- https://huggingface.co/flowxai/scam-guard-qwen17b/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/flowxai/scam-guard-qwen17b/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/flowxai/scam-guard-qwen17b/raw/main/inference_contract/prompt_scamguard_sys_v1.txt — frozen system prompt
- https://www.flowx.ai/models — vendor page repeating the parent and LoRA claim
- https://huggingface.co/datasets/flowxai/scamguardbench — named benchmark dataset card
- https://huggingface.co/api/datasets/flowxai/scamguardbench — benchmark files and load metadata
- https://huggingface.co/datasets/ucirvine/sms_spam — UCI SMS Spam Collection on the Hub
- https://huggingface.co/api/datasets/ucirvine/sms_spam — 5,574-row load metadata
- https://huggingface.co/datasets/SetFit/enron_spam — Enron spam/ham dataset card
- https://huggingface.co/api/datasets/SetFit/enron_spam — Enron files and load metadata
- https://huggingface.co/datasets/zefang-liu/phishing-email-dataset — phishing email dataset card
- https://huggingface.co/api/datasets/zefang-liu/phishing-email-dataset — 18,650-row load metadata

No arXiv paper and no GitHub repository name this checkpoint. A search for the model name returned Qwen3Guard, which is a different model, and flowx-ai/openner, which is a different project.

## Record

The card names five data sources. The training text is a relabeled public seed plus a synthetic layer. The seed sentence is: "Public seed layer (relabeled): UCI SMS Spam Collection (CC BY 4.0), enron_ham (SetFit/enron_spam ham slice; no explicit license → reference/research-use), phishing_email (zefang-liu; LGPL-3.0)." Those Hub datasets are `ucirvine/sms_spam` (5,574 English SMS, loads), `SetFit/enron_spam` (loads; the card does not say how many ham rows were kept), and `zefang-liu/phishing-email-dataset` (18,650 rows, English, loads). The synthetic layer "generated from specs (tactic × channel × language × register)" has no Hub id and no example count. `flowxai/scamguardbench` is the card's YAML dataset and a 753-row English/Romanian benchmark that loads. The card also says "Train ∩ ScamGuardBench = ∅" and that the bench "is built from the same synthetic generator the model trained on (held-out split)."

The training objective is supervised fine-tuning with LoRA. The card says: "CUDA full-budget 3-epoch LoRA (`training/train_cuda.py`, transformers + PEFT + trl `SFTTrainer`), from `Qwen/Qwen3-1.7B`. LoRA rank 16 / alpha 32 / dropout 0.05, all-linear modules, adamw, cosine 2e-5→2e-6 with 60-step warmup, effective batch 4, seq 1280, bf16." That is 3 epochs, learning rate 2e-5, effective batch 4, and bf16 rather than a quantized base. The step count is not stated; 60 is the warmup. The repository ships full BF16 weights (1,720,574,976 parameters) and no `adapter_config.json`. The card does not say whether the LoRA was merged.

The parent is `Qwen/Qwen3-1.7B`. The card says the checkpoint is "from `Qwen/Qwen3-1.7B`", and https://www.flowx.ai/models says "Qwen3-1.7B (LoRA)". `config.json` is `Qwen3ForCausalLM`. The card calls the size "1.7B".

This is a message classifier, not a conversation model. The card says: "Given one message, scam-guard returns a 3-level verdict." The use claim is Absent: "An on-device scam & fraud message detector for SMS, email, and chat text (English + Romanian)." There is no mental-health claim. The warning is Unrelated limitations only: "Not a guarantee. A verdict is a signal, not proof." Languages are "EN and RO at v1." License is Apache-2.0.

Serving is text only: "Text only at v1: no image/OCR, no audio, no attachment parsing, no email-header/routing analysis." A Qwen3 chat template is present in `chat_template.jinja`. The system prompt is the frozen file `prompt_scamguard_sys_v1.txt`, which begins "You are an on-device scam and fraud detector." `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. The card's own examples set temperature 0, and the MLX example sets `max_tokens` 256. `max_position_embeddings` is 40960. On the 120-item bench the card reports verdict macro-F1 0.975 and legit-confusable false-positive rate 0.000. On 20 fresh messages it reports 19/20 correct.

Inventory methods `lora|sft` and parent `Qwen/Qwen3-1.7B` match. The inventory dataset matches the card YAML, and the training section says that benchmark is held out. Match: partly.
