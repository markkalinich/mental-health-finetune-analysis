# ShivomH/Falcon3-1B-MentalHealth

## Sources

- https://huggingface.co/ShivomH/Falcon3-1B-MentalHealth/raw/main/README.md — current model card; byte-identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/ShivomH__Falcon3-1B-MentalHealth__2026-10-09.md — cached card (sha256 b84c4c783601dc25b8b532d040c405f97c3600d3a2883b3623b20ad036653b89)
- https://huggingface.co/api/models/ShivomH/Falcon3-1B-MentalHealth — repository file list and parameter count
- https://huggingface.co/ShivomH/Falcon3-1B-MentalHealth/raw/main/config.json — architecture, parent path, context length
- https://huggingface.co/ShivomH/Falcon3-1B-MentalHealth/raw/main/generation_config.json — generation config, no sampling fields
- https://huggingface.co/ShivomH/Falcon3-1B-MentalHealth/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/datasets/marmikpandya/mental-health — dataset page, no dataset card
- https://datasets-server.huggingface.co/size?dataset=marmikpandya/mental-health — 13,358 rows
- https://datasets-server.huggingface.co/is-valid?dataset=marmikpandya/mental-health — viewer loads

## Record

The training set named on the card is `marmikpandya/mental-health`. The card says: "It was fine-tuned on the 'marmikpandya/mental-health' dataset." The Hub dataset has no card. The viewer loads, and the datasets server counts 13,358 rows in one train split. No source states the language or whether the rows are human, synthetic, or mixed.

The card does not name a loss. It says the checkpoint is a LoRA adapter that was merged into the base: "This is a LoRA adapter for the Falcon3-1B-Instruct LLM which has been merged with the respective base model." The training table lists LoRA rank 16 and "Quantization | 8-Bit", so this is LoRA on an 8-bit base. It also lists learning rate 2e-4, batch size 2, and 3 epochs. LoRA alpha and step count are not in the table. The repository has `model.safetensors` and no `adapter_config.json`.

The card names the parent `tiiuae/Falcon3-1B-Instruct`. `config.json` agrees: `"_name_or_path": "tiiuae/Falcon3-1B-Instruct"`. No paper or GitHub repository names this checkpoint.

The card presents a conversation model: "assist in mental health conversations, offering advice, guidance, and support for individuals dealing with issues like stress, anxiety, and depression." That is a support conversation, so the use claim is Strong and the output type is Chatbot. The warning is a disclaimer, not a ban: "This model is not a licensed mental health professional." The same section says the intended use is "general emotional support, not diagnosis or treatment."

The card's example reads a typed line (`user_input = input("\nYou: ")`) and tokenizes that text. No image or audio. The example uses temperature 0.5, top_p 0.85, max_new_tokens 100, repetition_penalty 1.2, and do_sample true. `generation_config.json` does not set those. `config.json` sets `max_position_embeddings` to 8192. A chat template is present in `tokenizer_config.json`. The mental-health system instruction is only in the card example. The Hub API reports 1,669,408,768 parameters. The license on the card is apache-2.0. The card reports no evaluation.
