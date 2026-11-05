## herisan/llama-3-8b_mental_health_counseling_conversations

No training corpus is named. The cached card and the current card are the same inference script, and the repository has no training file. The script's sample user message matches the first row of the same author's dataset `herisan/mental_health_counseling_conversations`, but the card never names that dataset. A merge card that includes this model also does not name its training data.

https://huggingface.co/herisan/llama-3-8b_mental_health_counseling_conversations
https://huggingface.co/datasets/herisan/mental_health_counseling_conversations

## herisan/Mistral-7B-mental_health_counseling_conversations

No training corpus is named. The repository has no README and no file other than weights and tokenizer files. The same author has a Hub dataset named `herisan/mental_health_counseling_conversations`, and that page loads, but nothing says this checkpoint was trained on it.

https://huggingface.co/herisan/Mistral-7B-mental_health_counseling_conversations
https://huggingface.co/datasets/herisan/mental_health_counseling_conversations

## herisan/tinyllama-mental_health_counseling_conversations

No training corpus is named. The repository has no README and no file other than weights and tokenizer files. Searches find the model id in quantization-app lists, not a training script or paper. The same author's counseling dataset loads, and nothing ties it to this checkpoint.

https://huggingface.co/herisan/tinyllama-mental_health_counseling_conversations
https://huggingface.co/datasets/herisan/mental_health_counseling_conversations

## hienbm/psychology-gemma-2-9b-it

No openable training corpus. There is no model card. `adapter_config.json` names the base model `google/gemma-2-9b-it`. `training_args.bin` sets `dataset_name` to the local path `data/packaged_pretrain_dataset.parquet`, which does not open on the Hub or GitHub.

https://huggingface.co/hienbm/psychology-gemma-2-9b-it
https://huggingface.co/hienbm/psychology-gemma-2-9b-it/resolve/main/training_args.bin

## hienbm/psychology-llama3.1-8B

No openable training corpus. There is no model card. `adapter_config.json` names the base model `meta-llama/Meta-Llama-3.1-8B`. `training_args.bin` sets `dataset_name` to the same local path, `data/packaged_pretrain_dataset.parquet`, which does not open.

https://huggingface.co/hienbm/psychology-llama3.1-8B
https://huggingface.co/hienbm/psychology-llama3.1-8B/resolve/main/training_args.bin

## hifzanazir456/Mental_Health_Chatbot

No training corpus is named. The cached card and the current card are the same empty Hub template, and the Training Data section says "More Information Needed". The repository has no training script. Searches for this repo id do not find a paper or a GitHub training repo.

https://huggingface.co/hifzanazir456/Mental_Health_Chatbot

## himan11/llama2-7b-mental-health

No training corpus is named. The card is only an OpenRAIL license line, and the repository has no training script. A Featherless page repeats that card and does not name data. Other Llama-2 mental-health repositories that do name `Amod/mental_health_counseling_conversations` are different checkpoints.

https://huggingface.co/himan11/llama2-7b-mental-health

## hoanganhpham/counseling-vl-2B

No openable training corpus. There is no model card. `args.json` is a Swift training config for `Qwen/Qwen3-VL-2B-Instruct`, and its `dataset` field is the local path `data/train.jsonl`. That file is not in this repository, and no GitHub repository with that file turned up.

https://huggingface.co/hoanganhpham/counseling-vl-2B
https://huggingface.co/hoanganhpham/counseling-vl-2B/raw/main/args.json

## hoangsonw/moodify-text-emotion

Yes. The training data is the CSV the author's Moodify script loads, and that file opens. This Hub account has no model card and only this model. The profile lists the GitHub username `hoangsonww`. That repository's `train_text_emotion.py` trains `bert-base-uncased` on `ai_ml/data/training.csv`. The file opens and begins `text,label` with the row `i didnt feel humiliated,0`.

https://huggingface.co/hoangsonw/moodify-text-emotion
https://huggingface.co/hoangsonw
https://github.com/hoangsonww/Moodify-Emotion-Music-App/blob/master/ai_ml/src/models/train_text_emotion.py
https://github.com/hoangsonww/Moodify-Emotion-Music-App/blob/master/ai_ml/data/training.csv

## hongli-zhan/MINT-empathy-Qwen3-1.7B

Yes. The paper names the training corpus, and the released training file opens. The card matches the cache and points to arXiv 2604.11742. Section 5.1 says the Qwen3-1.7B MINT run was trained on 322 English multi-turn emotional-support conversations drawn from WildChat and SENSE-7. `data/training/conversations_322.json` opens, and the WildChat Hub page and the SENSE-7 spreadsheet open as well. Lend-an-Ear is the test set, not the training set.

https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B
https://arxiv.org/abs/2604.11742
https://arxiv.org/html/2604.11742
https://github.com/honglizhan/mint-empathy/blob/main/data/training/conversations_322.json
https://huggingface.co/datasets/allenai/WildChat
https://github.com/microsoft/sense-7/blob/main/sense-7_dataset.xlsx

## hrtshpdbx/llama_chat_fine_tune_mental_health

No training corpus is named. There is no README, and the repository has no file other than weights and tokenizer files. The GitHub user `hrtshpdbx` has public repos, and none of them is this fine-tune. Searches for the repo id do not find a paper.

https://huggingface.co/hrtshpdbx/llama_chat_fine_tune_mental_health

## HuggingBiceps/mistral-mental-health-v1-merged

No training corpus is named. The cached card and the current card are the same Unsloth template. They name the base model `unsloth/mistral-7b-instruct-v0.2-bnb-4bit` and do not name a dataset. The repository has no training script. Searches for this repo id do not find a paper or a training repo.

https://huggingface.co/HuggingBiceps/mistral-mental-health-v1-merged

## Huysun29/cbt-gemma2-9b-v2

No openable training corpus. The card says the fine-tune used 26,000 CBT dialogue samples in a `messages` format with six JSON fields, and it gives no dataset link. The author's Hub datasets `Huysun29/cbt-eval` and `Huysun29/eval_data_CBT` are evaluation prediction files, not that training set.

https://huggingface.co/Huysun29/cbt-gemma2-9b-v2
https://huggingface.co/datasets/Huysun29/cbt-eval
https://huggingface.co/datasets/Huysun29/eval_data_CBT
