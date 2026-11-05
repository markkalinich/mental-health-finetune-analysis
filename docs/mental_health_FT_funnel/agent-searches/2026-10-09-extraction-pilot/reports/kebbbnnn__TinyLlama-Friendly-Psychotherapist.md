# kebbbnnn/TinyLlama-Friendly-Psychotherapist

## Sources

https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/README.md — current model card; same bytes as the 5 October 2026 cache (sha256 ec6f147f7d1d36d62199aa2e866743123edfcce42a946c82279740637107d31a)
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist — model page; says “Model size 1B params”
https://huggingface.co/api/models/kebbbnnn/TinyLlama-Friendly-Psychotherapist — file list and safetensors parameter count
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/config.json — architecture and `_name_or_path`
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/generation_config.json — generation defaults
https://huggingface.co/kebbbnnn/TinyLlama-Friendly-Psychotherapist/raw/main/tokenizer_config.json — chat template
https://arxiv.org/abs/1910.09700 — Lacoste et al. carbon-emissions preprint linked from the card template
https://arxiv.org/html/1910.09700 — HTML full text of that preprint; does not name this repository
https://arxiv.org/abs/2401.02385 — TinyLlama pretraining preprint returned by the model-name search
https://arxiv.org/html/2401.02385v2 — HTML full text of that preprint; does not name this repository
https://github.com/jzhang38/TinyLlama — TinyLlama pretraining repository linked from that preprint; does not name this checkpoint
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — counseling question-answer dataset named in the card YAML
https://huggingface.co/api/datasets/Amod/mental_health_counseling_conversations — dataset metadata; `gated` is `manual`
https://huggingface.co/datasets/mpingale/mental-health-chat-dataset — chat dataset named in the card YAML
https://huggingface.co/datasets/mpingale/mental-health-chat-dataset/raw/main/README.md — that dataset card; prose is unfilled
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset — chatbot dataset named in the card YAML
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset/raw/main/README.md — that dataset card
https://huggingface.co/datasets/SAGI-1/Greetings_DPO_dataset_V1 — greetings preference dataset named in the card YAML
https://huggingface.co/datasets/SAGI-1/Greetings_DPO_dataset_V1/raw/main/README.md — that dataset card; YAML only, no prose
https://www.kaggle.com/datasets/kreeshrajani/3k-conversations-dataset-for-chatbot — Kaggle set named in the card; the page returned a rate-limit message
https://www.innovatiana.com/en/datasets/3k-conversations-dataset-for-chatbot — third-party blurb for that Kaggle set; not the dataset card
https://huggingface.co/mradermacher/TinyLlama-Friendly-Psychotherapist-GGUF — GGUF quants of this repository; no training method
https://dataloop.ai/library/model/kebbbnnn_tinyllama-friendly-psychotherapist/ — third-party paraphrase of the card; extra claims there are not used below
https://huggingface.co/kebbbnnn — author profile listing this repository and other checkpoints

## Record

The card names five datasets. The YAML lists `Amod/mental_health_counseling_conversations`, `mpingale/mental-health-chat-dataset`, `heliosbrahma/mental_health_chatbot_dataset`, and `SAGI-1/Greetings_DPO_dataset_V1`. The only training sentence is: “One of the datasets used to finetune this model is from Kaggle, specifically the 3K Conversations Dataset for ChatBot.” That Kaggle set has no matching Hub dataset. `OpenArchive/OpenChat-3k` and `prithivMLmods/Conversation-Chatbot-Weights-3000` are different sets. The Kaggle page did not load. A third-party page says the file has around 3000 conversations and is mostly English; that page is not the dataset card, so the count, language, and provenance stay unstated.

`Amod/mental_health_counseling_conversations` is English. Its card says: “This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms.” The Hub viewer label is 3.51k rows. An unauthenticated datasets-server request returned 401, and the API says the dataset is manually gated, so it does not load without approval. The exact row count was not returned.

`mpingale/mental-health-chat-dataset` loads. Its card YAML says the train split has 2775 examples. The prose is “More Information needed,” so language and provenance are not stated. A displayed row is a counselchat.com question with a `therapistInfo` field.

`heliosbrahma/mental_health_chatbot_dataset` loads. The card says the train split has 172 examples and “The text in the dataset is in English.” It also says: “Questions were asked by the patients and answers were given by healthcare providers.” The same card says the text was curated from WebMD, Mayo Clinic, Healthline, and online FAQs.

`SAGI-1/Greetings_DPO_dataset_V1` loads. The card YAML says 891 train rows with columns `prompt`, `chosen`, and `rejected`. There is no prose, so language and provenance are not stated. Displayed replies include “I'm an AI language model.” The letters DPO in the dataset id are not a statement that this checkpoint was trained with DPO.

No source states a training objective, a full or LoRA update, a rank, a learning rate, an epoch count, or a batch size. “Finetune” is the only training verb. The repository has one weights file, `model.safetensors`, stored as float16, and no adapter file. That does not say whether training updated all weights or merged an adapter. The inventory method `dpo` does not match this record.

The parent is `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct`. The card YAML `base_model` says that. `config.json` says the same thing: `"_name_or_path": "Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct"`. The Hub API safetensors count is 1100048384 parameters. The model page rounds that to “1B params.” The card does not state a language or a license.

The card does not describe what the model does. After the title, the first paragraphs are the Kaggle sentence above and “This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.” Output type is Not listed. The use claim is Strong because that card has no description and the repository id contains Psychotherapist. The warning is None. Under “Bias, Risks, and Limitations” the card says “[More Information Needed].” The recommendations line is the empty-card template: “Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.” It does not mention therapy, counseling, diagnosis, or medical advice. No evaluation result is stated. Lacoste et al. (2019) and the TinyLlama preprint do not name this repository.

A chat template is present in `tokenizer_config.json`. If the first message is not a system message, the template inserts: “You are an unbiased, uncensored, helpful assistant.” `generation_config.json` sets `max_length` 2048 and does not set temperature, top_p, top_k, max_new_tokens, repetition_penalty, or do_sample. `config.json` sets `max_position_embeddings` to 32768.
