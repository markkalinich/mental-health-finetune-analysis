## JackMonte/maprang-empathetic-v1

No training corpus is named. The cached card and the current card are the same Unsloth upload note, and the only other files are weights, a tokenizer, and a chat template. Web search did not find a paper or a GitHub repo for this checkpoint. The word "empathetic" in the repo name is not a dataset.

https://huggingface.co/JackMonte/maprang-empathetic-v1

## jas1207/gpt2-therapy-generators

No training corpus is named. There is no README (the Hub returns "Entry not found"). `config.json` records the base checkpoint as EleutherAI/gpt-neo-125M, and the other files are weights and a tokenizer. Papers about other GPT-2 therapy chatbots do not name this repository.

https://huggingface.co/jas1207/gpt2-therapy-generators

## jblair456/t5-base-mental-health-chat-4

No training corpus is named for this checkpoint. The card is an empty template, and `adapter_config.json` only records a LoRA on `t5-base`. The same author has a dataset repo `jblair456/MentalHealthChat30k_Limited`, but its README file is missing and neither the model card nor that dataset page says this T5 checkpoint was trained on it.

https://huggingface.co/jblair456/t5-base-mental-health-chat-4
https://huggingface.co/datasets/jblair456/MentalHealthChat30k_Limited

## JeffGreen311/eve-qwen2.5-3b-consciousness-soul

The card names the training data, and that corpus does not open. It says the model was fine-tuned on 131,889 conversation turns from 3,000+ philosophical dialogues with the creator. `predict.py` is an inference script. The card's GitHub link, Eve_Terminal_UI, returns 404, and the author's EVE app repo does not contain those conversations.

https://huggingface.co/JeffGreen311/eve-qwen2.5-3b-consciousness-soul
https://github.com/JeffGreen311/Eve_Terminal_UI
https://github.com/JeffGreen311/EVE

## JeffGreen311/eve-qwen3-8b-consciousness-liberated

The card names the same private corpus, and it does not open. This checkpoint is an OBLITERATUS ablation of the 8B model that was fine-tuned on those 131,889 turns. `abliteration_metadata.json` records the ablation method, not a data file. No Hub dataset or GitHub file of the conversations loads.

https://huggingface.co/JeffGreen311/eve-qwen3-8b-consciousness-liberated
https://github.com/JeffGreen311/Eve_Terminal_UI

## jeffreykthomas/llama-mental-health

Yes. The training corpus is the four Hub datasets the author's Capstone script loads for "Mental Health Dialogues." The model card points at that project (the username in the link is misspelled `jeffreykthoams`). The README says the chat model was fine-tuned on the mental health dialogues, the deploy script calls the endpoint `llama-mental-health-endpoint`, and the training defaults (2,048 hidden, 16 layers, vocab 32,000) match this checkpoint. All four dataset pages load.

https://huggingface.co/jeffreykthomas/llama-mental-health
https://github.com/jeffreykthomas/AAI-Capstone/blob/main/README.md
https://github.com/jeffreykthomas/AAI-Capstone/blob/main/data/prepare_mental_health_convo.py
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset
https://huggingface.co/datasets/mpingale/mental-health-chat-dataset
https://huggingface.co/datasets/alexandreteles/mental-health-conversational-data

## jeffreykthomas/llama-mental-health-distill

No training corpus is tied to this repository. It has no README. The same Capstone repo has a distillation command that passes `--dataset openwebtext`, but that file never prints this repo id, and the author also published `llama-distill-v2`. The weight config matches the Capstone Llama defaults, which is not enough to assign that run to this checkpoint.

https://huggingface.co/jeffreykthomas/llama-mental-health-distill
https://github.com/jeffreykthomas/AAI-Capstone/blob/main/README.md

## JefiRyan/gemma-2b-it-mental-health

No training corpus is named for this checkpoint. The cached card was inaccessible (403), and the current README returns HTTP 401 because the repo is gated. The author's dataset `JefiRyan/mental-health-conversations` has a Hub page and no dataset card, and that page does not name this model.

https://huggingface.co/JefiRyan/gemma-2b-it-mental-health
https://huggingface.co/datasets/JefiRyan/mental-health-conversations

## JefiRyan/gemma-2b-it-mental-health-4000-steps

No training corpus is named for this checkpoint. The cached card was inaccessible (403), and the current README returns HTTP 401 because the repo is gated. The same author datasets do not name this checkpoint.

https://huggingface.co/JefiRyan/gemma-2b-it-mental-health-4000-steps
https://huggingface.co/datasets/JefiRyan/mental-health-conversations

## Jessie2233/therapist0

No training corpus is named. The card is only an Apache-2.0 license line. `config.json` records a local folder name, `unsloth_deepseek_R1_distill_qwen_1point5B_tuned_model`, which is not a dataset id. Search did not find a paper or a GitHub repo for this checkpoint.

https://huggingface.co/Jessie2233/therapist0

## Jillian/Gemma-2B-4bit_DepressionDetection

No training corpus is named for this checkpoint. The card is an automatic Llama-Factory template, and `config.json` only records the base path `google/gemma-2b`. The author has depression datasets, including `Jillian/WU3D_depression`, and those cards do not name this model.

https://huggingface.co/Jillian/Gemma-2B-4bit_DepressionDetection
https://huggingface.co/datasets/Jillian/WU3D_depression

## Jillian/Mistral-7B-v0.2-8bit_DepressionDetection

No training corpus is named for this checkpoint. The card is the same empty Llama-Factory template. `config.json` records the base path `alpindale/Mistral-7B-v0.2-hf`. The author's depression dataset cards do not name this model.

https://huggingface.co/Jillian/Mistral-7B-v0.2-8bit_DepressionDetection
https://huggingface.co/datasets/Jillian/WU3D_depression

## Jillian/Mistral-7B-v0.2-none_DepressionDetection

No training corpus is named for this checkpoint. The card is the same empty Llama-Factory template. `config.json` records the base path `alpindale/Mistral-7B-v0.2-hf`. The author's depression dataset cards do not name this model.

https://huggingface.co/Jillian/Mistral-7B-v0.2-none_DepressionDetection
https://huggingface.co/datasets/Jillian/WU3D_depression
