# maliksaad/empathLM-v2

## Sources

- https://huggingface.co/maliksaad/empathLM-v2/raw/main/README.md — current model card (same text as the 5 Oct cache)
- revision_3_experiments/hf_inventory/cache/readmes/maliksaad__empathLM-v2__2026-10-05.md — cached card, sha256 d87745e295e9b3c6adf6a3d5ec762ddae77c4cb5fb0756d4c20a0970119357a1
- https://huggingface.co/api/models/maliksaad/empathLM-v2 — file list and parameter count
- https://huggingface.co/maliksaad/empathLM-v2/raw/main/config.json — Llama config, context 8192
- https://huggingface.co/maliksaad/empathLM-v2/raw/main/generation_config.json — token ids only
- https://huggingface.co/maliksaad/empathLM-v2/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/maliksaad/empathLM-v2/raw/main/chat_template.jinja — SmolLM fallback template
- https://huggingface.co/datasets/maliksaad/empathLM-dataset — 200-row set named on this card; viewer shows rows
- https://huggingface.co/datasets/maliksaad/empathLM-dataset-v2 — 760-row set that lists this repo; viewer shows rows
- https://github.com/maliksaad/empathLM — linked from the card; returns 404
- https://huggingface.co/maliksaad — author page; spaces are named EmpathLM and EmpathLM Demo, without a repo id in the text fetched

## Record

The card says this checkpoint was "Trained on maliksaad/empathLM-dataset." That dataset card says it "contains 200 curated examples" and the Hub page shows 200 rows, so it loads. The training table says "Training Examples | ~180 (90% of 200)." The dataset card does not say whether the examples are human or synthetic. It also says "No existing HuggingFace model is trained specifically for this task." A second set, `maliksaad/empathLM-dataset-v2`, "contains 760 curated examples" and lists "Model: maliksaad/empathLM-v2" under related resources. That card uses the same sentence that no Hugging Face model is trained for the task. The v2 model card does not say it was trained on the 760-row set.

The card says the model is "fine-tuned" and does not name a loss. Fine-tuned alone is not an objective, so the objective is not stated. It does not say full, LoRA, or QLoRA, so the update scope is not stated. The table does state epochs 3, batch size 8, and learning rate 2e-5. No step count, LoRA rank, or quantization is stated. The repo contains `model.safetensors` (134,515,008 parameters, float32) and `training_args.bin`. That binary was not decoded. `https://github.com/maliksaad/empathLM` returns 404, so there is no training script to read.

The card's YAML says `base_model: HuggingFaceTB/SmolLM2-135M-Instruct`. No paper or live GitHub file names a parent. The size the card states is the base name SmolLM2-135M. License is `mit`. Language YAML is `en`.

This is a chatbot. The card says it is "trained to generate responses" and the usage example is a system-plus-user chat about failing an exam. The use claim is strong. The subtitle is "Fine-tuned for Psychologically Safe & Persuasive Emotional Support," and the card says the responses combine motivational interviewing and cognitive behavioral therapy. The warning is none. The card has no limitations section and does not say the model must not be used for therapy. "NEVER give unsolicited advice" is an instruction inside the example system prompt. The inventory parent and dataset id match the card. The match is only partly, because the usage example loads `maliksaad/empathLM` and the 760-row dataset also points at this repo. The card says it "was benchmarked against GPT-4o-mini and a Groq baseline on 20 unseen test situations" and does not print the scores.

Serving is text in, text out. The example passes a user string and calls `model.generate(inputs, max_new_tokens=200, temperature=0.7)`. `config.json` sets `max_position_embeddings` to 8192. The training table's max sequence length is 512. A chat template file is present. If the first message is not a system message, it inserts "You are a helpful AI assistant named SmolLM, trained by Hugging Face." The example system prompt begins "You are EmpathLM — an emotionally intelligent AI trained in Motivational Interviewing and Cognitive Behavioral Therapy."
