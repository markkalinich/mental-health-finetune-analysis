## cogni-x/wearable-intelli-model

No training corpus is named. The cached card is an access error, and the live README returns HTTP 401 because the repository is gated for manual access. The public metadata names the base model `google/gemma-3-270m-it` and tags it as QLoRA SFT, but it does not name a dataset. Repo files are weights, a tokenizer, and a chat template. Searches for the repository id and "wearable-intelli-model" did not find a paper or a GitHub training script for this checkpoint.

https://huggingface.co/cogni-x/wearable-intelli-model
https://huggingface.co/cogni-x/wearable-intelli-model/raw/main/README.md

## ColleenMacklin/blenderbot-400M-distill-couples_therapist_chat1

No training corpus is named. There is no model card: the cached fetch is missing, and the live README returns 404. The repository files are weights, a config, a TensorBoard event file, and `training_args.bin`. That arguments file records the output directory and does not record a dataset path. Searches did not find a paper, a GitHub training script, or a Hub dataset for this checkpoint.

https://huggingface.co/ColleenMacklin/blenderbot-400M-distill-couples_therapist_chat1

## ColleenMacklin/gpt-neo-125M-couples_therapist_full_renamed

No training corpus is named. The cached card and the live card match. The card says the model is a fine-tune of EleutherAI/gpt-neo-125M on the None dataset, and the training-data section says more information is needed. "None" is the Trainer placeholder, not a corpus that opens. The repository has no training script. Searches did not find a paper or a GitHub repo that names a dataset for this checkpoint.

https://huggingface.co/ColleenMacklin/gpt-neo-125M-couples_therapist_full_renamed
https://huggingface.co/ColleenMacklin/gpt-neo-125M-couples_therapist_full_renamed/raw/main/README.md

## connaaa/interpgpt-adhd-23M

The card names the training data, and that data does not open. The cached card and the live card match. They call the data an ADHD-variant task-decomposition corpus: task decompositions with smaller steps and interleaved lines such as "sip water" and "deep breath." The same author's standard-model card says the generation scripts live in github.com/cwklurks/interpgpt. That GitHub repository returns 404. The model repository has a notebook and modeling code, and no data file. No Hub dataset named InterpGPT loads.

https://huggingface.co/connaaa/interpgpt-adhd-23M
https://huggingface.co/connaaa/interpgpt-adhd-23M/raw/main/README.md
https://github.com/cwklurks/interpgpt
https://huggingface.co/connaaa/interpgpt-standard-23M

## ctopuz3/mental-health-response-model

No training corpus is named. The cached card and the live card match, and both are the automatic Hub template. The Training Data section says more information is needed. The repository files are the model, tokenizer, and config. Searches for the repository id did not find a paper, a GitHub training script, or a dataset by this author.

https://huggingface.co/ctopuz3/mental-health-response-model
https://huggingface.co/ctopuz3/mental-health-response-model/raw/main/README.md

## curiousily/Llama-3.2-1B-Mental-Health-Sentiment

No fine-tuning corpus is named for this checkpoint. The cached card and the live card match, and both are Meta's Llama 3.2 model card. That card says Llama 3.2 was pretrained on "a new mix of publicly available online data," which is not a corpus a reader can open, and it describes the base model rather than a mental-health fine-tune. The repository has weights, a GGUF file, and a TensorBoard event file, and no training script. Searches did not find a paper or a GitHub repo by Venelin Valkov that names a dataset for this repository id.

https://huggingface.co/curiousily/Llama-3.2-1B-Mental-Health-Sentiment
https://huggingface.co/curiousily/Llama-3.2-1B-Mental-Health-Sentiment/raw/main/README.md

## CYLoey98982/counselor_chatbot

No training corpus is named for this checkpoint. The cached card and the live card match, and both are the automatic Hub template. The repository files are a GPT-2 model, tokenizer, and chat template, and they do not name a dataset. The same account hosts `CYLoey98982/mental_health_chatbot`, which loads, but its card is only a feature list and does not say this model was trained on it. The author's Space says the demo is a DialoGPT chatbot and its app file is a greeting stub.

https://huggingface.co/CYLoey98982/counselor_chatbot
https://huggingface.co/CYLoey98982/counselor_chatbot/raw/main/README.md
https://huggingface.co/datasets/CYLoey98982/mental_health_chatbot
https://huggingface.co/spaces/CYLoey98982/counselor_chatbot

## cypsiSAS/Llama-2-7b-chat-finetune_depression

No training corpus is named for this checkpoint. There is no model card: the cached fetch is missing, and the live README returns 404. The config names the base model `NousResearch/Llama-2-7b-chat-hf`. The same account hosts `cypsiSAS/Depression`, which loads as a CSV, and that dataset has no card and does not name this model. Commit messages on the model are "Upload tokenizer," "Upload LlamaForCausalLM," and "initial commit."

https://huggingface.co/cypsiSAS/Llama-2-7b-chat-finetune_depression
https://huggingface.co/datasets/cypsiSAS/Depression

## daikooo/DialogGPT-finetune-mental-health-chatbot

No training corpus is named. There is no cached card. The live card is three YAML fields: license openrail, language en, and pipeline conversational. The repository files are a GPT-2 model and tokenizer, and the config's name path is `output-small-save`. The author's Space loads this model and does not name a dataset. This account has no public Hub datasets. The DialoGPT Reddit corpus is the base model's pretraining data, not a source about this fine-tune.

https://huggingface.co/daikooo/DialogGPT-finetune-mental-health-chatbot
https://huggingface.co/daikooo/DialogGPT-finetune-mental-health-chatbot/raw/main/README.md
https://huggingface.co/spaces/daikooo/DialoGPT-finetune-mental-health-chatbot

## DaJulster/Mental_health_response

No training corpus is named. The cached card and the live card match. The card says the model is a fine-tune of google-t5/t5-base on the None dataset, and the training-data section says more information is needed. "None" is the Trainer placeholder. The repository has weights, tokenizer files, TensorBoard logs, and `training_args.bin`, and that arguments file does not record a dataset path. Searches did not find a paper or a GitHub training script for this repository id.

https://huggingface.co/DaJulster/Mental_health_response
https://huggingface.co/DaJulster/Mental_health_response/raw/main/README.md

## Dakshina-mentalHealth/mh-sin-sft-1b

No training corpus is named for this checkpoint. The cached card and the live card match, and both are the automatic Hub template. The model is a Qwen2 checkpoint. Commit titles say "mh-v3 topic-conditioned dedup" and "mh-only retrain 2ep," and they do not give a dataset id. The same account hosts `Dakshina-mentalHealth/mental_health_si`, which loads and has no dataset card, and no file in this model repository names that dataset. The sibling models `mh-sin-qwen3` and `mh-sin-mistral` also have empty template cards.

https://huggingface.co/Dakshina-mentalHealth/mh-sin-sft-1b
https://huggingface.co/Dakshina-mentalHealth/mh-sin-sft-1b/raw/main/README.md
https://huggingface.co/datasets/Dakshina-mentalHealth/mental_health_si

## Dalton-Khatri/freud-mental-health-assistant

A training script names a corpus, and that corpus does not open. There is no model card. The config base is `EleutherAI/gpt-neo-125m`, and `training_args.bin` records the output directory `./freud_gpt_neo_125m_output`. The same author's GitHub notebook `gpt-neo-125m-trainer.ipynb` uses that output directory and reads `/kaggle/input/freud-1-0/train.json` and `validation.json`. The notebook's Hub name is `Dalton-Khatri/freud-gpt-neo-125m`, which returns HTTP 401. No public Kaggle page for freud-1-0 loads, the JSON files are not in the GitHub repo, and no Hub dataset with that name loads.

https://huggingface.co/Dalton-Khatri/freud-mental-health-assistant
https://github.com/Dalton-Khatri/Freud
https://github.com/Dalton-Khatri/Freud/blob/main/training/Training-neogpt-125M/gpt-neo-125m-trainer.ipynb
https://huggingface.co/Dalton-Khatri/freud-gpt-neo-125m

## DavidC/bart-large-psychology_misc_wiki_filtered

No training corpus is named. There is no model card: the cached fetch is missing, and the live README returns 404. The config base is `facebook/bart-large`. Commit titles say "Training in progress" and an epoch number, and they do not name a dataset. `training_args.bin` does not record a dataset path. Searches for the repository id and for `psychology_misc_wiki_filtered` did not find a paper or a GitHub training script. A different account's dataset, `burgerbee/psychology_wiki`, loads, and nothing ties it to this checkpoint.

https://huggingface.co/DavidC/bart-large-psychology_misc_wiki_filtered
https://huggingface.co/datasets/burgerbee/psychology_wiki
