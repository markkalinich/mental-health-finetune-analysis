# Mouhib007/DeepSeek-r1-Medical-Mini

## Sources

- https://huggingface.co/Mouhib007/DeepSeek-r1-Medical-Mini/raw/main/README.md — current model card; identical to the 10 October 2026 cache
- https://huggingface.co/api/models/Mouhib007/DeepSeek-r1-Medical-Mini — repository file list
- https://huggingface.co/Mouhib007/DeepSeek-r1-Medical-Mini/raw/main/config.json — Llama architecture, float16, context 131072
- https://huggingface.co/Mouhib007/DeepSeek-r1-Medical-Mini/raw/main/generation_config.json — temperature 0.6, top_p 0.95
- https://huggingface.co/Mouhib007/DeepSeek-r1-Medical-Mini/raw/main/tokenizer_config.json — DeepSeek chat template
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — training dataset card
- https://arxiv.org/abs/2412.18925 — dataset paper abstract link; does not name this repository
- https://arxiv.org/abs/2604.17988 — search hit; abstract page does not print this repository id; HTML full text returned 404
- https://www.kaggle.com/code/mohamednaffeti007/fine-tune-deepseek-model — demo link on the card; the page did not include the notebook source
- https://github.com/FreedomIntelligence/HuatuoGPT-o1 — GitHub linked from the dataset card, not from this model card

## Record

The only training set the card names is `FreedomIntelligence/medical-o1-reasoning-SFT`. It loads. The viewer has 90,120 rows across English, English-mix, Chinese, and Chinese-mix configs. The dataset card says: “This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier.” The model card does not say which config was used. The card’s language tag is English.

The objective is supervised fine-tuning. The card’s tags include `sft`, and the text says the model “is a fine-tuned version” of the parent “with LoRA (Low-Rank Adaptation).” Rank 16, alpha 16, dropout 0, target modules q, k, v, o, gate, up, and down. Epochs 1, max steps 60, learning rate 2e-4, batch size 2 per device, gradient accumulation 4, AdamW 8-bit, mixed precision fp16/bf16. The card does not say the base was quantized, and it does not say the adapter was merged. The repository holds four `pytorch_model.bin` shards and no `adapter_config.json`.

The parent on the card is `unsloth/DeepSeek-R1-Distill-Llama-8B`. No other source names a different parent for this checkpoint. The card does not state a parameter count.

The card says the model generates responses to medical questions and can assist in medical decision-making, so the use claim is strong and the output type is a chatbot. The warning is a disclaimer: “It should not be used as a substitute for professional medical advice, diagnosis, or treatment.” It also says the model “is not intended for use in high-stakes medical decision-making without human oversight.” That sentence does not use “must not” or “should not be used for.”

The purpose is stated: “intended for use in medical reasoning tasks, particularly those requiring complex chain-of-thought reasoning.” No audience is named. Downstream text mentions diagnostic tools, medical chatbots, and educational platforms, without saying who those are for.

The functions are answering medical questions, chain-of-thought medical reasoning, and help with medical decisions. The output is a chat reply that includes reasoning. The clinical work is medical question answering and medical decision-making. The specialty is general: “the medical domain,” with no field named.

Serving is text. A chat template is in `tokenizer_config.json`. It does not set a medical system prompt. Generation defaults are temperature 0.6, top_p 0.95, and do_sample true. Context length is 131,072. No license is on the card. The card links a Weights & Biases run and does not print the scores. No paper names this repository id. The dataset paper is about HuatuoGPT-o1.
