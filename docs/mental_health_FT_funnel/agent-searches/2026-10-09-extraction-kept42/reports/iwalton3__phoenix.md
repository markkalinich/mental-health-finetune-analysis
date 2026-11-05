# iwalton3/phoenix

## Sources

https://huggingface.co/iwalton3/phoenix/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/iwalton3__phoenix__2026-10-09.md — cached card, sha256 f5deafc079ace4b33157401bc8219c9aaab295e2124be04cc48f780c28b07f40
https://huggingface.co/api/models/iwalton3/phoenix — file list and safetensors parameter total
https://huggingface.co/iwalton3/phoenix/raw/main/config.json — architecture and context length
https://huggingface.co/iwalton3/phoenix/raw/main/generation_config.json — sampling defaults
https://huggingface.co/iwalton3/phoenix/raw/main/tokenizer_config.json — no chat_template key; use_default_system_prompt false
https://huggingface.co/iwalton3/phoenix/raw/main/chat_template.jinja — chat template file
https://huggingface.co/iwalton3/phoenix/raw/main/model.safetensors.index.json — parameter total 4300079472
https://huggingface.co/datasets/iwalton3/sycofact-training-data/raw/main/README.md — dataset card
https://huggingface.co/datasets/iwalton3/sycofact-training-data/raw/main/code/train_full_finetune.py — script that trains SycoFact, not this checkpoint
https://huggingface.co/iwalton3/sycofact/raw/main/README.md — sibling evaluator card
https://datasets-server.huggingface.co/size?dataset=iwalton3/sycofact-training-data — row counts
https://datasets-server.huggingface.co/rows?dataset=iwalton3/sycofact-training-data&config=phoenix&split=train&offset=0&length=1 — one Phoenix training row
https://ollama.com/izzie/phoenix — text chat example linked from the card
https://featherless.ai/models/iwalton3/phoenix — hosted demo
https://www.reddit.com/r/LocalLLaMA/comments/1rz1igl/phoenix_4b_an_honest_mental_health_companion/ — post that links this repo and repeats the card
https://huggingface.co/google/gemma-3-4b-it/raw/main/README.md — parent card; request returned 401

## Record

The card names iwalton3/sycofact-training-data and says to see the Phoenix training data for details. That dataset has a config named phoenix. The dataset card says phoenix_train.jsonl has 5,970 records and "This data was synthetically generated using steered Gemma 3 27B for assistant turns and Gemma 3 27B abliterated for user turns." The Hub viewer loads that split. Language on the dataset card is English. A loaded row uses the same system prompt as this model card. The rest of the dataset is SycoFact evaluator data: 37,898 train rows and 4,210 validation rows.

No source states the loss or the update scope for this checkpoint. The card says only "This is a custom fine-tune of Gemma3 4B." The dataset's training section is titled "Reproducing SycoFact." It says SycoFact was fully finetuned for 3 epochs at learning rate 5e-6, batch size 1 with 8 gradient-accumulation steps, in bf16, on both the evaluator files and the Phoenix conversations. The script `train_full_finetune.py` does that combined run and writes `output_4b_full`. Those settings are about iwalton3/sycofact. They are not a statement of how iwalton3/phoenix was trained. This repository has full BF16 weights and a Q8 GGUF file, and no adapter_config.json. LoRA rank, alpha, epochs, steps, learning rate, and batch size for this checkpoint are not stated.

The card YAML names the parent google/gemma-3-4b-it. The prose says "Gemma3 4B." No outside source names this checkpoint's parent. The card says the model is Gemma3 4B and "4.1GB." The safetensors index lists 4,300,079,472 parameters. The license is gemma.

The card calls it "an honest mental health companion" and "a compassionate listener." That is a chatbot. The use claim is moderate. It also says "Not a therapy bot." The warning is a disclaimer: "This model is not a substitute for professional mental health services. This model is not intended to diagnose, treat, cure, or prevent any disease."

The system prompt on the card is: "You are the voice of honest reason and compassion for someone who has lost their way in life. Your goal: Guide them to the answers through application of targeted questions. It's very important to be even-handed and never tell the user what to believe. Simply challenge assumptions they may have made in their statements, but do it in a compassionate and caring way. Don't ever be sycophantic or prescriptive." The Ollama page linked from the card sends a text user message, "Hello!". generation_config.json sets do_sample true, top_k 64, and top_p 0.95. text_config.max_position_embeddings is 131072. A chat template is in chat_template.jinja. The card does not report an evaluation score. The benchmark numbers on the SycoFact card are for that other model.
