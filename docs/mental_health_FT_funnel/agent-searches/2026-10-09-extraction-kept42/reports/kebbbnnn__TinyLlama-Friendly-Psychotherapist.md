# kebbbnnn/TinyLlama-Friendly-Psychotherapist

## Sources

https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/kebbbnnn__TinyLlama-Friendly-Psychotherapist__2026-10-09.md — cached card, sha256 ec6f147f7d1d36d62199aa2e866743123edfcce42a946c82279740637107d31a
https://huggingface.co/api/models/kebbbnnn/TinyLlama-Friendly-Psychotherapist — file list and parameter count
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/config.json — architecture, context length, parent id in `_name_or_path`
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/generation_config.json — generation max length
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/tokenizer_config.json — chat template and default system line
https://huggingface.co/Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct/raw/main/README.md — parent card, text prompt example
https://arxiv.org/abs/1910.09700 — abstract of the emissions-calculator paper linked from the card template
https://arxiv.org/html/1910.09700 — HTML full text of that paper; it does not name this repository
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — counseling question-answer dataset card; files are gated
https://huggingface.co/datasets/mpingale/mental-health-chat-dataset — dataset card and 2,775-row train split
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset — dataset card, English, 172 rows
https://huggingface.co/datasets/SAGI-1/Greetings_DPO_dataset_V1 — preference-format dataset, 891 rows, empty description
https://www.kaggle.com/datasets/kreeshrajani/3k-conversations-dataset-for-chatbot — Kaggle set named on the card; no Hub copy found

## Record

The card's dataset list names four Hub sets: Amod/mental_health_counseling_conversations, mpingale/mental-health-chat-dataset, heliosbrahma/mental_health_chatbot_dataset, and SAGI-1/Greetings_DPO_dataset_V1. The only prose about data says: "One of the datasets used to finetune this model is from Kaggle, specifically the 3K Conversations Dataset for ChatBot." Amod's card says the conversations are "real one-on-one mental health counseling conversations" in English, "Collected directly from two publicly accessible counselling websites." Its raw files returned 401 (gated). The Hub viewer label is a rounded 3.51k rows, and the card says "No predefined splits," so the exact count is not recorded here. mpingale's card is the placeholder "More Information needed"; the train split has 2,775 rows. heliosbrahma's card says the text "is in English" and "was curated from popular healthcare blogs," 172 rows. SAGI-1 has columns prompt, chosen, and rejected, 891 rows, and an empty card, so language and who wrote the text are not stated. No Hub dataset matched the Kaggle 3K set.

The card says the model was finetuned and does not name a loss. "Fine-tuned" is not an objective, and "DPO" inside SAGI-1/Greetings_DPO_dataset_V1 is not evidence that this checkpoint was trained with DPO. No sentence states full fine-tuning, LoRA, or QLoRA. Epochs, steps, learning rate, and batch size are not stated. The repository has a full `model.safetensors` and no adapter file; that does not say how the weights were updated.

The card YAML and `config.json` both name the parent `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct`. The Hub API safetensors total is 1,100,048,384 parameters, float16. The card body still says "Finetuned from model: [More Information Needed]."

The model-description section is the automatic sentence "This model card has been automatically generated," so the output type is not listed. The repository id is TinyLlama-Friendly-Psychotherapist, and the card has no description of the model, so the use claim is Strong under the 9 October ruling. The limitations section is "[More Information Needed]." The recommendations line is the template sentence "Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model," which does not mention therapy or medical use. No evaluation and no license are stated. The inventory row's datasets and parent match the YAML. Its method `dpo` does not: the card never states an objective. The card also names the Kaggle set, which the inventory row omits.

The parent card's example is text only: "The intended prompt format is a modified multi-turn Alpaca instruction format." This repository's chat template is in `tokenizer_config.json`. If the first message is not a system message it inserts "You are an unbiased, uncensored, helpful assistant." `generation_config.json` sets `max_length` 2048 and no sampling fields. `config.json` sets `max_position_embeddings` to 32768.
