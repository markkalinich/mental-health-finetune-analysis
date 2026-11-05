# tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep

## Sources

- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/tzchen07__rai-n3-nano-4b-safety-l7-fullfix-15ep__2026-10-05.md — cached card
- https://huggingface.co/api/models/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep — file list and safetensors count
- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep/raw/main/config.json — Nemotron-H config, context length
- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep/raw/main/generation_config.json — no sampling values
- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep/raw/main/tokenizer_config.json — no chat template key
- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep/raw/main/chat_template.jinja — chat template file
- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep/raw/main/lora_adapter/adapter_config.json — DoRA adapter config
- https://huggingface.co/datasets/tzchen07/rai-safety-campaign-2026 — campaign notes, scripts, and some jsonl files
- https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-lora-r64-ipfix/raw/main/prompts/v3_1_VerdictReason.jinja — policy template the card tells users to render
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0
- https://huggingface.co/datasets/Anthropic/hh-rlhf — HH-RLHF
- https://huggingface.co/datasets/databricks/databricks-dolly-15k — Dolly 15K
- https://huggingface.co/datasets/OpenAssistant/oasst1 — OASST1

## Record

The card's training table is 19,576 rows in 11 files. The largest file is "v1.6.0_train.jsonl | 9,657 | Base safety classification (Aegis 2.0, HH-RLHF, Dolly, OASST1)." Three of the smaller files are in `tzchen07/rai-safety-campaign-2026`: v1_6g_fpfix.jsonl (300 rows on the card; the campaign page says about 680), v1_6h_ip_fix.jsonl (100; campaign says about 250), and v1_6i_edu_style_fix.jsonl (170; campaign says about 120). That dataset's viewer is off, so those files do not load as a Hub dataset. Aegis 2.0 (`nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, 33,416 rows) loads. HH-RLHF (`Anthropic/hh-rlhf`, 169,352 rows) loads. Dolly 15K (`databricks/databricks-dolly-15k`, 15,011 rows) loads. OASST1 (`OpenAssistant/oasst1`) loads; the card says 161,443 messages in 35 languages, and the Hub split has 88,838 rows. The other seven jsonl names are only on this model card.

The method for this checkpoint is supervised fine-tuning with DoRA. The card says "Single-stage DoRA SFT, 1.5 epochs" and "LoRA: DoRA (Weight-Decomposed), r=35, alpha=70, all target modules." Learning rate is 1e-4. "Batch: 4 per device, gradient accumulation 16 (effective batch 64)." "Precision: bf16." `adapter_config.json` sets `use_dora` true, `r` 35, and `lora_alpha` 70. The title says the weights are merged, and the root has full safetensors; the adapter is also stored under `lora_adapter/`. The campaign table's L7 row is the same recipe: "DoRA r=35, alpha=70, lr=1e-4, 1.5ep." DPO and RLHF files in that campaign belong to other experiments. No sentence gives a step count.

The parent is `nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16`. The card says it has "3.97B params, hybrid Mamba-2 + Transformer." The Hub count is 3,973,556,832 parameters. No source states a language.

The card calls it an "enterprise content safety classifier" over "13 risk categories." The linked VerdictReason template says "Determine whether a user query should be filtered for unsafe content" and names Violence/Harassment, Hate/Discrimination, Misinformation, Sexual Content, Illegal Activity, Self-harm, Jailbreak/Prompt Injection, Intellectual Property, PII, Politics, Impersonation, Specialist Advice, and High-risk decisions. The input in the example is a system policy plus one user query. The output is a category line such as "Verdict: none" or "Verdict: Violence/Harassment." If generation is not stopped, a Reason paragraph follows; the card says that Reason text is hallucinated and tells users to stop at "Reason:". VerdictReason on v200 is precision 1.0000 and recall 0.2250. License is apache-2.0.

Serving is text. `chat_template.jinja` is present. `generation_config.json` does not set temperature. The card example uses temperature 0.0 and max_tokens 50. `config.json` sets max_position_embeddings to 262144. The vLLM snippet uses `--max-model-len 8192`. The quick-start system string is the placeholder "<v3.1 safety policy>". Searches found no paper and no GitHub repository for this repo id.
