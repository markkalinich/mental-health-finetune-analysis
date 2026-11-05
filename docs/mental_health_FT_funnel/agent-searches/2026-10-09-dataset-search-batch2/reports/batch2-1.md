## 7680josephgithaiga/mental-health-chatbot

No. The cached card and the current card are the automatic Hub template, and the training-data line is still "More Information Needed." Checkpoint `trainer_state.json` logs loss and learning rate and does not name a corpus. Searches on this repository id did not find a paper or a training script.

https://huggingface.co/7680josephgithaiga/mental-health-chatbot

## a1273352/LFM2-1.2B-LEAP-counselor

No. The repository has no README. Its files are weights, a tokenizer, and `config.json`, and the config does not name a training corpus. No paper or GitHub repository describes this checkpoint.

https://huggingface.co/a1273352/LFM2-1.2B-LEAP-counselor

## a1273352/LFM2-1.2B-LEAP-multi-counselor-1012

No. The repository has no README. Its files are weights, a tokenizer, and `config.json`, and the config does not name a training corpus. No paper or GitHub repository describes this checkpoint.

https://huggingface.co/a1273352/LFM2-1.2B-LEAP-multi-counselor-1012

## a1273352/LFM2-2.6B-LEAP-counselor

No. The repository has no README. Its files are weights, a tokenizer, and `config.json`, and the config does not name a training corpus. No paper or GitHub repository describes this checkpoint.

https://huggingface.co/a1273352/LFM2-2.6B-LEAP-counselor

## a1273352/LFM2-2.6B-LEAP-multi-counselor

No. The repository has no README. Its files are weights, a tokenizer, and `config.json`, and the config does not name a training corpus. No paper or GitHub repository describes this checkpoint.

https://huggingface.co/a1273352/LFM2-2.6B-LEAP-multi-counselor

## A5CENSION-SRT/mental-health-deepseek-v1-CUDA

No. The card says this checkpoint was fine-tuned from `unsloth/deepseek-r1-distill-llama-8b-bnb-4bit` and does not name a dataset. The same author's notebook trains a different repository, `A5CENSION-SRT/mental-health-deepseek-v1`, on `ShenLab/MentalChat16K`, and that notebook does not name this CUDA repository.

https://huggingface.co/A5CENSION-SRT/mental-health-deepseek-v1-CUDA
https://github.com/A5CENSION-SRT/Personalized-Mental-Wellness-Assistant/blob/main/python/training_deepseek.ipynb
https://huggingface.co/datasets/ShenLab/MentalChat16K

## aamirmiy/Dialo_empathetic

No. There is no model card. `config.json` records `_name_or_path` as `/content/output` and does not name a corpus. The author's GitHub account has no repository that describes this checkpoint.

https://huggingface.co/aamirmiy/Dialo_empathetic

## Aarya4536/therapy-bot-v1

No. There is no model card. `config.json` names the base model `NousResearch/Llama-2-7b-chat-hf`, not a training corpus. The same author has Hub datasets, including `Aarya4536/therapy-bot-data-10k`, and those dataset cards do not say they trained this checkpoint.

https://huggingface.co/Aarya4536/therapy-bot-v1
https://huggingface.co/datasets/Aarya4536/therapy-bot-data-10k

## Aarya4536/tinyllama-therapy-bot-v1

No. There is no model card. `config.json` names the base model `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. A quantized copy links back to this repository and does not name a training corpus. The author's dataset cards do not name this checkpoint.

https://huggingface.co/Aarya4536/tinyllama-therapy-bot-v1
https://huggingface.co/mradermacher/tinyllama-therapy-bot-v1-GGUF

## Abdo36/LLAMA2_Mental_Counseling_Data

No. This model repository has no card. A dataset with the same id loads, with columns Context, Response, and LLAMA2 format. That dataset card does not say this checkpoint was trained on it.

https://huggingface.co/Abdo36/LLAMA2_Mental_Counseling_Data
https://huggingface.co/datasets/Abdo36/LLAMA2_Mental_Counseling_Data

## Abdullah-Baqais/gemma3-4b-it-arabic-empathy

Yes. The model card is the automatic template and does not name a dataset. The author's training script sets the output directory to `gemma3-4b-it-arabic-empathy-lora` and loads `arbml/arabic_empathetic_conversations`. That Hub dataset page loads and shows 36,628 rows.

https://huggingface.co/Abdullah-Baqais/gemma3-4b-it-arabic-empathy
https://github.com/Abdullah-Baqais/gemma3-arabic-empathy/blob/main/gemma3_finetune.py
https://huggingface.co/datasets/arbml/arabic_empathetic_conversations

## abhay2727/emotional_response_model_SFT_t5Small

No. The card is only a MIT license line. The author's dataset `abhay2727/akino_dataset` is also only a license line. A post by the same person names a different model, `abhay2727/emotion_model`, and does not give an open corpus for this checkpoint.

https://huggingface.co/abhay2727/emotional_response_model_SFT_t5Small
https://huggingface.co/datasets/abhay2727/akino_dataset

## abishekcodes/distilgpt2-therapist

No. The card says the model was fine-tuned on TherapyDataset and that the corpus is publicly available, and it gives no link. `RishiKompelli/TherapyDataset` loads, but that card is a list of other corpora and does not say it trained this checkpoint.

https://huggingface.co/abishekcodes/distilgpt2-therapist
https://huggingface.co/datasets/RishiKompelli/TherapyDataset
