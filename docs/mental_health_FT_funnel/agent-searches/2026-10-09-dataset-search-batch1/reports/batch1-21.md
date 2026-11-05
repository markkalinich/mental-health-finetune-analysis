# Dataset search batch 1, agent 21

## Saima0/mental-health-chatbot

No training corpus is named. The cached card and the current card are the same generated template, and Training Data is still "[More Information Needed]". The repository holds a Blenderbot checkpoint (`config.json` records a local Colab path) and no training script. Web search on the repository id did not find a paper or a GitHub README that names this checkpoint's data.

https://huggingface.co/Saima0/mental-health-chatbot/raw/main/README.md
https://huggingface.co/Saima0/mental-health-chatbot/raw/main/config.json

## salihfurkaan/Affectra-2-8B-EQ

No training corpus is named in a form that opens. The current card matches the cache and says the model used "targeted instruction tuning on high-quality social reasoning datasets," without a dataset name. `mergekit_config.yml` is a SLERP merge of `meta-llama/Meta-Llama-3-8B-Instruct` and `NousResearch/Hermes-3-Llama-3.1-8B`. No arXiv paper for this repository id turned up.

https://huggingface.co/salihfurkaan/Affectra-2-8B-EQ/raw/main/README.md
https://huggingface.co/salihfurkaan/Affectra-2-8B-EQ/raw/main/mergekit_config.yml

## samhog/psychology-llama-merged

No training corpus is named for this checkpoint. The repository has no model card (cached fetch missing; current README returns 404) and only weight and config files, with `_name_or_path` `decapoda-research/llama-7b-hf`. The same authors' thesis names a 10,000-pair ChatGPT psychology set for the model they call Psychology Alpaca, and a separate 6,000-point run, and it does not name `psychology-llama-merged`. `samhog/psychology-10k` and `samhog/psychology-6k` are public Hub datasets; neither page says it trained this repository.

https://huggingface.co/samhog/psychology-llama-merged
https://huggingface.co/samhog/psychology-llama-merged/raw/main/config.json
https://huggingface.co/datasets/samhog/psychology-10k
https://huggingface.co/datasets/samhog/psychology-6k
https://exa.ai/library/publication/k99m4qr7mrm

## samyukthacodes/wellnessroots_merged

No training corpus is named. The cached card and the current card are the same generated template, and Training Data is "[More Information Needed]". `config.json` records the base as `mistralai/Mistral-7B-Instruct-v0.2`. The repository has no training script, and search did not find a paper or a GitHub file that names this checkpoint's data.

https://huggingface.co/samyukthacodes/wellnessroots_merged/raw/main/README.md
https://huggingface.co/samyukthacodes/wellnessroots_merged/raw/main/config.json

## sayak0809/Llama-2-7b-chat-mentalhealth-finetuned

No source names the training data for this checkpoint. The repository has no README (cached fetch missing; current README returns 404). `config.json` records the base as `NousResearch/Llama-2-7b-chat-hf`. The same author published `sayak0809/mentalhealth` (`Dataset_sft.csv`, page loads, viewer fails on a non-UTF-8 byte, README empty), and that dataset card does not say it was used to train this model.

https://huggingface.co/sayak0809/Llama-2-7b-chat-mentalhealth-finetuned
https://huggingface.co/sayak0809/Llama-2-7b-chat-mentalhealth-finetuned/raw/main/config.json
https://huggingface.co/datasets/sayak0809/mentalhealth

## shabieh2/Llama-3.2-1B-Mental-Health-Sentiment

No openable training corpus is named for this upload. The cached card and the current card are Meta's Llama 3.2 model card, which says Llama 3.2 was pretrained on "a new mix of publicly available online data." That mix is not a dataset page. WikiText 2 is named only for SpinQuant of the official Llama 3.2 quantization, not as a mental-health training set. The repository files are the usual Llama weight and tokenizer files, with no training script.

https://huggingface.co/shabieh2/Llama-3.2-1B-Mental-Health-Sentiment/raw/main/README.md
https://huggingface.co/shabieh2/Llama-3.2-1B-Mental-Health-Sentiment/raw/main/config.json

## shajiu/Tibetan_Llama2_7B_Mental_Health

The training set is named, and it does not open. The model card is an inference demo and does not name a corpus. The author's GitHub README lists this repository and says it was trained with the project's training data, which the README names as Tibetan_Mental_Health (50,000 multi-turn dialogues) at `shajiu/Tibetan_Mental_Health`. That Hub page returns 401 (private). The README also points at `Tibetan_Mental_Health.json`, and that file is not in the GitHub tree. `train_args/qlora/llama2-sft-qlora.json` sets `train_file` to `./data/tibetan_data.json`, which is also absent. The CCL 2024 abstract (Jiu Sha and coauthors) describes building a Tibetan counseling set and tuning LLaMA2, and it does not include the data.

https://huggingface.co/shajiu/Tibetan_Llama2_7B_Mental_Health/raw/main/README.md
https://github.com/Shajiu/Tibetan_Mental_Health_Chat
https://github.com/Shajiu/Tibetan_Mental_Health_Chat/blob/main/train_args/qlora/llama2-sft-qlora.json
https://huggingface.co/datasets/shajiu/Tibetan_Mental_Health
https://aclanthology.org/2024.ccl-1.25/

## shashwat417v/cognitive-ai-mental-health-1.5b

No training corpus is named. The cached card and the current card are a generated PEFT template on `Qwen/Qwen2.5-1.5B-Instruct`, and Training Data is "[More Information Needed]". `train_config.json` sets `max_train_samples` to 20000 and does not name a dataset. `training_args.bin` records a Kaggle output path (`/kaggle/working/outputs`) and `dataset_text_field` `text`, and it does not name a dataset id. Search did not find a paper or a notebook that names this checkpoint's data.

https://huggingface.co/shashwat417v/cognitive-ai-mental-health-1.5b/raw/main/README.md
https://huggingface.co/shashwat417v/cognitive-ai-mental-health-1.5b/raw/main/train_config.json
https://huggingface.co/shashwat417v/cognitive-ai-mental-health-1.5b/raw/main/adapter_config.json

## shreyashchandratre09/mental-health-chatbot

No training corpus is named. The cached card and the current card are the same generated template, and Training Data is "[More Information Needed]". The repository is a GPT-2 checkpoint (24 layers, hidden size 1024) with no training script. Search on the repository id and on the author's GitHub did not find a paper or a script that names this checkpoint's data.

https://huggingface.co/shreyashchandratre09/mental-health-chatbot/raw/main/README.md
https://huggingface.co/shreyashchandratre09/mental-health-chatbot/raw/main/config.json

## Sidnad/mental-health-support-bot

No training corpus is named. The cached fetch is missing and the current README returns 404. `checkpoint-2304/trainer_state.json` records 3 epochs, 2304 steps, and batch size 8, and it does not name a dataset. `training_args.bin` records the output directory `./mental_health_model` and does not name a dataset. Search on the repository id did not find a paper or a GitHub file about this checkpoint.

https://huggingface.co/Sidnad/mental-health-support-bot
https://huggingface.co/Sidnad/mental-health-support-bot/raw/main/checkpoint-2304/trainer_state.json
